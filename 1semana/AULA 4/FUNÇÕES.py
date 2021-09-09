# def nomeDaFuncao(parametro):
#     comando
#     return - para retornar um valor ao código principal



# Faça uma calculadora com funções

def soma(n1,n2):
    result = n1 + n2
    print("Resultado: ", result)

def sub(n1,n2):
    result = n1 - n2
    return result

def mult(n1,n2):
    result = n1 * n2
    return result

def div(n1,n2):
    result = n1 / n2
    return result

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

op = input("Operação: ")

if(op == "+"):
    soma(num1,num2)
elif(op == "-"):
    print("Resultado: ", sub(num1,num2))
elif(op == "*"):
    print("Resultado: ",mult(num1,num2))
elif(op == "/"):
    print("Resultado: ", div(num1,num2))