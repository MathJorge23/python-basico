'''

- Criar variáveis e identificar tipos de dados 
- Printar 
- Ler dados do usuário (input)
- Converter tipos (casting)

Obs: Em Python não precisamos declarar o tipo de variável, ele é identificado automaticamente.
'''

#exemplos práticos
# 🔹 STRING (str) - Texto
nome = "Matheus"  # Sempre entre aspas simples ou duplas
print("O valor de 'nome' é " + nome + " e seu tipo é " + str(type(nome)))

# 🔹 INTEIRO (int) - Número inteiro (positivo, negativo ou zero)
idade = 29
print("O valor de 'idade' é " + str(idade) + " e seu tipo é " + str(type(idade)))

# 🔹 PONTO FLUTUANTE (float) - Número com casas decimais
altura = 1.75
print("O valor de 'altura' é " + str(altura) + " e seu tipo é " + str(type(altura)))

# 🔹 BOOLEANO (bool) - Verdadeiro ou Falso
ativo = True
print("O valor de 'ativo' é " + str(ativo) + " e seu tipo é " + str(type(ativo)))

# 🔹 Tipo None - Ausência de valor
sem_valor = None
print("O valor de 'sem_valor' é " + str(sem_valor) + " e seu tipo é " + str(type(sem_valor)))



#entrada de dados
usuario_nome = input ("Digite seu nome: ")
usuario_idade = int(input("Digite sua idade: ")) #Ao receber um dado o Python trata como String (texto) 
                                                 #então é necessário realizar a conversão para numerico (int)

print("Olá "+ nome + "ano que vem você fará " + str(idade+1))#em Phyton é necessário converter o int
                                                             #para str para printar

'''
 Exercícios:
1. Crie um programa que pergunte ao usuário o nome, a idade e a cidade, e depois exiba a frase:
   "Olá <nome>, você tem <idade> anos e mora em <cidade>."
2. Faça um programa que peça 3 numeros inteiros e exiba a média deles.

Resolução.

'''
#1
nome = input("Qual o seu nome?")
idade = int(input("Quantos anos você tem?"))
cidade = input("Qual cidade você mora?")

print ("olá "+ nome +" você tem "+ str(idade) +" anos de idade e mora em "+ cidade)

#2
nota1 = int(input("Informe o primeiro numero: "))
nota2 = int(input("Informe o segundo numero: "))
nota3 = int(input("Informe o terceiro numero: "))

media = (nota1 + nota2 + nota3) / 3

print(" A média dos números é: "+str(media))