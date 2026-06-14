
# Engineering Log

**Date:** 13 June 2026

**Project:** Sales Forecasting System

**Session / Topic:** Project Initialization, Dataset Loading & Preprocessing

---

## Objective

Set up the Sales Forecasting System project, configure the development environment, load and inspect the dataset, and begin preprocessing for time-series forecasting.

---

## Work Done

### Project Setup

- Created project repository structure.
- Created and activated Python virtual environment.
- Installed required dependencies:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
- Created `requirements.txt`.
- Created `.gitignore`.
- Downloaded and added the Store Item Demand Forecasting dataset.

### Data Loading

- Implemented `data_loader.py`.
- Added validation checks:
  - Dataset is not empty.
  - Required columns exist.
- Implemented `main.py` to load and inspect the dataset.
- Successfully loaded dataset and displayed:
  - Shape
  - Columns
  - Sample records
  - Data types.

### Dataset Inspection

Dataset characteristics:

```text
Shape: (913000, 4)

Columns:
- date
- store
- item
- sales
```

Observed data types:

```text
date  -> string
store -> int64
item  -> int64
sales -> int64
```

### Preprocessing

- Created `preprocessor.py`.
- Converted `date` column from string to datetime format.
- Sorted dataset by date.
- Reset DataFrame index after sorting.
- Integrated preprocessing step into the main workflow.

Observed result:

```text
date  -> datetime64
store -> int64
item  -> int64
sales -> int64
```

---

## Observations

- Dataset contains historical sales data across multiple stores and items.
- No missing values were observed during initial inspection.
- Datetime conversion is essential because forecasting models require temporal ordering.
- Sorting by date changes record ordering because multiple store-item combinations exist for the same day.
- Validation logic successfully detected incorrect dataset usage (`test.csv` instead of `train.csv`).

---

## Challenges

### Challenge 1: Wrong Dataset File

Attempted to load:

```text
test.csv
```

Result:

```text
Missing columns: ['sales']
```

Resolution:

- Switched to `train.csv`.
- Validation correctly prevented downstream errors.

### Challenge 2: Incorrect Column Name

Used:

```python
df["items"]
```

instead of:

```python
df["item"]
```

Result:

```text
KeyError: 'items'
```

Resolution:

- Corrected the column reference.

### Challenge 3: Incorrect Filtering Logic

Implemented filtering logic but received:

```text
Shape: (2, 4)
```

instead of expected:

```text
~(1826, 4)
```

Resolution:

- Identified as a logical filtering issue.
- Scheduled investigation for the next session.

---

## Key Learnings

- Data validation catches problems early and prevents pipeline failures.
- Time-series projects require careful handling of datetime fields.
- Correct temporal ordering is critical before feature engineering.
- Successful code execution does not always mean the logic is correct.
- Debugging involves both syntax errors and logical errors.

---

## Changes Made

- Added project environment configuration.
- Added dataset loading module.
- Added dataset validation.
- Added preprocessing module.
- Added datetime conversion.
- Added date-based sorting.
- Integrated preprocessing into the main workflow.

---

## Next Step

1. Fix filtering logic for selecting a single store-item series.
2. Verify filtered dataset size.
3. Create forecasting feature engineering module.
4. Implement:
   - Year feature
   - Month feature
   - Day-of-week feature
   - Lag features
   - Rolling average features.
5. Continue preparation for model training.

---

## Session Status

```text
Environment Setup          ✅
Dataset Loading            ✅
Validation                 ✅
Dataset Inspection         ✅
Datetime Conversion        ✅
Preprocessing              ✅
Filtering Logic            ⏳
Feature Engineering        ⏳
Model Training             ⏳
Forecasting                ⏳
```

---
---

## Date :: June 14, 2026

---

# Session Objective

Implement the core machine learning pipeline for a sales forecasting system using time-series data.

---

# Tasks Completed

## 1. Data Loading

### Work Performed
- Loaded training dataset from `train.csv`
- Implemented dataset validation
- Verified required columns:
  - date
  - store
  - item
  - sales

### Outcome
Dataset loaded successfully.

Dataset Shape:

```text
(913000, 4)
```

---

## 2. Data Preprocessing

### Work Performed

- Converted date column to datetime format
- Sorted records chronologically
- Filtered dataset for:

```text
Store = 1
Item = 1
```

- Reset dataframe index

### Outcome

Created a single continuous time series suitable for forecasting.

Filtered Dataset Shape:

```text
(1826, 4)
```

Date Range:

```text
2013-01-01
to
2017-12-31
```

---

## 3. Calendar Feature Engineering

### Work Performed

Created time-based features:

```python
year
month
day
day_of_week
```

### Purpose

Transform raw datetime values into numerical signals usable by machine learning models.

### Outcome

Successfully generated calendar features.

---

## 4. Forecasting Feature Engineering

### Work Performed

Created lag features:

```python
lag_1
lag_7
lag_30
```

Created rolling statistics:

```python
rolling_mean_7
rolling_mean_30
```

### Purpose

Allow model to learn historical sales patterns and trends.

### Outcome

Forecasting features generated successfully.

---

## 5. Missing Value Handling

### Work Performed

Observed expected missing values generated by lag and rolling calculations.

Initial Missing Values:

```text
lag_1              1
lag_7              7
lag_30            30
rolling_mean_7     6
rolling_mean_30   29
```

Applied:

```python
dropna()
reset_index()
```

### Outcome

Final feature dataset contains no missing values.

---

## 6. Model Training Pipeline

### Work Performed

Created target variable:

```python
y = sales
```

Created feature matrix:

```python
X = all columns except date and sales
```

Implemented time-based train/test split:

```text
80% Training
20% Testing
```

Trained:

```python
LinearRegression()
```

### Outcome

Training completed successfully.

Training Shape:

```text
(1436, 11)
```

Testing Shape:

```text
(360, 11)
```

---

## 7. Prediction Pipeline

### Work Performed

Created predictor module.

Generated forecasts using trained model.

### Outcome

Predictions generated successfully.

Example Predictions:

```text
17.97
17.67
20.28
12.31
14.12
...
```

---

## 8. Model Evaluation

### Work Performed

Implemented evaluation metrics:

```python
MAE
RMSE
R²
```

### Outcome

Model Performance:

```text
MAE  = 3.54
RMSE = 4.38
R²   = 0.60
```

---

# Issues Encountered

## Issue 1

Incorrect preprocessing filter:

```python
sales == 1
```

### Resolution

Updated filter to:

```python
store == 1
item == 1
```

---

## Issue 2

Feature engineering generated expected NaN values.

### Resolution

Applied:

```python
dropna()
```

after feature creation.

---

## Issue 3

Function import error:

```text
NameError:
train_model not defined
```

### Resolution

Imported function properly in main.py.

---

## Issue 4

RMSE calculation compatibility issue:

```text
unexpected keyword argument 'squared'
```

### Resolution

Calculated RMSE manually:

```python
mse = mean_squared_error(...)
rmse = np.sqrt(mse)
```

---

# Technical Concepts Reinforced

- Time-series preprocessing
- Datetime feature extraction
- Lag features
- Rolling window statistics
- Time-based train/test splitting
- Linear Regression
- Forecast generation
- Model evaluation metrics
- Modular ML project structure

---

# Current Project Status

```text
✓ Data Loading
✓ Validation
✓ Preprocessing
✓ Calendar Features
✓ Lag Features
✓ Rolling Features
✓ Missing Value Handling
✓ Model Training
✓ Prediction
✓ Evaluation
```

---

# Next Steps

- Prepare Engineering Notes
- Create README
- Perform project review
- Project closure and retrospective
