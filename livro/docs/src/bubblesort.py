# Leia os dados em uma lista
dados = list(map(int, input().split()))

# Enquanto os dados não estiverem em ordem
num_dados = len(dados)
houve_troca = True
while houve_troca:
    houve_troca = False
    # Compare dos dados dois a dois
    for primeiro in range(num_dados - 1):
        segundo = primeiro + 1
        # Troque dados fora de ordem
        if dados[segundo] < dados[primeiro]:
            aux = dados[segundo]
            dados[segundo] = dados[primeiro]
            dados[primeiro] = aux
            houve_troca = True

# Apresente a lista
print(dados)