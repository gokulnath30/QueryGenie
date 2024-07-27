import sqlite3

class Database:
    def __init__(self):
        self.db_name = "userdatabase.db"
        self.connection = None

    def connect(self):
        """Connect to the SQLite database."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """Create a table with user name (not null), user email (primary key), and data fields."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL,
            useremail TEXT NOT NULL PRIMARY KEY,
            data TEXT
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_user(self, user_name, user_email, data):
        """Insert a new user into the users table."""
        insert_query = """
        INSERT INTO users (user_name, user_email, data)
        VALUES (?, ?, ?);
        """
        try:
            self.cursor.execute(insert_query, (user_name, user_email, data))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error inserting user: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage:
if __name__ == "__main__":
    db = Database("example.db")
    db.connect()
    db.create_table()
    db.insert_user("John Doe", "john.doe@example.com", "Sample data")
    db.close()