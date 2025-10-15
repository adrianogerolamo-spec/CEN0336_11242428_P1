import sys

#recebendo argumentos pela linha de comando e transformando em numeros inteiros
a = int(sys.argv[1])
b = int(sys.argv[2])

#checando se os numeros sao menores que 500
if a<500 and b<500:
    A = (a*b)/2
    print("A área do triangulo retângulo com lados a=X e b=Y, é {}".format(A))
else:
    #ensinando o usuario a usar o script
    print("este é um script que calcula a área de um triangulo \npara utiliza-lo, coloque dois numeros inteiros como parametros na linha de comando, como demonstrado a seguir: \npython3 script_area.py <numero> <numero> \nambos os numeros devem ser menores que 500")

