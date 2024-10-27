import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r"C:\Users\Nasee\Downloads\archive (1)\olist_sellers_dataset.csv"
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Basic Information about the dataset:")
print(data.info())
print("\nDescriptive Statistics:")
print(data.describe(include='all'))

# Count unique values for each column
print("\nUnique values count for each column:")
print(data.nunique())

# Distribution of sellers by state
state_counts = data['seller_state'].value_counts()
print("\nNumber of sellers by state:")
print(state_counts)

# Distribution of sellers by city
city_counts = data['seller_city'].value_counts().head(10)
print("\nTop 10 cities by number of sellers:")
print(city_counts)

# Plot distribution of sellers by state
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='seller_state', order=state_counts.index, palette='viridis')
plt.title("Distribution of Sellers by State")
plt.xlabel("State")
plt.ylabel("Number of Sellers")
plt.xticks(rotation=45)
plt.show()

# Plot top 10 cities by number of sellers
plt.figure(figsize=(12, 6))
city_counts.plot(kind='bar', color='skyblue')
plt.title("Top 10 Cities by Number of Sellers")
plt.xlabel("City")
plt.ylabel("Number of Sellers")
plt.xticks(rotation=45)
plt.show()
