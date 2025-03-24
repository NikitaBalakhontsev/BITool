# import streamlit as st
# import pandas as pd
# import plotly.express as px
#
# def dashboard():
#     # dashboard.py
#     st.title("Интерактивный BI-инструмент")
#
#     # --- 1. Загрузка данных пользователем ---
#     uploaded_file = st.file_uploader("Загрузите Excel-файл с данными", type=["xlsx"])
#
#     if uploaded_file:
#         df = pd.read_excel(uploaded_file)
#         st.success("Файл успешно загружен!")
#
#         # Отобразим данные
#         if st.checkbox("Показать загруженные данные"):
#             st.dataframe(df.head())
#
#         # --- 2. Выбор данных для анализа ---
#         columns = df.columns.tolist()
#
#         # Выбор категориального признака
#         category_col = st.selectbox("Выберите категориальный признак (ось X):", columns)
#
#         # Выбор числового признака
#         numeric_cols = df.select_dtypes(include='number').columns.tolist()
#         value_col = st.selectbox("Выберите числовой признак (ось Y):", numeric_cols)
#
#         # --- 3. Выбор функции агрегации ---
#         agg_func = st.selectbox("Выберите функцию агрегации:", ["sum", "mean", "count", "median"])
#
#         # --- 4. Построение графика по выбору пользователя ---
#         if st.button("Построить дашборд"):
#             df_agg = df.groupby(category_col)[value_col].agg(agg_func).reset_index()
#
#             fig = px.bar(df_agg, x=category_col, y=value_col,
#                          title=f"{agg_func.capitalize()} по столбцу '{value_col}' группировка по '{category_col}'")
#             st.plotly_chart(fig, use_container_width=True)
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     dashboard()
#


import streamlit as st
import pandas as pd

from modules.data_processing import load_data, clean_data
from modules.chart_builders import build_bar_chart, build_line_chart, build_scatter_chart

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
