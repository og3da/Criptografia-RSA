from itertools import repeat
import random
import sympy
from sympy import *

#tabela de dominio publico em que o usuario digita o valor da letra inicial
tabela = {
    1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:'', 12:'', 13:'', 14:'', 15:'', 16:'', 17:'', 18:'', 19:'', 20:'', 21:'', 22:'', 23:'', 24:'', 25:'', 26:'' 
}
x=1    

# CRIPTOGRAFIA RSA
alfabeto= 'abcdefghijklmnopqrstuvwxyz'
palavra=input("Digite a palavra a se criptografar: ")
palavra=palavra.lower() #convertendo para minusculo
valoresTabela=int(input("Digite o primeiro valor da tabela publica(>=10): ")) 
preCod=''
for x in tabela: #inserindo valor inicial da tabela(A) e os seguintes são= A+1
    tabela.update({x:valoresTabela})
    valoresTabela=valoresTabela+1
print("Valores inseridos na tabela...")

for caractere in palavra:   #trocando cada caractere digitado na 'palavra' por uma posição na tabela para formar a pré-cod
    posicao= alfabeto.find(caractere)
    novaPosicao= tabela[posicao+1]
    preCod += str(novaPosicao)

print("Pré-Codificação: ",preCod)
#print(preCod.split('-'))

print("Gerando par de numeros primos...")
p=sympy.randprime(1,200)
q=sympy.randprime(1,200)
print("valor de p: ",p)
print("valor de q: ",q)
print("")
print("Definindo valor de n e φ...")
n=p*q
o=(p-1)*(q-1)
print("valor de n: ",n)
print("valor de φ: ",o)
print("")
print("Calculando fatores primos de φ...")
fatoresPrimos=primefactors(o)
print(fatoresPrimos)
print("")
print("Definir valor de e> Escolhendo qualquer valor menor que φ, que não seja divisível pelos fatores primos")
notValid=1
while notValid==1:
    e=random.randint(1,o)
    teste=igcd(e,o) #testar se o valor de 'e' não é divisivel/multiplo de 'φ'. Se sim gera outro valor aleatorio.
    if(teste!=1):
        continue
    else:
        notValid=2
print("valor de e: ",e)
print("")
blocos=int(input("Divida a pré codificação em blocos b (b<n): ")) #afazer

#parei na página 7