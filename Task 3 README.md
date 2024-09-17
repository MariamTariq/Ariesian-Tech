# Cereal Dataset Analysis
This project involves an exploratory data analysis (EDA) on a dataset of cereals, focusing on key nutritional factors such as sugar content, sodium, calories, and their correlations with consumer ratings. The analysis provides insights into the healthiness of different cereals based on their nutritional profiles and ratings.
## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Steps](#analysis-steps)
- [Results](#results)
- [Contributing](#contributing)
## Introduction
The goal of this project is to perform a comprehensive analysis of the cereals dataset, identifying trends and correlations in nutritional data. The analysis includes identifying cereals with the highest sugar, sodium, and calorie content, as well as understanding how these factors correlate with consumer ratings. It provides valuable insights for consumers seeking healthier cereal options and for manufacturers to improve their product formulations.
## Dataset
The dataset used in this analysis contains information on 77 cereals, including:
- **Nutritional factors**: Calories, protein, fat, sodium, fiber, carbohydrates, sugars, potassium
- **Vitamins percentage**
- **Consumer ratings**
- **Manufacturer information**
### Dataset Source
The dataset file `cereal.csv` is included in the project repository.
## Project Structure
The project repository contains the following files:
```
.
├── cereal.csv                  # Dataset file
├── cereal_analysis.ipynb        # Jupyter notebook for analysis
├── analysis.py                  # Python script for performing EDA
└── README.md                    # Project README file
```
## Installation
To run the analysis on your local machine, follow these steps:
1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cereal-analysis.git
   cd cereal-analysis
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the analysis:**

   ```bash
   python analysis.py
   ```
## Usage
The project contains two main components for analysis:
- **`analysis.py`**: A Python script that performs the exploratory data analysis (EDA).
- **`cereal_analysis.ipynb`**: A Jupyter notebook for interactive data exploration and visualization.
You can run either of these files to explore the dataset and visualize trends. The analysis includes histograms, scatter plots, and correlation heatmaps to illustrate relationships between nutritional factors and consumer ratings.
## Analysis Steps
The following key steps are performed in the analysis:
1. **Data Loading**: Load the cereal dataset for analysis.
2. **Descriptive Statistics**: Generate basic statistics for numerical columns such as sugar, sodium, and calories.
3. **Key Nutritional Factor Analysis**: Identify the top 5 cereals with the highest sugar, sodium, and calorie content.
4. **Data Visualization**: Histograms for sugar, sodium, and calories. Scatter plot for sugar content vs. consumer ratings.
5. **Correlation Analysis**: A correlation matrix to explore relationships between nutritional factors.
6. **Manufacturer Insights**: Group cereals by manufacturer to explore average sugar content by brand.
## Results
Some key insights from the analysis include:
- Cereals with the highest sugar content, which are typically targeted at children, have lower consumer ratings.
- High-sodium cereals often have high-calorie content as well.
- Manufacturers vary significantly in their average sugar content, with certain brands consistently producing sweeter cereals.
## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
Please ensure that your changes are well-documented and tested.
### Sugar,Sodium and Calorie Distribution Graph:
![Figure_1 task 3](https://github.com/user-attachments/assets/7da0dced-f526-4f17-ac37-dcb6b916a672)
### Correlational Matrix of Nutritional Factors:
![Figure_2 task 3](https://github.com/user-attachments/assets/0545091a-6ed2-4d95-8de5-8d7022abfc41)
### Sugar Content Vs Consumer Rating:
![Figure_3 task 3](https://github.com/user-attachments/assets/beabc170-123b-4cf9-96e7-e2c454f5f066)
### Average Sugar Content by Manufacturer:
![Figure_4 task 3](https://github.com/user-attachments/assets/e09e346b-fffb-4201-960f-28011c3382a0)
