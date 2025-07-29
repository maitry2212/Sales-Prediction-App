# 📊 Sales Prediction Web App (Streamlit + Decision Tree)

This is an interactive **web application built with Streamlit** that predicts sales values based on user-uploaded datasets. It uses a **Decision Tree Regressor** from Scikit-learn to train a machine learning model and visualize the results.

---

## 🚀 Demo

[![Streamlit App Demo](https://img.shields.io/badge/Live%20App-Click%20Here-green?style=for-the-badge&logo=streamlit)](http://localhost:8501)  
*(Deploy it to Streamlit Cloud to make this button work online)*

---

## 📌 Features

✅ Upload your own CSV dataset  
✅ Choose the **target** and **feature** columns  
✅ Automatically handles missing values  
✅ Trains a **Decision Tree Regressor**  
✅ Displays evaluation metrics (MSE and R² score)  
✅ Interactive visualizations:
- 📉 Actual vs Predicted Scatter Plot  
- 🌡️ Feature Correlation Heatmap  

---

## 🧠 How It Works

This app allows non-technical users to apply regression-based ML on their datasets:

1. **Data Upload:** Accepts any CSV file
2. **Data Cleaning:** Drops rows with missing values
3. **Modeling:** Trains a Decision Tree Regressor
4. **Evaluation:** Shows performance metrics (Mean Squared Error, R²)
5. **Visualization:** Plots actual vs predicted results & feature correlations

---

## 📂 Dataset Format

Make sure your CSV file includes:

- At least **1 numerical target column** (e.g. `Sales`)
- At least **1 or more feature columns** (e.g. `TV`, `Radio`, etc.)

**Example:**

| TV   | Radio | Newspaper | Sales |
|------|-------|-----------|--------|
| 230.1| 37.8  | 69.2      | 22.1   |
| 44.5 | 39.3  | 45.1      | 10.4   |
| 17.2 | 45.9  | 69.3      | 12.0   |

---

## 📸 Screenshots

> Replace the links below with your own screenshots (after running the app locally)

| Home Page | Prediction Output | Heatmap |
|-----------|-------------------|---------|
| ![Home](screenshots/home.png) | ![Output](screenshots/prediction.png) | ![Heatmap](screenshots/heatmap.png) |

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/sales-prediction-app.git
cd sales-prediction-app
