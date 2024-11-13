import statistics
import csv

monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {stdev_sales}")

variance_sales = statistics.variance(sales)
print(f"La moda es: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')