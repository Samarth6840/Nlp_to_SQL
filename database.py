# database.py
import sqlite3
import pandas as pd

TABLE_NAME = "data"

def load_file_to_db(filepath, db_name="data.db"):
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Only CSV and Excel files are supported!")

    conn = sqlite3.connect(db_name)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()
    return df

def run_query(query, db_name="data.db"):
    conn = sqlite3.connect(db_name)
    try:
        result = pd.read_sql_query(query, conn)
    finally:
        conn.close()
    return result

def get_schema_info(df):
    cols = []
    for col in df.columns:
        cols.append(f"{col}: {df[col].dtype}")
    return "\n".join(cols)

def get_column_names(df):
    return list(df.columns)

def get_preview(df, n=5):
    return df.head(n)