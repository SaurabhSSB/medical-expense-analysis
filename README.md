
# 🩺 Medical Expense Analysis

This repository contains an exploratory data analysis (EDA) of a medical insurance dataset. The goal is to investigate how various demographic and health-related factors such as age, BMI, smoking habits, gender, and diabetes status influence the insurance claim amounts.

This project includes both **Python and R-based analysis**, enabling cross-platform exploration and reproducibility of results using tools like Jupyter Notebooks and R Markdown.

---

## 📂 Files Included

- `medical_expenses.csv` – Cleaned dataset used for analysis
- `1_data_preprocessing.ipynb` – Handling missing values and outliers (Python)
- `2_eda.ipynb` – Detailed visual EDA with insights (Python)
- `Insurance EDA.py` – Python script version of the analysis
- `insurance_data.docx` – Summary, recommendations, and discussion questions
- `medica_expense.Rmd` & `medica_expense.html` – R Markdown notebook and rendered HTML output for EDA using ggplot2 and dplyr

---

## 📊 Dataset Overview

The dataset includes the following columns:

- `age`: Age of the policyholder
- `gender`: Male/Female
- `bmi`: Body Mass Index
- `bloodpressure`: Blood pressure level
- `diabetic`: Yes/No
- `children`: Number of children covered by insurance
- `smoker`: Smoking status
- `region`: Residential region
- `claim`: Insurance claim amount

---

## 🔍 Analysis Highlights

- **Age & Claim**: Older individuals tend to have higher claims.
- **BMI & Smoking**: Smokers and people with higher BMI incur higher medical expenses.
- **Regional Trends**: Southeast region shows higher average claim amounts.
- **Diabetes & Risk**: Diabetic individuals have distinct trends in BMI and claim distribution.
- **Outlier Treatment**: Handled outliers in BMI and filled missing values in age and region.

---

## 💡 Recommendations

- **Tailored Insurance Plans**: Customize offerings based on demographic segments.
- **Health Incentives**: Encourage wellness programs in high-risk areas.
- **Risk Assessment Models**: Use data insights to improve pricing and risk models.
- **Policyholder Education**: Help customers understand how lifestyle affects insurance cost.

> See `insurance_data.docx` for detailed conclusions and discussion questions.

---

## 🛠️ How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/medical-expense-analysis.git
   cd medical-expense-analysis
   ```

2. Install required Python libraries  
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. Run the Jupyter notebooks or Python script.

4. To run the R analysis, open `medica_expense.Rmd` in RStudio and knit to HTML.

---

## 📘 Author

**Saurabh Singh Bhandari**  
_Data Science Enthusiast | EDA & Automation Specialist_

---

## 📎 License

This project is for educational and portfolio purposes only. No commercial use allowed without permission.
