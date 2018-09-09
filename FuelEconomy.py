
# coding: utf-8

# ### Fuel Economy Data
# This information is provided by the U.S. Environmental Protection Agency, Office of Mobile Sources, National Vehicle and Fuel Emissions Laboratory.
# 
# Attribute	Description
# Model	Vehicle make and model
# Displ	Engine displacement - the size of an engine in liters
# Cyl	The number of cylinders in a particular engine
# Trans	Transmission Type and Number of Gears
# Drive	Drive axle type (2WD = 2-wheel drive, 4WD = 4-wheel/all-wheel drive)
# Fuel	Fuel Type
# Cert Region*	Certification Region Code
# Sales Area**	Certification Region Code
# Stnd	Vehicle emissions standard code (View Vehicle Emissions Standards here)
# Stnd Description*	Vehicle emissions standard description
# Underhood ID	This is a 12-digit ID number that can be found on the underhood emission label of every vehicle. It's required by the EPA to designate its "test group" or "engine family." This is explained more here
# Veh Class	EPA Vehicle Class
# Air Pollution Score	Air pollution score (smog rating)
# City MPG	Estimated city mpg (miles/gallon)
# Hwy MPG	Estimated highway mpg (miles/gallon)
# Cmb MPG	Estimated combined mpg (miles/gallon)
# Greenhouse Gas Score	Greenhouse gas rating
# SmartWay	Yes, No, or Elite
# Comb CO2*	Combined city/highway CO2 tailpipe emissions in grams per mile
# 
# * Not included in 2008 dataset
# * Not included in 2018 dataset

# ### Assessing Data:
# Using pandas, explore all_alpha_08.csv and all_alpha_18.csv in the Jupyter Notebook below to answer
# questions below the notebook about these characteristics of the datasets:
# 
# - number of samples in each dataset
# - number of columns in each dataset
# - duplicate rows in each dataset
# - datatypes of columns
# - features with missing values
# - number of non-null unique values for features in each dataset
# - what those unique values are and counts for ea

# In[ ]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv') 
df_18 = pd.read_csv('all_alpha_18.csv')


# In[ ]:


# view 2008 dataset
df_08.head(1)


# In[ ]:


# view 2018 dataset
df_18.head(1)


# In[ ]:


print(df_08.shape)
df_08.head()


# In[ ]:


print(df_18.shape)
df_18.head()


# In[ ]:


df_18.isnull().sum()


# In[ ]:


df_08.isnull().sum()


# In[ ]:


df_18.duplicated().sum()


# In[ ]:


df_08.duplicated().sum()


# In[ ]:


# save progress for the next section
df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)


# ### Cleaning Column Labels
# 1. Drop extraneous columns
# Drop features that aren't consistent (not present in both datasets) or aren't relevant to our questions. Use pandas' drop function.
# 
# #### Columns to Drop:
# - From 2008 dataset: 'Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'
# - From 2018 dataset: 'Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'
# 
# 
# 2. Rename Columns
# Change the "Sales Area" column label in the 2008 dataset to "Cert Region" for consistency.
# Rename all column labels to replace spaces with underscores and convert everything to lowercase. (Underscores can be much easier to work with in Python than spaces. For example, having spaces wouldn't allow you to use df.column_name instead of df['column_name'] to select columns or use query(). Being consistent with lowercase and underscores also helps make column names easy to remember.)

# ### Drop Extraneous Columns:

# In[ ]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv') 
df_18 = pd.read_csv('all_alpha_18.csv')


# In[ ]:


# drop columns from 2008 dataset
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)

# confirm changes
df_08.head(1)


# In[ ]:


# drop columns from 2018 dataset
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1, inplace=True)

# confirm changes
df_18.head(1)


# ### Rename Columns

# In[ ]:


# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area': 'Cert Region'}, inplace=True)

# confirm changes
df_08.head(1)


# In[ ]:


# replace spaces with underscores and lowercase labels for 2008 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_08.head(1)


# In[ ]:


