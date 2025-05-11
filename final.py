import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('owid-covid-data.csv')  

print(df.columns)


print(df.head())

print(df.isnull().sum())

# Filter for countries of interest
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

# Drop rows with missing dates or critical values (e.g., total_cases or total_deaths)
df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Fill or interpolate missing numeric values
numeric_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df[numeric_cols] = df[numeric_cols].interpolate(method='linear')

# Total cases over time
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()


# Total deaths over time
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.show()

# Daily new cases comparison
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='new_cases', hue='location')
plt.title('Daily New COVID-19 Cases')
plt.show()

# Calculate death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']




# Cumulative vaccinations
plt.figure(figsize=(12,6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_vaccinations'], label=country)
plt.title('Cumulative Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

