# Aperçu

Dash est un excellent outil utilisé par beaucoup pour l'analyse de données, l'exploration de données,
visualisation, modélisation, contrôle des instruments et création de rapports.

L'exemple suivant illustre une application Dash hautement réactive et personnalisée
avec peu de code.

<!-- prettier-ignore -->
!!! danger "Exécution de votre serveur Notebook et accès au port"
     Lorsque vous exécutez un outil de votre Jupyter Notebook qui publie un site Web sur un port,
     vous ne pourrez pas simplement y accéder depuis `http://localhost:5000/` car
     normalement suggéré dans la sortie lors de l'exécution de l'application Web.

     Pour accéder au serveur Web, vous devrez utiliser l'URL de base. Dans ton cahier
     exécution terminale :

     ```python
     echo https://kubeflow.covid.cloud.statcan.ca${JUPYTER_SERVER_URL:19}proxy/5000/
     ```

## Visualisation des données avec Dash

Dash simplifie la création d'une interface graphique interactive autour de votre code d'analyse de données.
Ceci est un exemple de mise en page avec figure et curseur de
[Dash](https://dash.plotly.com/basic-callbacks).

![dash_plot](../images/plot.png)

### Complot Dash

_Publier avec des logiciels fabriqués au Canada._

**[Plotly Dash](/2-Publishing/Dash/)** est une bibliothèque Python populaire qui vous permet de créer facilement des visualisations et des tableaux de bord Web interactifs. Développé par la société montréalaise Plotly, Dash a acquis la réputation d'être un outil puissant et flexible pour créer des graphiques de science des données personnalisés. Avec Dash, vous pouvez tout créer, des simples graphiques linéaires aux tableaux de bord complexes de plusieurs pages avec des widgets et des commandes interactifs. Parce qu'il repose sur des technologies open source telles que Flask, React et Plotly.js, Dash est hautement personnalisable et peut être facilement intégré à d'autres outils et workflows de science des données. Que vous soyez data scientist, analyste ou développeur, Dash peut vous aider à créer des visualisations attrayantes et informatives qui donnent vie à vos données.

# Commencer

Ouvrez une fenêtre de terminal dans votre notebook Jupyter et exécutez les commandes suivantes :

```python
# installations requises si elles ne sont pas déjà installées
pip3 install dash==1.16.3
pip3 install pandas
```

Créez un fichier appelé app.py avec le contenu suivant :

```python
# app.py

#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

### Exécutez votre application

```python
python app.py

# ou vous pouvez utiliser :

export FLASK_APP=app.py
flask run
```