# confirm column labels for 2008 and 2018 datasets are identical
df_08.columns == df_18.columns


# In[ ]:


# make sure they're all identical like this
(df_08.columns == df_18.columns).all()


# In[ ]:


# replace spaces with underscores and lowercase labels for 2018 dataset
df_18.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_18.head(1)


# In[ ]:


df_08.to_csv('all_alpha_08.csv_edited.csv', index=False)


# In[ ]:


df_18.to_csv('all_alpha_18.csv_edited.csv', index=False)


# ### Filter, Drop Nulls, Dedupe:
# 1. Filter
# For consistency, only compare cars certified by California standards. Filter both datasets using query to select only rows where cert_region is CA. Then, drop the cert_region columns, since it will no longer provide any useful information (we'll know every value is 'CA').
# 
# 2. Drop Nulls
# Drop any rows in both datasets that contain missing values.
# 
# 3. Dedupe
# Drop any duplicate rows in both datasets.

# In[ ]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')


# In[ ]:


# view dimensions of dataset
df_08.shape


# In[ ]:


# view dimensions of dataset
df_18.shape


# ### Filter by Certification Region:

# In[ ]:


# filter datasets for rows following California standards
df_08 = df_08.query('cert_region == "CA"')
df_18 = df_18.query('cert_region == "CA"')


# In[ ]:


# confirm only certification region is California
df_08['cert_region'].unique()


# In[ ]:


# confirm only certification region is California
df_18['cert_region'].unique()


# In[ ]:


# drop certification region columns form both datasets
df_08.drop('cert_region', axis=1, inplace=True)
df_18.drop('cert_region', axis=1, inplace=True)


# In[ ]:


df_08.shape


# In[ ]:


df_18.shape


# ### Drop Rows with Missing Values:

# In[ ]:


# view missing value count for each feature in 2008
df_08.isnull().sum()


# In[ ]:


# view missing value count for each feature in 2018
df_18.isnull().sum()


# In[ ]:


# drop rows with any null values in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)


# In[ ]:


# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()


# In[ ]:


# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()


# ### Dedupe Data:

# In[ ]:


# print number of duplicates in 2008 and 2018 datasets
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())


# In[ ]:


# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)


# In[ ]:


# print number of duplicates again to confirm dedupe - should both be 0
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())


# In[ ]:


# save progress for the next section
df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)


# ### Fixing Data Types:
# In the next three sections, I'll make the following changes to make the datatypes consistent and practical to work with.
# 
# Fix cyl datatype
# - 2008: extract int from string.
# - 2018: convert float to int.
# 
# Fix air_pollution_score datatype
# - 2008: convert string to float.
# - 2018: convert int to float.
# 
# Fix city_mpg, hwy_mpg, cmb_mpg datatypes
# - 2008 and 2018: convert string to float.
# 
# Fix greenhouse_gas_score datatype
# - 2008: convert from float to int.

# ### Fixing cyl Data Type:
# - 2008: extract int from string
# - 2018: convert float to int

# In[ ]:


# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv') 


# In[ ]:


# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()


# In[ ]:


# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)


# In[ ]:


# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()


# In[ ]:


# convert 2018 cyl column to int
df_18['cyl'] = df_18['cyl'].astype(int)


# In[ ]:


df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)


# ### Fixing air_pollution_score Data Type:
# - 2008: convert string to float
# - 2018: convert int to float

# In[ ]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')


# In[ ]:


df_08.iloc[582]


# In[ ]:


# First, let's get all the hybrids in 2008
hb_08 = df_08[df_08['fuel'].str.contains('/')]
hb_08


# In[ ]:


# hybrids in 2018
hb_18 = df_18[df_18['fuel'].str.contains('/')]
hb_18


# In[ ]:


# create two copies of the 2008 hybrids dataframe
df1 = hb_08.copy()  # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy()  # data on second fuel type of each hybrid vehicle

# Each one should look like this
df1


# In[ ]:


# columns to split by "/"
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])


