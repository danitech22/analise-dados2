notas = []

while True:
    entrada = input("Digite uma nota (0 a 10) ou 'fim': ")

    if entrada == "fim":
        break

    notas.append(float(entrada))

quantidade = len(notas)
media = sum(notas) / quantidade
maior = max(notas)
menor = min(notas)

boas_notas = 0
for nota in notas:
    if nota >= 7:
        boas_notas += 1

print("Quantidade de notas:", quantidade)
print("Nota média:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Notas >= 7:", boas_notas)


