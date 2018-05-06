
# PyCity Schools Analysis
* **Observed Trend 1:** Based on overall passing rate, top 5 schools are all charter schools with small to medium sizes; bottom 5 schools are all district schools with large sizes.
* **Observed Trend 2:** Grade does not appear to influence math and reading scores.
* **Observed Trend 3:** Scores are higher in charter schools that have small to medium sizes and less per student budget.


```python
import numpy as np
import pandas as pd
import os
```


```python
file_path1 = os.path.join('raw_data', 'schools_complete.csv')
file_path2 = os.path.join('raw_data', 'students_complete.csv')
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df1.head()
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
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.head()
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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>



### District Summary

* Create a high level snapshot (in table form) of the district's key metrics, including:
  * Total Schools
  * Total Students
  * Total Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


```python
# Calculate metrics
district_summary = pd.DataFrame()
district_summary['Total Schools'] = [df1['name'].nunique()]
district_summary['Total Students'] = df2['Student ID'].nunique()
district_summary['Total Budget'] = df1['budget'].sum()
district_summary['Average Math Score'] = df2['math_score'].mean()
district_summary['Average Reading Score'] = df2['reading_score'].mean()
district_summary['% Passing Math'] = df2.loc[df2['math_score'] >= 60, 'math_score'].count() \
                                        / district_summary['Total Students'] * 100
district_summary['% Passing Reading'] = df2.loc[df2['reading_score'] >= 60, 'reading_score'].count() \
                                        / district_summary['Total Students'] * 100
district_summary['% Overall Passing Rate'] = np.mean([district_summary['% Passing Math'], \
                                                    district_summary['% Passing Reading']])

# Format values
district_summary['Total Students'] = district_summary['Total Students'].map('{:,}'.format)
district_summary['Total Budget'] = district_summary['Total Budget'].map('${:,.2f}'.format)
district_summary['Average Math Score'] = round(district_summary['Average Math Score'], 2)
district_summary['Average Reading Score'] = round(district_summary['Average Reading Score'], 2)
district_summary['% Passing Math'] = round(district_summary['% Passing Math'], 2)
district_summary['% Passing Reading'] = round(district_summary['% Passing Reading'], 2)
district_summary['% Overall Passing Rate'] = round(district_summary['% Overall Passing Rate'], 2)
district_summary
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
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>92.45</td>
      <td>100.0</td>
      <td>96.22</td>
    </tr>
  </tbody>
</table>
</div>



### School Summary

* Create an overview table that summarizes key metrics about each school, including:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


```python
# Extend df2 to categorize math and reading scores
bins = np.array([0, 59.999, 100])
labels = [0, 1]
df2['math_score_pass'] = pd.cut(df2['math_score'], bins = bins, right = True, include_lowest = True, labels = labels)
df2['reading_score_pass'] = pd.cut(df2['reading_score'], bins = bins, right = True, 
                                   include_lowest = True, labels = labels)
df2['math_score_pass'] = pd.to_numeric(df2['math_score_pass'])
df2['reading_score_pass'] = pd.to_numeric(df2['reading_score_pass'])

# Calculate metrics
group_school = df2.groupby(['school'])
total_student = group_school['Student ID'].nunique()
average_math_score = group_school['math_score'].mean()
average_reading_score = group_school['reading_score'].mean()
passing_math = group_school['math_score_pass'].sum() / total_student * 100
passing_reading = group_school['reading_score_pass'].sum() / total_student * 100
passing_overall = (passing_math + passing_reading) / 2

# Constructing dataframe
df_school = pd.DataFrame({'Total Student': total_student, 'Average Math Score': average_math_score, 
                         'Average Reading Score': average_reading_score, '% Passing Math': passing_math,
                         '% Passing Reading': passing_reading, '% Overall Passing Rate': passing_overall})

# Join school_summary by a copy of df1
df1_copy = df1.set_index('name')
df_school_merged = pd.merge(df_school, df1_copy[['type', 'budget']], \
                            left_index = True, right_index = True, how = 'inner')
df_school_merged = df_school_merged.rename(columns = {'type': 'School Type', 'budget': 'Total School Budget'})
df_school_merged['Per Student Budget'] = df_school_merged['Total School Budget'] / df_school_merged['Total Student']

# Format dataframe
school_summary = df_school_merged[['School Type', 'Total Student', 'Total School Budget',
                                       'Per Student Budget','Average Math Score','Average Reading Score',
                                       '% Passing Math','% Passing Reading', '% Overall Passing Rate']]

school_summary['Total Student'] = school_summary['Total Student'].map('{:,}'.format)
school_summary['Total School Budget'] = school_summary['Total School Budget'].map('${:,.2f}'.format)
school_summary['Per Student Budget'] = school_summary['Per Student Budget'].map('${:,.2f}'.format)
school_summary['Average Math Score'] = round(school_summary['Average Math Score'], 2)
school_summary['Average Reading Score'] = round(school_summary['Average Reading Score'], 2)
school_summary['% Passing Math'] = round(school_summary['% Passing Math'], 2)
school_summary['% Passing Reading'] = round(school_summary['% Passing Reading'], 2)
school_summary['% Overall Passing Rate'] = round(school_summary['% Overall Passing Rate'], 2)
school_summary
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
      <th>School Type</th>
      <th>Total Student</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4,976</td>
      <td>$3,124,928.00</td>
      <td>$628.00</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>89.53</td>
      <td>100.0</td>
      <td>94.76</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1,858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2,949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>88.44</td>
      <td>100.0</td>
      <td>94.22</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2,739</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>89.30</td>
      <td>100.0</td>
      <td>94.65</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1,468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4,635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>89.08</td>
      <td>100.0</td>
      <td>94.54</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2,917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>88.86</td>
      <td>100.0</td>
      <td>94.43</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4,761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>89.18</td>
      <td>100.0</td>
      <td>94.59</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3,999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>88.55</td>
      <td>100.0</td>
      <td>94.27</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1,761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1,635</td>
      <td>$1,043,130.00</td>
      <td>$638.00</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2,283</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1,800</td>
      <td>$1,049,400.00</td>
      <td>$583.00</td>
      <td>83.68</td>
      <td>83.96</td>
      <td>100.00</td>
      <td>100.0</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>



### Top Performing Schools (By Passing Rate)

* Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


```python
top_schools = school_summary.sort_values(['% Overall Passing Rate'], ascending = False).iloc[0:5]
top_schools
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
      <th>School Type</th>
      <th>Total Student</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1,858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1,468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1,761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>



### Bottom Performing Schools (By Passing Rate)

* Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.


```python
bottom_schools = school_summary.sort_values(['% Overall Passing Rate'], ascending = True).iloc[0:5]
bottom_schools
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
      <th>School Type</th>
      <th>Total Student</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2,949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>88.44</td>
      <td>100.0</td>
      <td>94.22</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3,999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>88.55</td>
      <td>100.0</td>
      <td>94.27</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2,917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>88.86</td>
      <td>100.0</td>
      <td>94.43</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4,635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>89.08</td>
      <td>100.0</td>
      <td>94.54</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4,761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>89.18</td>
      <td>100.0</td>
      <td>94.59</td>
    </tr>
  </tbody>
</table>
</div>



### Math Scores by Grade

* Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


```python
# Group by school and grade
group_school_grade = df2.groupby(['school', 'grade'])

# Average math score
df_grade_math = round(group_school_grade['math_score'].mean(), 2)
math_by_grade = df_grade_math.unstack(level=-1)[['9th', '10th', '11th', '12th']]
math_by_grade
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
      <th>grade</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.08</td>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.09</td>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.40</td>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.36</td>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.04</td>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.44</td>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.79</td>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.03</td>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.19</td>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.63</td>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.86</td>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.42</td>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.59</td>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.09</td>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.26</td>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
    </tr>
  </tbody>
</table>
</div>



### Reading Scores by Grade

* Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


```python
# Group by school and grade
group_school_grade = df2.groupby(['school', 'grade'])

# Average reading score
df_grade_reading = round(group_school_grade['reading_score'].mean(), 2)
reading_by_grade = df_grade_reading.unstack(level=-1)[['9th', '10th', '11th', '12th']]
reading_by_grade
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
      <th>grade</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.30</td>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.68</td>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.20</td>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.63</td>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.37</td>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.87</td>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.68</td>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.29</td>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.26</td>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.81</td>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.99</td>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.12</td>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.73</td>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.94</td>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.83</td>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
    </tr>
  </tbody>
</table>
</div>



### Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


```python
# Convert objects to numeric
school_summary_copy = school_summary
school_summary_copy['Per Student Budget'] = school_summary_copy['Per Student Budget']\
                                            .replace('\$', '', regex=True).astype('float')
school_summary_copy['Total Student'] = school_summary_copy['Total Student']\
                                            .replace(',', '', regex=True).astype('int')
pd.to_numeric(school_summary_copy['Average Math Score'])
pd.to_numeric(school_summary_copy['Average Reading Score'])
pd.to_numeric(school_summary_copy['% Passing Math'])
pd.to_numeric(school_summary_copy['% Passing Reading'])
print(f"min per student budget: {school_summary_copy['Per Student Budget'].min()}")
print(f"max per student budget: {school_summary_copy['Per Student Budget'].max()}")

# Cut per student budget into categories
bins = [0, 600, 625, 650, 675]
labels = ['<$600', '$600-625', '$625-650', '$650-675']
school_summary_copy['Per Student Budget Category'] = pd.cut(school_summary_copy['Per Student Budget'], \
                                                           bins=bins, labels=labels)

