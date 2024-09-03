import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('sub-division_population_of_pakistan.csv')
print(df)

#generate a report
profile = ProfileReport(df, title="Subdivision population of Pakistan")
#html file
profile.to_file("sub-division_population_of_pakistan.html")