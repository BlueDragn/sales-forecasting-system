
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
