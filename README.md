# spaceTechAnalysis

A Python Jupyter Notebook project whose structure was created by Angela Yu and which I completed for Professional Portfolio Project: Assignment 18: [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) -- "Data Science: Analyse and Visualise the Space Race".

This is the penultimate project in Angela Yu's 100 Day's course. Since the most recent .csv data file was aggregated in 2020, I decided to scrape the source site's more recent info on space launches. I used Selenium for this task.

_[MIT License](https://github.com/andrewblais/spaceTechAnalysis/blob/main/LICENSE): Copyright (c) 2024- Andrew Blais_

---

Project structure:

---

### Future Updates

---

### Documentation:

```requirements
```

---

## Created in completing an assignment for Angela Yu Course 100 Days of Code: The Complete Python Pro Bootcamp.

### **Day 99, Professional Portfolio Project [Data Science]**

#### **_Assignment 18: "Analyse and Visualise the Space Race"_**

Use space mission data from 1957 onwards to analyse and visualise trends over time.

### **Assignment instructions:**

You've learnt about all the core aspects of data exploration, data cleaning, and data visualisation.

Download, unzip and open the notebook I've included for this assignment.

You'll find an incredibly rich dataset from [nextspaceflight.com](nextspaceflight.com) that includes all the space missions since the beginning of Space Race between the USA and the Soviet Union in 1957!

It has data on the mission status (success/failure), the cost of the mission, the number of launches per country, and much much more.

There's so much we can learn from this dataset about the dominant organisations and the trends over time.

For example:

-   Who launched the most missions in any given year?

-   How has the cost of a space mission varied over time?

-   Which months are the most popular for launches?

-   Have space missions gotten safer or has the chance of failure remained unchanged?

I'm sure that you'll discover many more questions that you can formulate and answer with this dataset!

Use it to practice what you learnt about creating various types of charts and visualisations, from choropleths to sunburst charts to segmented bar charts and see if you can turn data into insight.

Good luck!

![Rocket](static/yu_rocket.jpg)

---

### My Submission:

My project is viewable here: https://github.com/andrewblais/spaceTechAnalysis

---

### **Questions for this assignment**

#### _Reflection Time:_

**_Write down how you approached the project._**

Initially I noticed that the .csv file's data ends in 2020, so I used what I'd learned in this course about Selenium and further scraped the site to update the .csv to the present (May 2024).

This was challenging, the site does not have classes and id's well-named to enable this process, so it took a bit of time to identify and properly label the desired data's elements in the web scraping script.

**_What was hard?_**

The biggest challenge for me is the more advanced aspects of transforming/cleaning data with NumPy.

Here's an operation which I needed help from Stack Overflow and Chat GPT to complete:

```python
# Create a DF which counts the number of total missions per year:
df_cold_missions = df_usa_ussr.groupby(
    ['Country_Name', 'Year']).size().reset_index(name='Total_Missions')

# Create another DF which counts the successes per year for each country:
df_cold_successes = df_usa_ussr[df_usa_ussr['Mission_Status'] == 'Success'].groupby(
    ['Country_Name', 'Year']).size().reset_index(name='Success_Count')

# Merge the total missions and successes DataFrames:
df_cold_merged = df_cold_missions.merge(
    df_cold_successes, on=['Country_Name', 'Year'], how='left')

# Ensure years without successes have `0` instead of `NaN`:
df_cold_merged['Success_Count'] = df_cold_merged['Success_Count'].fillna(0)

# Now add a column for success percentage:
success_ratio = (df_cold_merged.Success_Count / df_cold_merged.Total_Missions)
df_cold_merged['Success_Percentage'] = success_ratio * 100

# Sort by year for clarity of chronology in viewing DF:
df_cold_merged.sort_values(by=['Year'], inplace=True)
```

I definitely have a decent understanding of how the NumPy works, but it will require more practice and study to make operations like this work naturally.

I don't want to rely too heavily on outside help to complete these kinds of tasks.

This will come with time.

**_What was easy?_**

Honestly, I love writing and formatting text in Markdown.

It's a lot of fun, and a nice way to break up the more difficult challenges when working with Jupyter Notebooks.

Also, I took a lot of time to enjoy creating customized color lists/schemes to make the plots more interesting.

I've enjoyed learning CSS in Angela's Web Development course, and this knowledge has helped a lot in understanding the graphic design/color elements at play in this kind of project.

I really enjoy breaking up advanced coding challenges with easier one's like creating fun arrays of colors and looking for interesting ways to spice up my code.

**_How might you improve for the next project?_**

Study the source documentation for NumPy.

Study, study, study...

**_What was your biggest learning from today?_**

That although I've learned a lot, there's still a long way to go.

Some of the more challenging NumPy operations did become easier, so I feel like I've definitely upped my NumPy/Data Analysis game.

**_What would you do differently if you were to tackle this project again?_**

Research which plots work best for each type of situation, rather than diving in too quickly and relying on trial and error.

On to the final day!
