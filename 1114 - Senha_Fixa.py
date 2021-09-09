valida = False
while not valida:
    senha = input()
    if senha == '2002':
        print('Acesso Permitido')
        valida = True
    else:
        print('Senha Invalida')
