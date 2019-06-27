from collections import deque

#initialize data structures
stack = []
queue = deque([])
stack_out = ""
queue_out = ""

#prompt user for input
to_check = input("Enter item to check: ")

#loop to populate stack and queue
for i in range(len(to_check)):
    stack.append(to_check[i].lower())
    queue.append(to_check[i].lower())

#empty stack
while len(stack) > 0:
    stack_out += stack.pop()

#empty queue
while len(queue) > 0:
    queue_out += queue.popleft()

#check if palindrome
if queue_out == stack_out:
    print(to_check + " is a palindrome!")
else:
    print(to_check + " is not a palindrome.")