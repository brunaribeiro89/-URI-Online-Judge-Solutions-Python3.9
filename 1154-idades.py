idade = int(input())
soma = 0
contador = 0
while idade >= 0:
    soma += idade
    contador += 1
    idade = int(input())
media = soma / contador
print(f'{media:.2f}')
