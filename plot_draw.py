import plotly.offline as py


def draw(df, name):
    py.plot([{
        'x': df.index,
        'y': df[col],
        'name': col
    } for col in df.columns], filename='plots/' + name + '.html')
