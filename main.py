import pandas as pd

houses = pd.read_csv("/home/kinkini/Desktop/house-price-search/Housing.csv")

print(houses.head())

print("\nHOUSE SEARCH SYSTEM")
print("-------------------")

search_price = float(input("Enter the maximum price: "))

found  = False

for index, house in houses.iterrows():
    if house["price"] <= search_price:
        print("\nHouse Found")
        print("Price:", house["price"])
        print("Area:", house["area"])
        print("Bedrooms:", house["bedrooms"])
        print("Bathrooms:", house["bathrooms"])
        print("Stories:", house["stories"])
        print("Main Road:", house["mainroad"])
        print("Guest Room:", house["guestroom"])
        print("Basement:", house["basement"])
        print("Hot Water Heating:", house["hotwaterheating"])
        print("Air Conditioning:", house["airconditioning"])
        print("Parking:", house["parking"])
        print("Preferred Area:", house["prefarea"])
        print("Furnishing Status:", house["furnishingstatus"])

        fround = True

if not found:
    print("No House Found")


