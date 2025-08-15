"""
Operadores Lógicos e Relacionais


- Comparações: >, <, >=, <=, ==, !=

> maior que 

< menor que 

>= maior ou igual a

<= menor ou igual a

== igual a

!= diferente de

- Operadores lógicos: and, or, not

and 'e' --> Retorna true se todas as virificações forem verdadeiras

or 'ou'--> Retorna true se pelo menos uma verificação for verdadeira

not 'negação' --> Inverte o valor lógico

- Combinar condições

📍 Dica:
Use operadores lógicos para criar regras mais complexas em decisões.
"""

idade = 20
tem_carteira = True

# Comparações simples
print(idade > 18)   # True
print(idade == 20)  # True
print(idade != 15)  # True
print(idade < 18)   #false

# Combinação com "and" 
if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

# Usando "not"
chovendo = False
if not chovendo:
    print("Pode sair sem guarda-chuva.")


