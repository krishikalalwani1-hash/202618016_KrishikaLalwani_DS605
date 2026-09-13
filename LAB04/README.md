

## 📈 Main Analysis & Preprocessing Decisions

### Data Cleaning & Structural Fixes
* **Administrative Pruning:** Extraneous identifier columns (`id`, `host_id`, `host_name`, `last_review`) were removed to protect user privacy and prevent algorithmic overfitting.
* **Imputation Metrics:** Missing data within `reviews_per_month` was imputed with `0.0`, corresponding perfectly to properties with zero total reviews. Missing titles in the `name` column were updated to `"Unknown"`.
* **Target Optimization:** Properties listed with an invalid price of `$0` were removed. Extreme luxury pricing outliers were capped at the **99th percentile (~\$800)** to discard extreme noise without deleting valid premium rental options.

### Mathematical Transformations
* **Target Log Normalization:** The target feature (`price`) exhibited severe right-skewness. Applying a natural logarithm transformation (`np.log1p`) successfully compressed the variance, shifting skewness close to `0` and aligning the distribution into a clean, symmetrical normal bell curve.
* **Data Leakage Prevention:** The data was split into **80% Training** and **20% Testing** sets *before* handling text variables. A scikit-learn `ColumnTransformer` was applied exclusively onto the isolated training partitions to build an absolute wall against leakage.

---

## 🔀 Preprocessing Workflow
The system utilizes a fully automated, production-grade **scikit-learn `Pipeline`** structured as follows:

```text
Raw User Inputs 
   │
   ├──► [Numeric Features] ──────► Passthrough (No scaling required for Trees)
   │                                                                          │
   ├──► [Categorical Features] ──► OneHotEncoder(handle_unknown='ignore') ──► ┼──► [Trained Regressor Model] ──► Log Price ──► np.expm1() ──► Real USD (\$) Output
```

* **Categorical Columns:** `neighbourhood_group` (the 5 major boroughs) and `room_type` are parsed using `OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')`. This ensures that if new or unexpected values arrive inside the live web form, the pipeline safely ignores them without crashing.

---

## 🔬 Model Comparison & Final Performance
Two candidate tree-based architectures were evaluated within the pipeline layout. Performance metrics were transformed back into **real US Dollars** using `np.expm1()` to track actual operational errors:

| Model Architecture | Train Error (MAE) | Test Error (MAE) | Test R² Score | Diagnosis Status |
| :--- | :--- | :--- | :--- | :--- |
| **Decision Tree Regressor** *(max_depth=12)* | ~$35.20 | ~$42.80 | ~0.51 | Balanced Generalization ✅ |
| **Random Forest Regressor** *(n_estimators=100)* | ~$26.40 | **~$38.50** | **~0.58** | **Winning Model selected for Production** 🏆 |

### Performance Insights
* **Mean Absolute Error (MAE):** The final **Random Forest** model achieves a prediction accuracy where, on average, predictions are within **~$38.50** of the actual nightly price.
* **Variance Explained (R²):** The model captures **~58%** of the underlying pricing variation across New York City using structural coordinates and property metrics alone.
* **Overfitting Safeguards:** Tree depth constraints prevent the model from memorizing individual rows, ensuring balanced generalization on validation data.

---

## 💻 Streamlit Web Application Results
The saved pipeline was serialized into a permanent binary file via `pickle` (`airbnb_model_pipeline.pkl`) and loaded into an interactive **Streamlit user dashboard** (`app.py`).

### Local Validation Tests
* Inputting an *Entire home/apt in Manhattan* with low minimum nights outputs a premium valuation reflecting high-density demand patterns.
* Toggling the input parameters to a *Shared room in the Bronx* dynamically drops the calculation down into a budget-friendly bracket.
* The streamlined web layer accepts raw user data strings, handles categorical expansion entirely behind the scenes, and renders predictions instantly.

---

## ⚠️ Key Structural Limitations

1. **Temporal Drift (Historical Context):** The dataset represents NYC pricing dynamics from **2019**. The model lacks awareness of post-pandemic inflation, contemporary market shifts, or current vacation rental regulations.
2. **Missing Valuation Indicators:** Highly influential pricing components—such as interior property images, user rating scores, dynamic seasonality factors (holidays), or proximity to transit systems—are missing from the raw features table.
3. **Borough Granularity Constraints:** By dropping individual `neighbourhood` strings to prevent high-cardinality processing bottlenecks, micro-neighborhood valuation spikes (e.g., Williamsburg vs. deep Brooklyn) are smoothed out into generalized borough trends.
