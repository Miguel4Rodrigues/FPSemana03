from collections import deque

stack = deque(input().split()[::-1]) #input = Fito Caixa Rotor Marta

print(stack)

while stack:
    nome = stack.pop()
    if "a" in nome:
        print(nome)