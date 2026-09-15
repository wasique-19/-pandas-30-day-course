import pandas as pd

# Create a personal book collection
books = pd.DataFrame({
    "Title": ["The Alchemist", "1984", "The Hobbit", "Atomic Habits"],
    "Author": ["Paulo Coelho", "George Orwell", "J.R.R. Tolkien", "James Clear"],
    "Pages": [208, 328, 310, 320],
    "Rating": [4.6, 4.7, 4.8, 4.5]
})

# Export to CSV and JSON
books.to_csv("books.csv", index=False)
books.to_json("books.json", orient="records")

# Read both files back
csv_books = pd.read_csv("books.csv")
json_books = pd.read_json("books.json", orient="records")

# Display the loaded DataFrames
print("CSV DataFrame:")
print(csv_books)

print("\nJSON DataFrame:")
print(json_books)

# Confirm whether the two loaded DataFrames match
print("\nDataFrames match:", csv_books.equals(json_books))

# Check data types
print("\nCSV data types:")
print(csv_books.dtypes)

print("\nJSON data types:")
print(json_books.dtypes)

# Comment: In this example, the CSV- and JSON-loaded DataFrames have matching
# values and data types, so equals() returns True.