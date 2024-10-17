def adicao():
    print(x + y)
def subtracao():
    print(x - y)
def multiplicacao():
    print(x * y)
def divisao():
    print(x / y)

print('---------------------------------------')
print('Ola seja bem vindo a minha calculadora ')
print('Qual operação deseja realizar')
print('1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão ')
print('---------------------------------------')

x = float(input('Digite o primeiro numero'))
y = float(input('Digite o segundo numeoro'))

n = int(input('Digite o numero correpondente a operação - '))

if n == 1:
    adicao()
elif n == 2:
    subtracao()
elif n == 3:
    multiplicacao()
elif n == 4:
    divisao()
else:
    print('Por favor digite um numero que correponda a uma operação')