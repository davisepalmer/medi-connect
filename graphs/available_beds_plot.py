import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import math as m

# Load data
df = pd.read_csv('hospBedsIndia.csv')

# Convert 'Bed-to-Pop. Ratio' column to numeric, ignoring errors
df['Bed-to-Pop. Ratio'] = pd.to_numeric(df['Bed-to-Pop. Ratio'], errors='coerce')

# Drop NaN values if any
df.dropna(inplace=True)

# Extract columns
x = df['Total Beds']
y = df['Population']
state = df['State']

# Calculate R-squared
r_squared = abs(r2_score(y, x))

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, s=100)

# Add labels and title
plt.xlabel('Total Beds')
plt.ylabel('Population')
plt.title(f'Population vs Total Beds (R²={r_squared:.2f})')

# Add legend
legend = plt.legend(*scatter.legend_elements(), title='State', loc='upper left', bbox_to_anchor=(1, 1))
plt.setp(legend.get_texts(), rotation=45, ha='right')

# Annotate the plot with R-squared value
plt.annotate(f'R²={r_squared:.2f}', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=12)

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
