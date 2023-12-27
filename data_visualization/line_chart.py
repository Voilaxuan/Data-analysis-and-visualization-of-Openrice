import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

print(df.isnull().sum())#check null
print(df.duplicated().sum())#check duplicated
df.isnull().sum()
df = df.dropna()
df.replace({'price': {'$50以下': '25', '$51-100': '75', '$101-200': '150','$201-400': '300','$401-800': '600','$801以上': '800'}}, inplace=True)

sns.barplot(y=df['district_map'].value_counts().index, x=df['district_map'].value_counts().values).set_title('Regional distribution of restaurants')
plt.savefig('bar.png')
plt.show()

# Scatter Plot
df['price'] = pd.to_numeric(df['price'], errors='coerce')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='price', y='smile_rate', hue='district_map')
plt.title('Price vs. Smile Count')
plt.xlabel('Price')
plt.ylabel('Smile Count')
plt.savefig('Scatter_Plot2.png')
plt.show()

df['price'] = pd.to_numeric(df['price'], errors='coerce')
# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='category', y='price')
plt.title('Price Distribution by Category')
plt.xlabel('Category')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.savefig('box.png')
plt.show()

df['price'] = pd.to_numeric(df['price'], errors='coerce')
sns.pairplot(data=df, vars=['price', 'smile_rate', 'cry_rate'], hue='district_map')
plt.suptitle('Pairwise Relationships by District')
plt.savefig('Pair.png')
plt.show()

plt.figure(figsize=(10, 6))
df_category_district = df.groupby(['category', 'district_map']).size().unstack()
# df_category_district.plot(kind='bar', stacked=True)

df_category_district = df_category_district.loc[(df_category_district != 0).any(axis=1)]
df_category_district.plot(kind='bar', stacked=True)

plt.title('Restaurant Count by Category and District')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='District')
# plt.legend(handles=[])
plt.savefig('groupbar2.png')
plt.show()