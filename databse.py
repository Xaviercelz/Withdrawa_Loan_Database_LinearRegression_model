import sqlite3
import banking_system

def setup_tables():
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS accounts (
        user_id TEXT PRIMARY KEY, 
        name TEXT,
        age INTEGER,
        balance REAL,
        pin INTEGER
    )
    """, (banking_system.user.user_id,
          banking_system.user.name,
          banking_system.user.age,
          banking_system.user.balance,
          banking_system.user.account_pin,
          banking_system.user.cre)
    
    
    cursor.execute(create_table_sql)
    connection.commit()
    
    
    connection.close()
    
    print("Database is setup and ready!")


setup_tables()


