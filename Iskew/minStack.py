'''Rar the Cat has developed a new data structure, the MinStack!

Rar's data structure supports the following operations:

push: pushing an integer X to the top of the stack. (0)
pop: removes the top integer from the stack. (1)
top: retrieves the value of the top integer on the stack. (2)
getMin: retrieves the value of the minimum integer in the stack. (3)
There will be a total of Q queries to the data structure. Help Rar implement it.

Implementation Details:

This is a function-call question. You are to implement the following functions:

void push(int X): push X into the stack.
void pop(): remove the top element from the stack.
int top(): returns (but not remove) the top element on the stack.
int getMin(): returns (but not remove) the minimum element on the stack.
It is guaranteed that pop, top and getMin will not be called when the stack is empty.

You may access the sample grader and solution template from the Attachments tab to test your solutions.

Limits

Subtask 1 (15%): 1 ≤ Q ≤ 103, 1 ≤ X ≤ 109.

Subtask 2 (23%): 1 ≤ Q ≤ 105, 1 ≤ X ≤ 109.

Subtask 3 (17%): 1 ≤ Q ≤ 3 * 106, 1 ≤ X ≤ 2.

Subtask 4 (10%): 1 ≤ Q ≤ 3 * 106, 1 ≤ X ≤ 109. pop will never be called.

Subtask 5 (35%): 1 ≤ Q ≤ 3 * 106, 1 ≤ X ≤ 109.

Subtask 6 (0%): Sample Testcases

Sample Testcase 1

Input

6 0 5 0 9 2 3 0 1 3

Output

9 5 1'''
s=[]
mins = []

def push(x):
    s.append(x)
    if not mins or x <= mins[-1]:
        mins.append(x)

def pop():
    k=s.pop()
    if k==mins[-1]:
        mins.pop()

def top():
    print(s[-1])
    
def getMin():
    print(mins[-1])
 
def main():
    
    Q = int(input())
    for _ in range(Q):
        parts = input().split()
        cmd = int(parts[0])
        if cmd == 0:
            x = int(parts[1])
            push(x)
        elif cmd == 1:
            pop()
        elif cmd == 2:
            top()
        elif cmd == 3:
            getMin()

main()