# Calculate totals to be averaged later, otherwise averages will be biased
school_summary_copy['Total Math Score']=school_summary_copy['Average Math Score']*school_summary_copy['Total Student']
school_summary_copy['Total Read Score']=school_summary_copy['Average Reading Score']*school_summary_copy['Total Student']
school_summary_copy['Total Math Passing']=school_summary_copy['% Passing Math']*school_summary_copy['Total Student']
school_summary_copy['Total Read Passing']=school_summary_copy['% Passing Reading']*school_summary_copy['Total Student']

# Group by school spending
group_spending = school_summary_copy.groupby(['Per Student Budget Category'])

math_score = group_spending['Total Math Score'].sum() / group_spending['Total Student'].sum()
read_score = group_spending['Total Read Score'].sum() / group_spending['Total Student'].sum()
math_percent = group_spending['Total Math Passing'].sum() / group_spending['Total Student'].sum()
read_percent = group_spending['Total Read Passing'].sum() / group_spending['Total Student'].sum()
overall_percent = (math_percent + read_percent) / 2

# Create a table
school_spending = pd.DataFrame({'Average Math Score': math_score, 'Average Reading Score': read_score,
                               '% Passing Math': math_percent, '% Passing Reading': read_percent,
                               '% Overall Passing': overall_percent})
school_spending
```

    min per student budget: 578.0
    max per student budget: 655.0





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
      <th>% Overall Passing</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
    </tr>
    <tr>
      <th>Per Student Budget Category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$600</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>83.360124</td>
      <td>83.915292</td>
    </tr>
    <tr>
      <th>$600-625</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>83.543984</td>
      <td>83.907095</td>
    </tr>
    <tr>
      <th>$625-650</th>
      <td>94.947551</td>
      <td>89.895103</td>
      <td>100.0</td>
      <td>77.468095</td>
      <td>81.162095</td>
    </tr>
    <tr>
      <th>$650-675</th>
      <td>94.497512</td>
      <td>88.995024</td>
      <td>100.0</td>
      <td>77.035072</td>
      <td>81.026564</td>
    </tr>
  </tbody>
</table>
</div>



### Scores by School Size

* Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).


```python
print(f"min total student: {school_summary_copy['Total Student'].min()}")
print(f"max total student: {school_summary_copy['Total Student'].max()}")

# Cut total student into categories
bins2 = [0, 1000, 2000, 5000]
labels2 = ['Small(<1000)', 'Medium(1000-2000)', 'Large(2000-5000)']
school_summary_copy['School Size Category'] = pd.cut(school_summary_copy['Total Student'], \
                                                           bins=bins2, labels=labels2)

# Group by school size
group_size = school_summary_copy.groupby(['School Size Category'])

math_score = group_size['Total Math Score'].sum() / group_size['Total Student'].sum()
read_score = group_size['Total Read Score'].sum() / group_size['Total Student'].sum()
math_percent = group_size['Total Math Passing'].sum() / group_size['Total Student'].sum()
read_percent = group_size['Total Read Passing'].sum() / group_size['Total Student'].sum()
overall_percent = (math_percent + read_percent) / 2

# Create a table
school_size = pd.DataFrame({'Average Math Score': math_score, 'Average Reading Score': read_score,
                               '% Passing Math': math_percent, '% Passing Reading': read_percent,
                               '% Overall Passing': overall_percent})
school_size
```

    min total student: 427
    max total student: 4976





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
      <th>% Overall Passing</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
    </tr>
    <tr>
      <th>School Size Category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small(&lt;1000)</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>83.827703</td>
      <td>83.969294</td>
    </tr>
    <tr>
      <th>Medium(1000-2000)</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>83.371971</td>
      <td>83.871612</td>
    </tr>
    <tr>
      <th>Large(2000-5000)</th>
      <td>94.943289</td>
      <td>89.886578</td>
      <td>100.0</td>
      <td>77.476441</td>
      <td>81.197566</td>
    </tr>
  </tbody>
</table>
</div>



### Scores by School Type

* Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).


```python
# Group by school type
group_type = school_summary_copy.groupby(['School Type'])

math_score = group_type['Total Math Score'].sum() / group_type['Total Student'].sum()
read_score = group_type['Total Read Score'].sum() / group_type['Total Student'].sum()
math_percent = group_type['Total Math Passing'].sum() / group_type['Total Student'].sum()
read_percent = group_type['Total Read Passing'].sum() / group_type['Total Student'].sum()
overall_percent = (math_percent + read_percent) / 2

# Create a table
school_type = pd.DataFrame({'Average Math Score': math_score, 'Average Reading Score': read_score,
                               '% Passing Math': math_percent, '% Passing Reading': read_percent,
                               '% Overall Passing': overall_percent})
school_type
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
      <th>% Overall Passing</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>83.404792</td>
      <td>83.904904</td>
    </tr>
    <tr>
      <th>District</th>
      <td>94.515336</td>
      <td>89.030671</td>
      <td>100.0</td>
      <td>76.986128</td>
      <td>80.961240</td>
    </tr>
  </tbody>
</table>
</div>


