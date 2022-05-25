import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings("ignore")


def prep_telco_data(df):
    df = df.drop(columns=['payment_type', 'customer_id', 'contract_type', 'internet_service_type']) 
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    df['total_charges'] = df.total_charges.astype(float)
    
    # Convert binary categorical variables to numeric
    ordinal_label = {k: i for i, k in enumerate(df['gender'].unique(), 0)}
    df['gender'] = df['gender'].map(ordinal_label)
    ordinal_label2 = {k: i for i, k in enumerate(df['partner'].unique(), 0)}
    df['partner'] = df['partner'].map(ordinal_label2)
    ordinal_label3 = {k: i for i, k in enumerate(df['dependents'].unique(), 0)}
    df['dependents'] = df['dependents'].map(ordinal_label3)
    ordinal_label4 = {k: i for i, k in enumerate(df['phone_service'].unique(), 0)}
    df['phone_service'] = df['phone_service'].map(ordinal_label4)
    ordinal_label5 = {k: i for i, k in enumerate(df['multiple_lines'].unique(), 0)}
    df['multiple_lines'] = df['multiple_lines'].map(ordinal_label5)
    ordinal_label6 = {k: i for i, k in enumerate(df['online_security'].unique(), 0)}
    df['online_security'] = df['online_security'].map(ordinal_label6)
    ordinal_label7 = {k: i for i, k in enumerate(df['online_backup'].unique(), 0)}
    df['online_backup'] = df['online_backup'].map(ordinal_label7)
    ordinal_label8 = {k: i for i, k in enumerate(df['device_protection'].unique(), 0)}
    df['device_protection'] = df['device_protection'].map(ordinal_label8)
    ordinal_label9 = {k: i for i, k in enumerate(df['tech_support'].unique(), 0)}
    df['tech_support'] = df['tech_support'].map(ordinal_label9)
    ordinal_label10 = {k: i for i, k in enumerate(df['streaming_tv'].unique(), 0)}
    df['streaming_tv'] = df['streaming_tv'].map(ordinal_label10)
    ordinal_label11 = {k: i for i, k in enumerate(df['streaming_movies'].unique(), 0)}
    df['streaming_movies'] = df['streaming_movies'].map(ordinal_label11)
    ordinal_label12 = {k: i for i, k in enumerate(df['paperless_billing'].unique(), 0)}
    df['paperless_billing'] = df['paperless_billing'].map(ordinal_label12)
    ordinal_label13 = {k: i for i, k in enumerate(df['churn'].unique(), 0)}
    df['churn'] = df['churn'].map(ordinal_label13)
    
    return df