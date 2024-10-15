import pandas as pd
from scripts.postgres_helper import upload_overwrite_table

def process_and_clean_csv(file_path, output_file):
    try:
        df = pd.read_csv(file_path, sep=',', quotechar='"', escapechar='\\', encoding='latin1', on_bad_lines='skip', skip_blank_lines=True)

        print("Visualização do arquivo original corrigido:")
        print(df.head())

        df.to_csv(output_file, sep=',', index=False)
        print(f"Arquivo corrigido salvo como {output_file}")

    except Exception as e:
        print(f"Erro ao processar o arquivo CSV: {e}")

def upload_to_postgres(**kwargs):
    file_name = kwargs.get('file_name')
    table_name = file_name.split('.')[0]
    input_file = f'dags/scripts/data_examples/{file_name}'
    output_file = f'dags/scripts/data_examples/{table_name}_cleaned.csv'

    process_and_clean_csv(input_file, output_file)

    raw_df = pd.read_csv(output_file)

    upload_overwrite_table(raw_df, table_name)
