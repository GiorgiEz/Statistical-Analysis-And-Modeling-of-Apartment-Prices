import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



def price_by_city_boxplot():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="city", y="price")

    plt.title("Apartment Sale Prices by City")
    plt.xlabel("City")
    plt.ylabel("Price")

    plt.tight_layout()
    plt.savefig(f"{PLOTS_DIR}/price_boxplot_by_city.png", dpi=300)
    plt.show()
    plt.close()


def histogram_by_city():
    cities = df["city"].unique()

    for city in cities:
        plt.figure(figsize=(8, 5))
        sns.histplot(
            df[df["city"] == city]["price"],
            bins=40,
            kde=True
        )
        plt.title(f"Price Distribution in {city}")
        plt.xlabel("Price")
        plt.ylabel("Frequency")

        plt.tight_layout()
        plt.savefig(f"{PLOTS_DIR}/price_histogram_{city}.png", dpi=300)
        plt.show()
        plt.close()

def numerical_heatmap():
    # Select numerical variables only
    num_vars = ["price", "area_m2", "bedrooms", "floor"]
    df_num = df[num_vars].dropna()

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
    plt.savefig(f"{PLOTS_DIR}/spearman_correlation_heatmap.png", dpi=300)
    plt.show()
    plt.close()



if __name__ == "__main__":
    PLOTS_DIR = "plots"
    os.makedirs(PLOTS_DIR, exist_ok=True)

    df = pd.read_csv("../../data/apartments.csv")

    """ Part 4 of Data Analysis """
    price_by_city_boxplot()
    histogram_by_city()

    """ Part 5 of Data Analysis """
    numerical_heatmap()
