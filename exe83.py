exp = []
exp.append(str(input('Digite uma expressão: ')))
v1 = exp.count('(')
v2 = exp.count(')')
print(v1)
print(v2)
if v1 == v2:
    print('É uma expressão válida!')
else:
    print('Não é uma expressão válida!')
