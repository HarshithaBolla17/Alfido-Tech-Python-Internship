# Pandas Data Analysis Project

## 📌 Project Overview
This project demonstrates basic data analysis using Python and the Pandas library.  
The dataset contains product information such as product name, category, price, quantity, and date.

The project includes:
- Loading and inspecting CSV data
- Cleaning and processing data
- Filtering records
- Grouping and aggregation
- Data visualization
- Insight generation

---

## 📂 Project Structure

```text
Pandas_Project/
│
├── data.csv
├── cleaned_data.csv
├── analysis.py
└── README.md
```

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code

---

## 📊 Dataset Information

The dataset contains the following columns:

| Column Name | Description |
|-------------|-------------|
| name | Product name |
| category | Product category |
| price | Product price |
| quantity | Quantity available |
| date | Product date |

---

## ⚙️ Features Implemented

### ✅ Data Loading
Loaded CSV data using Pandas.

### ✅ Data Inspection
Used:
- `head()`
- `info()`
- `describe()`

to understand dataset structure and statistics.

### ✅ Data Cleaning
- Checked missing values
- Removed null values
- Converted data types

### ✅ Data Filtering
Filtered products with prices greater than a specific value.

### ✅ Grouping and Aggregation
Performed category-wise analysis using:
- Mean
- Maximum
- Minimum
- Sum

### ✅ Data Visualization
Created a bar chart using Matplotlib.

---

## ▶️ How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install pandas matplotlib
```

### Step 2: Run the Python Script

```bash
python analysis.py
```

---

## 📈 Sample Insights

- Electronics products have higher average prices than Clothing products.
- Laptop is the most expensive product in the dataset.
- No missing values were found in the dataset.
- Grouping and aggregation helped analyze category-wise product statistics.

---

## 📷 Output

The project generates:
- Terminal-based analysis output
- Bar chart visualization
- Cleaned CSV dataset

---

## 📚 Learning Outcome

This project helped in understanding:
- Data analysis workflow
- Pandas DataFrame operations
- Data cleaning techniques
- Aggregation and filtering
- Basic data visualization

---

