import pandas as pd
import pyarrow
import fastparquet


# Load the data
data_file = "D:/taxi/green_tripdata_2019-02.parquet"
df = pd.read_parquet(data_file)
#print(df.head())



# 1. Remove trips with missing or corrupt data
df_cleaned = df.dropna(subset=['lpep_pickup_datetime', 'lpep_dropoff_datetime', 'trip_distance', 'fare_amount', 'passenger_count'])


#print(df_cleaned.head())
# Clean data Save in file
df_cleaned.to_csv("D:/taxi/green_tripdata_2019-02_cleaned.csv", index=False)




# 2. Derive new columns such as trip duration and average speed
# Convert 'lpep_pickup_datetime' and 'lpep_dropoff_datetime' to datetime
df_cleaned['lpep_pickup_datetime'] = pd.to_datetime(df_cleaned['lpep_pickup_datetime'])
df_cleaned['lpep_dropoff_datetime'] = pd.to_datetime(df_cleaned['lpep_dropoff_datetime'])

# Calculate trip duration in seconds
df_cleaned['trip_duration'] = (df_cleaned['lpep_dropoff_datetime'] - df_cleaned['lpep_pickup_datetime']).dt.total_seconds()


# Calculate average speed (assuming distance is in kilometers and trip_duration is in seconds)
# Average speed in km/h
df_cleaned['average_speed'] = (df_cleaned['trip_distance'] / (df_cleaned['trip_duration'] / 3600)).round(2)
#print(df_cleaned.head())

# Derived columns Save
df_cleaned.to_csv("D:/taxi/green_tripdata_2019-02_new.csv", index=False)




# 3. Aggregate data to calculate total trips and average fare per day
# Create a 'day' column
df_cleaned['day'] = df_cleaned['lpep_pickup_datetime'].dt.date

# Group by 'day' and aggregate
aggregated_data = df_cleaned.groupby('day').agg(
    total_trips=pd.NamedAgg(column='passenger_count', aggfunc='count'),  # Assuming 'trip_id' is a unique identifier for each trip
    average_fare=pd.NamedAgg(column='fare_amount', aggfunc='mean')
).reset_index()

# Save the aggregated data to a new CSV file
aggregated_data.to_csv('D:/taxi/green_tripdata_2019-02_aggregated_data.csv', index=False)

#print(aggregated_data.head())

print("Data cleaning and transformation complete.")

