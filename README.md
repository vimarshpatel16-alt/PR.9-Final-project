
# 🌍 Global Happiness Report Analysis 📊

### ✨ Exploring Happiness Around the World Using Python

Welcome to my **Global Happiness Report Analysis** project! 🎉

This project uses Python and data visualization libraries to analyze happiness scores across different countries. It explores how factors such as GDP per capita, social support, healthy life expectancy, freedom, and generosity relate to people's happiness.

The main goal is to transform raw data into meaningful insights using data analysis and visualization. 🚀

---

## 🎯 Project Objectives

- 🌎 Analyze happiness scores across different countries.
- 🏆 Identify the top 10 happiest countries.
- 💰 Explore the relationship between GDP per capita and happiness.
- 🤝 Understand how social support relates to happiness.
- ❤️ Study the relationship between healthy life expectancy and happiness.
- 📈 Analyze changes in average happiness scores over time.
- 🔥 Visualize correlations between different happiness factors.
- 🧹 Clean and prepare data for analysis.

---

## 🛠️ Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming language |
| 🐼 Pandas | Data loading, cleaning, and analysis |
| 🔢 NumPy | Numerical operations |
| 📊 Matplotlib | Creating charts and graphs |
| 🎨 Seaborn | Statistical data visualization |
| 📓 Jupyter Notebook | Writing and executing Python code |

---

## 📂 Dataset Information

**Dataset:** World Happiness Report

The dataset contains information about countries, happiness scores, and several factors associated with well-being.

📥 **Dataset Source:**  
[World Happiness Report CSV Dataset](https://github.com/VStanys/CSV-WHR/blob/main/world-happiness-report.csv)

### 📋 Important Dataset Columns

- 🌍 `Country name` — Name of the country.
- 😊 `Life Ladder` — Happiness score reported in the dataset.
- 💰 `Log GDP per capita` — Logarithmic measure of GDP per capita.
- 🤝 `Social support` — Reported social support.
- ❤️ `Healthy life expectancy at birth` — Healthy life expectancy measure.
- 🕊️ `Freedom to make life choices` — Reported freedom.
- 🎁 `Generosity` — Measure of generosity.
- 🔍 `Perceptions of corruption` — Perceived corruption measure.
- 📅 `year` — Year of the observation.

---

## ✨ Project Features

### 1️⃣ Data Loading and Cleaning
- Load the dataset directly from a CSV URL.
- Display the first five rows and dataset information.
- Remove records missing country names or happiness scores.

### 2️⃣ Top 10 Happiest Countries 🏆
Identify and display the ten countries with the highest happiness scores in the latest available year.

### 3️⃣ Happiness Score Distribution 📊
Create a histogram to understand how happiness scores are distributed among countries.

### 4️⃣ GDP vs Happiness 💰
Use a scatter plot to explore the relationship between GDP per capita and happiness scores.

### 5️⃣ Social Support vs Happiness 🤝
Visualize how reported social support relates to happiness.

### 6️⃣ Correlation Heatmap 🔥
Use a heatmap to examine correlations between happiness and other numerical factors.

### 7️⃣ Happiness Over Time 📈
Create a line chart showing changes in average happiness scores across available years.

### 8️⃣ Statistical Summary 📋
Calculate:
- Total countries in the latest available year.
- Average happiness score.
- Highest happiness score.
- Lowest happiness score.

### 9️⃣ Export Results 💾
Save the cleaned dataset and the top 10 happiest countries to CSV files.

---

## ⚙️ Installation and Setup

### Step 1: Install Python
Download Python from the official website:

🔗 https://www.python.org/downloads/

During installation on Windows, select **Add Python to PATH**.

### Step 2: Install Required Libraries

Open Command Prompt or a Jupyter Notebook cell and run the appropriate command.

**In Command Prompt:**

```bash
python -m pip install pandas numpy matplotlib seaborn
```

**In Jupyter Notebook:**

```python
%pip install pandas numpy matplotlib seaborn
```

### Step 3: Open Jupyter Notebook

Run this command in Command Prompt:

```bash
python -m notebook
```

### Step 4: Run the Project

1. Open your Jupyter Notebook.
2. Create a new Python notebook.
3. Copy the project code into a cell.
4. Press `Shift + Enter`.
5. Wait for the charts and analysis results to appear.

**Note:** An active internet connection is required to load the dataset from its online source.

---

## 📊 Visualizations Included

| No. | Visualization | Purpose |
|---|---|---|
| 1 | 🏆 Top 10 Countries Bar Chart | Compare happiness scores |
| 2 | 📊 Happiness Distribution | Understand score distribution |
| 3 | 💰 GDP vs Happiness Scatter Plot | Examine economic relationships |
| 4 | 🤝 Social Support Scatter Plot | Explore social support |
| 5 | 🔥 Correlation Heatmap | Compare numerical relationships |
| 6 | 📈 Happiness Trend Line Chart | Analyze average scores over time |

---

## 📁 Project Structure

```text
Global-Happiness-Analysis/
│
├── Global_Happiness_Analysis.ipynb
├── happiness_cleaned_data.csv
├── top_10_happiest_countries.csv
└── README.md
```

**File descriptions:**

- `Global_Happiness_Analysis.ipynb` — Main Python project and visualizations.
- `happiness_cleaned_data.csv` — Cleaned dataset exported by the program.
- `top_10_happiest_countries.csv` — Top 10 countries for the latest available year.
- `README.md` — Project documentation.

The two CSV files are generated when the program runs successfully.

---

## 🔍 Key Insights

This project helps investigate questions such as:

- 🌍 Which countries have the highest reported happiness scores?
- 💰 Do countries with higher GDP per capita tend to report higher happiness?
- 🤝 How is social support associated with happiness?
- ❤️ What relationships exist between life expectancy and happiness?
- 📈 How have average happiness scores changed over time?

**Important:** Actual findings should be based on the results generated by the program. Correlation does not prove causation, and country-level data may not represent every individual's experience.

---

## 🚀 Future Improvements

- 🌐 Add an interactive dashboard.
- 📅 Compare individual countries across multiple years.
- 🧠 Apply machine learning to explore happiness-score prediction.
- 📊 Add more statistical analysis.
- 🎨 Improve chart formatting and presentation.
- 🗺️ Create geographical visualizations of happiness scores.

---

## 🎓 Learning Outcomes

Through this project, I practiced:

- Python programming fundamentals.
- Data cleaning and preprocessing.
- Data analysis using Pandas and NumPy.
- Data visualization using Matplotlib and Seaborn.
- Statistical correlation analysis.
- Working with real-world CSV datasets.
- Exporting results and documenting a project.

---
