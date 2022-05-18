#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
# O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior
# 
# E-mail da diretoria: seugmail+diretoria@gmail.com<br>
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[1]:


import pyautogui
import pyperclip
import time

#Passo a passo algoritmo ultilizado.
#Passo 1: abrir o sistema
#passo 2: navegar no site até encontrar o banco de dados.
#passo 3: fazer a exportação do banco de vendas
#passo 4: calcular os indicadores (faturamento e quantidade de produtos vendidos)
#passo 5: enviar um e-mail para a diretoria com os indicadores.

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing") 
#pode ser qualquer sistema, só precisa ter o código e a ordem das coordenadas alterados.
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(4)

# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(298,300, clicks =2)

time.sleep(4)

#passo 3: Fazer o downlaod
pyautogui.click(298,300, button ="right")
time.sleep(4)
pyautogui.click(482,654)
time.sleep(4)
pyautogui.click(1346, 700)
#fechei a aba aberta no inferior da tela para não prejudicar na coordenada específica da minha última cédula de código.


# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# 
# - Faturamento
# - Quantidade de Produtos

# In[2]:


#passo 4: calcular os indicadores (faturamento e quantidade de produtos vendidos)
import pandas as pd 

tabela = pd.read_excel(r"C:\Users\Renan\Downloads\Vendas - Dez.xlsx")
#Varíavel tabela <- panda(pd) vai ler o arquivo em excel localizado no endereçamento posterior. 
#r serve para não ler caracteres especiais
display (tabela)
faturamento = tabela["Valor Final"].sum() #varíavel faturamento recebe a soma da coluna Valor Final localizado na varíavel tabela.
quantidade = tabela["Quantidade"].sum() #varíavel quantidade recebe a soma da coluna Quantidade localizado na varíavel tabela.


# ### Vamos agora enviar um e-mail pelo gmail

# In[ ]:


#passo 5 enviar um e-mail para a diretoria com os indicadores.
pyautogui.hotkey ("ctrl", "t")
pyperclip.copy ("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep (4)

pyautogui.click (28,197)
pyperclip.copy("seugmail+diretoria@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press ("tab")
time.sleep (2)
pyperclip.copy ("RELATÓRIO DE VENDAS - TESTE AUTOMAÇÃO DE DADOS EM PHYTON")
pyautogui.hotkey ("ctrl","v")
time.sleep (2)
pyautogui.press("tab")

#Definindo e-mail:
texto =f"""   
Bom dia,

Segue anexo a análise da planilha de vendas.

O faturamento de ontem foi de:R${faturamento:,.2f} 
A quantidade de produtos foi de:{quantidade:,}

Abs
Renan Leal - TESTE PHYTON """
#Enviando e-mail:
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(954, 693)
pyautogui.click(333,200)
pyautogui.doubleClick(480,178)
pyautogui.hotkey("ctrl", "enter")

#Análise de dados e envio dos indicadores efetuados em apenas 1m.

