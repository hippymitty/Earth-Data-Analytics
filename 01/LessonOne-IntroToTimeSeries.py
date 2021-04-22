from matplotlib.axes._axes import _log as matplotlib_axes_logger
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import earthpy as et


# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Dealing with error thrown by one of the plots
matplotlib_axes_logger.setLevel('ERROR')
import warnings
warnings.filterwarnings('ignore')

# Adjust font size and style of all plots in notebook with seaborn
sb.set(font_scale=1.5, style="whitegrid")

# Download data
data = et.data.get_data('colorado-flood')

# Set working directory
os.chdir(os.path.join(et.io.HOME, 'Documents/Dev/EarthDataAnalytics', "data"))

# Define relative path to the data
file_path = os.path.join("colorado-flood",
                         "precipitation",
                         "805325-precip-daily-2003-2013.csv")

# Import the file as a pandas dataframe
boulder_precip_2003_2013 = pd.read_csv(file_path)
boulder_precip_2003_2013.head()

boulder_precip_2003_2013.plot(x="DATE", y="HPCP", title="Daily Precipitation ")
plt.show()

# Look at the range of values in the data - specifically the HPCP column, and the data types
boulder_precip_2003_2013["HPCP"].describe()
boulder_precip_2003_2013.dtypes

# Import data using datetime and no data value
boulder_precip_2003_2013 = pd.read_csv(file_path,
                                       # Make sure the dates import in datetime format
                                       parse_dates=['DATE'],
                                       # Set DATE as the index so you can subset data by time period
                                       index_col=['DATE'],
                                       # Mask no data values so they are not plotted / used in analysis
                                       na_values=['999.99'])

# View the data
boulder_precip_2003_2013.head()

# View summary statistics == Notice the DATE column is not included
boulder_precip_2003_2013.describe()

# List data types
boulder_precip_2003_2013.dtypes

# View the index for your data frame
boulder_precip_2003_2013.index

#Reset the index (if you want it to turn it back into a normal column)
boulder_precip_2003_2013.reset_index()

boulder_precip_2003_2013.plot(y="HPCP",
                              title="Hourly Precipitation")
plt.show()

# Subset data from 2005
precip_2005 = boulder_precip_2003_2013['2005']
precip_2005.head()

# Remove missing data values
precip_2005_clean = precip_2005.dropna()

precip_2005_clean = pd.read_csv(file_path,
                                       # Make sure the dates import in datetime format
                                       parse_dates=['DATE'],
                                       # Set DATE as the index so you can subset data by time period
                                       index_col=['DATE'],
                                       # Mask no data values so they are not plotted / used in analysis
                                       na_values=['999.99'])

precip_2005_clean.head()

# Plot the data using pandas
precip_2005_clean.reset_index().plot(x="DATE",
                                     y="HPCP",
                                     title="Hourly Precipitation",
                                     kind="scatter")
plt.show()


# Plot the data using native matplotlib
f, ax = plt.subplots()
ax.scatter(x=precip_2005_clean.index.values, y=precip_2005_clean["HPCP"])
plt.show()

#Resample Time Series Data
#Resampling time series data refers to the act of summarizing data over different time periods.
#For example, above you have been working with hourly data. However, you may want to plot data summarized by day.
precip_2005_daily = precip_2005_clean.resample("D").sum()

# Plot the data using native matplotlib
f, ax = plt.subplots()
ax.scatter(x=precip_2005_daily.index.values, y=precip_2005_daily["HPCP"])
plt.show()


#To do listed below

"""
Next steps & to do:
* Create a variable that contains precipitation data from 2012 and a second variable that contains data from 2013.
* Plot each variable on a subplot within a matplotlib figure. The 2012 data should be on the top of your figure and the 2013 data should be on the bottom.
Then answer the following questions:
* In which year 2012 or 2013 do you see the highest hourly precipitation value(s)?
* What is the max hourly precipitation value for each year? HINT: data-frame.max() should help you answer this question.
Recreate the same plot that you made above. However, this time set the y limits of each plot to span from 0 to 2 (ax1.set(ylim=[0, 2])) & customize your plot by changing the colors.
In the cell below create a scatter plot of your precipitation data. Subset the data to the date range September 1, 2013 (2013-09-01) to November 1, 2013 (2013-11-01). (data_frame_name['2005-05-01':'2005-06-31'])


Changes dates to display in a more readable format:
from matplotlib.dates import DateFormatter

# Place your code to plot your data here
flood_data = boulder_precip_2003_2013['2013-09-01':'2013-11-01']

f, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x=flood_data.index.values,
           y=flood_data["HPCP"])

# Define the date format
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)
ax.set(title="Optional Challenge \n Precipitation Sept - Nov 2013 \n Optional Plot with Dates Formatted Cleanly")
plt.show()

"""



