
import re
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('/mnt/data/log_analysis.db')
c = conn.cursor()

# Create a table to store log data
c.execute("CREATE TABLE IF NOT EXISTS logs (timestamp TEXT, log_level TEXT, message TEXT)")

# Function to parse log entries and insert into the database
def parse_and_store(log_line):
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)$"
    match = re.match(pattern, log_line)
    if match:
        timestamp, log_level, message = match.groups()
        c.execute("INSERT INTO logs (timestamp, log_level, message) VALUES (?, ?, ?)", 
                  (timestamp, log_level, message))

# Read the log file and process each line
with open('/mnt/data/demo_log_file.log', 'r') as file:
    for line in file:
        parse_and_store(line.strip())

# Commit changes and close the database connection
conn.commit()
conn.close()
