import sys

# Obtendo a sequência de DNA e os 6 números inteiros a partir dos argumentos
dna_sequence = sys.argv[1]
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])
n5 = int(sys.argv[6])
n6 = int(sys.argv[7])
#print(type(n1))

# Verificando se a sequência de DNA é uma string e se os números são inteiros válidos
if not isinstance(dna_sequence, str):
    print("O primeiro argumento deve ser uma sequência de DNA (string)")
    sys.exit(1)

# Verificando se os números são maiores que o tamanho da sequência de DNA
for n in sys.argv[2:7]:
    #convertendo os valores para numeros inteirios, permitindo comparação
    if int(n) > len(dna_sequence):
        print("Um dos numeros passados é maior que o comprimento da sequencia de dna")
        sys.exit(1)

# Extraindo as sequências entre CDS, de acordo com os índices indicados nos argumentos
cds_1_2 = dna_sequence[n1-1:n2]
cds_2_3 = dna_sequence[n3-1:n4]

# Verificando se a sequência entre CDS 1 e CDS 2 começa com 'GT' e termina com 'AG'
if cds_1_2.startswith('GT') and cds_1_2.endswith('AG'):
    print(f"Sequência entre CDS 1 e CDS 2: {cds_1_2}")
else:
    print("A sequência entre CDS 1 e CDS 2 não começa com 'GT' ou não termina com 'AG'.")
    sys.exit(1)

# Verificando se a sequência entre CDS 2 e CDS 3 começa com 'GT' e termina com 'AG'
if cds_2_3.startswith('GT') and cds_2_3.endswith('AG'):
    print(f"Sequência entre CDS 2 e CDS 3: {cds_2_3}")
else:
    print("A sequência entre CDS 2 e CDS 3 não começa com 'GT' ou não termina com 'AG'.")
    sys.exit(1)

# Concatenando as sequências CDS 1, CDS 2 e CDS 3
cds_1 = dna_sequence[n1-1:n2]
cds_2 = dna_sequence[n2:n3]
cds_3 = dna_sequence[n4-1:n5]

# Imprimindo a sequência concatenada das CDS
final_sequence = cds_1 + cds_2 + cds_3
print(f"Sequência final concatenada das CDS 1, 2 e 3: {final_sequence}")
