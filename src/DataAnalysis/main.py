import os
from DataStatistics import DataStatistics
from GraphicalStatistics import GraphicalStatistics
from Regression import Regression


if __name__ == '__main__':
    PLOTS_DIR = "plots"
    os.makedirs(PLOTS_DIR, exist_ok=True)

    """ Part 3 of Data Analysis """
    data_statistics = DataStatistics()
    data_statistics.descriptive_statistics()

    """ Part 4 of Data Analysis """
    graphical_statistics = GraphicalStatistics(PLOTS_DIR)
    graphical_statistics.price_by_city_boxplot()
    graphical_statistics.histogram_by_city()

    """ Part 5 of Data Analysis """
    graphical_statistics.numerical_heatmap()

    """ Part 6 and 7 of Data Analysis"""
    regression = Regression()
    regression.linear_regression()
