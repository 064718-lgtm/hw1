# Simple Linear Regression with Streamlit

This project is a web application built with Streamlit that demonstrates a simple linear regression model. The application follows the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology to structure the process.

## CRISP-DM Steps Implemented

1.  **Business Understanding**: The application starts by explaining the goal of understanding linear relationships.
2.  **Data Understanding**: Users can generate and visualize a synthetic dataset.
3.  **Data Preparation**: The data is prepared in a pandas DataFrame for modeling.
4.  **Modeling**: A linear regression model from scikit-learn is trained on the data.
5.  **Evaluation**: The model is evaluated using MSE and R-squared, and the regression line is plotted.
6.  **Deployment**: The Streamlit application itself serves as the deployment, allowing for interactive use.

## Features

-   **Interactive Controls**: Users can modify the parameters of the data generation process:
    -   Slope (`a`) of the line
    -   Intercept (`b`) of the line
    -   Amount of `noise` in the data
    -   `Number of points` to generate
-   **Real-time Updates**: The application updates the data, model, and evaluation in real-time as the parameters are changed.
-   **Visualizations**: Includes scatter plots of the data and the fitted regression line.

## Installation

1.  Clone the repository or download the source code.
2.  Install the required Python packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application, execute the following command in your terminal from the project's root directory:

```bash
streamlit run app.py
```

This will open the application in your default web browser.
