from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('Definitivo.xlsx')
df_array = df.values

######################################################### PRIMEIRO ###################################################


Tudo = []

for i in df_array:
    (Ano) = i[0].split()[0]
    Ano = int(Ano)
    (Street_V) = (i[5])
    (lol) = (i[9])
    (Street_p) = (i[1])
    (Lol_p) = (i[26])
    Tudo.append([Ano, Street_V, lol, Street_p, Lol_p])


def Filtro(Data):
    Final = [x for x in Tudo if x[0] == Data]
    return Final


anoop = []
for x in Tudo:
    anoop.append(x[0])
anoop = sorted(set(anoop))
pitagoras = str(anoop)

# filtrado = filter(lambda t: t[0] == 2021,Tudo)

jogos = []
views = []
players = []
Streetmax = Lolmax = Streetpmax = Lolpmax = 0






############################################# SEGUNDO #############################################################################################


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

fig = px.line(NovaLista, x=0, y=[
              1, 2], markers=True, title='Street Fighter V - Ganho de jogadores e jogadores médios')


def visualfig(fig):  # Função que altera o visual do gráfico
    fig.update_xaxes(rangeslider_visible=True, title='Data')
    fig.update_yaxes(title='Valor')
    fig.layout.template = 'plotly_dark'


############################################################### TERCEIRO #########################################################################


# criacao de grafico
fig1 = go.Figure()

# leitura dos dados da data base
df.dropna(inplace=True)  # retirada de dados nulos
# definição da array com os valores da db

# criação de listas vazias para receber os valores de cada coluna
ganhos_cs = []
datas = []


# leitura dos arrays transformando em listas de cada coluna
for coluna in df_array:
    datas.append(coluna[0])

for coluna in df_array:
    ganhos_cs.append(coluna[20])


# --------------------retirada de dados vazios-------------------------

meses_coluna = []
for z in datas:  # importação dos valores dos anos para a lista anos_coluna
    if z[5:] not in meses_coluna:
        meses_coluna.append(z[5:])

datas = datas[27:]
ganhos_cs = ganhos_cs[27:]
# criação de uma lista para receber os anos pro callback, o Todos é
anos_coluna = ['Todos']
contador = 0  # por conta da função ter essa parte para mostrar todo o gráfico
for z in datas:  # importação dos valores dos anos para a lista anos_coluna
    if z[:4] not in anos_coluna:
        anos_coluna.append(z[:4])


####################################################################################### QUARTO #################################################


# filtragem  de anos
dt = []
for d in df_array:
    dt.append(d[0])
dtf = []
for d in dt:
    for v in range(2016, 2023):
        if str(v) in d:
            dtf.append(d)

# dados do grafico
views = []
for p in df_array:
    if int(p[0][0:4]) in range(2016, 2023):
        views.append(p[9])
stream = []
for s in df_array:
    if int(s[0][0:4]) in range(2016, 2023):
        stream.append(s[16])

fig = px.bar(x=dtf, y=[views, stream], barmode='group', labels={
             'x': 'Anos', "value": 'Views', 'variable': 'Audiencia'},)


######################################################################################### QUINTO ##################################################################


# declara variáveis
anos_dx = []
faturamento = []
anos_dxTemp = []
faturamentoTemp = []
fig2 = go.Figure()

# Valores nos Eixos


def dadosorg():
    db = pd.read_excel('Jogos (1).xlsx')
    Base = db.values
    for coluna in Base:
        anos_dx.append(coluna[0])
    for coluna in Base:
        faturamento.append(coluna[1])


# Mudança na linha
def carregarMudancasLinha(anos_dx, faturamento):
    fig2.data = []
    fig2.add_trace(
        go.Scatter(
            x=anos_dx,
            y=faturamento,
            name='',
            line=dict(
                color='red',
                width=3
            )
        )
    )

    fig2.add_trace(
        go.Scatter(
            mode='markers',
            x=anos_dx,
            y=faturamento,
            marker=dict(
                color='yellow',
                size=5
            )
        )
    )
    fig2.layout.template = 'plotly_dark'
    fig2.update()
# plot do grafico


dadosorg()
fig2 = go.Figure()

# Legenda
fig2.update_layout(showlegend=False)


