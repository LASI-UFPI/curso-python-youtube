# ESTRUTURA
# 
# if(condição):
#     comando
# else:
#     comando

#--------

# if(condição):
#     comando
# elif(condição):  -  *opcional*
#     comando
# else:  -  *opcional*
#     comando


# Faça uma calculadora de soma, subtração, multiplicação e divisão


num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

op = input("Digite a operação: ")

if(op == "+"):
    result = num1 + num2
    print(result)
elif(op == "-"):
    result = num1 - num2
    print(result)
elif(op == "*"):
    result = num1 * num2
    print(result)
elif(op == "/"):
    result = num1 / num2
    print(result)
else:
    print("Operação inválida.")

