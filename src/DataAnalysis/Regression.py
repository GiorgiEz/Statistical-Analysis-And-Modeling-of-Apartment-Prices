import pandas as pd
import statsmodels.api as sm


class Regression:
    def __init__(self):
        """
        Initialize the Regression class.

        Loads the apartment dataset that will be used
        for fitting the linear regression model.
        """
        self.df = pd.read_csv("../../data/apartments.csv")

    def linear_regression(self):
        """
        Fit a linear regression model to apartment sale prices
        using ordinary least squares (OLS).

        The model explains apartment price as a function of:
        - apartment area,
        - number of bedrooms,
        - city-level location,
        - district-level location.

        Categorical variables (city and district) are encoded
        using dummy variables with one reference category
        omitted to avoid multicollinearity.
        """
        # Select relevant variables and remove missing values
        df_model = self.df[
            ["price", "area_m2", "bedrooms", "city", "district_name"]
        ].dropna()

        # Dummy-encode categorical variables (city and district)
        df_encoded = pd.get_dummies(
            df_model,
            columns=["city", "district_name"],
            drop_first=True,
            dtype=int
        )

        # Define outcome and predictors
        y = df_encoded["price"]
        X = df_encoded.drop(columns="price")

        # Add intercept term to the design matrix
        X = sm.add_constant(X)

        # Fit ordinary least squares regression
        model = sm.OLS(y, X)
        results = model.fit()

        # Print regression results summary
        print(results.summary())
