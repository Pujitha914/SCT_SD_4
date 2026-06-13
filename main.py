import csv
products = [
    ["iPhone 15", "69999", "4.5"],
    ["Samsung S24", "74999", "4.6"],
    ["OnePlus 13", "59999", "4.4"],
    ["Realme GT", "34999", "4.3"]
]
with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])
    writer.writerows(products)
print("Product information extracted successfully!")
print("CSV file created successfully!")
