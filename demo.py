import psycopg2

connection = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='password'
)

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table2(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT false
    );        
''')

cursor.execute('''
    INSERT INTO table2(id,completed) VALUES
        (1,true);      
''')

connection.commit()
connection.close()
cursor.close()