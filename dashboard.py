import streamlit as st
import pandas as pd

from modules.data_processing import load_data, clean_data
from modules.chart_builders import (
    build_bar_chart,
    build_line_chart,
    build_scatter_chart,
)

def main():
    st.title("BI-инструмент (MVP)")

    st.subheader("1. Загрузка данных")
    uploaded_file = st.file_uploader("Выберите CSV или Excel", type=["csv", "xlsx"])

    if uploaded_file:
        df = load_data(uploaded_file)
        df = clean_data(df)

        if st.checkbox("Показать первые строки"):
            st.dataframe(df.head())

        # Список колонок
        columns = df.columns.tolist()
        numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()

        st.subheader("2. Параметры визуализации")
        chart_type = st.selectbox("Тип графика:", ["Bar", "Line", "Scatter"])
        x_col = st.selectbox("X (ось)", columns)
        y_col = st.selectbox("Y (ось)", numeric_cols)
        color_col = st.selectbox("Цветовая категория", [None] + columns)

        if st.button("Построить график"):
            if chart_type == "Bar":
                fig = build_bar_chart(df, x_col, y_col, color_col)
            elif chart_type == "Line":
                fig = build_line_chart(df, x_col, y_col, color_col)
            else:
                fig = build_scatter_chart(df, x_col, y_col, color_col)

            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
