# Car Price Prediction

This project aims to predict the selling prices of cars based on features such as fuel type, seller type, and transmission type using both Linear Regression and Lasso Regression.

## Dependencies

The following libraries and modules are required to run the code:

- pandas
- matplotlib
- seaborn
- sklearn (specifically, train_test_split, LinearRegression, Lasso, and metrics)

## Dataset

The dataset, named 'car data.csv', contains features about cars along with their selling prices. It includes columns such as:

- Car Name
- Fuel Type
- Seller Type
- Transmission
- And others...

## Workflow

1. **Data Collection and Preprocessing**:
   - Load the dataset and inspect the first few rows.
   - Check the shape, null values, and data types.
   - Explore the distribution of categorical data.

2. **Encoding Categorical Data**:
   - Convert categorical columns (Fuel Type, Seller Type, and Transmission) into numerical representations.

3. **Splitting Data**:
   - Separate the features and target variable.
   - Further split the dataset into training and testing sets.

4. **Model Training using Linear Regression**:
   - Train a Linear Regression model on the training data.
   - Evaluate its performance on both training and test data.
   - Visualize the actual versus predicted prices.

5. **Model Training using Lasso Regression**:
   - Train a Lasso Regression model.
   - Similar to Linear Regression, evaluate its performance and visualize the predictions.

## Visualizations

Throughout the workflow, visualizations are created to aid understanding:
- Distribution of categorical data.
- Actual vs. predicted prices for both models.
