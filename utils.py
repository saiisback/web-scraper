import csv
import sqlite3
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def save_to_db(data, db_name='scraper_data.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    fields = ', '.join([f'{key} TEXT' for key in data[0].keys()])
    cursor.execute(f'CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY AUTOINCREMENT, {fields})')
    
    placeholders = ', '.join(['?' for _ in data[0].keys()])
    cursor.executemany(f"INSERT INTO articles ({', '.join(data[0].keys())}) VALUES ({placeholders})", [tuple(row.values()) for row in data])
    
    conn.commit()
    conn.close()

def read_config(config_file='config.yaml'):
    import yaml
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def exponential_backoff(attempt, base=2, factor=1):
    return factor * (base ** attempt)

def rotate_user_agent(user_agents):
    return random.choice(user_agents)
