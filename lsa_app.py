import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Create a Plotly Dash app instance and use the Bootstrap stylesheet
lsa_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, ])

# Create a dataframe (note you will load from csv file instead)
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Create a figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Create the layout
lsa_app.layout = html.Div(children=[
    # Provide a title for each chart
    html.H1(children='Chart title goes here'),

    # Display each chart
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    # Provide the explanation for each chart
    html.H2(children='Code'),
    html.P(
        children='Explain where the code for the file is here. For example, it may be a function in lsa_app.py in '
                 'which '
                 'case state the function name, or you may have created a separate python file, in which case you '
                 'should state the file name.'),
    html.H2(children='Explanation and evaluation'),
    html.P(
        'State the question that the visualisation is intended to answer. Each visualisation may only partly '
        'address a question, several visualisations may be needed to answer a question more fully.'),
    html.P('Explain why you chose that particular visualisation.'),
    html.P('Reflect on the extent to which your visualisation helps to answer the question.'),
    html.P('Suggest any ways in which your visualisation could be improved or what you might do differently.')
])

if __name__ == '__main__':
    lsa_app.run_server(debug=True)
