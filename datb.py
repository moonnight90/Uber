import sqlite3
from datetime import datetime
conn = sqlite3.connect('vehicles_data.sqlite3')
cursor = conn.cursor()

def create_vehicle_table(vehicle_type):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {vehicle_type} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time_of_entry TEXT,
            origination_address TEXT,
            destination_address TEXT,
            min_price REAL,
            max_price REAL
        );
    ''')
    conn.commit()

def insert_data(vehicle_type, origination, destination, min_price, max_price):
    time_of_entry = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(f'''
        INSERT INTO {vehicle_type} (time_of_entry, origination_address, destination_address, min_price, max_price)
        VALUES (?, ?, ?, ?, ?);
    ''', (time_of_entry, origination, destination, min_price, max_price))
    conn.commit()

# Example usage
vehicle_types = ['Car', 'Truck', 'Motorcycle']

for vehicle_type in vehicle_types:
    create_vehicle_table(vehicle_type)

# Insert sample data
insert_data('Car', '123 Main St', '456 Elm St', 10, 20)
insert_data('Truck', '789 Oak St', '234 Birch St', 30, 60)
insert_data('Motorcycle', '567 Maple St', '890 Pine St', 5, 10)

conn.close()