carregarMudancasLinha(anos_dx, faturamento)
# dashbord creation
opcoes = list(anos_dx)
opcoes.append("Todos anos")


######################################################################################## CONFIGURAÇÃO DO DASH ###############################################


#########################################################################################################################################################


app = Dash(__name__)

app.layout = html.Div(children=[

    html.Div(children=[
        html.Div(className="grafico11", children=[
            html.H1(children='Comparações de números'),
            html.Div(id='body-div'),
            dcc.Graph(id='g'),
            dcc.Dropdown(options=anoop, value="2021",
                         id='data', clearable=False),
            dcc.Dropdown(options=['Players x Players',
                                  'Views x Views'], value='Views x Views', id='tag'),
        ]),

    html.Div(className="grafico22",children=[
            html.Div(style={'backgroundColor': '#111111'}, children=[
                html.H2(
                    children='SFV',
                    style={'textAlign': 'center',
                           'color': '#ffffff', 'font': 'Arial'}
                ),

                dcc.Graph(  # Imprime o gráfico
                    id='gráfico1',
                    figure=fig
                ),
                html.Div(  # Dropdown
                    dcc.Dropdown(options=AnosDif, value='', multi=True, searchable=False, placeholder='Selecione os anos',
                                 id='Escolha de Anos'
                                 )),
            ]),
        ]),
    ]),

    html.Div(children=[
        html.Div(children=[html.Div([
        html.H3('Gráfico Prêmios por mês em campeonatos de Counter Strike'),  # titulo
        html.Div('''
        Gráfico relacionando meses com os prêmios cumulativos de cada ano, de 2012 a 2022'''),  # subtitulo
        html.Div(['Escolha um ano para destacar no gráfico:',  # dropdown
            dcc.Dropdown(id='anos_disponiveis', options=anos_coluna, value='Todos',
            searchable=True),  # opções recebe os anos, value mostra o valor inicial
                  # inicial, serchable deixa o usuario pesquisar
                ]),
        dcc.Graph(id='grafico cs principal', figure=fig1),

    html.Div(children=[ html.Div(children=[
        html.H4(children='Grafico Audiencia league'),

        html.Div(children='Espectadores League of Legends'
                 ),
        dcc.Dropdown(['views', 'stream', 'Geral'], value='Geral', id='Anos'),

        dcc.Graph(
            id='Grafico audiencia',
            figure=fig
        )
    ]),
    ])

    ]),
    ]),
    ]),
    html.Div(children=[
        html.H5(children='Faturamento da industria de jogos'),
        html.H6(id="header2"),

        html.Div(children='''
            OBS: Ano de 2022 é uma estimativa.
        '''),

        dcc.Dropdown(opcoes, value='Todos anos', id='anoref'),

        dcc.Graph(
            id='grafico_faturamento',
            figure=fig2
        ),
    ]),

])


################################################################################### PRIMERIO CALLBACK #########################################################


@app.callback(

    Output("g", "figure"),
    Input('data', 'value'),
    Input('tag', 'value')
)
def upadte_graph(data, tag):
    value = int(data)
    Final = Filtro(Data=value)

    Ano = []
    Street_V = []
    Lol_v = []
    Street_P = []
    Lol_p = []

    for i in Final:
        Ano.append(i[0])
        Street_V.append(i[1])
        Lol_v.append(i[2])
        Street_P.append(i[3])
        Lol_p.append(i[4])

    Streetmax = sum(Street_V)
    Lolmax = sum(Lol_v)
    Streetpmax = sum(Street_P)
    Lolpmax = sum(Lol_p)

    jogos = ['StreetFigheter ', 'League of Legends']
    views = [Streetmax, Lolmax]
    players = [Streetpmax, Lolpmax]

    if tag == 'Players x Players':
        fig = px.pie(values=players, names=jogos )
        fig.layout.template = 'plotly_dark'
        return fig
    elif tag == 'Views x Views':
        fig = px.pie(values=views, names=jogos)
        fig.layout.template = 'plotly_dark'
        return fig



########################################################################## SEGUNDO CALLBACK #######################################################


