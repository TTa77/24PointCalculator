# Description
This package is to generate a formula using the 4 numbers given by the user and make the calculation result to be *24*.

The idea of this implement is to enumerate every possible combination of numbers, operators and parentheses, and then check which one can be calculated as 24.

### The overall workflow is:
1. Receive input from keyboard;
2. Generate all the arrangements of these 4 numbers, e.g., getting input of '1 2 3 4', generate '1 2 3 4', '1 2 4 3', '1 3 2 4', ..., '4 3 2 1';
3. Adding three operators of every possible sequences into these arrangements of number, between each two numbers, e.g., for '1 2 3 4', the candidate formula includes '1+2+3+4', '1+2+3-4', '1+2-3+4', ..., '1/2/3/4';
4. Adding parentheses of every valid form for each combination of operators, e.g., '(1+2)\*3/4', '1+(2\*(3+4))' ...
5. Calculate the formula, once get 24, output this formula and quit.

### Multi-threading
The *step 3-5* mentioned above is realized concurrently, which means one independent thread for calculating one number sequence, and the adding operators, adding parentheses, and calculation works are done by this thread sequentially.

# Usage
Run *main.py*, input 4 numbers and press *ENTER* to wait for the answer. The time-consuming should be about **1-2s**. Otherwise press *"Q"* or *"q"* to quit.

For some input, there will be more than one solution. The program will throw one of which. However, actually every correct answers have been generated and the program just gives that of being first seen.

# TODO
- Have not found a way to eliminate redundant parentheses yet, e.g., will generate a solution like (1+(2+3))*4.
- Improve the concurrency.
