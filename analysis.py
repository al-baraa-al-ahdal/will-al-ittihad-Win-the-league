import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "itt_league_2025_2026"
    )
table_name = 'itt'
query = f"SELECT * FROM {table_name}"
df = pd.read_sql(query,db)
df.to_csv(f"{table_name}.csv",index=False,encoding="utf-8")
db.close()