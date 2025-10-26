
# Google Play Store App Analysis
# Author: Sandhya Shree B V
# Date: 2025-10-26

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("playstore.csv")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Cleaning data
df.dropna(inplace=True)
df['Installs'] = df['Installs'].replace('[+,]', '', regex=True).astype(int)
df['Price'] = df['Price'].replace('[$]', '', regex=True).astype(float)
df['Reviews'] = df['Reviews'].astype(int)
df['Rating'] = df['Rating'].astype(float)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Top 10 most installed apps
top_installed = df.sort_values(by='Installs', ascending=False).head(10)
print("\nTop 10 Most Installed Apps:")
print(top_installed[['App', 'Installs']])

# Visualization: Category vs Rating
plt.figure(figsize=(12, 6))
df.groupby('Category')['Rating'].mean().sort_values(ascending=False).plot(kind='bar', color='teal')
plt.title('Average Rating by Category')
plt.ylabel('Average Rating')
plt.xlabel('Category')
plt.tight_layout()
plt.show()

# Visualization: Free vs Paid Apps
plt.figure(figsize=(6, 6))
df['Type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
plt.title('Distribution of Free vs Paid Apps')
plt.ylabel('')
plt.show()

# Correlation analysis
corr = df[['Rating', 'Reviews', 'Installs', 'Price']].corr()
print("\nCorrelation Matrix:")
print(corr)

plt.figure(figsize=(6, 4))
plt.matshow(corr, cmap='coolwarm', fignum=1)
plt.colorbar()
plt.title("Correlation Heatmap", pad=20)
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()
