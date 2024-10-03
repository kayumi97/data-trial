# Clever

## Goal of the Project:

Data Engineer Trial Project

At Clever, we are turning data into personalized and localized content so our readers can make well-informed decisions about any step of their real estate journey.

Using the data set below, and the Airflow-based data pipeline docker configuration, perform basic analysis for the chosen in `company_profiles_google_maps.csv`. There are basic errors on the DAG that you will need to fix for the pipeline to work properly. 

To perform this project you will need to
Perform transforms on the raw data and load them into a PostgreSQL database
Be able to join datasets together in way for an analyst to be able to rank by a certain set of criteria (you can determine this criteria)
Be able to filter the data by city or state so analysis can be performed by locality
Given a locality, create a ranked list according to the criteria you’ve chosen
Bonus:
Additional analysis based on the underlying data
An example could be Review Sentiment, common themes among ratings, complaints, etc.

Moving company data set (files can be found at 'dags/scripts/data_examples' folder)
fmcsa_companies.csv
fmcsa_company_snapshot.csv
fmcsa_complaints.csv
fmcsa_safer_data.csv
company_profiles_google_maps.csv
customer_reviews_google.csv


## Getting started
Want to see it working? check the [getting started](docs/getting_started.md) documentation.
