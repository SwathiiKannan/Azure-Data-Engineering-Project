-- CREATE VIEW CALENDAR --
CREATE VIEW servinglayer.calendar
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Calendar/',
            FORMAT = 'PARQUET'
) as CalQuery

-- CREATE VIEW CUSTOMERS --
CREATE VIEW servinglayer.customers
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Customers/',
            FORMAT = 'PARQUET'
) as CusQuery

-- CREATE VIEW PRODUCT CATEGORIES --
CREATE VIEW servinglayer.pro_cat
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Product_Categories/',
            FORMAT = 'PARQUET'
) as procatQuery

-- CREATE VIEW PRODUCT SUBCATEGORIES --
CREATE VIEW servinglayer.pro_scat
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Product_Subcategories/',
            FORMAT = 'PARQUET'
) as proscatQuery

-- CREATE VIEW PRODUCTS --
CREATE VIEW servinglayer.products
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Products/',
            FORMAT = 'PARQUET'
) as ProQuery

-- CREATE VIEW RETURNS --
CREATE VIEW servinglayer.returns
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Returns/',
            FORMAT = 'PARQUET'
) as RetQuery

-- CREATE VIEW TERRITORIES --
CREATE VIEW servinglayer.territories
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Territories/',
            FORMAT = 'PARQUET'
) as TertQuery

-- CREATE VIEW SALES --
CREATE VIEW servinglayer.sales
AS
select * from 
OPENROWSET( BULK 'https://awdataalakestorage.dfs.core.windows.net/transformationlayer/AdventureWorks_Sales/',
            FORMAT = 'PARQUET'
) as SalQuery