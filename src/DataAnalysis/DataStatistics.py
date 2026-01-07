import pandas as pd


def descriptive_statistics():
    df = pd.read_csv('../../data/apartments.csv')
    df = df[["city", "price"]]      # Select relevant columns

    results = []  # Container for results

    for city, g in df.groupby("city"):
        prices = g["price"]

        # Quantiles
        q1 = prices.quantile(0.25)
        q2 = prices.quantile(0.50)  # median
        q3 = prices.quantile(0.75)
        iqr = q3 - q1

        # Skewness
        skewness = prices.skew()

        # 1.5 * IQR rule
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = prices[(prices < lower_bound) | (prices > upper_bound)]

        # Store results
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

    # Convert to DataFrame
    summary_df = pd.DataFrame(results)

    # Display results
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)

    print(summary_df.round(2))


if __name__ == '__main__':
    """ Part 3 of Data Analysis """
    descriptive_statistics()
