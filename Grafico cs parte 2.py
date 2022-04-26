#Grafico CS


from sqlite3 import DatabaseError
from turtle import bgcolor
from matplotlib.pyplot import figure
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
df=pd.read_excel(r'Data base definitivo.xlsx')
df.dropna(inplace=True)                                     #retirada de dados nulos
df_array = df.values                                        #definição da array com os valores da db


#criação de listas vazias para receber os valores de cada coluna
ganhos_cs = []
datas = []
index = 0
df_array


#leitura dos arrays transformando em listas de cada coluna
for coluna in df_array:
    datas.append(coluna[0])

for coluna in df_array:
    ganhos_cs.append(coluna[20])

#--------------------retirada de dados vazios-------------------------

datas = datas[27:]
ganhos_cs = ganhos_cs[27:]


#--------------------------------------- implementação de funçoes do dash----------------------------

app.layout = html.Div([
    
    html.H1('Gráfico Prêmios por mês em campeonatos de Counter Strike'),
    html.Div('''
    Gráfico relacionando meses com os prêmios cumulativos de cada ano, de 2012 a 2022'''),
    html.Div(['Escolha um ano para destacar no gráfico',
        dcc.Dropdown(id='anos_disponiveis', options= [
            {'label': 'Todos', 'value': 'data'},
            {'label': '2012', 'value' : '2012'},
            {'label': '2013', 'value' : '2013'},
            {'label': '2014', 'value' : '2014'},
            {'label': '2015', 'value' : '2015'},
            {'label': '2016', 'value' : '2016'},
            {'label': '2017', 'value' : '2017'},
            {'label': '2018', 'value' : '2018'},
            {'label': '2019', 'value' : '2019'},
            {'label': '2020', 'value' : '2020'},
            {'label': '2021', 'value' : '2021'},
            {'label': '2022', 'value' : '2022'},
        ], value= 'Todos',
        searchable= True),
        html.Div(id= 'container_escolha'),
        html.Br(),
     ]),
     dcc.Graph(id='grafico cs principal', figure= fig),

])

#----------------------------------------callback-------------------------------------
@app.callback(
    Output(component_id= 'grafico cs principal', component_property='figure'),
    [Input(component_id= 'anos_disponiveis', component_property= 'value')]
)
 
def update_graph(anos_disponiveis):
    '''
    dff = df
    meses = ['janeiro', 'fevereiro','março','abril','maio','junho',
    'julho','agosto','setembro','outubro','novembro', 'dezembro']
    x_function = []
    i = 0
    if anos_disponiveis != 'Todos':
        while i <12:
                x_function.append(anos_disponiveis)
                i += 1
        for a in range(len(x_function)):
            x_function[a] = str(x_function[a]) + ' ' + meses[a]
            print (x_function) 
    if anos_disponiveis == "Todos":
        x_function = datas
    ganhos_especificados = []
    for a in datas:
        for c in a:
            if x_function[:4] in list(c):
                ganhos_especificados.append(ganhos_cs[index(a)])
    grafico = px.line(data_frame= dff,
     x=x_function, y= ganhos_especificados, markers= True)
     '''
    return 








    datas_select = []
    #anos = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
    meses = ['janeiro', 'fevereiro','março','abril','maio','junho',
    'julho','agosto','setembro','outubro','novembro', 'dezembro']
    if value != 0:
        i = 0
        while i <12:
            datas_select.append(value)
            i += 1
        for a in range(len(datas_select)):
            datas_select[a] = str(datas_select[a]) + ' ' + meses[a]
            print (datas_select)      
    datas_select = datas
    return fig



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