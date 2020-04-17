import math
import numpy
def conta_zeros():
    numeros = [] #declarando array vazio
    numeros = input("Entre com 0 ou 1:")#pegando numeros do teclado
    conta0 = numeros.count('0')
    print("0 count is:", conta0)

def conta_uns():
    numeros = [] #declarando array vazio
    numeros = input("Entre com 0 ou 1:")#pegando numeros do teclado
    conta1 = numeros.count('1')
    print("1 count is:", conta1)


#chamando funcao
conta_zeros()
conta_uns()
