#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[71]:


#passo 1 - Importar a base de dados para o phyton
#passo2 - vizualizar essa base de dados
    #entender as informações que você tem disponível
    #descobrir as cagadas da base de dados
#passo 3 - tratamento de dados
#passo 4 - análise inicial / análise global
#passo 5 - análise detalhada (buscar causa e solução dos cancelamentos)


# In[72]:


import pandas as pd
#passo 1 - Importar a base de dados para o phyton
tabela = pd.read_csv("telecom_users.csv")

#passo2 - vizualizar essa base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
display (tabela)

#entender as informações que você tem disponível
#descobrir as cagadas da base de dados


# In[73]:


#passo 3 - tratamento de dados
#analisar se o phyton está lendo as infomrações no formato correto.

print(tabela.info())
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")



# In[74]:


#será que existe alguma coluna completamente vázia?
tabela = tabela.dropna(how = "all", axis = 1)
#será que existe informação em alguma linha vazia?
tabela = tabela.dropna(how = "any", axis = 0)
print(tabela.info())


# In[75]:


#passo 4 Análise inicial / Global.
#Quantos clientes cancelaram e quantos não
print(tabela["Churn"].value_counts())
#0% de clientes que cancelaram e n cancelaram
print(tabela["Churn"].value_counts(normalize = True).map("{:.1%}".format))


# In[76]:


import plotly.express as px

# etapa 1: criar o gráfico
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    # etapa 2: exibir o gráfico
    grafico.show()


# ### Conclusões e Ações

# -Clientes com contrato mensal tem MUITO mais chance de cancelar:
# 
# -Podemos fazer promoções para o cliente ir para o contrato anual
# -Familias maiores tendem a cancelar menos do que famílias menores
# 
# -Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone
# -MesesComoCliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito
# 
# -A primeira experiência do cliente na operadora pode ser ruim
# -Talvez a captação de clientes tá trazendo clientes desqualificados
# -Ideia: a gente pode criar incentivo pro cara ficar mais tempo como cliente
# -QUanto mais serviços o cara tem, menos chance dele cancelar
# 
# -podemos fazer promoções com mais serviços pro cliente
# -tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes cancelarem
# 
# -Agir sobre a fibra
# -Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento
