
# coding: utf-8

# # Wine Quality Analysis

# ### Purpose:
# 
# -  Use the analysis process to investigate a dataset on wine quality. 
# -  Explore new ways of manipulating data with NumPy and Pandas, as well as powerful visualization tools with Matplotlib.

# ### Data Set Information:
# 
# The Wine Qualithy Data Set is gathered from the following website:
# https://archive.ics.uci.edu/ml/datasets/Wine+Quality
# 
# The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult: [Web Link] or the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.). 
# 
# These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are munch more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods. 
# 
# 
# ### Attribute Information:
# 
# For more information, read [Cortez et al., 2009]. 
# Input variables (based on physicochemical tests): 
# 1 - fixed acidity 
# 2 - volatile acidity 
# 3 - citric acid 
# 4 - residual sugar 
# 5 - chlorides 
# 6 - free sulfur dioxide 
# 7 - total sulfur dioxide 
# 8 - density 
# 9 - pH 
# 10 - sulphates 
# 11 - alcohol 
# Output variable (based on sensory data): 
# 12 - quality (score between 0 and 10)
# 
# ### Source:
# 
# Paulo Cortez, University of Minho, Guimarães, Portugal, http://www3.dsi.uminho.pt/pcortez 
# A. Cerdeira, F. Almeida, T. Matos and J. Reis, Viticulture Commission of the Vinho Verde Region(CVRVV), Porto, Portugal 
# @2009
# 
# ### Tools:
# You will need pandas, numpy, matplotlib, and seaborn.
# 
# Install seasborn - https://seaborn.pydata.org/installing.html
# Install matplotlib - https://matplotlib.org/faq/installing_faq.html

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
sns.set_context('notebook')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# ### Assessing Data:
# 
# Using Pandas, explore winequality-red.csv and winequality-white.csv in the Jupyter notebook below to answer quiz questions below the notebook about these characteristics of the datasets:
# 
# number of samples in each dataset
# number of columns in each dataset
# features with missing values
# duplicate rows in the white wine dataset
# number of unique values for quality in each dataset
# mean density of the red wine dataset

# In[ ]:


red_df = pd.read_csv('winequality-red.csv', sep=';')
white_df = pd.read_csv('winequality-white.csv', sep=';')


# In[ ]:


red_df.rename(columns={'total_sulfur-dioxide':'total_sulfur_dioxide'}, inplace=True)


# - How many samples of red wine are there?
# - How many columns are in each dataset?

# In[ ]:


print(red_df.shape)
red_df.head()


# - How many samples of white wine are there?
# - How many columns are in each dataset?

# In[ ]:


print(white_df.shape)
white_df.head()


# - Which features have missing values?

# In[ ]:


red_df.isnull().sum()


# In[ ]:


white_df.isnull().sum()


# - How many duplicate rows are in the white wine dataset?

# In[ ]:


white_df.duplicated().sum()


# - How many unique values of quality are in the red wine dataset?

# In[ ]:


red_df.quality.nunique()


# - How many unique values of quality are in the white wine dataset?

# In[ ]:


white_df.quality.nunique()


# - What is the mean density in the red wine dataset?

# In[ ]:


red_df.density.mean()


# ### Appending Data:
# 
# Combine the red and white datasets to make your analysis more efficient. Use NumPy to create a new column that preserves color information, and then use pandas to combine the dataframes.
# 
# ### Create Color Columns:
# Create two arrays as long as the number of rows in the red and white dataframes that repeat the value “red” or “white.” 

# In[ ]:


# create color array for red dataframe
color_red = np.repeat('red', red_df.shape[0])

# create color array for white dataframe
color_white = np.repeat('white', white_df.shape[0])


# Add arrays to the red and white dataframes. Do this by setting a new column called 'color' to the appropriate array. 

# In[ ]:


red_df['color'] = color_red
red_df.head()


# In[ ]:


white_df['color'] = color_white
white_df.head()


# ### Combine DataFrames with Append:

