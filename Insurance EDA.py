# perform linear operations
import numpy as np
# Data manipulation
import pandas as pd
# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# Remove warnings
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
insurance = pd.read_csv(r"C:\Users\Lenovo\Downloads\content\Insurance Data Analysis\insurance_data - insurance_data.csv")
# Print top 5 rows
insurance.head()
insurance

# check for shape
insurance.shape

# Check info of each column
insurance.info()

# Checking null values
insurance.isnull().sum()

insurance.age.isna().sum()

insurance[insurance.age.isnull()]
mean_age = insurance.age.mean()
mean_age

insurance.age.fillna(mean_age, inplace=True)
insurance.age.isna().sum()

insurance.region.isnull().sum()

insurance[insurance.region.isnull()]
mode_region = insurance.region.mode()
mode_region

insurance.region.fillna('southeast', inplace=True)
insurance.region.isnull().sum()

# check for duplicate
insurance.duplicated().sum()

insurance.drop(columns='index', inplace=True)
insurance

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
# Plot a displot
sns.histplot(insurance.age, kde=True, ax=axes[0])
axes[0].set_title('Distribution of Age')
# Plot a boxplot
sns.boxplot(x=insurance.age, ax=axes[1])
axes[1].set_title('Boxplot of Age')
# Display the plots
plt.tight_layout()
plt.show()

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
# Plot a displot
sns.histplot(insurance.bmi, kde=True, ax=axes[0])
axes[0].set_title('Distribution of BMI')
# Plot a boxplot
sns.boxplot(x=insurance.bmi, ax=axes[1])
axes[1].set_title('Boxplot of BMI')
# Display the plots
plt.tight_layout()
plt.show()

# Lets check the data of outliers
l = insurance[insurance.bmi > 50].index.to_list()
insurance[insurance.bmi > 50]

# dropping outliers whose BMI value is above 50
insurance.drop(index=l, inplace=True)

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
# Plot a displot
sns.histplot(insurance.bmi, kde=True, ax=axes[0])
axes[0].set_title('Distribution of BMI')
# Plot a boxplot
sns.boxplot(x=insurance.bmi, ax=axes[1])
axes[1].set_title('Boxplot of BMI')
# Display the plots
plt.tight_layout()
plt.show()

# Plot a displot
sns.histplot(insurance.bloodpressure, kde=True)
plt.title('Distribution of Blood Pressure')
plt.show()

ax = sns.countplot(x=insurance.gender)
for i in ax.containers:
    ax.bar_label(i)
plt.title("Distribution of each category in Gender Column")
plt.show()

ax = sns.countplot(x=insurance.diabetic)
for i in ax.containers:
    ax.bar_label(i)
plt.title("Distribution of each category in Diabetic Column")
plt.show()

ax = sns.countplot(x=insurance.children)
for i in ax.containers:
    ax.bar_label(i)
plt.title("Distribution of each category in Children Column")
plt.show()

ax = sns.countplot(x=insurance.smoker)
for i in ax.containers:
    ax.bar_label(i)
plt.title("Distribution of each category in Smoker Column")
plt.show()

ax = sns.countplot(x=insurance.region)
for i in ax.containers:
    ax.bar_label(i)
plt.title("Distribution of each category in Region Column")
plt.show()

# Plot a displot
sns.histplot(insurance.claim, kde=True)
plt.title('Distribution of Claim Amount')
# Display the plots
plt.show()

def agegroup(x):
    if x >= 18 and x < 29:
        return '18-29'
    elif x >= 29 and x < 39:
        return '29-39'
    elif x >= 39 and x < 49:
        return '39-49'
    else:
        return '49-60'

insurance['agegroup'] = insurance.age.apply(agegroup)
insurance

plt.figure(figsize=(12, 8))
sns.violinplot(x='agegroup', y='bmi', hue='region', data=insurance, inner='quart', palette='Set2')
plt.title('Distribution of BMI across Age Groups and Regions')
plt.xlabel('Age Group')
plt.ylabel('BMI')
plt.show()

plt.figure(figsize=(12, 8))
ax = sns.barplot(x='region', y='age', data=insurance[insurance.diabetic == 'Yes'], ci=None, palette='Set3')
for p in ax.patches:
    ax.annotate('{:.2f}'.format(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5), textcoords='offset points')
plt.title('Average Age of Diabetic People Across Different Regions')
plt.xlabel('Region')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=insurance, x="bloodpressure", y="bmi", hue="diabetic")
plt.title('Correlation Between Blood Pressure and BMI for Patients with and without Diabetes')
plt.xlabel('Blood Pressure')
plt.ylabel('BMI')
plt.show()

sns.countplot(hue='diabetic', x='children', data=insurance)
plt.title('Diabetic Condition Based on the Number of Children')
plt.show()

plt.figure(figsize=(12, 8))
ax = sns.barplot(x='agegroup', y='claim', hue='gender', data=insurance, ci=None, palette='Set3')
for label in ax.containers:
    ax.bar_label(label)
plt.title('Average Insurance Claim Amount for Different Age Groups and Genders')
plt.xlabel('Age Group')
plt.ylabel('Average Claim Amount')
plt.show()

plt.figure(figsize=(12, 8))
ax = sns.barplot(x='smoker', y='claim', hue='region', data=insurance, ci=None, palette='Set3')
for label in ax.containers:
    ax.bar_label(label)
plt.title('Insurance Claims Based on Smoking Habits and Regions')
plt.xlabel('Smoker')
plt.ylabel('Insurance Claim Amount')
plt.show()
