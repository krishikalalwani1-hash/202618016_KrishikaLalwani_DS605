# DS605: Fundamentals of Machine Learning
## Lab Assignment - 2
### Vectorized Programming with NumPy and Data Wrangling with Pandas

---

## Student Details

**Name:** Krishika Lalwani  
**Course:** M.Sc. Data Science  
**Course Code:** DS605  
**Assignment:** Lab Assignment - 2  

---

## 1. Assignment Overview

This assignment focuses on practicing vectorized programming using NumPy and basic data wrangling with Pandas.

The assignment covers:

- NumPy arrays and statistics
- Vectorized arithmetic operations
- Linear algebra operations
- Normal distribution
- Histograms
- Pandas data loading and inspection
- Data filtering and querying
- Groupby and aggregation
- Missing-value handling
- Data imputation
- Outlier detection
- Feature engineering
- Pivot tables
- Data visualization

The Titanic `train.csv` dataset is used for the Pandas data-wrangling tasks.

---

## 2. Dataset

### Titanic Dataset

The dataset used in Part B is the Kaggle Titanic dataset (`train.csv`).

The dataset contains information about Titanic passengers, including:

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

---

## 3. Libraries Used

The following Python libraries were used:

- NumPy
- Pandas
- Matplotlib
- Seaborn

---

# Part A - Vectorized Programming with NumPy

## Task 1 - Arrays, Statistics, and Indexing

The following operations were performed:

- Generated an array of 100 random integers using a random seed.
- Calculated minimum, maximum, median, mean, and standard deviation.
- Generated an array of exactly 100 values using `np.arange()`.
- Implemented `np.zeros()` and `np.ones()`.
- Displayed shape and data type.
- Implemented `np.linspace()`.
- Compared `np.linspace()` with `np.arange()`.
- Created 2D and 3D arrays.
- Demonstrated shape, dimensions, indexing, rows, columns, and slicing.
- Used `reshape()` to create a matrix.
- Used `flatten()` to convert the matrix back to a 1D array.

---

## Task 2 - Vectorized Arithmetic and Linear Algebra

Two matrices were created and the following operations were performed:

- Matrix addition
- Element-wise multiplication
- Matrix multiplication using `@`
- Transpose of a square matrix
- Determinant of a matrix
- Inverse of a matrix
- Verification of the inverse using `np.allclose()`

All operations were performed using vectorized NumPy operations without explicit Python loops.

---

## Task 3 - Normal Distribution and Histogram

At least 1,000 values were generated from a normal distribution.

The following operations were performed:

- Chosen mean = 50
- Chosen standard deviation = 10
- Generated 1,000 random values
- Calculated sample mean
- Calculated sample standard deviation
- Compared the sample values with the chosen values
- Plotted a histogram of the generated normal distribution

---

# Part B - Data Wrangling with Pandas

## Task 4 - Load and Inspect Data

The Titanic `train.csv` dataset was loaded using Pandas.

The following functions and properties were used:

- `head()`
- `tail()`
- `shape`
- `columns`
- `info()`
- `describe()`

Both `loc` and `iloc` were also demonstrated.

### Difference Between loc and iloc

- `loc` is used for label-based selection.
- `iloc` is used for integer-position-based selection.

---

## Task 5 - Filtering and Querying

Boolean indexing was used to answer the following questions:

1. How many male passengers were older than 50?

2. How many female first-class passengers were there, and what percentage survived?

3. How many passengers aged 20-40 had a fare above the overall median and survived?

4. How many passengers were travelling alone, were younger than 30, and did not survive?

5. How many passengers embarked at Southampton (`S`), were in Pclass 2 or 3, and had a fare above the Southampton median?

---

## Task 6 - Groupby and Aggregation

The following analyses were performed using `groupby()`:

### Survival Rate by Sex

Calculated the survival rate for male and female passengers.

### Survival Rate by Pclass

Calculated the survival rate for each passenger class.

### Average Age and Fare by Pclass

Calculated the average age and average fare for each passenger class.

### Passenger Count and Survival Rate by Sex-Pclass

Calculated passenger count and survival rate for each combination of Sex and Pclass.

### Passenger Count, Average Fare and Survival Rate by Embarked

Calculated:

- Passenger count
- Average fare
- Survival rate

for each embarkation location.

---

## Task 7 - Missing Values and Fare Outliers

### Missing Values

Calculated the missing-value count and percentage for every column.

A bar chart was created to visualize missing-value counts.

### Age Imputation

Missing Age values were filled using the mean Age.

The following imputation methods were also explored:

- Mean
- Median
- Mode
- Random value

Missing values before and after imputation were compared.

### Fare Outliers

Fare outliers were detected using the Interquartile Range (IQR) method.

The following were calculated:

- Q1
- Q3
- IQR
- Lower bound
- Upper bound
- Number of outliers

The formulas used were:

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
