from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_excel('Definitivo.xlsx')
df_array = df.values

Data1 = []
for colunas in df_array:
    Data1.append(colunas[0])

all = []
for n in Data1:
    for time in range(2016, 2022):
        if str(time) in n:
            all.append(n)

Usuarios1 = []
for linha in df_array:
    if not linha[1] == 0:
        Usuarios1.append(linha[1])

Usuarios1.insert(0, 0)

Ganho1 = []
for linha in df_array:
    if not linha[2] == 0:
        Ganho1.append(linha[2])

Ganho1.insert(0, 0)

NovaLista = []
contador = 0
for n in all:
    NovaLista += [[all[contador], Usuarios1[contador], Ganho1[contador]]]

    contador += 1

AnosDif = []
for a in NovaLista:
    x = a[0].split()
    if x[0] not in AnosDif:
        AnosDif.append(x[0])

fig = px.line(NovaLista, x=0, y=[1, 2], markers=True, title='Street Fighter V - Ganho de jogadores e jogadores médios')

def visualfig(fig):      #Função que altera o visual do gráfico
    fig.update_xaxes(rangeslider_visible=True, title='Data')
    fig.update_yaxes(title='Valor')
    fig.layout.template = 'plotly_dark'

#------------------Layout---------------------------------

app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#111111'}, children=[
    html.H1(
        children='SFV',
        style={'textAlign': 'center','color': '#ffffff','font':'Arial'}
    ),

    dcc.Graph(  #Imprime o gráfico
        id='gráfico1',
        figure=fig
    ),
    html.Div(  #Dropdown
    dcc.Dropdown(options=AnosDif, value='', multi=True, searchable=False, placeholder='Selecione os anos', id = 'Escolha de Anos'
   ))
])

@app.callback(
    Output('gráfico1', 'figure'),
    Input('Escolha de Anos', 'value')
)
def update_output(value):  #Função que atualiza o gráfico
    ano = list(value) 
    ListaFiltrada = []
    print(ano)
    for z in NovaLista:
        for e in ano:
            if e in z[0]:
                ListaFiltrada.append(z)
    if(len(ListaFiltrada) == 0):
        ListaFiltrada = NovaLista
    
    fig = px.line(ListaFiltrada, x=0, y=[1, 2], markers=True, title='Street Fighter V - Ganho de jogadores e jogadores médios')
    visualfig(fig)
    
    return fig 

if __name__ == '__main__':
    app.run_server(debug=True)

