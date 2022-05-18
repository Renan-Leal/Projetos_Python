#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[2]:


#Sempre estruturar o código por passo a passo antes de traduzir para phyton.
from selenium import webdriver #controlar o navegador
from selenium.webdriver.common.keys import Keys #controlar o teclado
from selenium.webdriver.common.by import By #lozalizar os itens no navegador

# criar o navegador
navegador = webdriver.Chrome()
# entrar no google e pesquisar cotação do dólar
navegador.get("https://www.google.com.br/")

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação do dólar")

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#pegaria a cotação do dólar

cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#entraria no google e pesquisaria a cotação do euro

navegador.get("https://www.google.com.br/")

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação do euro", Keys.ENTER)

#pegaria a cotação do euro
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print (cotacao_euro, cotacao_dolar)

#entraria no google e pesquisaria a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

#pegaria a cotação do ouro num site especcífico https://www.melhorcambio.com/ouro-hoje
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')

#fechar o navegador
navegador.quit()

cotacao_ouro = cotacao_ouro.replace(',','.')
display (cotacao_dolar, cotacao_euro, cotacao_ouro)





# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# - Importando a base de dados

# In[3]:


#importar a base de dados
import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')


#aualizar a cotação na base de dados
#tabela.loc(linha,coluna)
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)

#cotação do euro
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)

#cotação do ouro
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)



# - Atualizando os preços e o cálculo do Preço Final

# In[4]:


#Atualizar preço de compra e venda
#preço de compra = preço original x cotacao
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

#preço de venda = preço de compra x margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
display(tabela)


# ### Agora vamos exportar a nova base de preços atualizada

# In[5]:


#exportar essa base de dados para ter o resultado atualizado
tabela.to_excel("ProdutosNovo.xlsx", index = False)

