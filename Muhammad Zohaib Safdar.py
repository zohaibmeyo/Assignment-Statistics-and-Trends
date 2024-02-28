#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Stock_TLKM_2005-2024.csv")

df




# In[7]:


# Plot 1: Histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Close'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Closing Prices')
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[54]:


# Plot 2: Line graph
plt.figure(figsize=(8, 6))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-')
plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[53]:


# Plot 3: box plot using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data=df)
plt.title('Box Plot of Closing Prices by Category')
plt.xlabel('Category')
plt.ylabel('Closing Price')
plt.show()


# In[ ]:




