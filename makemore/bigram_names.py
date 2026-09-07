import torch
import sys
import random
import torch.nn.functional as F
from typing import List, Dict, Tuple

def load_names(path:str) -> list[str]:
    words = open(path,'r').read().splitlines()
    lower_names = [x.lower() for x in words]
    return lower_names
    
def build_vocab() -> tuple[list[str], dict[str,int], dict[int,str]]:
    chars = list("abcdefghijklmnopqrstuvwxyz")
    char_to_idx = {s:i+1 for i,s in enumerate(chars)}
    char_to_idx["."] = 0
    idx_to_char = {i:s for s,i in char_to_idx.items()}
    return (chars,char_to_idx,idx_to_char)

def build_bigram_counts(names: list[str], c2i: dict[str, int]) -> torch.tensor:
    N = torch.zeros(27,27, dtype=torch.int32)
    
    for w in names:
        chs = ["."] + list(w) + ['.']
        for ch1,ch2 in zip(chs,chs[1:]):
            ix1 = c2i[ch1]
            ix2 = c2i[ch2]
            
            N[ix1,ix2] += 1
    return N

def counts_to_probs(n: torch.tensor) -> list[list[float]]:
    #P = torch.zeros_like(N, dtype=torch.float32)
    
    """    for i in N:
        row_sum = sum(N[i])
        for j in N[i]:
            P[i,j] = N[i,j] / row_sum"""
    
    N_float = n.float()
    N_float += 1 # To prevent zeros on all entries
    P = N_float/N_float.sum(1,keepdim=True)
    return P

g = torch.Generator().manual_seed(2147483647)
def sample_name(P: list[list[float]], i2c: dict[int, str], c2i: dict[str, int], max_len: int = 20) -> str:
    idx = c2i['.']
    name_chars = []
    while True:
        probs = P[idx]
        idx = torch.multinomial(probs, num_samples=1, replacement=True, generator = g).item()
        
        name_chars.append(i2c[idx])
        if idx == c2i['.'] or len(name_chars) >= 20:
            break
    if name_chars[-1] == '.':
       del  name_chars[-1]
    out = ''.join(name_chars)
    return(out)

if __name__ == "__main__":
    import sys, random

    path = sys.argv[1]
    num_names = int(sys.argv[2])
    seed = None
    if "--seed" in sys.argv:
        idx = sys.argv.index("--seed")
        seed = int(sys.argv[idx + 1])
    
    if seed is not None:
        random.seed(seed)

    names = load_names(path)
    chars, c2i, i2c = build_vocab()
    N = build_bigram_counts(names, c2i)
    P = counts_to_probs(N)

    print(f"Generated {num_names} names:")
    for i in range(num_names):
        name = sample_name(P, i2c, c2i)
        print(f"{i+1}. {name}")