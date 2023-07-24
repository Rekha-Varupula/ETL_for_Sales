# loading.py

import sqlalchemy

def load_data(df, db_connection_string, table_name):
    engine = sqlalchemy.create_engine(db_connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
