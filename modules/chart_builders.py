import plotly.express as px
import pandas as pd

def build_bar_chart(df: pd.DataFrame, x_col: str, y_col: str, color_col: str = None):
    fig = px.bar(df, x=x_col, y=y_col, color=color_col, barmode='group')
    return fig

def build_line_chart(df: pd.DataFrame, x_col: str, y_col: str, color_col: str = None):
    fig = px.line(df, x=x_col, y=y_col, color=color_col)
    return fig

def build_scatter_chart(df: pd.DataFrame, x_col: str, y_col: str, color_col: str = None):
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col)
    return fig