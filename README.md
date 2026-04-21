# Baseline Model Comparison and Reproducible NLP Deployment

## Project Overview
This project builds and compares multiple baseline NLP classification models using different feature representations and algorithms. The goal is to determine which model should be deployed first based on both performance metrics and business considerations.

The key focus is not just accuracy, but also how well the model performs across all classes, especially minority or weaker-performing classes.

---

## What This Script Does
This script does not retrain the original NLP models. Instead, it reproduces the baseline comparison from the assignment prompt by storing the provided validation results and analyzing them in code.

Specifically, it:
1. Stores the four baseline pipelines and their validation metrics
2. Prints a clean comparison of accuracy and macro F1 across all pipelines
3. Finds the best pipeline by accuracy
4. Finds the best pipeline by macro F1
5. Prints the recommended first deployment choice based on the business priority of stronger performance across all classes

---

## Why This Matters (Business Context)
In real-world deployment, we care about more than just overall accuracy.
For example:
- A model could be highly accurate overall but perform poorly on important minority classes.
- This could lead to poor user experiences or biased outcomes.
That is why we also evaluate **macro F1 score**, which treats all classes equally and helps ensure balanced performance.

---

## Files in This Repository
- `baseline_homework.py`  
→ Main script that runs all models, evaluates them, and prints results

- `requirements.txt`  
→ No external dependencies required. But in other cases, this will be make sure to install all the external libraries that the code will need to ensure the same results.   

- `README.md`  
→ This file explaining setup and execution

---

## Setup Instructions

### Step 1: Clone the Repository
This downloads the project files to your computer.

```bash
git clone https://github.com/hvo12-star/baseline-model.git 
```

### Step 2: Navigate into the Project folder 

```bash 
cd baseline-model 
```

### Step 3: Install Required Libraries 
This installs all the dependencies needed to run the script 

```bash 
pip install -r requirements.txt 
```

Note: 
- This project uses only standard Python libraries 
- No additional packages are required

### Step 4: Run the Script 

```bash 
python baseline_homework.py
```
#### Environment
This project was developed using:
    - Python 3.10

What this does: 
- Prints the baseline pipeline results
- Compares accuracy and macro F1 across models
- Identifies the best model by accuracy
- Identifies the best model by macro F1
- Prints the recommended first model to ship

---

## Expected Output 

When you run the script, you will see output like this: 

Baseline Model Comparison
-------------------------------------------------- 
Count + MultinomialNB: accuracy=0.6544, macro_f1=0.6259  
Count + LogisticRegression: accuracy=0.6228, macro_f1=0.6138  
TFIDF + MultinomialNB: accuracy=0.6913, macro_f1=0.6655  
TFIDF + LinearSVC: accuracy=0.6824, macro_f1=0.6713  
 
Best by accuracy:  
TFIDF + MultinomialNB (accuracy=0.6913)  
 
Best by macro F1:  
TFIDF + LinearSVC (macro_f1=0.6713)  
 
Recommended first model to ship:  
TFIDF + LinearSVC   
Reason: It has the strongest macro F1, which better matches the business goal of avoiding weak performance on minority or weaker classes.  

---

## One-line Reproducible Run 

This command allows someone to fully reproduce the results from scratch: 

```bash 
git clone https://github.com/hvo12-star/baseline-model.git ; cd baseline-model ; pip install -r requirements.txt ; python baseline_homework.py
```

---

## Model Selection Decision 

The recommended model is chosen based on macro F1 score rather than accuracy.
Reason:
- Accuracy measures overall correctness but can hide poor performance on smaller classes
- Macro F1 treats all classes equally by averaging F1 scores per class
- This ensures the model performs consistently across all groups, not just the majority class

Business Impact:
- Prevents deploying a model that ignores minority cases
- Reduces risk of biased or unfair predictions
- Leads to more reliable real-world performance

--- 

## Assumptions
- Dataset is clean and properly labeled
- Text data is preprocessed through vectorization
- No data leakage exists between train and test sets