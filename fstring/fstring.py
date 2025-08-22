'''
Melhorando o print com o f-string

O fstring foi introduzido no Python 3.6, é a melhor forma (praticidade e legibilidade) de formatar strings.
'''

#Exemplo
nome = 'Matheus'
idade = 30

print (f'meu nome é {nome} e tenho {idade} anos de idade.')

#No exemplo acima podemos ver como ler a string foi muito mais fácil, sem a necessidade de converter
#sem as diversas concatenações e mesmo sem conhecimento é possivel entender onde cada variavel vai ser inserida

#operações 

print(f'No ano que vem, {nome} terá {idade+1} anos de idade')
print(f'No ano passado, {nome} tinha {idade-1} anos de idade')
print(f'O dobro da idade de {nome} é  {idade*2} ')
print(f'A metade da idade de  {nome} é {idade/1} ')

#Também podemos fazer operações dentro do f-string, assim não temos necessidade de realizar a operação 
#antes de exibir a mensagem, deixando o código mais limpo e fluido.

#Formatando numeros com casas decimais
saldo = 12345.6789

print(f'Saldo: R${saldo:.2f}')# 2 casas decimais
print(f'Saldo: R${saldo:.3f}')# 3 casas decimais

#Formatar com o separador de milhar
print(f'Saldo: R${saldo:,.2f}')

# Usando f-string para alinhamento de texto
print(f"|{nome:<11}| alinhado à esquerda")
print(f"|{nome:>11}| alinhado à direita")
print(f"|{nome:^11}| centralizado")


