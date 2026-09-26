# Machine Learning Assignment 5
## Garment Employee Productivity Prediction

### Overview

This project uses the **UCI Productivity Prediction of Garment Employees** dataset to build regression and classification models using Scikit-learn and from-scratch NumPy/Pandas implementations.

### Objectives

- Predict `actual_productivity` using Linear Regression.
- Predict whether the target productivity is achieved using Logistic Regression.
- Compare Scikit-learn and from-scratch implementations.
- Compare model performance and execution time.
- Optimize the from-scratch Logistic Regression model.

### Dataset

The dataset contains information about garment production, including targeted productivity, SMV, WIP, overtime, incentive, idle time, number of workers, department, quarter, day, team, and actual productivity.

The `date` column was converted into `month` and `day_of_month`.

### Models

**Regression**
- Scikit-learn Linear Regression
- Linear Regression from scratch using NumPy

Target: `actual_productivity`

**Classification**
- Scikit-learn Logistic Regression
- Logistic Regression from scratch
- Optimized Logistic Regression with L2 regularization

A new target was created:

`MeetsTarget = 1 if actual_productivity >= targeted_productivity, otherwise 0`

`actual_productivity` was not used as a classification feature.

### Preprocessing

- Missing value handling
- One-hot encoding of categorical features
- Feature scaling
- 80/20 train-test split
- Same train-test split used for all models

### Results

#### Regression

| Metric | Scikit-learn | From Scratch |
|---|---:|---:|
| MAE | 0.1075 | 0.1075 |
| RMSE | 0.1411 | 0.1411 |
| R² | 0.3146 | 0.3146 |

#### Classification

| Metric | Scikit-learn | From Scratch | Optimized |
|---|---:|---:|---:|
| Accuracy | 0.7083 | 0.7083 | 0.7042 |
| Precision | 0.7807 | 0.7807 | 0.7708 |
| Recall | 0.8343 | 0.8343 | 0.8457 |
| F1-Score | 0.8066 | 0.8066 | 0.8065 |

### Key Observations

- The from-scratch Linear Regression produced the same results as Scikit-learn.
- The from-scratch Logistic Regression achieved comparable classification performance.
- The optimized Logistic Regression reduced the recorded execution time while maintaining a similar F1-Score.
- NumPy vectorization was used to improve the manual implementation.

### Files

- `assignment.ipynb` – Complete implementation and analysis
- `README.md` – Project documentation
- `garment_worker_productivity.csv` – Dataset
