## End to End Azure Data Engineering Project
This project demonstrates an End-to-End Data Engineering Pipeline built on Microsoft Azure. 

## Overview
Data was extracted from Kaggle, processed and transformed using Azure Databricks (PySpark), and stored in Azure Data Lake Gen2. The processed data was then loaded into Azure Synapse Analytics for analysis and querying.
Power BI was connected to Synapse to verify the connection and preview the dataset for reporting purposes.

## Architecture Diagram
Kaggle Dataset → GitHub Repo → Azure Data Factory → Data Lake Gen2(Raw Layer) → Azure Databricks (Transformation Layer) → Serving Layer → Azure Synapse Analytics → Power BI Dashboard

## Tools & Technologies
**Azure Data Factory (ADF)** – Data ingestion & pipeline orchestration
**Azure Data Lake Gen2** – Data storage (Raw → Transformed → Serving layers)
**Azure Databricks (PySpark)** – Data cleaning, transformation, and preparation
**Azure Synapse Analytics** – Data warehouse, SQL views & analytics
**Power BI** – Reporting and visualization
**GitHub** – Version control and project hosting
**Kaggle** – Dataset source

