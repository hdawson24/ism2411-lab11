# Reflection Exercise
# 1: If I worked at someplace like a doctors office and there was no name on file I would use the .get() method so that it would return the no name on file and then I would be able to ask the patient their name. My rule of thumb for choosing would be if I need missing info and dont have it then Id use .get() but if I do not need it and I just need to see it is not working then I would use the try and except method.
# 2: This pattern reminds me of having to manually input every single purchase and region into excel and then add it all up by hand, for large data sets python and a for loop would work way better because it runs it so much faster and it automates it for me.

print("---Exercise 1 ---")
customer = {
    "name": "Alice",  # Key : Value , 
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


print("--- Exercise 2 ---")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary 
print(customer)
customer['tier'] = 'platinum' # Updating the value of an existing key
print(customer)
del customer['email'] # Deleting  a key-value pair from the dictionary 
print(customer)

print(customer.get('ytd_spend', 0))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

# try:
# print(customer["email"])
# except KeyError as error:
# print("KeyError caught:", error)

print("--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")


for something in customer:
    print(something, customer [something]) 

# The difference between the two for loops is that the .items() method makes it quicker and easier to find my items and it allows me to print them nice and neatly.


print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.1, "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price: .2f}")



print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record["name"]} ({record["tier"]}): ${discount:.2f} off a $300 purchase.")

# --- Exercise 7: Nested catalog ---
print(" --- Exercise 7 ---")
catalog =  {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}

}


for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details ['stock']} left")




# --- Exercise 8: Sales by region ---
print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

totals = {}

for transaction in transactions:
    region = transaction.get("region")
    amount = transaction.get("amount", 0)
    totals[region] = totals.get(region, 0) + amount

for region, total in totals.items():
    print(f"{region}: {total}")