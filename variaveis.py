# Python - Variáveis são usadas para armazenar valores que podem ser referenciados e manipulados ao longo de um programa. Elas não precisam de declaração explícita de tipo (como acontece em algumas linguagens), já que Python é uma linguagem de tipagem dinâmica. Isso significa que o tipo de uma variável é determinado automaticamente pelo valor que você atribui a ela.

nome = "Anna"
idade = 28
altura = 1.62
casado = False

# Como ficaria exibido as variáveis?
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Casado {casado}")

# Como verificar o tipo de uma variável?
x = 42
print(type(x))  # Output: <class 'int'>

y = "Olá"
print(type(y))  # Output: <class 'str'>

#Operações com variáveis:
# Operação matemática
a = 10
b = 5
soma = a + b
print(soma)  # Output: 15

# Concatenar strings
nome = "Ana"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # Output: Ana Silva

#Concatenar - significa juntar as coisas. Como dois blocos de legos separados que queremos que forme algo, por exemplo: uma torre maior. Concatenar em programação é juntar palavras com números.

