import pandas as pd

df = pd.read_csv("Walmart_Sales.csv")
print(df.head())
print(df.shape)


import pandas as pd

df = pd.read_csv("Walmart_Sales.csv")

# Превращаем дату в нормальный формат
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Вопрос 1: какие магазины приносят больше всего денег?
top_stores = df.groupby("Store")["Weekly_Sales"].sum().sort_values(ascending=False)
print("Топ-5 магазинов по продажам:")
print(top_stores.head(5))

# Вопрос 2: в какие месяцы продажи растут?
df["Month"] = df["Date"].dt.month
monthly = df.groupby("Month")["Weekly_Sales"].mean().sort_values(ascending=False)
print("\nСредние недельные продажи по месяцам:")
print(monthly)

# Вопрос 3: влияют ли безработица, топливо и температура на продажи?
print("\nСвязь факторов с продажами:")
print(df[["Weekly_Sales", "Temperature", "Fuel_Price", "CPI", "Unemployment"]].corr()["Weekly_Sales"])

# Вопрос 4: как слабые магазины отличаются от сильных?
bottom_stores = df.groupby("Store")["Weekly_Sales"].sum().sort_values().head(5)
print("\nХудшие 5 магазинов:")
print(bottom_stores)