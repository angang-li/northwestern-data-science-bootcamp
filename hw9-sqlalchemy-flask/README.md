# Surfs Up!

From raw data to climate analysis API

![surfs-up.jpeg](Images/surfs-up.jpeg)

## Step 1 - Data Engineering

Data Cleaning ([data_engineering.ipynb](data_engineering.ipynb))

* Read measurement and station CSV files as DataFrames
* Inspect the data for NaNs and missing values
* Remove NaNs from measurements table
* Save the cleaned CSV files

## Step 2 - Database Engineering

Sqlite database ([database_engineering.ipynb](database_engineering.ipynb))

* Load cleaned measurements and stations data
* Create ORM classes for each table
* Create the tables in Sqlite database
* Confirm database and table creation

## Step 3 - Climate Analysis and Exploration

Climate Analysis and Exploration ([climate_analysis.ipynb](climate_analysis.ipynb))

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.
* Plot the results using the DataFrame plot method.
* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.
* Design a query to find the most active stations.
* Design a query to retrieve the last 12 months of temperature observation data.

### Temperature Analysis

* Create a function that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.
* Use the function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year
* Plot the min, avg, and max temperature from your previous query as a bar chart.

### Optional challenge queries

* Calculate the rainfall per weather station using the previous year's matching dates.
* Calculate the daily normals. Normals are the averages for min, avg, and max temperatures.
* Plot the daily normals as area plot.

## Step 4 - Climate App

A Flask API based on the hawaii database ([hawaii_app.py](hawaii_app.py))

Available Routes: <br>
/api/v1.0/precipitation<br/>
/api/v1.0/stations<br/>
/api/v1.0/\<start\>, for example, /api/v1.0/2017-01-01<br/>
/api/v1.0/\<start\>/\<end\>, for example, /api/v1.0/2017-01-01/2017-01-04