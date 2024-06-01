import sqlite3

# Connect to your database


# Function to check if a column exists in a table
def column_exists(cursor, table, column):
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [info[1] for info in cursor.fetchall()]
    return column in columns
def read_schema(filename):
    columns_to_add = {}
    with open(filename,'r') as file:
        for line in file:
            table, columns = line.strip().split(':')
            columns = [col.strip().split() for col in columns.split(',')]
            columns_to_add[table] = [(col[0], col[1]) for col in columns]
        return columns_to_add
            # List of columns to add for each table
conn = sqlite3.connect('acds.db')
cursor = conn.cursor()

schemaf = 'schema.txt'
columns_to_add = read_schema(schemaf)

# Add new colu mns if they do not exist
for table, columns in columns_to_add.items():
    for column, col_type in columns:
        if not column_exists(cursor, table, column):
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")

# Commit changes and close connection
conn.commit()
conn.close()