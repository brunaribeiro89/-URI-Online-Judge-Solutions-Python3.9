  
valores = input().split()
N1, N2, N3, N4 = valores

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print(f'Media: {media:.1f}')

if (media >= 7.0):
     print("Aluno aprovado.")
if(media < 5.0):
    print("Aluno reprovado.")

if(media >= 5.0 and media <= 6.9):
     print("Aluno em exame.")
     nota_exame = float(input())
     print(f'Nota do exame: {nota_exame:.1f}')
     nova_media= (media + nota_exame)/2
     if(nova_media >= 5.0):
         print(f'Aluno aprovado.')
     else:
         print('Aluno reprovado')
     print(f'Media final: {nova_media:.1f}')
