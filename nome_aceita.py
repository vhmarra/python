import math

def testa_idade():
    name = input("Entre com o nome:") #get name

    try:
        age = int(input("Entre com idade:")) #get age
    except ValueError:
        print("Entre com um valor inteiro") #exception for integer numbers
    
    gender = input("Entre com o sexo m ou f:")#get gender

    if age < 18 and gender == 'f':
        print("Invalido")
    else:
        print("Valido")



testa_idade()
    