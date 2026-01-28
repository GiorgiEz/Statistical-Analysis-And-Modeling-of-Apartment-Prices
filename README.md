# Statistical Analysis and Modeling of Apartment Prices

This project analyzes apartment price data using both **computational/statistical modeling** and **exploratory data analysis with visualization**.
The project is divided into **two independent parts**, each run separately.

---

## Project Structure

```
Statistical-Analysis-And-Modeling-of-Apartment-Prices/
│
├── data/
│   └── apartments.csv
│
├── src/
│   ├── ComputationalAndAnalytical/
│   │   └── NegativeBinomialMLE.py
│   │
│   └── DataAnalysis/
│       ├── plots/
│       │   ├── price_boxplot_by_city.png
│       │   ├── price_histogram_*.png
│       │   └── spearman_correlation_heatmap.png
│       ├── DataStatistics.py
│       ├── GraphicalStatistics.py
│       ├── Regression.py
│       └── main.py
│
├── requirements.txt
├── README.md
└── Statistical_Analysis_and_Modeling_of_Apartment_Prices.docx
```

---

## Requirements

* Python **3.9+**
* Required libraries are listed in `requirements.txt`

### Install dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

---

## Part 1: Computational and Analytical Modeling

**Location:**

```
src/ComputationalAndAnalytical/
```

**Description:**

* Focuses on computational/statistical modeling.
* Implements **Negative Binomial Maximum Likelihood Estimation (MLE)**.
* This part is **independent** of the data analysis pipeline.

### How to run

Run the file **directly**:

```bash
python src/ComputationalAndAnalytical/NegativeBinomialMLE.py
```

---

## Part 2: Data Analysis and Visualization

**Location:**

```
src/DataAnalysis/
```

**Description:**

* Performs descriptive statistics, regression analysis, and visualization.
* Generates plots such as:

  * Price histograms by city
  * Boxplots
  * Spearman correlation heatmap
* Output figures are saved in `src/DataAnalysis/plots/`.

### How to run

Run the main entry point:

```bash
python src/DataAnalysis/main.py
```

This script internally calls:

* `DataStatistics.py`
* `GraphicalStatistics.py`
* `Regression.py`

---

## Data

* Input data file:

  ```
  data/apartments.csv
  ```

---

## Notes

* The two parts are **not dependent on each other** and must be run separately.
* All generated plots are saved automatically; no manual configuration is required.
* The `.docx` file contains the written report of the analysis.

---