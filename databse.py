import sqlite3
from datetime import datetime

# Bank's total available credit
BANK_CREDIT_LIMIT = 1_000_000_000  # $1 trillion

def setup_tables():
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    create_accounts_table = """
    CREATE TABLE IF NOT EXISTS accounts (
        user_id TEXT PRIMARY KEY, 
        username TEXT,
        name TEXT,
        age INTEGER,
        balance REAL,
        pin INTEGER,
        creditscore INTEGER
    )
    """
    
    create_loans_table = """
    CREATE TABLE IF NOT EXISTS loans (
        loan_id TEXT PRIMARY KEY,
        user_id TEXT UNIQUE,
        loan_amount REAL,
        interest_rate REAL,
        fee_amount REAL,
        total_owed REAL,
        created_date TEXT,
        FOREIGN KEY (user_id) REFERENCES accounts(user_id)
    )
    """
    
    cursor.execute(create_accounts_table)
    cursor.execute(create_loans_table)
    connection.commit()
    connection.close()
    
    print("Database is setup and ready!")


def save_account_to_database(account):
    """Save an account to the SQLite database"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    insert_sql = """
    INSERT OR REPLACE INTO accounts (user_id, username, name, age, balance, pin, creditscore)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    
    try:
        cursor.execute(insert_sql, (
            account.user_id,
            account.username,
            account.name,
            account.age,
            account.balance,
            account.account_pin,
            account.creditscore
        ))
        connection.commit()
        print(f"\nAccount {account.user_id} saved to database successfully!")
    except Exception as e:
        print(f"Error saving account: {e}")
    finally:
        connection.close()


def get_all_accounts():
    """Retrieve all accounts from the database"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    select_sql = "SELECT user_id, username, name, balance, creditscore FROM accounts"
    
    try:
        cursor.execute(select_sql)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error retrieving accounts: {e}")
        return []
    finally:
        connection.close()


def get_account_from_database(user_id):
    """Retrieve a specific account from the database by user_id"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    select_sql = "SELECT * FROM accounts WHERE user_id = ?"
    
    try:
        cursor.execute(select_sql, (user_id,))
        result = cursor.fetchone()
        if result:
            return result
        else:
            print(f"No account found with User ID: {user_id}")
            return None
    except Exception as e:
        print(f"Error retrieving account: {e}")
        return None
    finally:
        connection.close()


def user_has_active_loan(user_id):
    """Check if user already has an active loan"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    select_sql = "SELECT * FROM loans WHERE user_id = ?"
    
    try:
        cursor.execute(select_sql, (user_id,))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(f"Error checking loan status: {e}")
        return False
    finally:
        connection.close()


def save_loan_to_database(loan_id, user_id, loan_amount, interest_rate, fee_amount, total_owed):
    """Save a loan to the database"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    insert_sql = """
    INSERT INTO loans (loan_id, user_id, loan_amount, interest_rate, fee_amount, total_owed, created_date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    
    try:
        cursor.execute(insert_sql, (loan_id, user_id, loan_amount, interest_rate, fee_amount, total_owed, created_date))
        connection.commit()
        print(f"Loan {loan_id} saved successfully!")
    except Exception as e:
        print(f"Error saving loan: {e}")
    finally:
        connection.close()


def get_user_loan(user_id):
    """Get active loan for a user"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    select_sql = "SELECT * FROM loans WHERE user_id = ?"
    
    try:
        cursor.execute(select_sql, (user_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Error retrieving loan: {e}")
        return None
    finally:
        connection.close()


def get_total_loaned():
    """Get total amount currently loaned out by the bank"""
    connection = sqlite3.connect("banking.db")
    cursor = connection.cursor()
    
    select_sql = "SELECT SUM(total_owed) FROM loans"
    
    try:
        cursor.execute(select_sql)
        result = cursor.fetchone()
        total = result[0] if result[0] is not None else 0
        return total
    except Exception as e:
        print(f"Error calculating total loaned: {e}")
        return 0
    finally:
        connection.close()


# Setup the database when this module is imported
setup_tables()


