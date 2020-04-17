#Estimating Pi using the Monte Carlo Method#S

import random
import math

def estimate_pi(numero):
    numero_no_circulo = 0
    numero_total = 0
    for _ in range(numero):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 1:
            numero_no_circulo = numero_no_circulo+1
        numero_total = numero_total+1
    
    return 4*numero_no_circulo/numero_total
   
