
## Heroes Of Pymoli Data Analysis
* **Trend 1:** Male players dominate the purchase record. Male players dominate the total number of purchase and the total value of purchase.
* **Trend 2:** Age group of 20-24 has the highest number of purchase and the highest revenue of purchase.
* **Trend 3:** The most popular items (that has the highest number of purchase) does not overlap with the most profitable items (that has the highest revenue of purchase).


```python
# Import libraries
import pandas as pd
import os
import numpy as np
```


```python
# Import data
file_path = os.path.join('.', 'purchase_data.json')
df = pd.read_json(file_path)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check whether there is any null entry
df.isnull().sum()
```




    Age          0
    Gender       0
    Item ID      0
    Item Name    0
    Price        0
    SN           0
    dtype: int64



### Player count


```python
# Check whether same player occurs more than once
df['SN'].value_counts().head()
```




    Undirrala66    5
    Saedue76       4
    Sondastan54    4
    Qarwen67       4
    Hailaphos89    4
    Name: SN, dtype: int64




```python
# Count players
player_total = len(df['SN'].unique()) # total number of players
player_count = pd.DataFrame([{'Total Players': player_total}])
player_count
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Total)

* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue


```python
number_unique_items = len(df['Item ID'].unique())
average_purchase_price = df['Price'].mean()
total_number_purchase = df['Item ID'].count()
total_revenue = df['Price'].sum()

purchase_analysis_total = pd.DataFrame([{'Number of Unique Items': number_unique_items,
                                  'Average Purchase Price': round(average_purchase_price, 2),
                                 'Total Number of Purchases': total_number_purchase,
                                 'Total Revenue': round(total_revenue, 2)}])
purchase_analysis_total
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
      <td>183</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>



### Gender Demographics

* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed


```python
# Group by gender
df_grouped_gender = df.groupby(['Gender']) # group by gender

# Gender demographics
df_gender = pd.DataFrame()
df_gender['Total Count'] = df_grouped_gender['SN'].nunique() # count unique players
df_gender['Percentage of Palyers (%)'] = round(df_gender['Total Count'] / player_total * 100, 2) # percentage
gender_demo = df_gender[['Percentage of Palyers (%)', 'Total Count']] # reorganize columns
gender_demo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Palyers (%)</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Gender)

* The below each broken by gender
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals


```python
# Store data into a dataframe
purchasing_analysis_gender = pd.DataFrame() # Initiate the dataframe
purchasing_analysis_gender['Purchase Count'] = df_grouped_gender.count()['Item Name']
purchasing_analysis_gender['Average Purchase Price'] = round(df_grouped_gender.mean()['Price'], 2)
purchasing_analysis_gender['Total Purchase Value'] = round(df_grouped_gender.sum()['Price'], 2)
purchasing_analysis_gender['Normalized Totals'] = round(purchasing_analysis_gender['Total Purchase Value'] \
                                                  / gender_demo['Total Count'], 2)

# Format price as currency
purchasing_analysis_gender['Average Purchase Price'] = \
                        purchasing_analysis_gender['Average Purchase Price'].map('${:,.2f}'.format)
purchasing_analysis_gender['Total Purchase Value'] = \
                        purchasing_analysis_gender['Total Purchase Value'].map('${:,.2f}'.format)
purchasing_analysis_gender['Normalized Totals'] = \
                        purchasing_analysis_gender['Normalized Totals'].map('${:,.2f}'.format)
purchasing_analysis_gender
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



### Age Demographics

* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.) 
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals


```python
# Look for min and max of age
df['Age'].describe()
```




    count    780.000000
    mean      22.729487
    std        6.930604
    min        7.000000
    25%       19.000000
    50%       22.000000
    75%       25.000000
    max       45.000000
    Name: Age, dtype: float64




