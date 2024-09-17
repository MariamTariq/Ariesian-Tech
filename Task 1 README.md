# Data Profiling with `ydata_profiling`
This project includes a Python script for generating a data profiling report using the `ydata_profiling` library. The profiling report provides an overview of the dataset, including statistics, distributions, and correlations, making it easier to understand the structure and quality of the data.
## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
- [Usage](#usage)
- [Example](#example)
## Overview
This project is designed to simplify the process of data profiling by automating the generation of detailed reports on datasets. The report includes statistics, distribution plots, correlation matrices, and missing value analysis, which help users quickly gain insights into the data.
## Prerequisites
To run this project, you will need the following Python packages:
- `pandas`
- `ydata_profiling`
You can install these packages using `pip`:
```bash
pip install pandas ydata-profiling
```
## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/data-profiling.git
   cd data-profiling
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Place your dataset** (`sub-division_population_of_pakistan.csv`) in the project directory.
4. **Run the script**:

   ```bash
   python profile_data.py
   ```
## Code Explanation
Here's a breakdown of the script:
```python
import pandas as pd
from ydata_profiling import ProfileReport
```
- **Imports**: 
  - `pandas` is used for data manipulation and analysis.
  - `ProfileReport` from `ydata_profiling` is used to generate a detailed data profiling report.

```python
df = pd.read_csv('sub-division_population_of_pakistan.csv')
print(df)
```
- **Read CSV File**: 
  - This line reads a CSV file named `sub-division_population_of_pakistan.csv` into a Pandas DataFrame named `df`. 
  - `print(df)` outputs the contents of the DataFrame to the console.

```python
profile = ProfileReport(df, title="Subdivision population of Pakistan")
```
- **Generate Profile Report**: 
  - `ProfileReport` creates a profiling report of the DataFrame. 
  - The `title` parameter sets the report title to `"Subdivision population of Pakistan"`.
```python
profile.to_file("sub-division_population_of_pakistan.html")
```
- **Save Report as HTML**: 
  - `to_file` saves the generated report to an HTML file named `sub-division_population_of_pakistan.html`. 
  - You can open this HTML file in a web browser to view the comprehensive data profiling report.
## Usage
1. Place your CSV file (`sub-division_population_of_pakistan.csv`) in the same directory as this script.
2. Run the script to generate the data profiling report.
3. Open the resulting `sub-division_population_of_pakistan.html` file in a web browser to explore the report.
## Example
For a dataset on the subdivision population of Pakistan, the generated HTML report will include:
- Overview statistics (mean, median, etc.)
- Data distribution visualizations
- Correlation matrices
- Missing value information
- And much more!
