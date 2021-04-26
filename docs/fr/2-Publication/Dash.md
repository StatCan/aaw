# Bien démarrer avec Dash!

Pour les outils de visualisation de données, nous allons utiliser Dash. Dash est
un excellent outil utilisé par plusieurs pour l'analyse des données,
l'exploration des données, la visualisation, la modélisation, le contrôle des
instruments et la création de rapports.

L'exemple suivant démontre une application Dash hautement réactive et
personnalisée avec peu de code.

<!-- prettier-ignore -->
!!! danger "Exécution de votre serveur de bloc-notes et accès au port"
    Lors de l'exécution de tout outil à partir de votre bloc-notes Jupyter qui affiche un site web sur un port, vous ne serez pas en mesure d'y accéder simplement à partir de `http://localhost:5000/` comme normalement suggéré dans la sortie lors de l'exécution de la web-app.

    Pour accéder au serveur web, vous devrez utiliser l'URL de base. Dans le terminal du bloc-notes exécutez le suivant:

    ```python
    echo https://kubeflow.covid.cloud.statcan.ca${JUPYTER_SERVER_URL:19}proxy/5000/
    ```

## Visualisation de données avec Dash

Dash permet de facilement créer une interface graphique interactive autour de
votre code d'analyse de données. Le suivant s'agit d'un exemple de mise en page
avec une figure et curseur à partir de
[Dash](https://dash.plotly.com/basic-callbacks).

![dash_plot](../images/plot.png)

```python
# installations requis
pip3 install dash==1.16.3
pip3 install pandas
```

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

### Exécuter votre application

```python
python app.py

# ou vous pouvez utiliser:

export FLASK_APP=app.py
flask run
```
