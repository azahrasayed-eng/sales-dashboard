# Sales Data Analysis Dashboard

## Overview
This project analyzes the Superstore Sales Dataset using Python (Pandas, NumPy, Matplotlib). It covers loading, inspecting, cleaning, processing, analyzing, and visualizing sales data to uncover patterns and business insights.

## Dataset
- Source: [Superstore Dataset Final on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Rows: 9,994
- Columns: 21
- No missing values, no duplicate rows

## How to Run
1. Install the required libraries:
   ```
   pip install pandas numpy matplotlib
   ```
2. Place `Sample - Superstore.csv` inside the `Data` folder.
3. Run the script:
   ```
   python main.py
   ```
4. Generated charts will be saved in the `visualizations` folder.

## Key Insights

1. **Technology leads in both sales and profit.** The Technology category has the highest total sales and the highest total profit among all categories, showing strong performance on both fronts.

2. **The West region generates the most sales**, making it the strongest-performing region overall.

3. **Phones sell the most, but Copiers are the most profitable.** Phones lead in total sales volume within sub-categories, while Copiers generate the highest profit per sub-category — suggesting a smaller number of high-margin sales.

4. **Sales values are right-skewed.** The mean sale value ($229.86) is much higher than the median ($54.49), meaning most orders are relatively small, while a handful of large orders (up to $22,638) pull the average up significantly.

5. **The dataset is fully clean**, with zero missing values and zero duplicate records, making the analysis reliable.

## Visualizations
- `sales_by_category.png` — Total sales by category
- `sales_over_time.png` — Monthly sales trend
- `sales_distribution.png` — Distribution of sale values
- `sales_vs_profit.png` — Relationship between sales and profit
- `sales_by_region.png` — Total sales by region

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
