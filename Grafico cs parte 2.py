#Grafico CS


from sqlite3 import DatabaseError
from turtle import bgcolor
from matplotlib.pyplot import figure
from numpy import size
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc,  Input, Output
from tomlkit import value
import plotly_express as px

#implantação do dash
app = Dash(__name__)


#criacao de grafico
fig = go.Figure()


#leitura dos dados da data base
df=pd.read_excel(r'Definitivo.xlsx')
df.dropna(inplace=True)                                     #retirada de dados nulos
df_array = df.values                                        #definição da array com os valores da db


#criação de listas vazias para receber os valores de cada coluna
ganhos_cs = []
datas = []
index = 0

#leitura dos arrays transformando em listas de cada coluna
for coluna in df_array:
    datas.append(coluna[0])

for coluna in df_array:
    ganhos_cs.append(coluna[20])

#--------------------retirada de dados vazios-------------------------

meses_coluna = []
for z in datas:                             #importação dos valores dos anos para a lista anos_coluna
    if z[5:] not in meses_coluna:
        meses_coluna.append(z[5:])

datas = datas[27:]
ganhos_cs = ganhos_cs[27:]
anos_coluna = ['Todos']                 #criação de uma lista para receber os anos pro callback, o Todos é 
contador = 0                                #por conta da função ter essa parte para mostrar todo o gráfico
for z in datas:                             #importação dos valores dos anos para a lista anos_coluna
    if z[:4] not in anos_coluna:
        anos_coluna.append(z[:4])

#--------------------------------------- implementação de funçoes do dash----------------------------

app.layout = html.Div([
    
    html.H1('Gráfico Prêmios por mês em campeonatos de Counter Strike'),                #titulo
    html.Div('''
    Gráfico relacionando meses com os prêmios cumulativos de cada ano, de 2012 a 2022'''),  #subtitulo
    html.Div(['Escolha um ano para destacar no gráfico:',                                    #dropdown
        dcc.Dropdown(id='anos_disponiveis', options= anos_coluna, value= 'Todos',
        searchable= True),                                          # opções recebe os anos, value mostra o valor inicial
                                                                    # inicial, serchable deixa o usuario pesquisar
     ]),
     dcc.Graph(id='grafico cs principal', figure= fig),

])

#----------------------------------------callback-------------------------------------
@app.callback(
    Output(component_id= 'grafico cs principal', component_property='figure'),
    [Input(component_id= 'anos_disponiveis', component_property= 'value')]
)
 
def update_graph(anos_disponiveis):
    x_function = []
    i = 0
    if anos_disponiveis != 'Todos':
        while i <12:
                x_function.append(anos_disponiveis)
                i += 1
        for a in range(len(x_function)):
            x_function[a] = str(x_function[a]) + ' ' + meses_coluna[a] 
        
    if anos_disponiveis == 'Todos':
        x_function = datas
    ganhos_especificados = []
    for z in range(len(datas)):
        if datas[z] in x_function:
            ganhos_especificados.append(ganhos_cs[z])
    if anos_disponiveis == '2012':
        i=0
    while i <3:
        ganhos_especificados.insert(0, 0)
        
        i +=1
    grafico = fig.update_traces(x= x_function, y = ganhos_especificados)
    return (grafico)





#confecção de uma lista geral com formato ano/valor
lista_all = []
index = 0
for a in datas:
    for c in ganhos_cs:
        lista_all.append(a)
        lista_all.append(ganhos_cs[index])
        index += 1
        break




#-----------------------------------------organização do eixo y do grafico----------------------------------------
fig.update_yaxes(title = 'Prêmios', title_font_color = 'white',
                 title_font_family = "Overpass",
title_font_size = 20, showgrid= True)


#------------------------------------organização do eixo x do grafico--------------------------------------
fig.update_xaxes(title = 'Ano', title_font_color = 'white',
                 title_font_family = "Overpass",
title_font_size = 20, showgrid=False)


#------------------------------------organização do titulo do grafico-----------------------------------------
fig.update_layout(title = 'Prêmios de campeonatos de CS:GO',
                  plot_bgcolor= 'black' ,
 paper_bgcolor='black', 
 title_yanchor= 'top', title_xref= 'paper', title_yref= 'paper',
 title_font_family = "Gravitas One", title_font_size = 30,
 font=dict(color='white'))


# ativação da legenda para a ativação e desativação do grafico
fig.update_layout(showlegend= True)


# criação da linha para o grafico de linhas
fig.add_trace(go.Scatter(x=datas, y=ganhos_cs, name =  '',
                         line = dict(color='lightskyblue', width=3,
)))

#---------------------------- criação das bolinhas--------------------------
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=datas,
        y=ganhos_cs,
        marker=dict(
            color='aquamarine',
            size=5,

        ),

        showlegend=False

    )
)



if __name__ == '__main__' :
    app.run_server(debug=True)