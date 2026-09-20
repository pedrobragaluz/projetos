import requests as req
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

pokemons = ["pikachu", "charizard", "bulbasaur","Mewtwo",""]

janela = Tk()
janela.title("Pokémons")

imagens = []

for cod, pkm in enumerate(pokemons):

    endpoint = f"https://pokeapi.co/api/v2/pokemon/{pkm}"
    resposta = req.get(endpoint)

    if resposta.status_code == 200:

        vetor = resposta.json()

        nome_pokemons = vetor["name"].capitalize()
        link_imagens = vetor["sprites"]["front_default"]

        linha = cod // 3
        coluna = cod % 3

        baixar_img = req.get(link_imagens)

        img = Image.open(BytesIO(baixar_img.content))
        img = img.resize((100, 100))

        imagem_tk = ImageTk.PhotoImage(img)

        imagens.append(imagem_tk)

        label_pkm_nome = Label(
            janela,
            text=nome_pokemons
        )

        label_pkm_nome.grid(
            row=linha * 2,
            column=coluna,
            pady=(15, 5)
        )

        label_imagem = Label(
            janela,
            image=imagem_tk
        )

        label_imagem.grid(
            row=linha * 2 + 1,
            column=coluna,
            padx=20,
            pady=(0, 20)
        )

    else:
        print("POKÉMON NÃO ENCONTRADO")

janela.mainloop()