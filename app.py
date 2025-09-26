
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# --- 1. Business Understanding ---
st.title("CRISP-DM: Simple Linear Regression")

st.header("1. Business Understanding")
st.write("""
This application demonstrates a simple linear regression model to predict a target variable based on a single feature. 
The goal is to understand the relationship between two variables and to predict future outcomes.
We will follow the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.
""")

# --- 2. Data Understanding ---
st.header("2. Data Understanding")
st.write("""
In this step, we generate synthetic data to simulate a real-world scenario. 
You can adjust the parameters to see how they affect the data distribution and, consequently, the model's performance.
""")

# --- 3. Data Preparation ---
st.header("3. Data Preparation")
st.write("The data is generated and prepared for modeling based on your inputs.")

st.sidebar.header("Data Generation Parameters")
st.sidebar.write("Modify the parameters to generate new data.")

# Allow user to modify parameters
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
b = st.sidebar.slider("Intercept (b)", -10.0, 10.0, 1.0, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 2.0, 0.1)
n_points = st.sidebar.slider("Number of points", 50, 1000, 200, 10)

# Generate data
np.random.seed(42)
X = np.random.rand(n_points, 1) * 10
y = a * X + b + np.random.randn(n_points, 1) * noise

df = pd.DataFrame(data=np.hstack([X, y]), columns=["Feature (X)", "Target (y)"])

st.subheader("Generated Data")
st.write(df.head())

# Plot the data
st.subheader("Data Visualization")
fig, ax = plt.subplots()
ax.scatter(X, y, alpha=0.5, label="Generated Data")
ax.set_xlabel("Feature (X)")
ax.set_ylabel("Target (y)")
ax.set_title("Generated Data Distribution")
ax.legend()
st.pyplot(fig)


# --- 4. Modeling ---
st.header("4. Modeling")
st.write("""
We use a Simple Linear Regression model from scikit-learn to find the best-fit line for the data.
The model learns the optimal values for the slope and intercept from the data.
""")

# Train the model
model = LinearRegression()
model.fit(X, y)

st.subheader("Model Coefficients")
st.write(f"**Learned Slope (a):** {model.coef_[0][0]:.2f}")
st.write(f"**Learned Intercept (b):** {model.intercept_[0]:.2f}")


# --- 5. Evaluation ---
st.header("5. Evaluation")
st.write("""
We evaluate the model's performance using two common metrics:
- **Mean Squared Error (MSE):** The average of the squares of the errors. Lower is better.
- **R-squared (R²):** The proportion of the variance in the target variable that is predictable from the feature. Higher is better (closer to 1).

We also visualize the regression line against the original data.
""")

# Make predictions
y_pred = model.predict(X)

# Evaluation metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

st.subheader("Model Performance")
st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
st.write(f"**R-squared (R²):** {r2:.2f}")

# Plot the regression line
st.subheader("Regression Line vs. Data")
fig, ax = plt.subplots()
ax.scatter(X, y, alpha=0.5, label="Generated Data")
ax.plot(X, y_pred, color='red', linewidth=2, label="Regression Line")
ax.set_xlabel("Feature (X)")
ax.set_ylabel("Target (y)")
ax.set_title("Linear Regression Fit")
ax.legend()
st.pyplot(fig)


# --- 6. Deployment ---
st.header("6. Deployment")
st.write("""
This Streamlit application itself serves as the deployment of the model. 
It provides an interactive interface for users to:
- Generate new data by tuning parameters.
- See the model learn and make predictions in real-time.
- Evaluate the model's performance instantly.

To run this application on your own machine, you would execute the following command in your terminal:
```
streamlit run app.py
```
""")
