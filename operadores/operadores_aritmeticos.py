"""
- Operadores Aritméticos
()  Parênteses
Usados para forçar uma ordem ou agrupar operações.
O que estiver dentro dos parênteses é calculado primeiro.

** Potência
Eleva um número a outro
Tem prioridade sobre multiplicaçao e divisão

* Multiplicação
Multiplica valores

/ Divisão real
Retorna um número float (mesmo se o resultado for um número inteiro)

// Divisão inteira
Retorna apenas a parte inteira do resultado

% Módulo (resto da divisão)
Retorna o resto da divisão entre dois números

+ Soma 
Soma dois números 

- Subtração 
Subtrai dois números

1. ()  → Parênteses
2. **  → Potência
3. *, /, //, %  → Multiplicação e divisões
4. +, - → Soma e subtração

Dica:
Use parênteses para deixar a expressão mais clara e evitar erros de interpretação.
"""

# Exemplo prático: cálculo de compra
preco = 50
quantidade = 3
total = preco * quantidade
print(f"Total da compra: R${total:.2f}")

# Divisão inteira e resto
dias = 365
semanas = dias // 7
resto_dias = dias % 7
print(f"{dias} dias = {semanas} semanas e {resto_dias} dias")

# Potência
print(f"2 elevado a 3 = {2 ** 3}")

# Ordem de precedência ((), **, *, /, //, %, +, -)
resultado = (2 + 3) * 4 ** 2 / 8
print(f"Resultado da expressão: {resultado}")


