import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("Missing values per column:")
print(df.isnull().sum())
df = df.dropna()

print("\nFirst 5 rows:")
print(df.head())

df['date'] = pd.to_datetime(df['date'])
daily = df.groupby('date')['new_confirmed'].sum().reset_index()

plt.figure(figsize=(14, 6))
sns.lineplot(data=daily, x='date', y='new_confirmed', color='blue')
plt.title('Global Daily New Confirmed COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_locations = df.groupby('location_key')['cumulative_confirmed'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_locations.values, y=top_locations.index, palette='Reds_r')
plt.title('Top 10 Locations by Cumulative Confirmed Cases')
plt.xlabel('Cumulative Confirmed Cases')
plt.ylabel('Location')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df[['cumulative_confirmed', 'cumulative_deceased', 'cumulative_recovered']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
