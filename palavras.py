texto = input("Digite um texto: ")

palavras_longas = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)

if palavras_longas:
    print("Palavras longas encontradas:")
    for palavra in palavras_longas:
        print(palavra)

else:
    print("Nenhuma palavra longa foi encontrada no texto.")