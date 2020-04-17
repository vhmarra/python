import random
import sys

def pedra_papel_tesoura():
    possibilidades = ["pedra","papel","tesoura"]
    maquina_joga = possibilidades[random.randint(0,2)]
    pessoa_joga = input("Faça sua jogada: ")
    
    if(maquina_joga == "papel" and pessoa_joga == "tesoura") or (maquina_joga == "pedra" and pessoa_joga == "papel") or (maquina_joga == "tesoura" and pessoa_joga == "pedra"): #VITORIA
        return "VITORIA"
    
    elif(pessoa_joga == maquina_joga): #EMPATE
        return "EMPATE"
    
    else: #DERROTA
        return "DERROTA"



if __name__ == "__main__":
    vitorias = 0
    empates = 0
    derrotas = 0
    rounds_jogados = 0
    jogando = True

    print("=====BEM VINDO AO JOGO PEDRA PAPEL TESOURA=====")
    if input("Deseja iniciar? S/n: ") == "n":
        print("TCHAU ATÈ A PROXIMA")
        exit()
    else:
        while jogando:
            jogar = pedra_papel_tesoura()
            rounds_jogados =+ 1
            if jogar == "VITORIA":
                print("VITORIA")
                vitorias =+1
            elif jogar == "EMPATE":
                print("EMPATE")
                empates =+1
            else:
                print("DERROTA")
                derrotas =+1
            if input("Deseja jogar novamente? S/n: ") == "n":
                print("==FIM DE JOGO==")
                print("Rodadas: ", rounds_jogados)
                print("Vitorias: ", vitorias)
                print("Derrotas: ", derrotas)
                print("Empates: ", empates)
                print("===================")
                exit()
