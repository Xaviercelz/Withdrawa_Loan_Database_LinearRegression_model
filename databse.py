import sqlite3

def setup_tables():
    # 1. CONNECT TO THE DATABASE
    # If "bank_of_xavier.db" does not exist in your folder, Python will 
    # magically create it for you the moment this line runs!
    connection = sqlite3.connect("banking.db")
    
    # 2. CREATE THE CURSOR
    # The cursor is the messenger that takes our SQL commands to the database.
    cursor = connection.cursor()
    
    # 3. WRITE THE SQL COMMAND
    # We use triple quotes (""") in Python so we can write on multiple lines.
    # 'IF NOT EXISTS' is a safety check so the program doesn't crash if the table is already there.
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS accounts (
        user_id TEXT PRIMARY KEY, 
        name TEXT,
        age INTEGER,
        balance REAL,
        pin INTEGER
    )
    """
    
    # 4. EXECUTE AND SAVE
    # Tell the cursor to run the command, then commit (save) the changes.
    cursor.execute(create_table_sql)
    connection.commit()
    
    # 5. HANG UP THE PHONE
    # Always close the connection when you are done to prevent file corruption.
    connection.close()
    
    print("Database is setup and ready!")

# We put this at the bottom just to test it right now!
setup_tables()