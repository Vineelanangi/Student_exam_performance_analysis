
# 🎓 Student Exam Performance Analysis

This project analyzes *student performance* data using Python libraries like *Pandas, Numpy, Matplotlib, and Seaborn*.  
The goal is to explore the dataset, find patterns, and generate meaningful insights through data visualization.

---

## 📂 Dataset
- *Source:* [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- *File:* StudentsPerformance.csv
- *Description:*  
  The dataset contains student exam scores in Math, Reading, and Writing along with information about:
  - Gender  
  - Race/Ethnicity  
  - Parental Level of Education  
  - Lunch Type  
  - Test Preparation Course  

---

## 🛠️ Libraries Used
- *numpy* – Numerical computations  
- *pandas* – Data loading, cleaning, and manipulation  
- *matplotlib* – Visualization (bar charts, histograms)  
- *seaborn* – Advanced visualization (heatmaps, distributions)

---

## 📊 Project Workflow

1. *Load Dataset*  
   - Read CSV file using Pandas
   - Display first 5 rows

2. *Data Exploration*  
   - Check dataset shape, column names, data types  
   - Identify missing values  
   - Generate statistical summary

3. *Data Analysis & Visualization*
   - Average scores by gender (bar chart)  
   - Distribution of math scores (histogram)  
   - Correlation between subjects (heatmap)

---

## 📸 Sample Output

| Chart | Description |
|------|-------------|
| *Gender vs Average Scores* | Compares math, reading, writing average scores for male & female students |
| *Math Score Distribution* | Shows how math scores are distributed across all students |
| *Correlation Heatmap* | Displays relationship strength between math, reading, and writing scores |

---

## 💡 Insights
- Female students perform slightly better in reading and writing.
- Math scores are more spread out compared to reading and writing.
- Reading and Writing scores are strongly correlated (students who read well also write well).

---

## 🚀 How to Run the Project
1. Clone the repository  
```bash
git clone https://github.com/your-username/student-performance-analysis.git
cd student-performance-analysis
