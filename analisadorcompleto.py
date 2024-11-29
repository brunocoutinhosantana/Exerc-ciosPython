somaidade = 0
maioridadehomem = 0
nomevelho = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos!'.format(mediaidade))
print('O homem mais velho tem {} anos e o nome dele é {}'.format(maioridadehomem, nome))
