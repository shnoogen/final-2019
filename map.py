import plotly
plotly.tools.set_credentials_file(username='shnoogen', api_key='2r1Bf00YeU3nYlesxhsH')

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/shnoogen/final-2019/master/ACS_Vietnam%20-%20ACS_15_SPT_DP05_with_ann%20(1).csv')

for col in df.columns:
    df[col] = df[col].astype(str)

#scl is corresponding color to percentage of population
scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

# df is column title in the csv
df['text'] = df['State'] + '<br>' + \
    'Total Vietnamese Population ' + df['Total V Population'] + '<br>' 'Total Vietnamese Percentage ' + df['Total Percentage'] + '%'

data = [go.Choropleth(
    colorscale = scl,
    autocolorscale = False,
    locations = df['Id2'],
    z = df['Total Percentage'].astype(float),
    locationmode = 'USA-states',
    text = df['text'],
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "Total Vietnamese Percentage")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = 'Vietnamese Diaspora in America'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)

fig = go.Figure(data = data, layout = layout)
py.plot(fig, filename = 'd3-cloropleth-map')
