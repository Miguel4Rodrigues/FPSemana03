from collections import deque

stack = deque(map(int, input().replace(" ", ""))) #input = 1 2 3 4 5

print(stack)

while stack:
    numeros = int(stack.pop()) * 2
    print(numeros)