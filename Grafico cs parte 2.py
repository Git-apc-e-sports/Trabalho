# Grafico CS


import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('Tabela_dinheiro_por_ano.xlsx')

df_array = df.values

anos_px = []
for coluna in df_array:
    try:
        anos_px.append(coluna[0])
    except:
        continue
anos_px_total = 0
anos_px_filtragem = []
total = []
premio_total = []
for coluna in df_array:
    try:
        premio_total.append(coluna[1])
    except:
        continue

fig = go.Figure()

fig.update_yaxes(title='Prêmios', title_font_color='black',
                 title_font_family="Overpass",
                 title_font_size=20, showgrid=True)

fig.update_xaxes(title='Ano', title_font_color='black',
                 title_font_family="Overpass",
                 title_font_size=20, showgrid=False)

fig.update_layout(title='Prêmios de campeonatos de CS:GO', title_pad_r=10000,
                  plot_bgcolor='#edbb05',
                  paper_bgcolor='#bd9c24', title_xanchor='left',
                  title_yanchor='top', title_xref='paper', title_yref='paper', title_x=0.23,
                  title_font_family="Gravitas One", title_font_size=30,
                  font=dict(color='black'))

fig.update_layout(showlegend=True)

fig.add_trace(go.Scatter(x=anos_px, y=premio_total, name='',
                         line=dict(color='black', width=3,
                                   )))
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=anos_px,
        y=premio_total,
        marker=dict(
            color='white',
            size=10,

        ),

        showlegend=False

    )
)

fig.show()
