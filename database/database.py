import sqlite3
import pandas as pd
import os

# ==============================
# Database Location
# ==============================

DB_PATH = "database/sentinelx.db"

# ==============================
# Connect Database
# ==============================

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Connected to SentinelX Database")

# ==============================
# Create Tables
# ==============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS logon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    user TEXT,
    pc TEXT,
    activity TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    user TEXT,
    pc TEXT,
    activity TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS http (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    user TEXT,
    pc TEXT,
    url TEXT
)
""")

conn.commit()

print("Tables Created Successfully")

# ==============================
# Import Logon CSV
# ==============================

logon_df = pd.read_csv("data/logon.csv")

# Remove the unnecessary ID column
logon_df = logon_df.drop(columns=["id"])

logon_df.to_sql(
    "logon",
    conn,
    if_exists="replace",
    index=False
)

print("Logon Data Imported")

# ==============================
# Import Device CSV
# ==============================

device_df = pd.read_csv("data/device.csv")

# Remove the ID column
device_df = device_df.iloc[:, 1:]

device_df.to_sql(
    "device",
    conn,
    if_exists="replace",
    index=False
)

print("Device Data Imported")

# ==============================
# Import HTTP CSV
# ==============================

http_df = pd.read_csv("data/http.csv")

# Remove ID column
http_df = http_df.iloc[:, 1:]

http_df.to_sql(
    "http",
    conn,
    if_exists="replace",
    index=False
)

print("HTTP Data Imported")

conn.commit()
conn.close()

print("Database Ready!")

