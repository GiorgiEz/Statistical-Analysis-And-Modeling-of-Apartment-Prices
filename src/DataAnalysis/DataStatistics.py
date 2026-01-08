import pandas as pd


class DataStatistics:
    def __init__(self):
        """
        Initialize the DataStatistics class.

        Loads the apartment dataset that will be used
        to compute descriptive statistics for analysis.
        """
        self.df = pd.read_csv('../../data/apartments.csv')

    def descriptive_statistics(self):
        """
        Compute descriptive statistics for apartment prices by city.

        This method evaluates the distribution of apartment sale prices
        in each city by calculating:
        - skewness,
        - median and interquartile range (IQR),
        - outlier thresholds using the 1.5·IQR rule,
        - minimum and maximum values.

        The results are used to assess distribution shape and
        to justify the use of robust summary statistics.
        """
        # Select relevant columns
        df = self.df[["city", "price"]]

        results = []  # Container for city-level statistics

        # Compute statistics separately for each city
        for city, g in df.groupby("city"):
            prices = g["price"]

            # Quantiles and interquartile range
            q1 = prices.quantile(0.25)
            q2 = prices.quantile(0.50)  # Median
            q3 = prices.quantile(0.75)
            iqr = q3 - q1

            # Measure skewness of the price distribution
            skewness = prices.skew()

            # Define outlier thresholds using the 1.5·IQR rule
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            # Identify outliers
            outliers = prices[(prices < lower_bound) | (prices > upper_bound)]

            # Store results for the current city
            results.append({
                "city": city,
                "count": len(prices),
                "skewness": skewness,
                "Q1": q1,
                "median": q2,
                "Q3": q3,
                "IQR": iqr,
                "lower_bound": lower_bound,
                "upper_bound": upper_bound,
                "outliers_count": len(outliers),
                "min": prices.min(),
                "max": prices.max()
            })

        # Convert results to a DataFrame for display
        summary_df = pd.DataFrame(results)

        # Configure display options to show all columns
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", None)

        # Print rounded summary statistics
        print(summary_df.round(2))
