# D2K_tech_Project
Project Overview 

New York Taxi Data Processing 

The New York Taxi Data Cleaning and Processing project focuses on ensuring data quality by cleaning and transforming raw taxi trip data from New York City. The main goal is to prepare the data for subsequent analysis by removing rows with missing or corrupt data, deriving new metrics, and loading the cleaned data into an SQLite database. Key steps include: 

Data Cleaning and Transformation: Removing trips with missing or corrupt data and deriving new columns such as trip duration and average speed. 

Database Integration: Loading the cleaned and transformed data into an SQLite database. 

Data Analysis: Performing SQL queries to uncover insights such as peak usage hours and fare trends based on passenger count. 

Visualization: Visualizing the results for better understanding and communication of the insights. 

Detailed Steps 

Data Cleaning and Transformation: 

Remove rows with missing or corrupt data by dropping any row containing null values. 

Derive new columns such as trip duration and average speed to enhance the dataset. 

Database Integration: 

Load the cleaned and transformed data into an SQLite database for efficient querying and analysis. 

Aggregation and Storage: 

Use aggregate functions to calculate total trips and average fares per day. 

Save the aggregated data into a CSV file for further analysis. 

Data Analysis: 

Perform SQL queries to uncover insights, such as: 

Peak usage hours. 

Fare trends based on passenger count. 

Visualization: 

Visualize the analysis results using the matplotlib library in Python to enhance understanding and communication of the insights. 

 
