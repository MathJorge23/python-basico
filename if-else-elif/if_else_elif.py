idade = 20

if idade >= 18:
    print("Você é maior de idade.")

numero = 7

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

nota = 65

if nota >= 90:
    print("Aprovado com nota excelente!")
elif nota >= 70:
    print("Aprovado.")
else:
    print("Reprovado.")

a = 10
b = 20

if a > b:
    print("a é maior que b")
elif a < b:
    print("a é menor que b")
else:
    print("a é igual a b")

idade = 22
carteira = True

if idade >= 18:
    if carteira:
        print("Pode dirigir.")
    else:
        print("Precisa ter a carteira de motorista.")
else:
    print("Não pode dirigir.")

idade = 17
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

x = 10

if x > 0:
    pass  # ainda vou decidir o que fazer
else:
    print("x é menor ou igual a 0")
