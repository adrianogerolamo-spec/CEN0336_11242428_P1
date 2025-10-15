#recebendo input do usuario e convertendo para numeros inteiros e flutuante
print("este script calcula o crescimento de uma população ao longo do tempo")

Po = int(input("Digite o tamanho inicial da população: "))

r = float(input("Digite a taxa de crescimento anual (em decimal): "))

t = int(input("Digite o número de anos:"))

#loop for, com o range baseado nos anos fornecidos, num range iniciado em 1
for i in range(1,t):
    Pt = Po * (1+r)**i
    print("ano {}: {:<20}".format(i,Pt))
