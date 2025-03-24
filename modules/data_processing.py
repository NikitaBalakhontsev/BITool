import pandas as pd
from streamlit.runtime.uploaded_file_manager import UploadedFile


def load_data(uploaded_file: UploadedFile) -> pd.DataFrame:
    """
    Загрузка данных из CSV или Excel из объекта Streamlit UploadedFile.
    """
    # Проверяем расширение файла по его имени
    filename = uploaded_file.name.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif filename.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Формат файла не поддерживается. Допустимы .csv или .xlsx")

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(how='all')  # пример очистки
    # Здесь любая кастомная логика, конверсия типов и т.д.
    return df