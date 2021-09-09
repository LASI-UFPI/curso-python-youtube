# faça um programa que indique se o número é maior do que 5 e menor que 10,
# é maior que 30 e menor que 40, ou igual a 50.
# Caso contrário, informe que stá fora do intervalo

num = int(input("Número: "))

if(num>5 and num<10):
    print("O número é maior do que 5 e menor que 10")

elif(num>30 and num<40):
    print("O número é maior do que 30 e menor que 40")

elif(num == 50):
    print("O número é igual a 50")

else:
    print("Número fora dos intervalos")