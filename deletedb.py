import os

# Specify the path to the SQLite database file
db_file = 'mydatabase.db'

# Close any existing connections to the database
# ...

# Delete the database file
os.remove(db_file)
