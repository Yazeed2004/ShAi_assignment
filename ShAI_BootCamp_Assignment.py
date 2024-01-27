#!/usr/bin/env python
# coding: utf-8

# #About Dataset
# salaries dataset generally provides information about the employees of an organization in relation to their compensation. It typically includes details such as how much each employee is paid (their salary), their job titles, the departments they work in, and possibly additional information like their level of experience, education, and employment history within the organization.

# # Features
# - 'Id'
# - 'EmployeeName'
# - 'JobTitle'
# - 'BasePay'
# - 'OvertimePay'
# - 'OtherPay'
# - 'Benefits'
# - 'TotalPay' -> salary
# - 'TotalPayBenefits'
# - 'Year'
# - 'Notes'
# - 'Agency'
# - 'Status'
# 

# # Tasks
# 
# 1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.
# 
# 2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
# 
# 3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.
# 
# 4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.
# 
# 5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.
# 
# 6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.
# 
# 8. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.

# # Very Important Note
# There is no fixed or singular solution for this assignment, so if anything is not clear, please do what you understand and provide an explanation.

# In[ ]:


df.columns


# In[2]:


import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv(r'C:/Users/yazee/Downloads/Salaries.csv')
df.head()


# In[3]:


#1
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")


data_types = df.dtypes
print("\nData types of each column:")
print(data_types)


missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)


# In[4]:


#2
static=pd.DataFrame(df,columns=['TotalPayBenefits'])
print(static.describe())
salary_range=static['TotalPayBenefits'].max()-static['TotalPayBenefits'].min()
print("salary_range = ",salary_range)
print("std ",static['TotalPayBenefits'].std())


# In[5]:


#3
df['OvertimePay'] = df['OvertimePay'].fillna(df['OvertimePay'].mean())
df['OtherPay'] = df['OtherPay'].fillna(df['OtherPay'].mean())


# In[24]:


#4
import matplotlib.pyplot as plt
import seaborn as sns

department_counts = df['JobTitle'].value_counts()
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

sns.histplot(df['TotalPay'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Salaries')
axes[0, 0].set_xlabel('Salary')
axes[0, 0].set_ylabel('Frequency')


axes[1, 0].pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=90)
axes[1, 0].set_title('Proportion of Employees in Different Departments')


# In[27]:


#5
grouped_df = df.groupby(['TotalPay', 'JobTitle'])
summary_statistics = grouped_df.agg({'TotalPay': ['count', 'mean', 'median', 'min', 'max', 'std']})
print(summary_statistics)


# In[36]:


#6
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

numerical_column = 'TotalPay'

correlation = df['Year'].corr(df[numerical_column])
print(f"Correlation between Salary and {numerical_column}: {correlation}")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=numerical_column, y='Year', data=df)
plt.title(f'Scatter Plot: Year vs {numerical_column}')
plt.xlabel(numerical_column)
plt.ylabel('Year')
plt.show()


# In[ ]:





# # Good Luck!
