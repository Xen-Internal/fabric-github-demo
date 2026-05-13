# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ef63f64d-1ae5-488b-8f4f-003071c35ce0",
# META       "default_lakehouse_name": "SalesLakehouse_Source",
# META       "default_lakehouse_workspace_id": "4429eb60-032e-49a0-a7e3-0b28c4ee5eca",
# META       "known_lakehouses": [
# META         {
# META           "id": "ef63f64d-1ae5-488b-8f4f-003071c35ce0"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # **Sales Data Transformation**

# CELL ********************

df = spark.sql("SELECT * FROM SalesLakehouse_Source.dbo.Sales LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Get first row
first_row = df.first()

# Extract header names
new_columns = list(first_row)

print(new_columns)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Remove first row
df_without_header = df.subtract(spark.createDataFrame([first_row], df.schema))

display(df_without_header)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Apply new headers
df_final = df_without_header.toDF(*new_columns)

display(df_final)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
