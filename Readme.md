# Evaluating Churn at Telco Co

Introduction: The purpose of this project is to identify drivers of churn at TelcoCo. This task is accomplished by the following: 
- Acquiring the data from the CodeUp SQL database 
- Preparing the data 
- Exploring the data 
- Visualizing the data 
- Modeling the data

### Project Goals

- Find drivers for customer churn at Telco. Why are customers churning? 
- Construct a ML classification model that accurately predicts customer churn 
- Deliver a report that a non-data scientist can read through and understand what steps are taken, why and what was the outcome?

### Deliverables

- Readme: project description with goals, initial hypothesis and/or questions, data dictionary, project planning, instructions how someone else can reproduce your project and findings, key findings, recommendations, and takeaways from your project 

- Final Report: a report that has filtered out all the extraneous elements. Report must include four visualizations paired with questions. Report must also include at least two statistical tests.  

- Prediction CSV file- 3 columns: customer_id, probability of churn, and prediction of churn. 

Prepare.py:
- Drops duplicate columns: payment_type_id, internet_service_type_id, contract_type_id, customer_id
- Encodes: gender, partner, dependents, phone service, paperless billing, and churn 
- Creates dummy variables: multiple lines, online security, online backup, device protection, tech support, streaming tv, streaming movies, contract type, internet service type, payment type
- Concat dummy DataFrame to original DataFrame
- Strips total charges of white space
- Changes total charges datatype from object to float 
- Splits the data: train, validate, test

Acquire_telco.py
- Used to download dataset from SQL 

Data Dictionary
Customer Identification and Demographic Data:
- Customer ID 
- Gender 
- Partner status 
- Dependent status 
- Senior citizen status 
- Tenure in months 
- Monthly charges 
- Total charges 
- Paperless Billing 
- Payment type 
- Multiple lines : One Line, Multiple Lines, No Phone Service 
- Internet Service Type: Fiber Optic, DSL, None 
- Internet Service Option columns 
- Online security
- Online backup
- Device protection
- Tech support
- Streaming TV
- Streaming movies
- Churn status 

To Reproduce this Project: 

In order to reproduce this project download acquire_telco.py, prepare.py, prepare_telco.py and Telco Presentation Final.ipnyb. You will need an env.py to access the CodeUp SQL database. Import .py files including your own personal env.py into the Telco Presentation Final notebook and run it. 

# Conclusion

The main drivers of churn are: fiber optic internet customers, customers who pay by Electronic check, and senior citizen customers

Add on services like online security, online backup, and tech support might support better customer retention

Monthly cost and total cost is also a driver of churn

Month to month customers churn at a higher rate than customers under contract