# In[ ]:


# this dataframe holds info for the FIRST fuel type of the hybrid
# aka the values before the "/"s
df1


# In[ ]:


# this dataframe holds info for the SECOND fuel type of the hybrid
# aka the values before the "/"s
df2


# In[ ]:


# combine dataframes to add to the original dataframe
new_rows = df1.append(df2)

# now we have separate rows for each fuel type of each vehicle!
new_rows


# In[ ]:


# drop the original hybrid rows
df_08.drop(hb_08.index, inplace=True)

# add in our newly separated rows
df_08 = df_08.append(new_rows, ignore_index=True)


# In[ ]:


# check that all the original hybrid rows with "/"s are gone
df_08[df_08['fuel'].str.contains('/')]


# In[ ]:


df_08.shape


# In[ ]:


# create two copies of the 2018 hybrids dataframe, hb_18
df1 = hb_18.copy()
df2 = hb_18.copy()


# Split values for fuel, city_mpg, hwy_mpg, cmb_mpg

# In[ ]:


# list of columns to split
split_columns = ['fuel', 'city_mpg', 'hwy_mpg', 'cmb_mpg']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])


# In[ ]:


# append the two dataframes
new_rows = df1.append(df2)

# drop each hybrid row from the original 2018 dataframe
# do this by using Pandas drop function with hb_18's index
df_18.drop(hb_18.index, inplace=True)

# append new_rows to df_18
df_18 = df_18.append(new_rows, ignore_index=True)


# In[ ]:


# check that they're gone
df_18[df_18['fuel'].str.contains('/')]


# In[ ]:


df_18.shape


# In[ ]:


# convert string to float for 2008 air pollution column
df_08.air_pollution_score = df_08.air_pollution_score.astype(float)


# In[ ]:


# convert int to float for 2018 air pollution column
df_18.air_pollution_score = df_18.air_pollution_score.astype(float)


# In[ ]:


df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)


# ### Fix `city_mpg`, `hwy_mpg`, `cmb_mpg` datatypes:
#     2008 and 2018: convert string to float

# In[ ]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')


# In[ ]:


# convert mpg columns to floats
mpg_columns = ['city_mpg', 'hwy_mpg', 'cmb_mpg']
for c in mpg_columns:
    df_18[c] = df_18[c].astype(float)
    df_08[c] = df_08[c].astype(float)


# ### convert from float to int:
# df_08['greenhouse_gas_score'] = df_08['greenhouse_gas_score'].astype(int)

# In[ ]:


# convert from float to int
df_08['greenhouse_gas_score'] = df_08['greenhouse_gas_score'].astype(int)


# In[ ]:


df_08.dtypes


# In[ ]:


df_18.dtypes


# In[ ]:


df_08.dtypes == df_18.dtypes


# In[ ]:


# Save your new CLEAN datasets as new files!
df_08.to_csv('clean_08.csv', index=False)
df_18.to_csv('clean_18.csv', index=False)


# ### Exploring with Visuals:

# In[ ]:


# load datasets
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# Compare the distributions of greenhouse gas score in 2008 and 2018:

# In[ ]:


df_08['greenhouse_gas_score'].hist();


# In[ ]:


df_18['greenhouse_gas_score'].hist();


# Distributions are more skewed to the left.

# How has the distribution of combined mpg changed from 2008 to 2018?

# In[ ]:


df_08['cmb_mpg'].hist();


# In[ ]:


df_18['cmb_mpg'].hist();


# Became much more skewed to the right.

# Describe the correlation between displacement and combined mpg.

# In[ ]:


# scatter plot 
df_18.plot(x='displ', y='cmb_mpg', kind='scatter');


# Negative correlation

# In[ ]:


# scatter plot 
df_18.plot(x='greenhouse_gas_score', y='cmb_mpg', kind='scatter');


# Positive Correlation

# ### Conclusions:

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# load datasets
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# In[ ]:


df_08.head(1)


# Q1: Are more unique models using alternative sources of fuel? By how much?

