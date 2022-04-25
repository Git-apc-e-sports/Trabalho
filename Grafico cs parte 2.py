#Grafico CS


from sqlite3 import DatabaseError
from matplotlib.pyplot import figure
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc,  Input, Output
from tomlkit import value


#implantação do dash
app = Dash(__name__)


#leitura dos dados da data base
df=pd.read_excel(r'Data base definitivo.xlsx')
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

datas = datas[27:]
ganhos_cs = ganhos_cs[27:]


#confecção de uma lista geral com formato ano/valor
lista_all = []
index = 0
for a in datas:
    for c in ganhos_cs:
        lista_all.append(a)
        lista_all.append(ganhos_cs[index])
        index += 1
        break



#criacao de grafico
fig = go.Figure()


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


#--------------------------------------- implementação de funçoes do dash----------------------------

app.layout = html.Div(children=[
    
    html.H1(children='Gráfico Prêmios por mês em campeonatos de Counter Strike'),
    html.Div(children='''
    Gráfico relacionando meses com os prêmios cumulativos de cada ano, de 2012 a 2022'''),
    dcc.Graph(id='grafico cs principal', figure=fig),
    html.Div(['Escolha um ano para destacar',
        dcc.Dropdown(options= [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022],
     value= '', multi=True,id='anos_disponiveis'),
        html.Div(id= 'container_escolha'),
        html.Br(),
     ]),

])

    
@app.callback(
    Output('grafico cs principal', figure),
    Input('anos_disponiveis', 'value')
)
    
def update_layout(value):
    print(value)
    datas_select = []
    datas = []
    df=pd.read_excel(r'Data base definitivo.xlsx')
    df.dropna(inplace=True)                                     #retirada de dados nulos
    df_array = df.values                                        #definição da array com os valores da db

    for coluna in df_array:
        datas.append(coluna[0])

    datas = datas[27:]
    data = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
    for c in data:
        if c == value:
            datas_select.append(c)
    if datas_select == []:
        datas_select = datas
    for a in datas:
        for c in datas_select:
            if c == a[:4]:
                datas_select.append(a)
    if datas_select[0] == value:
        datas_select.remove[0]
    datas = datas_select
    return figure



if __name__ == '__main__' :
    app.run_server(debug=True)