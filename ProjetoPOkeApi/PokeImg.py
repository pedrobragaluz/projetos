import requests as req
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

pokemons = ["pikachu", "charizard", "bulbasaur",]

janela = Tk()
janela.title(" POKEMON API TESTE")

for cod, pkm in enumerate(pokemons):
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{pkm}"
    resposta = req.get(endpoint)

    if resposta.status_code == 200:

        vetor = resposta.json()

        img = vetor['sprites']['front_default']

        baixar_imagem = req.get(img)
        imgtk = Image.open(BytesIO(baixar_imagem.content))
        imagem = imgtk.resize(250, 250)