# In[ ]:


df_08.fuel.value_counts()


# In[ ]:


df_18.fuel.value_counts()


# Alternative sources of fuel available in 2008 are CNG and ethanol, and those in 2018 ethanol and electricity. 

# In[ ]:


# how many unique models used alternative sources of fuel in 2008
alt_08 = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
alt_08


# In[ ]:


# how many unique models used alternative sources of fuel in 2018
alt_18 = df_18.query('fuel in ["Ethanol", "Electricity"]').model.nunique()
alt_18


# In[ ]:


plt.bar(["2008", "2018"], [alt_08, alt_18])
plt.title("Number of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Number of Unique Models");


# Since 2008, the number of unique models using alternative sources of fuel increased by 24.

# In[ ]:


# total unique models each year
total_08 = df_08.model.nunique()
total_18 = df_18.model.nunique()
total_08, total_18


# In[ ]:


prop_08 = alt_08/total_08
prop_18 = alt_18/total_18
prop_08, prop_18


# In[ ]:


plt.bar(["2008", "2018"], [prop_08, prop_18])
plt.title("Proportion of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Proportion of Unique Models");


# Q2: How much have vehicle classes improved in fuel economy?

# In[ ]:


veh_08 = df_08.groupby('veh_class').cmb_mpg.mean()
veh_08


# In[ ]:


veh_18 = df_18.groupby('veh_class').cmb_mpg.mean()
veh_18


# In[ ]:


# how much they've increased by for each vehicle class
inc = veh_18 - veh_08
inc


# In[ ]:


# only plot the classes that exist in both years
inc.dropna(inplace=True)
plt.subplots(figsize=(8, 5))
plt.bar(inc.index, inc)
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG');


# Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?

# In[ ]:


# smartway labels for 2008
df_08.smartway.unique()


# In[ ]:


# get all smartway vehicles in 2008
smart_08 = df_08.query('smartway == "yes"')


# In[ ]:


# explore smartway vehicles in 2008
smart_08.describe()


# In[ ]:


# smartway labels for 2018
df_18.smartway.unique()


# In[ ]:


# get all smartway vehicles in 2018
smart_18 = df_18.query('smartway in ["Yes", "Elite"]')


# In[ ]:


smart_18.describe()


# Q4: What features are associated with better fuel economy?

# In[ ]:


top_08 = df_08.query('cmb_mpg > cmb_mpg.mean()')
top_08.describe()


# In[ ]:


top_18 = df_18.query('cmb_mpg > cmb_mpg.mean()')
top_18.describe()


# ### Merging Datasets:
# 
# Use Pandas Merges to create a combined dataset from clean_08.csv and clean_18.csv.

# In[ ]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# Create combined dataset

# In[ ]:


# rename 2008 columns
df_08.rename(columns=lambda x: x[:10] + "_2008", inplace=True)


# In[ ]:


# view to check names
df_08.head()


# In[ ]:


# merge datasets
df_combined = df_08.merge(df_18, left_on='model_2008', right_on='model', how='inner')


# In[ ]:


# view to check merge
df_combined.head()


# In[ ]:


df_combined.to_csv('combined_dataset.csv', index=False)


# 1. Create a new dataframe, model_mpg, that contain the mean combined mpg values in 2008 and 2018 for each unique model

# In[ ]:


# load datasets
import pandas as pd

new_df = pd.read_csv('combined_dataset.csv')
new_df.dtype


# 2. Create a new column, mpg_change, with the change in mpg

# In[ ]:


new_df.groupby('model').mean()


# In[ ]:


new_df['mpg_change'] = new_df['cmb_mpg_2008'] - new_df['cmb_mpg']
#new_df.insert(1, 'mpg_change',int)


# In[ ]:


new_df.head(1)


# 3. Find the vehicle that improved the most

# In[ ]:


new_df['mpg_change'].max()


# In[ ]:


new_df.query('mpg_change == 6')


# Answer: Cheverolet Impala
