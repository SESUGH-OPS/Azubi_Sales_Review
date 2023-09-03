# Provided data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products
average_price = sum(prices) / len(prices)

# Create a new price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]

# Calculate the total revenue generated from the products
total_revenue = sum(prices[i] * last_week[i] for i in range(len(products)))

# Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / sum(last_week)

# Find products that are less than $30 based on the new prices
affordable_products = [products[i] for i in range(len(products)) if new_prices[i] < 30]

# Print the results
print("Average Price for All Products:", average_price)
print("New Price List (Reduced by $5):", new_prices)
print("Total Revenue Generated:", total_revenue)
print("Average Daily Revenue Generated:", average_daily_revenue)
print("Products Less Than $30 (Based on New Prices):", affordable_products)