import sqlite3
import pandas as pd

# Step 1: Create the SQLite Database and Table
connection = sqlite3.connect('New_York_Taxi_Data.db')
curs = connection.cursor()
curs.execute('''
CREATE TABLE IF NOT EXISTS taxi3 (
    VendorID INTEGER,
    lpep_pickup_datetime TEXT,
    lpep_dropoff_datetime TEXT,
    store_and_fwd_flag TEXT,
    RatecodeID DECIMAL,
    PULocationID REAL,
    DOLocationID REAL,
    passenger_count DECIMAL,
    trip_distance DECIMAL,
    fare_amount DECIMAL,
    extra DECIMAL,
    mta_tax DECIMAL,
    tip_amount DECIMAL,
    tolls_amount DECIMAL,
    ehail_fee DECIMAL,
    improvement_surcharge DECIMAL,
    total_amount DECIMAL,
    payment_type DECIMAL,
    trip_type DECIMAL,
    congestion_surcharge DECIMAL,
    trip_duration DECIMAL,
    average_speed DECIMAL
)
''')
connection.commit()

#  Read Data
data_file = "D:/taxi/green_tripdata_2019-02_new.csv"
df = pd.read_csv(data_file)

# Convert start_time and end_time to datetime
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])


# Load Data into the Database
df.to_sql('taxi3', connection, if_exists='append', index=False)

# Verify the data was inserted
curs.execute('SELECT * FROM taxi3 limit 5')
rows = curs.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
curs.close()
connection.close()
