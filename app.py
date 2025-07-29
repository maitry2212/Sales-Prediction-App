import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Page setup
st.set_page_config(page_title="Sales Prediction App", layout="centered")

st.title("📊 Sales Prediction Using Decision Tree")
st.markdown(
    """
    This app predicts sales using a **Decision Tree Regressor**.
    Upload your dataset, select features, and get instant insights with clear visualizations.
    """
)

# File upload
uploaded_file = st.file_uploader("📂 Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset successfully uploaded!")

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Handle missing values
    if df.isnull().sum().sum() > 0:
        st.warning("⚠️ Missing values detected. Dropping rows with nulls.")
        df.dropna(inplace=True)

    # Column selection
    target_col = st.selectbox("🎯 Select the target column", df.columns)

    feature_cols = st.multiselect(
        "📌 Select feature columns",
        [col for col in df.columns if col != target_col],
        default=[col for col in df.columns if col != target_col]
    )

    if feature_cols:
        # Prepare training data
        X = df[feature_cols]
        y = df[target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Train Decision Tree
        model = DecisionTreeRegressor(random_state=42)
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        st.subheader("📈 Model Evaluation")
        st.metric(label="Mean Squared Error", value=f"{mse:.2f}")
        st.metric(label="R² Score", value=f"{r2:.2f}")

        # Actual vs Predicted Plot (smaller size)
        st.subheader("📉 Actual vs Predicted")
        fig1, ax1 = plt.subplots(figsize=(4.2, 3))
        ax1.scatter(y_test, y_pred, color='green', alpha=0.7)
        ax1.set_xlabel("Actual")
        ax1.set_ylabel("Predicted")
        ax1.set_title("Actual vs Predicted")
        st.pyplot(fig1)

        # Correlation Heatmap (smaller size)
        st.subheader("🧠 Correlation Heatmap")
        fig2, ax2 = plt.subplots(figsize=(5.5, 3.5))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax2)
        st.pyplot(fig2)

    else:
        st.warning("⚠️ Please select at least one feature column.")

else:
    st.info("📎 Upload a CSV file to begin.")
