# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC # TRANS LAYER SCRIPT

# COMMAND ----------

# MAGIC %md
# MAGIC #### DATA ACCESS USING APP
# MAGIC

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.awdataalakestorage.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.awdataalakestorage.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.awdataalakestorage.dfs.core.windows.net", "<client-id-here>")
spark.conf.set("fs.azure.account.oauth2.client.secret.awdataalakestorage.dfs.core.windows.net", "<secret-placeholder>")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.awdataalakestorage.dfs.core.windows.net", "<oauth-endpoint>")

# COMMAND ----------

# MAGIC %md
# MAGIC #### DATA LOADING

# COMMAND ----------

df_cal = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')



# COMMAND ----------

df_cus = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

df_pr_cat = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

df_pr_scat = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

df_pro = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

df_ret = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

df_sales = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

df_terr = spark.read.format('csv')\
.option("header",True)\
.option("inferSchema",True)\
.load('<YOUR_ADLS_PATH_HERE>')

# COMMAND ----------

# MAGIC %md
# MAGIC #### TRANSFORMATION

# COMMAND ----------

# MAGIC %md
# MAGIC #### Calendar

# COMMAND ----------

df_cal.display()

# COMMAND ----------

from pyspark.sql.functions import month, col
df_cal = df.withColumn("Month", month(col("Date")))\
           .withColumn("Year", year(col("Date")))
display(df_cal)

# COMMAND ----------

df_cal.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Customers

# COMMAND ----------

df_cus.display()

# COMMAND ----------

df_cus.withColumn("FullName",concat(col("Prefix"),lit(" "),col("FirstName"),lit(" "),col("LastName"))).display()

# COMMAND ----------


df_cus = df_cus.withColumn("FullName",concat_ws(" ",col("Prefix"),col("FirstName"),col("LastName")))
display(df_cus)

# COMMAND ----------

df_cus.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sub Categories

# COMMAND ----------

df_pr_scat.display()

# COMMAND ----------

df_pr_scat.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Products

# COMMAND ----------

df_pro.display()

# COMMAND ----------

from pyspark.sql.functions import split, col
df_pro = df_pro.withColumn('ProductSKU',split(col('ProductSKU'),'-')[0])\
               .withColumn('ProductName',split(col('ProductName'),' ')[0])

df_pro.display()


# COMMAND ----------

df_pro.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Returns

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Territories

# COMMAND ----------

df_terr.display()

# COMMAND ----------

df_terr.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Product Categories

# COMMAND ----------

df_pr_cat.display()

# COMMAND ----------

df_pr_cat.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

from pyspark.sql.functions import to_timestamp
df_sales = df_sales.withColumn('StockDate',to_timestamp('StockDate'))

# COMMAND ----------

from pyspark.sql.functions import regexp_replace
df_sales = df_sales.withColumn('OrderNumber', regexp_replace('OrderNumber', 'S', 'T'))

# COMMAND ----------

df_sales = df_sales.withColumn('multiply',col('OrderLineItem')*col('OrderQuantity'))

# COMMAND ----------

df_sales.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales Analysis

# COMMAND ----------

df_sales.groupBy('OrderDate').agg(count('OrderNumber')).alias('TotalOrders').display()

# COMMAND ----------

df_sales.write.format('parquet')\
            .mode('append')\
            .option("Path","<YOUR_ADLS_PATH_HERE>")\
            .save()