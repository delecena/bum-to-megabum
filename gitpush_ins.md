# How to push (Faster Edition)

git commit -am "{message}" - add and commit
git pull --rebase origin main && git push origin main - pull and push

# How to Push

git remote -v
git status
git branch --show-current
git add -A
git commit -m "{message}"
git pull --rebase origin main
git push origin main

# Description
git remote -v # Check if you are in the right repo
git status # It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git.
git branch --show-current # Checks which branch you are on

---
_Local saves_
git add -A # Stages everything, tracks new files, updates modified files, and removes deleted files
git commit -m "{message}"
_Local saves_
---

git pull --rebase origin main # gets remote updates
git push origin <branch> # push edits to whichever branch you want