import pyautogui
import time


#Passo 1 abrir o navegador

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(3) # Tempo de espera para abrir o navegador

#Passo 2 Logar no site da empresa

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # Tempo de espera para de o site carregar

pyautogui.click(x=732, y=414)
pyautogui.write("davi@gmail.com")
pyautogui.press("tab")
pyautogui.write("MinhaSenha")
pyautogui.press("enter")

#Passo 3 Importar os Dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#Passo4 Transcrever os Dados

for linha in tabela.index:
    pyautogui.click(x=720, y=292)
    # Pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # Preencher o campo
    pyautogui.write (str(codigo))

    # Pular para o próximo campo
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write (str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write (str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write (str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write (str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write (str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write (str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter") #Cadastrar o produto

    pyautogui.scroll(5000)

#Passo 5 Repetir o processo