# In[ ]:


# append dataframes
wine_df = red_df.append(white_df)

# view dataframe to check for success
wine_df.head(10)


# In[ ]:


wine_df.describe()


# ### Save Combined Dataset:
# 
# - Save the newly combined dataframe as winequality_edited.csv. 
# - Set index=False to avoid saving with an unnamed column.

# In[ ]:


wine_df.to_csv('winequality_edited.csv', index=False)


# In[ ]:


wine_df = pd.read_csv('winequality_edited.csv')
wine_df.head(3)


# ### Exploring with Visuals:
# 
# - Based on histograms of columns in this dataset, which of the following feature variables appear skewed to the right? Fixed Acidity, Total Sulfur Dioxide, pH, Alcohol
# - Based on scatterplots of quality against different feature variables, which of the following is most likely to have a positive impact on quality? Volatile Acidity, Residual Sugar, pH, Alcohol

# In[ ]:


# scatter plot 
wine_df.plot(x= 'volatile acidity', y= 'quality', kind='scatter');


# In[ ]:


# scatter plot 
wine_df.plot(x='pH', y='quality', kind='scatter');


# In[ ]:


# scatter plot 
wine_df.plot(x='alcohol', y='quality', kind='scatter');


# In[ ]:


# scatter plot 
wine_df.plot(x='residual sugar', y='quality', kind='scatter');


# In[ ]:


# plot distribution 
wine_df['fixed acidity'].hist();


# In[ ]:


wine_df['total sulfur dioxide'].hist();


# In[ ]:


wine_df['volatile acidity'].hist();


# In[ ]:


wine_df['citric acid'].hist();


# In[ ]:


wine_df['residual sugar'].hist();


# In[ ]:


wine_df['chlorides'].hist();


# In[ ]:


wine_df['alcohol'].hist();


# In[ ]:


wine_df['free sulfur dioxide'].hist();


# In[ ]:


wine_df['density'].hist();


# In[ ]:


wine_df['sulphates'].hist();


# In[ ]:


wine_df['pH'].hist();


# ### Drawing Conclusions Using Groupby:

# Q1: Is a certain type of wine (red or white) associated with higher quality?
# 
# For this question, compare the average quality of red wine with the average quality of white wine with groupby. To do this group by color and then find the mean quality of each group.

# In[ ]:


# Find the mean quality of each wine type (red and white) with groupby
wine_df.groupby('color').mean().quality


# Q2: What level of acidity (pH value) receives the highest average rating?
# 
# 
# Create a categorical variable from a quantitative variable by creating your own categories. pandas' cut function let's you "cut" data in groups. Using this, create a new column called acidity_levels with these categories:
# 
# #### Acidity Levels:
# 1. High: Lowest 25% of pH values
# 2. Moderately High: 25% - 50% of pH values
# 3. Medium: 50% - 75% of pH values
# 4. Low: 75% - max pH value

# In[ ]:


# View the min, 25%, 50%, 75%, max pH values with Pandas describe
wine_df.describe().pH


# In[ ]:


# Bin edges that will be used to "cut" the data into groups
bin_edges = [2.72, 3.11, 3.21, 3.32, 4.01] # Fill in this list with five values you just found


# In[ ]:


# Labels for the four acidity level groups
bin_names = ['high', 'mod_high', 'medium', 'low'] # Name each acidity level category


# In[ ]:


# Creates acidity_levels column
wine_df['acidity_levels'] = pd.cut(wine_df['pH'], bin_edges, labels=bin_names)

# Checks for successful creation of this column
wine_df.head()


# - Is the mean quality of red wine greater than, less than, or equal to that of white wine?

# In[ ]:


# Find the mean quality of each acidity level with groupby
wine_df.groupby('acidity_levels').mean().quality


# In[ ]:


wine_df.groupby(['quality','color'], as_index = False)['pH'].mean()


# In[ ]:


wine_df.groupby(['quality','color'], as_index = False)['fixed acidity', 'volatile acidity'].mean()


