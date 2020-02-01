# Project-2: Ames Housing Data and Kaggle Challenge

Submitted by: Loh Si Jun Shauna

# Problem Statement
This model aims to predict the sale price of a house given the Ames Housing Dataset.

# Executive Summary
## Contents:

Data Import and Cleansing

Exploratory Data Analysis and Data Visualisation

Feature Engineering: Interaction terms

Feature Selection: Chi-Square Test (Categorical Variables)

Feature Selection: Heatmap (Numerical Variables)

Dummy Variables

Create our features matrix (X) and target vector (y)

Build a linear regression model and conduct Cross Validation

Scaling

Regularization: Lasso Model

Regularization: Ridge Model

Prediction of target variable

# Data Dictionary

Refer to './datasets/data_dictionary.csv'.

# Conclusion

Using LassoCV algorithm on my test dataset produced the best predictions based on the RMSE score of 26,813.

To further improve the prediction model, it is important to know how external events affect housing sale prices, such as economic recession, trade war, natural disaster etc. This would be considered in addition to the given features in the housing dataset such as building type, house quality and neighbourhood. The trends observed via charts could also be better explained given the inputs from external events.

Another approach to improve the prediction model could be to include additional feature selection methods such as Recursive Feature Elimination and Variance Inflation Factor, which detects multi-collinearity in regression.
