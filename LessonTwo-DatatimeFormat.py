import os
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import earthpy as et


# // Working With Datetime Objects in Python //

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn
sb.set(font_scale=1.5, style="whitegrid")

# Download csv of temp (F) and precip (inches) in July 2018 for Boulder, CO
file_url = "https://ndownloader.figshare.com/files/12948515"
et.data.get_data(url=file_url)

# Set working directory
os.chdir(os.path.join(et.io.HOME, 'Documents/Dev/EarthDataAnalytics'))

# Define relative path to file
file_path = os.path.join("data", "earthpy-downloads",
                         "july-2018-temperature-precip.csv")

# Import file into pandas dataframe
boulder_july_2018 = pd.read_csv(file_path)

# Display first few rows
boulder_july_2018.head()

# View dataframe info
boulder_july_2018.info()

# View column data types
boulder_july_2018.dtypes

# Check data type of first value in date column
type(boulder_july_2018['date'][0])

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.plot(boulder_july_2018['date'], boulder_july_2018['precip'], color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Precipitation (inches)",
       title="Daily Total Precipitation\nBoulder, Colorado in July 2018")

plt.show()
#There are many negative values in this dataset - these are actually “no data” values
#You can avoid this problem by converting the dates from strings to a datetime object during the import of data into a pandas dataframe. 
#Once the dates are converted to a datetime object, you can more easily customize the dates on your plot, resulting in a more visually appealing plot.


# // Import Date Column into Pandas Dataframe As Datetime Object //

# Import data using datetime and set index to datetime
boulder_july_2018 = pd.read_csv(file_path, parse_dates=['date'], index_col=['date'])

boulder_july_2018.head()

# View dataframe info
boulder_july_2018.info()

# View column data types
boulder_july_2018.dtypes

# View dataframe index
boulder_july_2018.index



# // Plot Dates From Pandas Dataframe Using Datetime //
#Version one
# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.scatter(boulder_july_2018.index.values,
        boulder_july_2018['precip'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Precipitation (inches)",
       title="Daily Total Precipitation\nBoulder, Colorado in July 2018")

plt.show()

#Tidying up, version two

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(boulder_july_2018.index.values,
        boulder_july_2018['precip'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Precipitation (inches)",
       title="Daily Total Precipitation\nBoulder, Colorado in July 2018")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

plt.show()


# // Work With No Data Values in Pandas Dataframe //

#Often, you’ll find a dataset that uses a specific value for “no data”. 
# In many scientific disciplines, the value -999 is often used to indicate “no data” values.
# If you do not specify that the value -999 is the “no data” value, the values will be imported 
# as real data, which will impact any statistics, calculations, and plots using the data.


# Both min and mean are affected by these negative, no data values
boulder_july_2018.describe()

# Tell pandas to treat all values of -999 as no data, and thus, not to include them in the analysis or on a plot.
# Import data using datetime and no data value
boulder_july_2018 = pd.read_csv(file_path,
                                parse_dates=['date'],
                                index_col=['date'],
                                na_values=[-999])

boulder_july_2018.head()
# Both min and mean now accurately reflect the true data
boulder_july_2018.describe()

#Finally, plot the data one last time to see that the negative values -999 are no longer on the plot.
# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.scatter(boulder_july_2018.index.values,
        boulder_july_2018['precip'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Precipitation (inches)",
       title="Daily Total Precipitation\nBoulder, Colorado in July 2018")

plt.show()

#Note: if there are multiple types of missing values in your dataset, you can add multiple values in the na_values parameter as follows:
#na_values=['NA', ' ', -999])