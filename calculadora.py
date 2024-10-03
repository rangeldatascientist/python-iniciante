# Código de uma calculadora simples:
# Primeiro vamos definir o que a calculadora vai fazer: somar, diminuir, multiplicar e dividir.
# O que são Funções? São pequenas máquinas que fazem algo específico. Cada função vai receber dois números como parâmetro (x e y) e retornará o resultado da operação.


# Função para somar:
def somar(x, y):
    return x + y

# Função para subtrair:
def subtrair(x, y):
    return x - y

# Função para multiplicar:
def multiplicar(x, y):
    return x * y

# Função para dividir:
def dividir(x, y):
    return x / y

# Lista para exibir as opções para o usuário escolher:
print("Escolha a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

# Recebendo a escolha do usuário:
escolha = input("Digite o número da operação (1/2/3/4): ")

# Depois os dois números que o usuário deseja calcular:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verificar qual operação o usuário escolheu e executar a função correspondente:
if escolha == '1':
    print(f"{num1} + {num2} = {somar(num1, num2)}")
elif escolha == '2':
    print(f"{num1} - {num2} = {subtrair(num1, num2)}")
elif escolha == '3':
    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
elif escolha == '4':
    print(f"{num1} / {num2} = {dividir(num1, num2)}")
else:
    print("Opção inválida! Por favor, escolha entre 1 e 4.")
