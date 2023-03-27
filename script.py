#Biblioteca psycopg2 para estabelecer a conexão com os bancos de dados;
import psycopg2


# Lista de tabelas que serão transferidas do banco de dados transacional 
# para o banco de dados analytics;
# Os tabelas que estão comentadas não consigui fazer a transferência para o banco de dados analytics 
# por conta de um erro de Tipo de dados =( 

tables_to_transfer =[
    'address',
    'category',
    'city',
    'country',
    'customer',
    #'film',
    'film_actor',
    'film_category',
    'inventory',
#   'language',
    'payment',
    'rental',
#   'staff',
    'store',
#   'actor',
 ]


# Dicionário que mapeia os tipos de dados do banco de dados transacional
# para os tipos de dados do banco de dados analytics;

data_type_map = {
    16: "BOOLEAN",
    20: "BIGINT",
    21: "SMALLINT",
    23: "INTEGER",
    25: "TEXT",
    700: "REAL",
    701: "DOUBLE PRECISION",
    1700: "NUMERIC",
    1042: "CHAR",
    1043: "VARCHAR",
    1082: "DATE",
    1114: "TIMESTAMP",
    1184: "TIMESTAMP WITH TIME ZONE",
    1266: "TIME",
    1560: "BIT",
    1562: "VARBIT",
}
# Conexões feitas com as portas mapeadas do Compose;

# Conexão com o banco de dados transacional dvdrental
conn_transacional = psycopg2.connect(
    host="localhost",
    port=5432,
    database="dvdrental",
    user="postgres",
    password="password"
)

# Conexão com o banco de dados analytics
conn_analytics = psycopg2.connect(
    host="localhost",
    port=5440,
    database="analytics",
    user="postgres",
    password="password"
)
# Cursor para o banco de dados analytics
cursor_analytic = conn_analytics.cursor()
# Cursor para o banco de dados Transacional
cursor_trans = conn_transacional.cursor()

# Loop para transferir cada tabela da lista de tabelas para o banco de dados analytics

for table in tables_to_transfer:
    # Executa a consulta para selecionar todos os registros da tabela do banco de dados transacional
    cursor_trans.execute(f"SELECT * FROM {table}")
    # Recupera os nomes das colunas da tabela
    columns = [desc[0] for desc in cursor_trans.description]
    # Recupera os tipos de dados das colunas da tabela
    column_types = [desc[1] for desc in cursor_trans.description]

    # Concatena as informações das colunas em uma string para criar a tabela no banco de dados analytics
    column_str = ", ".join([f"{column} {data_type_map[column_type.type_code]}" for column, column_type in zip(columns, cursor_trans.description)])
    cursor_analytic.execute(f"CREATE TABLE {table} ({column_str})")

for table in tables_to_transfer:
    cursor_trans.execute(f"SELECT * FROM {table}")
    # Recupera todas as linhas da tabela do banco de dados transaciona
    rows = cursor_trans.fetchall()
    for row in rows:
        placeholders = ", ".join(["%s"] * len(row))
        cursor_analytic.execute(f"INSERT INTO {table} VALUES ({placeholders})", row)


# Confirma as alterações no banco de dados analytics
conn_analytics.commit()
