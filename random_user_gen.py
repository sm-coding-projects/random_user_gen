import csv
import random
from datetime import datetime, timedelta

# Constants for generating random data
FIRST_NAMES = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah']
LAST_NAMES = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
EMAIL_DOMAINS = ['example.com', 'test.com']

def random_date_of_birth(start_year=1950, end_year=2005):
    start_date = datetime(year=start_year, month=1, day=1)
    end_date = datetime(year=end_year, month=12, day=31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%Y-%m-%d')

def random_email(first_name, last_name):
    domain = random.choice(EMAIL_DOMAINS)
    return f"{first_name.lower()}.{last_name.lower()}@{domain}"

def random_phone_number():
    return f"+1 555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def generate_user():
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    dob = random_date_of_birth()
    email = random_email(first_name, last_name)
    phone = random_phone_number()
    return [first_name, last_name, dob, email, phone]

# Number of users to generate
num_users = 100  # Reduced for demonstration purposes

# Create and write to the CSV file
with open('user_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['First Name', 'Last Name', 'Date of Birth', 'Email', 'Phone Number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for _ in range(num_users):
        user = generate_user()
        writer.writerow({
            'First Name': user[0],
            'Last Name': user[1],
            'Date of Birth': user[2],
            'Email': user[3],
            'Phone Number': user[4]
        })

print("User data CSV file generated successfully.")
