# 🏠 House Price Search

A simple Python-based house search system that reads house data from a CSV file and allows users to search for houses based on their maximum budget.

This project was created to practice **Data Structures and Algorithms (DSA)** concepts, especially **linear search, loops, conditions, and data processing**.

## 📌 Features

- Read house data from `Housing.csv`
- Search houses by maximum price
- Display complete house details
- Find matching houses using a linear search approach
- Simple command-line interface
- Beginner-friendly Python implementation

## 📂 Project Structure

```text
house-price-search/
│
├── Housing.csv
├── main.py
└── README.md
```

## 📊 Dataset

The `Housing.csv` dataset contains information about houses, including:

- Price
- Area
- Number of bedrooms
- Number of bathrooms
- Number of stories
- Main road availability
- Guest room
- Basement
- Hot water heating
- Air conditioning
- Parking
- Preferred area
- Furnishing status

## 🛠️ Technologies Used

- Python
- Pandas
- CSV Dataset
- Git & GitHub

## 🔍 How the Search Works

The program reads the CSV file using Pandas:

```python
import pandas as pd

houses = pd.read_csv("Housing.csv")
```

Then it goes through each house one by one:

```python
for index, house in houses.iterrows():
```

The program checks whether the house price is within the user's budget:

```python
if house["price"] <= search_price:
```

If the condition is true, the house details are displayed.

This is a simple example of **Linear Search**, because the program checks the houses sequentially from the beginning to the end.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/kinkini-cmd/house-price-search.git
```

### 2. Open the project

```bash
cd house-price-search
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run the program

```bash
python3 main.py
```

## 💻 Example

```text
HOUSE SEARCH SYSTEM
-------------------

Enter maximum price: 5000000

House Found
Price: 4900000
Area: 4000
Bedrooms: 3
Bathrooms: 2
...
```

If no house matches the budget:

```text
No houses found.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/711cd24d-fdc7-46cd-9152-6f4294fc226f" />

```

## 🧠 DSA Concepts Practiced

This project helps practice:

- Arrays / Lists
- Loops
- Conditional statements
- Linear Search
- Maximum and minimum values
- Counting
- Iterating through records
- Time complexity

### Linear Search Complexity

For `n` houses:

- **Best case:** O(1)
- **Worst case:** O(n)
- **Average case:** O(n)
- **Space:** O(1) additional search space

## 🚀 Future Improvements

Possible improvements include:

- Search by area
- Search by number of bedrooms
- Search by number of bathrooms
- Search by furnishing status
- Find the cheapest house
- Find the most expensive house
- Sort houses by price
- Add a menu-based interface
- Add a graphical user interface
- Build a house price prediction model using Machine Learning

## 👩‍💻 Author

**Dimalsha Kinkini**

Data Science Undergraduate  
Sri Lanka Technological Campus (SLTC)

## 📄 License

This project is created for educational and learning purposes.
