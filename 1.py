import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("supermarket_sales - Sheet1.csv")

data["Date"] = pd.to_datetime(data["Date"])

data["Year"] = data["Date"].dt.year
data["Month"] = data["Date"].dt.strftime("%Y-%m")
data["Day"] = data["Date"].dt.date

daily_sales = data.groupby("Day")["Total"].sum()
monthly_sales = data.groupby("Month")["Total"].sum()
yearly_sales = data.groupby("Year")["Total"].sum()

# Создание и сохранение графика дневных продаж
plt.figure(figsize=(10, 6))
daily_sales.plot(kind="line", marker="o")
plt.axhline(y=daily_sales.mean(), color="r", linestyle="--", label="Среднее значение")
plt.title("Дневные продажи")
plt.xlabel("Дата")
plt.ylabel("Объем продаж")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("daily sales.png")
plt.close()

# Создание и сохранение графика месячных продаж
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind="bar")
plt.title("Месячные продажи")
plt.xlabel("Месяц")
plt.ylabel("Объем продаж")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()


# Создание и сохранение графика годовых продаж
plt.figure(figsize=(10, 6))
yearly_sales.plot(kind="bar")
plt.title("Годовые продажи")
plt.xlabel("Год")
plt.ylabel("Объем продаж")
plt.tight_layout()
plt.savefig("yearly_sales.png")
plt.close()


# Распределения цен на товары
plt.figure(figsize=(12, 6))
plt.hist(data["Unit price"], edgecolor="black", bins=30)
plt.title("Ценовые диапозоны")
plt.xlabel("Цена товара")
plt.ylabel("Продажы")

plt.savefig("price_ranges.png")
