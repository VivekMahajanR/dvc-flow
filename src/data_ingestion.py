import pandas as pd
import numpy as np
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:, 3:]

df = df[df['Avg. Session Length'] >3]

df.to_csv(os.path.join('data', 'customer_data.csv'), index=False)