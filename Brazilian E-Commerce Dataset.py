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





import pandas as pd

data = pd.read_csv('/content/olist_customers_dataset.csv')

# عرض أول خمس صفوف للتأكد من البيانات
print("عرض أول خمس صفوف من البيانات:")
print(data.head())

# تحليل أكثر ولاية بها عملاء
top_states = data['customer_state'].value_counts().head(10)  # تأكد من أن اسم العمود هو 'customer_state'
print("\nأكثر 10 ولايات بها عملاء:")
print(top_states)

# تحليل أكثر العملاء الفريدين
unique_customers = data['customer_id'].nunique()  # عدد العملاء الفريدين
print(f"\nعدد العملاء الفريدين: {unique_customers}")

# تحليل أكثر المدن بها عملاء
top_cities = data['customer_city'].value_counts().head(10)  # تأكد من أن اسم العمود هو 'customer_city'
print("\nأكثر 10 مدن بها عملاء:")
print(top_cities)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# الرسوم البيانية
sns.set(style="whitegrid")

# قراءة ملف العملاء
file_path = r"C:\Users\Nasee\Downloads\archive (1)\olist_customers_dataset.csv"
data = pd.read_csv('/content/olist_customers_dataset.csv')

# عرض أول خمس صفوف من البيانات
print("عرض أول خمس صفوف من البيانات:")
print(data.head())

# تحليل أكثر ولاية بها عملاء
top_states = data['customer_state'].value_counts().head(10)

# رسم مخطط شريطي لأكثر 10 ولايات بها عملاء
plt.figure(figsize=(10, 6))
top_states.plot(kind='bar', color='skyblue')
plt.title("Top 10 States with Most Customers")
plt.xlabel("State")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.show()

# تحليل أكثر المدن بها عملاء
top_cities = data['customer_city'].value_counts().head(10)

# رسم مخطط شريطي لأكثر 10 مدن بها عملاء
plt.figure(figsize=(10, 6))
top_cities.plot(kind='bar', color='salmon')
plt.title("Top 10 Cities with Most Customers")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.show()

# رسم مخطط دائري لتوزيع العملاء حسب الولايات
plt.figure(figsize=(10, 6))
top_states.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title("Customer Distribution by State")
plt.ylabel("")  # لإخفاء التسمية الافتراضية
plt.show()




import pandas as pd

data = pd.read_csv('/content/olist_products_dataset.csv')

# عرض أول خمس صفوف للتأكد من البيانات
print("عرض أول خمس صفوف من البيانات:")
print(data.head())

# تحليل المنتجات الأكثر تكرارًا
top_products = data['product_id'].value_counts().head(10)
print("\nأكثر 10 منتجات تكرارًا:")
print(top_products)

# تحليل الفئات الأكثر تكرارًا
top_categories = data['product_category_name'].value_counts().head(10)
print("\nأكثر 10 فئات تكرارًا:")
print(top_categories)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# إعداد الشكل والتصميم للرسومات
sns.set(style="whitegrid")

# قراءة الملف CSV
file_path = r"C:\Users\Nasee\Downloads\archive (1)\olist_products_dataset.csv"
data = pd.read_csv('/content/olist_products_dataset.csv')
# تحليل المنتجات الأكثر تكرارًا
top_products = data['product_id'].value_counts().head(10)

# رسم مخطط شريطي للمنتجات الأكثر تكرارًا
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='skyblue')
plt.title("Top 10 Most Frequent Products")
plt.xlabel("Product ID")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
# تحليل الفئات الأكثر تكرارًا
top_categories = data['product_category_name'].value_counts().head(10)
# رسم مخطط شريطي للفئات الأكثر تكرارًا
plt.figure(figsize=(10, 6))
top_categories.plot(kind='bar', color='salmon')
plt.title("Top 10 Most Frequent Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
# (product_photos_qty)
plt.figure(figsize=(10, 6))
sns.histplot(data['product_photos_qty'], kde=True, color='purple', bins=10)
plt.title("Distribution of Product Photos Quantity")
plt.xlabel("Number of Photos")
plt.ylabel("Frequency")
plt.show()
# مخطط توزيع لوزن المنتجات (product_weight_g)
plt.figure(figsize=(10, 6))
sns.histplot(data['product_weight_g'], kde=True, color='green', bins=15)
plt.title("Distribution of Product Weight (grams)")
plt.xlabel("Weight (g)")
plt.ylabel("Frequency")
plt.show()

