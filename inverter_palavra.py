import string

def revert_string():
    concerta = ""
    palavra = input("Entre com a palavra: ")#receber palavras
    palavra_revertida = [] #reserva array para palavra invertida
    contador = len(palavra)
    while contador > 0: #loop para inverter palavras e armazenar no array
        palavra_revertida += palavra[contador-1]
        contador = contador-1
    final_revertida = (concerta.join(palavra_revertida)) #transforma o array em string
    print(final_revertida)




revert_string()