import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class GraphicalStatistics:
    def __init__(self, PLOTS_DIR):
        """
        Initialize the GraphicalStatistics class.

        Loads the apartment dataset and sets the directory
        where all generated plots will be saved.
        """
        self.df = pd.read_csv("../../data/apartments.csv")
        self.PLOTS_DIR = PLOTS_DIR

    def price_by_city_boxplot(self):
        """
        Create and save a boxplot of apartment sale prices by city.

        This plot visualizes the distribution of prices across cities,
        highlighting medians, interquartile ranges, and outliers.
        It is used to compare price levels and variability between cities.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df, x="city", y="price")

        plt.title("Apartment Sale Prices by City")
        plt.xlabel("City")
        plt.ylabel("Price")

        plt.tight_layout()
        plt.savefig(f"{self.PLOTS_DIR}/price_boxplot_by_city.png", dpi=300)
        plt.show()
        plt.close()

    def histogram_by_city(self):
        """
        Create and save histograms of apartment sale prices for each city.

        These histograms are used to assess the shape of the price
        distributions (e.g., skewness) within each city and to
        identify the presence of extreme values.
        """
        cities = self.df["city"].unique()

        for city in cities:
            plt.figure(figsize=(8, 5))
            sns.histplot(
                self.df[self.df["city"] == city]["price"],
                bins=40,
                kde=True
            )
            plt.title(f"Price Distribution in {city}")
            plt.xlabel("Price")
            plt.ylabel("Frequency")

            plt.tight_layout()
            plt.savefig(f"{self.PLOTS_DIR}/price_histogram_{city}.png", dpi=300)
            plt.show()
            plt.close()

    def numerical_heatmap(self):
        """
        Create and save a Spearman correlation heatmap for numerical variables.

        This heatmap assesses associations between the outcome variable
        (price) and numerical explanatory variables, as well as
        correlations among the explanatory variables themselves.
        """
        # Select numerical variables only
        num_vars = ["price", "area_m2", "bedrooms", "floor"]
        df_num = self.df[num_vars].dropna()

        # Compute Spearman correlation
        corr_matrix = df_num.corr(method="spearman")

        # Plot heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
            linewidths=0.5
        )

        plt.title("Spearman Correlation Heatmap (Numerical Variables)")
        plt.tight_layout()
        plt.savefig(f"{self.PLOTS_DIR}/spearman_correlation_heatmap.png", dpi=300)
        plt.show()
        plt.close()
