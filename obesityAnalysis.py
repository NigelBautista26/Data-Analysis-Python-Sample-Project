import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

# Factors identified as potential causes of obesity
factors = ['family_history_with_overweight', 'FAVC', 'CAEC', 'SCC', 'FAF']

factor_descriptions = {
    'family_history_with_overweight': 'Family History of Overweight',
    'FAVC': 'Frequent Consumption of High Caloric Food',
    'CAEC': 'Consumption of Food Between Meals',
    'SCC': 'Calories Consumption Monitoring',
    'FAF': 'Physical Activity Frequency'
}

# Calculating the prevalence or mean for each factor
factor_values = {factor_descriptions[factor]: (data[factor].mean() if data[factor].dtype != 'object'
                                               else data[factor].apply(lambda x: x == 'yes').mean())
                 for factor in factors}

# Sorting the factors by their calculated values
sorted_factors = sorted(factor_values.items(), key=lambda item: item[1], reverse=True)

# Taking the top 5 factors for visualization
top_factor_descriptions, top_values = zip(*sorted_factors[:5])

# Plotting
plt.figure(figsize=(12, 7))
plt.bar(top_factor_descriptions, top_values, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Factors')
plt.ylabel('Average Value / Proportion')
plt.title('Top 5 Causes of Obesity')
plt.xticks(rotation=25, ha="right")
plt.subplots_adjust(bottom=0.25)
plt.show()
