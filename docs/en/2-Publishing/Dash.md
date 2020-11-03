# Getting Started with Dash!

For data visualization tools, we will be using Dash. Dash is a great tool used
by many for data analysis, data exploration, visualization, modelling,
instrument control, and reporting.

The following example demonstrates a highly reactive and customised Dash app
with little code.

<!-- prettier-ignore -->
!!! danger "Running your Notebook Server and accessing the port"
    When running any tool from your Jupyter Notebook that posts a website to a port,
    you will not be able to simply access it from `http://localhost:5000/` as
    normally suggested in the output upon running the web-app.

    To access the web server you will need to use the base URL. In your notebook
    terminal run:

    ```python
    echo https://kubeflow.covid.cloud.statcan.ca${JUPYTER_SERVER_URL:19}proxy/5000/
    ```

## Data Visualization with Dash

Dash makes it simple to build an interactive GUI around your data analysis code.
This is an example of a Layout With Figure and Slider from
[Dash](https://dash.plotly.com/basic-callbacks).

![dash_plot](../images/plot.png)

```python
# required installations if not already installed
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

### Run your app

```python
python app.py

# or you can use:

export FLASK_APP=app.py
flask run
```
