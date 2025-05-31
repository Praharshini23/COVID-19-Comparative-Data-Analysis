import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/covid19/epidemiology.csv')
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])

indian_states = ['IN_MH', 'IN_TN', 'IN_DL', 'IN_KA', 'IN_GJ']  
df_india = df[df['location_key'].isin(indian_states)]

grouped = df_india.groupby(['date', 'location_key'])['new_confirmed'].sum().reset_index()
pivot_df = grouped.pivot(index='date', columns='location_key', values='new_confirmed')

plt.figure(figsize=(14, 7))
sns.lineplot(data=pivot_df)
plt.title('Daily New Confirmed COVID-19 Cases in Indian States')
plt.xlabel('Date')
plt.ylabel('New Confirmed Cases')
plt.xticks(rotation=45)
plt.legend(title='State')
plt.tight_layout()
plt.show()