@app.callback(
    Output('gráfico1', 'figure'),
    Input('Escolha de Anos', 'value')
)
def update_output(value):  # Função que atualiza o gráfico
    ano = list(value)
    ListaFiltrada = []
    for z in NovaLista:
        for e in ano:
            if e in z[0]:
                ListaFiltrada.append(z)
    if (len(ListaFiltrada) == 0):
        ListaFiltrada = NovaLista

    fig = px.line(ListaFiltrada, x=0, y=[1, 2], markers=True,
                  title='Street Fighter V - Ganho de jogadores e jogadores médios')
    visualfig(fig)

    return fig


################################################################################################## TERCEIRO CALLBACK ####################################################


@app.callback(
    Output(component_id='grafico cs principal', component_property='figure'),
    [Input(component_id='anos_disponiveis', component_property='value')]
)
def update_graph(anos_disponiveis):
    x_function = []
    i = 0
    if anos_disponiveis != 'Todos':
        while i < 12:
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
        i = 0
    while i < 3:
        ganhos_especificados.insert(0, 0)

        i += 1
    grafico = fig1.update_traces(x=x_function, y=ganhos_especificados)
    return (grafico)




# -----------------------------------------organização do eixo y do grafico----------------------------------------
fig1.update_yaxes(title='Prêmios', title_font_color='white',
                  title_font_family="Overpass",
                  title_font_size=20, showgrid=True)

# ------------------------------------organização do eixo x do grafico--------------------------------------
fig1.update_xaxes(title='Ano', title_font_color='white',
                  title_font_family="Overpass",
                  title_font_size=20, showgrid=False)

# ------------------------------------organização do titulo do grafico-----------------------------------------
fig1.update_layout(title='Prêmios de campeonatos de CS:GO',
                   plot_bgcolor='black',
                   paper_bgcolor='black',
                   title_yanchor='top', title_xref='paper', title_yref='paper',
                   title_font_family="Gravitas One", title_font_size=30,
                   font=dict(color='white'))

# ativação da legenda para a ativação e desativação do grafico
fig1.update_layout(showlegend=True)

# criação da linha para o grafico de linhas
fig1.add_trace(go.Scatter(x=datas, y=ganhos_cs, name='',
                          line=dict(color='lightskyblue', width=3,
                                    )))

# ---------------------------- criação das bolinhas--------------------------
fig1.add_trace(
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


############################################################################################################## QUARTO CALLBACK #######################################################


@app.callback(
    Output("Grafico audiencia", 'figure'),
    Input("Anos", 'value')
)
def update_output(value):
    if value == 'views':
        fig = px.bar(x=dtf, y=[views], barmode='group')
        fig.layout.template = 'plotly_dark'
        return fig
    elif value == 'stream':
        fig = px.bar(x=dtf, y=[stream], barmode='group')
        fig.layout.template = 'plotly_dark'
        return fig
    elif value == 'Geral':
        fig = px.bar(x=dtf, y=[views, stream], barmode='group', labels={
                     'x': 'Anos', "value": 'Views', 'variable': 'Audiencia'},)
        fig.layout.template = 'plotly_dark'
        return fig

############################################################################################################## QUINTO CALLBACK ############################################################


@app.callback(
    Output('grafico_faturamento', 'figure'),
    Input('anoref', 'value')
)
def update_output(value):
    if value == "Todos anos":
        carregarMudancasLinha(anos_dx, faturamento)
    else:
        pos = anos_dx.index(value)
        iArray = len(anos_dx) - 1

        if (pos == 0):
            i = pos
            while i < 3:
                anos_dxTemp.append(anos_dx[i])
                faturamentoTemp.append(faturamento[i])
                i += 1
        elif (pos == iArray):
            i = pos - 2
            fim = i + 3
            while i < fim:
                anos_dxTemp.append(anos_dx[i])
                faturamentoTemp.append(faturamento[i])
                i += 1
        else:
            i = pos - 1
            fim = i + 3
            while i < fim:
                anos_dxTemp.append(anos_dx[i])
                faturamentoTemp.append(faturamento[i])
                i += 1
        carregarMudancasLinha(anos_dxTemp, faturamentoTemp)
        anos_dxTemp.clear()
        faturamentoTemp.clear()
    return fig2


##############################################################################################################
if __name__ == '__main__':
    app.run_server(debug=True)








