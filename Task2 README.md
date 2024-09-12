# Retail Sales Data Analysis 
This project performs an analysis on a retail company's sales data to identify trends, peak sales periods, and popular products. The dataset includes features such as temperature, fuel prices, markdowns, CPI, unemployment, and weekly sales per store and department. The analysis uses **Pandas** for data manipulation and **Matplotlib** for visualization.
## Table of Contents 
#### Overview
#### Installation 
#### Usage 
#### Data Analysis
#### Sales Trend Over Time
#### Peak Sales Periods
#### Popular Departments
#### Holiday Sales Analysis
#### Markdown Effect on Sales
#### Results
## Overview
This project processes and analyzes sales data from a retail company to derive actionable insights. The following analyses are performed:
- Sales trends over time.
* Identification of peak sales periods.
+ Analysis of the most popular departments.
- Impact of holidays on sales.
* Analysis of how markdowns affect sales.
## Installation
To run this project, you need to have Python installed along with the following packages:
`pip install pandas matplotlib`
## Usage
1. Clone the repository:
`git clone https://github.com/your-username/retail-sales-analysis.git`
`cd retail-sales-analysis`
2. Place your dataset *(Features data set.csv)* in the project directory.
3. Run the script:
`python sales_analysis.py`
## Data Analysis
#### Sales Trend Over Time
The script groups the data by *Date* and sums the *Weekly_Sales* to visualize the sales trend over time. A line plot is generated showing the total weekly sales over the entire period.
#### Peak Sales Periods
By sorting the total weekly sales, the top 10 peak sales periods are identified, providing insights into the dates with the highest sales.
#### Popular Departments
The script groups the data by Dept and calculates the total weekly sales per department. The top 10 most popular departments by sales are identified and displayed.
#### Holiday Sales Analysis
The effect of holidays on sales is examined by grouping the data by the *IsHoliday* feature and calculating total weekly sales during holidays and non-holidays.
#### Markdown Effect on Sales
The correlation between markdowns and weekly sales is calculated using the *MarkDown1-5* features. This reveals the extent to which markdowns impact sales.
## Results
- **Sales Trend:** Sales fluctuate over time with noticeable peaks during certain periods.
- **Peak Sales Periods:** The highest sales occur during holidays and specific high-demand periods.
- **Popular Departments:** Certain departments consistently perform better than others in terms of weekly sales.
- **Holiday Sales:** Holidays significantly affect sales, often boosting them.
- **Markdown Impact:** Markdown strategies can influence sales, with varying levels of effectiveness depending on the markdown type.
Here is a visual representation in the form of graph about *Total Weekly Sales over Time.*
![Figure_1 task 2](https://github.com/user-attachments/assets/07661e6a-28f3-4204-bb25-16e13ed07011)
