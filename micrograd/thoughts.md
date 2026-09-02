This will most likely contain my understanding of what I have learned about in micrograd. 
Explanations can either be intuitive, mathemetical, or technical, it depends entirely on how I want to explain a concept. 

Note: Some explanations may be wrong, when it is wrong I'll address it and change it, or if I find a better way to explain it then I'll use that.

So, let's take an expression, the one in micrograd.ipynb. 

"-a**3 + sin(3*b) - 1.0/c + b**2.5 - a**0.5"

Naturally, this expression will equal to a certain scalar value. This progression is called a **forward pass**. 
If we ewa

But when we want to predict an output based on the inputs, parameters/weights should affect the inputs in a way that directs them to the actual value. So, let's discuss **backpropagation**.

#Backpropagation

This is when we redefine the weights based on the given gradients to optimize/minimize the loss function. Firstly, to get the gradients we get the derivative of the final output with respect to each variable in the expression. Let's say Z is the output of the expression above, the derivative of a would be dZ/da. In other words, if I nudge "a" by a small amount, what would be the value of the change. It would look something like: (**data/gradient** x **z.gradient**). And that is done throughout the variables present in the expression. 

##Value class

__init__(params) = self-call | data-value | _children=()-set | _op-operator | label-name
__init__(variables) = data-float/int value | grad-derivative | .prev-set of numbers | 
op-operator | label-name

__repr__ = return value

__add__(params) = self-first number | other-second number
- 


So, we give each *x* a **parameter**. 

Maximum Likelihood Estimation
People who don't know the difference of probability and likelihood are idiots. I dont know the difference, hence I am an idiot. So, I will call Probability as x and Like