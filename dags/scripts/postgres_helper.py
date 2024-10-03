import psycopg2
from sqlalchemy import create_engine, text
import scripts.constants as c

# Create SQLAlchemy engine
engine = create_engine(
    f'postgresql+psycopg2://{c.postgres_user}:{c.postgres_password}@{c.postgres_host}:{c.postgres_port}/{c.postgres_dbname}'
)

def run_sql(create_sql):
    with engine.connect() as conn:
        conn.execute(text(create_sql))
        conn.commit()
        conn.close()

def upload_overwrite_table(df, table_name):
    # Upload DataFrame to PostgreSQL
    df.to_sql(f'{table_name}', engine, index=False, if_exists='replace')