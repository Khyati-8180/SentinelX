from utils.db import get_connection
import pandas as pd

conn = get_connection()

logon_df = pd.read_sql("SELECT * FROM logon", conn)
device_df = pd.read_sql("SELECT * FROM device", conn)
http_df = pd.read_sql("SELECT * FROM http", conn)

active_users = logon_df["user"].nunique()

total_logins = len(logon_df)

usb_events = len(device_df)

web_events = len(http_df)

high_risk_users = device_df["user"].nunique()
http_requests = len(http_df)