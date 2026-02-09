def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b==0:
    return "Cannot divide by zero"
  return a/b

print("== Simple Calculator ==")

num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundo número:"))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op=input("Opção:")

if op== "1":
  print("Resultado:", add(num1,num2))
elif op== "2":
  print("Resultado:", subtract(num1,num2))
elif op== "3":
  print("Resultado:", multiply(num1,num2))
elif op== "4":
  print("Resultado:", divide(num1,num2))
else:
  print("Opção invalida")