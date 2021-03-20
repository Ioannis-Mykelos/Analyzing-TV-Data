#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Analyzing TV Data

# 1. TV, halftime shows, and the Big Game
#    Load the CSV data into DataFrames
#    Display the first five rows of each DataFrame
# 2. Taking note of dataset issues
#    Display and inspect the summaries of the TV and halftime musician DataFrames for issues.
# 3. Combined points distribution.
#    Plot a histogram of combined points then display the rows with the most extreme combined point outcomes.
# 4. Point difference distribution.
#    Modify and display the histogram of point differences, then display the rows with the most extreme 
#    point difference outcomes.
#    Select the Super Bowl(s) where the point difference was equal to 1.
#    Select the Super Bowl(s) where the point difference was greater than or equal to 35.
# 5. Do blowouts translate to lost viewers?
#    Plot household share vs. point difference.
# 6. Viewership and the ad industry over time.
#    Create three line plots using the tv DataFrame to compare viewers, rating, and ad cost.
# 7. Halftime shows weren't always this great.
#    Filter and display the musicians for halftime shows up to and including Super Bowl XXVII.
# 8. Who has the most halftime show appearances?
#    Select and display the musicians with more than one halftime show appearance.
# 9. Who performed the most songs in a halftime show?
#    Modify the histogram of number of songs performed for non-band musicians.
# 10. Conclusion.
#     Who will win Super Bowl LIII?

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns



# 1. TV, halftime shows, and the Big Game
#    Load the CSV data into DataFrames
#    Display the first five rows of each DataFrame

super_bowls = pd.read_csv('super_bowls.csv')
tv = pd.read_csv('tv.csv')
halftime_musicians = pd.read_csv('halftime_musicians.csv')

# Display the first five rows of each DataFrame
display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())


# In[16]:


# 2. Taking note of dataset issues
#    Display and inspect the summaries of the TV and halftime musician DataFrames for issues.

# Summary of the TV data to inspect
tv.info()

print('\n')

# Summary of the halftime musician data to inspect
halftime_musicians.info()


# In[17]:


# 3. Combined points distribution.
#    Plot a histogram of combined points then display the rows with the most extreme combined point outcomes.

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')

# Plot a histogram of combined points
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
display(super_bowls[super_bowls['combined_pts'] > 70])
display(super_bowls[super_bowls['combined_pts'] < 25])


# In[18]:


# 4. Point difference distribution.
#    Modify and display the histogram of point differences, then display the rows with the most extremepoint difference
#    outcomes.
#    Select the Super Bowl(s) where the point difference was equal to 1.
#    Select the Super Bowl(s) where the point difference was greater than or equal to 35.


# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
display(super_bowls[super_bowls['difference_pts'] == 1])
display(super_bowls[super_bowls['difference_pts'] >= 35])


# In[20]:


# 5. Do blowouts translate to lost viewers?
#    Plot household share vs. point difference.


#seaborn's regplot() is like scatter plot except more specialized for visualizing linear relationships. 
#It draws a scatterplot, then fits a regression 
#model and plots the resulting regression line and a 95% confidence interval for that regression.

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn
import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)


# In[21]:


# 6. Viewership and the ad industry over time.
#    Create three line plots using the tv DataFrame to compare viewers, rating, and ad cost.

# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1) 
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()


# In[22]:


# 7. Halftime shows weren't always this great.
#    Filter and display the musicians for halftime shows up to and including Super Bowl XXVII.

# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
halftime_musicians[halftime_musicians.super_bowl <= 27]


# In[23]:


# 8. Who has the most halftime show appearances?
#    Select and display the musicians with more than one halftime show appearance.

# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
halftime_appearances[halftime_appearances['super_bowl'] > 1]


# In[24]:


# 9. Who performed the most songs in a halftime show?
#    Modify the histogram of number of songs performed for non-band musicians.

# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
display(no_bands.head(15))


# In[25]:


# 10. Conclusion.
#     Who will win Super Bowl LIII?

# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = patriots
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)


# In[ ]:




