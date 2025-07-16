import os
from dotenv import load_dotenv

ROOT_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

ENV_PATH=os.path.join(ROOT_PATH,'.env')

load_dotenv(ENV_PATH)


class Settings:
		#replace xxx with your information
    db_server=os.environ.get("DB_SERVER",'xxx')
    db_name  =os.environ.get("DB_DATABASE",'xxx')
    db_username =os.environ.get("DB_USERNAME",'xxx')
    db_password =os.environ.get("DB_PASSWORD",'xxx')
    db_driver =os.environ.get("DB_DRIVER",'{ODBC Driver 17 for SQL Server}')


settings=Settings()