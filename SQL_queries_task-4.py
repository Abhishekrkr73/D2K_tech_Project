import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('New_York_Taxi_Data.db')

# the peak hours for taxi usage
query1 = '''
SELECT 
    strftime('%H', lpep_pickup_datetime) AS hour, 
    COUNT(*) AS trip_count
FROM 
    taxi3
GROUP BY 
    hour
ORDER BY 
    trip_count DESC;
'''
df_peak_hours = pd.read_sql_query(query1, conn)

#  passenger count affect the trip fare
query2 = '''
SELECT 
    passenger_count ,
    AVG(fare_amount) AS average_fare,
    COUNT(*) AS trip_count
FROM 
    taxi3
GROUP BY 
    passenger_count
ORDER BY 
    passenger_count;
'''

df_trip_fare = pd.read_sql_query(query2, conn)

# Close the connection
conn.close()

# Display the result
print(df_peak_hours)
print(df_trip_fare)
