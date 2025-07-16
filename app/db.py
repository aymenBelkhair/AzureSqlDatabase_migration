from app.settings import settings as st
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import urllib


params = urllib.parse.quote_plus(
    f"DRIVER={st.db_driver};SERVER={st.db_server};DATABASE={st.db_name};UID={st.db_username};PWD={st.db_password};Encrypt=yes;TrustServerCertificate=no;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