# In[ ]:


# Save changes for the next section
wine_df.to_csv('winequality_edited.csv', index=False)


# - Do wines with higher alcoholic content receive better ratings?

# In[ ]:


# get the median amount of alcohol content
wine_df.alcohol.median()


# In[ ]:


# select samples with alcohol content less than the median
low_alcohol = wine_df[wine_df.alcohol < 10.3]

# select samples with alcohol content greater than or equal to the median
high_alcohol = wine_df[wine_df.alcohol >= 10.3]

# ensure these queries included each sample exactly once
num_samples = wine_df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # should be True


# In[ ]:


# get mean quality rating for the low alcohol and high alcohol groups
low_alcohol.quality.mean(), high_alcohol.quality.mean()


# - Do sweeter wines receive better ratings?¶

# In[ ]:


# get the median amount of residual sugar
wine_df['residual sugar'].median()


# In[ ]:


# select samples with alcohol content less than the median
low_alcohol = wine_df[wine_df.alcohol < 10.3]

# select samples with alcohol content greater than or equal to the median
high_alcohol = wine_df[wine_df.alcohol >= 10.3]

# ensure these queries included each sample exactly once
num_samples = wine_df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # should be True


# In[ ]:


# get mean quality rating for the low alcohol and high alcohol groups
low_alcohol.quality.mean(), high_alcohol.quality.mean()


# Do sweeter wines receive better ratings?

# In[ ]:


# get the median amount of residual sugar
wine_df['residual sugar'].median()


# In[ ]:


# select samples with residual sugar less than the median
low_sugar = wine_df[wine_df['residual sugar'] < 3]

# select samples with residual sugar greater than or equal to the median
high_sugar = wine_df[wine_df['residual sugar'] >= 3]

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() # should be True


# In[ ]:


# get mean quality rating for the low sugar and high sugar groups
low_sugar.quality.mean(), high_sugar.quality.mean()


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
colors = ['red', 'white']
color_means = wine_df.groupby('color')['quality'].mean()
color_means.plot(kind='bar', title='Average Wine Quality by Color', color=['red','white'], alpha=.7)
plt.xlabel('Colors', fontsize=18)
plt.ylabel('Quality', fontsize=18);


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

counts = wine_df.groupby(['quality', 'color']).count()['pH']
counts.plot(kind='bar', title='Counts by Wine Color and Quality', color=colors, alpha=.7)
plt.xlabel('Quality and Color' , fontsize=18)
plt.ylabel('Count', fontsize=18);


# ### Creating a Bar Chart Using Matplotlib:

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.bar([1, 2, 3], [224, 620, 425])

# plot bars
plt.bar([1, 2, 3], [224, 620, 425])

# specify x coordinates of tick labels and their labels
plt.xticks([1, 2, 3], ['a', 'b', 'c'])

# plot bars with x tick labels
plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])

plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label');


# In[ ]:


# Save changes for the next section
wine_df.to_csv('winequality_edited.csv', index=False)


# ### Plotting Wine Type and Quality with Matplotlib:

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set_style('darkgrid')

wine_df = pd.read_csv('winequality_edited.csv')


# ### Create arrays for red bar heights white bar heights:
# Remember, there's a bar for each combination of color and quality rating. Each bar's height is based on the proportion of samples of that color with that quality rating.
# 
# 1. Red bar proportions = counts for each quality rating / total # of red samples
# 2. White bar proportions = counts for each quality rating / total # of white samples

# In[ ]:


# get counts for each rating and color
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts


# In[ ]:


# get total counts for each color
color_totals = wine_df.groupby('color').count()['pH']
color_totals


# In[ ]:


# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions


# In[ ]:


# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions


# ### Plot proportions on a bar chart:
#     
# Set the x coordinate location for each rating group and and width of each bar.

# In[ ]:


red_proportions['9'] = 0
red_proportions
ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars


# In[ ]:


# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend()

