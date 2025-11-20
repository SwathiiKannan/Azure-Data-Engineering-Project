CREATE MASTER KEY ENCRYPTION BY PASSWORD ='Jeevi@1993'

CREATE DATABASE SCOPED CREDENTIAL cred_swat
WITH IDENTITY = 'Managed Identity'

CREATE EXTERNAL DATA SOURCE source_transformationlayer
with (LOCATION = 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer',
      CREDENTIAL= cred_swat)

CREATE EXTERNAL DATA SOURCE source_servinglayer
with (LOCATION = 'https://awdataalakestorage.dfs.core.windows.net/servinglayer',
      CREDENTIAL= cred_swat)

CREATE EXTERNAL FILE FORMAT format_parquet
WITH
(FORMAT_TYPE = PARQUET,
DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec')

-- CREATE EXTERNAL TABLE EXTSALES --
CREATE EXTERNAL TABLE servinglayer.extsales
WITH (
    LOCATION = 'extsales',
    DATA_SOURCE = source_servinglayer,
    FILE_FORMAT = format_parquet
) as select * from servinglayer.sales

select * from servinglayer.sales;