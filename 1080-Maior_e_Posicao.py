valor = 0
posicao = 0

for i in range(100):
    n = int(input())
    if(n > valor):
        valor = n
        posicao = i
print(f'{valor}')
print(f'{posicao + 1}')