```python
# Create bins
bins_raw = np.arange(10,51,5)
bins = np.insert(bins_raw, 0, 0)

# Convert continuous variable to categorical variable
labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49']
age_cat = pd.cut(df['Age'], bins = bins, right = False, labels = labels)

# Create new dataframe with age categories
df_age = df
df_age['Age Categories'] = age_cat
df_age.head()

# Store grouped data into a dataframe
df_grouped_age = df_age.groupby(['Age Categories']) # group by age categories
age_demo = pd.DataFrame()
age_demo['Percentage of Players (%)'] = round(df_grouped_age['SN'].nunique() / player_total * 100, 2)
age_demo['Total Count'] = df_grouped_age['SN'].nunique()
age_demo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players (%)</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Categories</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>1.75</td>
      <td>10</td>
    </tr>
    <tr>
      <th>45-49</th>
      <td>0.17</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Age)
* Purchase Count
* Average Purchase Price
* Total Purchase Value
* Normalized Totals


```python
# Store data into a dataframe
purchase_analysis_age = pd.DataFrame()
purchase_analysis_age['Purchase Count'] = df_grouped_age.count()['Item ID']
purchase_analysis_age['Average Purchase Price'] = round(df_grouped_age.mean()['Price'], 2)
purchase_analysis_age['Total Purchase Value'] = round(df_grouped_age.sum()['Price'], 2)
purchase_analysis_age['Normalized Totals'] = round(purchase_analysis_age['Total Purchase Value'] \
                                                  / age_demo['Total Count'], 2)

# Format price as currency
purchase_analysis_age['Average Purchase Price'] = \
                        purchase_analysis_age['Average Purchase Price'].map('${:,.2f}'.format)
purchase_analysis_age['Total Purchase Value'] = \
                        purchase_analysis_age['Total Purchase Value'].map('${:,.2f}'.format)
purchase_analysis_age['Normalized Totals'] = \
                        purchase_analysis_age['Normalized Totals'].map('${:,.2f}'.format)
purchase_analysis_age
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Categories</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40-44</th>
      <td>16</td>
      <td>$3.19</td>
      <td>$51.03</td>
      <td>$5.10</td>
    </tr>
    <tr>
      <th>45-49</th>
      <td>1</td>
      <td>$2.72</td>
      <td>$2.72</td>
      <td>$2.72</td>
    </tr>
  </tbody>
</table>
</div>



### Top Spenders

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value


```python
# Group by player
df_player = df.groupby(['SN'])

# Store player-specific info into dataframe
spenders = pd.DataFrame()
spenders['Purchase Count'] = df_player['Item ID'].count()
spenders['Average Purchase Price ($)'] = round(df_player['Price'].mean(), 2) #.map('${:,.2f}'.format)
spenders['Total Purchase Value ($)'] = round(df_player['Price'].sum(), 2) #.map('${:,.2f}'.format)

# Sort and find top 5 spenders
spenders_sorted = spenders.sort_values(by = ['Total Purchase Value ($)'], ascending = False)
top_spenders = spenders_sorted.iloc[0:5]
top_spenders
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price ($)</th>
      <th>Total Purchase Value ($)</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>3.41</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>3.39</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>3.18</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>4.24</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>3.86</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>



### Most Popular Items

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value


```python
# Group by Item ID
df_items = df.groupby(['Item ID', 'Item Name'])

# Store item-specific info into a dataframe
items = pd.DataFrame()
items['Purchase Count'] = df_items['Item ID'].count()
items['Item Price ($)'] = round(df_items['Price'].sum() / items['Purchase Count'], 2) #.map('${:,.2f}'.format)
items['Total Purchase Value ($)'] = round(df_items['Price'].sum(), 2) #.map('${:,.2f}'.format)

# Sort and find top 5 items by purchase count
items_sorted = items.sort_values(['Purchase Count'], ascending = False)
top_items = items_sorted.iloc[0:5]
top_items
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price ($)</th>
      <th>Total Purchase Value ($)</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>



### Most Profitable Items

* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value


```python
# Sort and find top 5 items by purchase value
items_sorted_by_value = items.sort_values(['Total Purchase Value ($)'], ascending = False)
top_items_by_revenue = items_sorted_by_value.iloc[0:5]
top_items_by_revenue
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price ($)</th>
      <th>Total Purchase Value ($)</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


