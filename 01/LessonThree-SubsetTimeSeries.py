import os
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import earthpy as et

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn
sb.set(font_scale=1.5, style="whitegrid")

# Download the data
data = et.data.get_data('colorado-flood')

# Set working directory
os.chdir(os.path.join(et.io.HOME, 'Documents/Dev/EarthDataAnalytics'))

# Define relative path to file with daily precip total
file_path = os.path.join("data", "colorado-flood",
                         "precipitation",
                         "805325-precip-dailysum-2003-2013.csv")

# Import data using datetime and no data value
boulder_precip_2003_2013 = pd.read_csv(file_path, parse_dates=['DATE'], index_col= ['DATE'], na_values=['999.99'])

# View first few rows
boulder_precip_2003_2013.head()

# View dataframe info
boulder_precip_2003_2013.info()

# View summary statistics
boulder_precip_2003_2013.describe()

# View index values of dataframe
boulder_precip_2003_2013.index


# // Subset Pandas Dataframe By Year //
# Select 2013 data - view first few records
boulder_precip_2003_2013['2013'].head()
# Select 2013 data - view last few records
boulder_precip_2003_2013['2013'].tail()



# // Subset Pandas Dataframe By Month //
# Select all December data - view first few rows
boulder_precip_2003_2013[boulder_precip_2003_2013.index.month == 12].head()
# Select all December data - view last few rows
boulder_precip_2003_2013[boulder_precip_2003_2013.index.month == 12].tail()

# // Subset Pandas Dataframe By Day of Month //
# Select data for 1st of month - view first rows
boulder_precip_2003_2013[boulder_precip_2003_2013.index.day == 1]


# // Subset Pandas Dataframe Using Range of Dates //
# Subset data to May-Aug 2005
precip_may_aug_2005 = boulder_precip_2003_2013['2005-05-01':'2005-08-31']
precip_may_aug_2005.head()

#Rather than just checking the results of head() and tail(), you can actually query the min and max values of the index as follows:
# Check min value of index 
print(precip_may_aug_2005.index.min())
# Check max value of index 
print(precip_may_aug_2005.index.max())


# // Plot Temporal Subsets From Pandas Dataframe //
# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(precip_may_aug_2005.index.values,
       precip_may_aug_2005['DAILY_PRECIP'],
       color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Precipitation (inches)",
       title="Daily Total Precipitation\nMay - Aug 2005 for Boulder Creek")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

plt.show()