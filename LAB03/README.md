

# DS605 Lab 3 – Scikit-learn Preprocessing and Model Evaluation

## Student Details

* **Name:** Krishika Lalwani
* **Student ID:** 202618016

## Assignment Title

**DS605 Lab 3 – Scikit-learn Preprocessing, Model Evaluation and Assignment**

## Dataset

**Dataset:** Hotel Booking Demand

The dataset contains hotel booking information for City Hotel and Resort Hotel, including booking details, guest information, stay duration, room information, and cancellation status.

**Dataset Link:**
[https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

The original dataset contains **119,390 rows and 32 columns**. The target variable used for classification is `is_canceled`. 

## Preprocessing

The following preprocessing steps were performed:

### 1. Missing Value Handling

* `company` was removed because approximately **94.3% of its values were missing**, making reliable imputation difficult.
* `agent` and `country` were retained and handled later through the preprocessing pipeline.
* Categorical missing values were handled using **most-frequent imputation**.
* Numerical missing values were handled using **KNN Imputation with 5 neighbors**.  

### 2. Leakage Removal

The following columns were removed because they directly reveal information about the cancellation outcome:

* `reservation_status`
* `reservation_status_date`

This prevents target leakage during model training. 

### 3. Outlier Removal

Rows with unrealistic values were removed:

* `adr < 0` or `adr >= 5000`
* `adults <= 0` or `adults > 10`

A total of **417 rows (0.349%)** were removed, leaving **118,973 rows**. 

### 4. Categorical Encoding

Categorical variables were processed using:

* `SimpleImputer(strategy='most_frequent')`
* `OneHotEncoder(handle_unknown='ignore')`

### 5. Scaling

Two preprocessing pipelines were compared:

**Pipeline A**

* KNN Imputer
* StandardScaler

**Pipeline B**

* KNN Imputer
* MinMaxScaler

The same categorical preprocessing was used in both pipelines. 

### 6. Train-Test Split

The cleaned dataset was divided into:

* **80% training data**
* **20% testing data**
* `stratify=y`
* `random_state=42`

The resulting training set contained **95,512 rows**, while the test set contained **23,878 rows**. 

## Models Evaluated

Two classification algorithms were compared with both preprocessing pipelines:

1. Logistic Regression + Pipeline A
2. Logistic Regression + Pipeline B
3. Decision Tree + Pipeline A
4. Decision Tree + Pipeline B

The notebook evaluates the models using:

* Accuracy
* Precision
* Recall
* F1-Score 

## Final Observations

1. **Decision Tree + Pipeline A gives the best overall result**, with a test accuracy of **85.67%** and F1-score of **0.8071**. 

2. **StandardScaler performs slightly better than MinMaxScaler for Logistic Regression.** Pipeline A achieves a test accuracy of **81.92%** and F1-score of **0.7320**, compared with **81.46%** and **0.7231** for Pipeline B. 

3. **Scaling has almost no effect on the Decision Tree.** The two Decision Tree models have almost identical results: 85.67% versus 85.66% test accuracy and F1-scores of 0.8071 versus 0.8069. 

4. **Decision Tree performs better than Logistic Regression overall**, particularly in recall and F1-score. The best Decision Tree has a recall of **0.8089**, compared with **0.6666** for the best Logistic Regression model. 

5. The Decision Tree has a very high training accuracy of **99.63%**, while its test accuracy is **85.67%**, indicating a substantial difference between training and test performance. 

## Conclusion

Among the four preprocessing-model combinations, **Decision Tree + StandardScaler (Pipeline A)** provides the best overall performance based on test accuracy and F1-score. StandardScaler gives Logistic Regression a small improvement over MinMaxScaler, while scaling makes almost no difference to the Decision Tree.

[1]: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?utm_source=chatgpt.com "Hotel booking demand"

