# Data Portfolio: Python to Power BI 


![python-sql-powerbi](assets/images/python-sql-powerbi.png)


# Table of Contents

- [Objective](#objective)
- [Data Source](#data-source)
- [Stages](#stages)
  - [Design](#design)
  - [Mockup](#mockup)
- [Tools](#tools)
- [Development](#development)
- [Pseudocode](#pseudocode)
- [Data Exploration](#data-exploration)
- [Data Cleaning](#data-cleaning)
- [Transform the Data](#transform-the-data)
- [Create the SQL View](#create-the-sql-view)
- [Testing](#testing)
  - [Data Quality Tests](#data-quality-tests)
- [Visualization](#visualization)
  - [Results](#results)
  - [DAX Measures](#dax-measures)
- [Analysis](#analysis)
  - [Findings](#findings)
  - [Validation](#validation)
  - [Discovery](#discovery)
- [Recommendations](#recommendations)
  - [Potential ROI](#potential-roi)
  - [Potential Courses of Action](#potential-courses-of-action)
- [Conclusion](#conclusion)





# Objective

- What is the key pain point?

  The Head of Marketing wants to find the top 100 US-based technology YouTubers in 2024 to decide which YouTubers would be best for running marketing campaigns throughout the rest of the year.

- What is the ideal solution?  

To create a dashboard that provides insights into the top 100 US-based technology YouTubers in 2024, including:
  - Subscriber count
  - Total views
  - Total videos
  - Engagement metrics

This will help the marketing team make informed decisions about which YouTubers to collaborate with for their marketing campaigns.

## User Story

As the Head of Marketing, I want to use a dashboard that analyzes YouTube channel data in the US.

This dashboard should allow me to identify the top-performing channels based on metrics like subscriber base and average views.

With this information, I can make more informed decisions about which YouTubers are right to collaborate with, maximizing the effectiveness of each marketing campaign.

## Data Source

What data is needed to achieve our objective?

To achieve our objective, we require data on the top UK YouTubers in 2024, which includes:

- Channel names
- Total subscribers
- Total views
- Total videos uploaded

Where is the data coming from? The data has been compiled from various websites that track YouTube metrics and analytics. 

# Stages

- Design
- Development
- Testing
- Analysis


## Design

## Dashboard Components Required
What should the dashboard contain based on the requirements provided? 

To understand what it should include, we need to figure out what questions we need the dashboard to answer:

1. Who are the top 10 YouTubers with the most subscribers?
2. Which 3 channels have uploaded the most videos?
3. Which 3 channels have the most views?
4. Which 3 channels have the highest average views per video?
5. Which 3 channels have the highest views per subscriber ratio?
6. Which 3 channels have the highest subscriber engagement rate per video uploaded?

For now, these are some of the questions we need to answer; this may change as we progress in our analysis.

## Dashboard Mockup

- What Should It Look Like?

Some of the data visuals that may be appropriate in answering our questions include:

1. Table
2. Treemap
3. Scorecards
4. Horizontal bar chart




![Dashboard-Mockup](assets/images/dashboard_mockup.png)



## Tools

| Tool         | Purpose                                               |
|--------------|-------------------------------------------------------|
| Excel        | Exploring the data                                   |
| SQL Server   | Cleaning, testing, and analyzing the data           |
| Power BI     | Visualizing the data via interactive dashboards      |
| GitHub       | Hosting the project documentation and version control |
| Mokkup AI    | Designing the wireframe/mockup of the dashboard      |



## Development

## Pseudocode

- What's the general approach in creating this solution from start to finish?

1. Get the data
2. Explore the data in Excel
3. Load the data into SQL Server
4. Clean the data with SQL
5. Test the data with SQL
6. Visualize the data in Power BI
7. Generate the findings based on the insights
8. Write the documentation and commentary
9. Publish the data to GitHub Pages


## Data Exploration Notes

This is the stage where you have a scan of what's in the data, errors, inconcsistencies, bugs, weird and corrupted characters etc


- What are your initial observations with this dataset? What’s caught your attention so far?

1. There are at least 4 columns that contain the data we need for this analysis, which signals we have everything we need from the file without needing to contact the client for any more data.
2. The first column contains channel IDs, which are separated by an @ symbol—we need to extract the channel names from this.
3. Some of the cells and header names are in a different language. We need to confirm if these columns are necessary, and if so, we need to address them.
4. We have more data than we need, so some of these columns will need to be removed.


## Data Cleaning

- What do we expect the clean data to look like?  (What should it contain? What contraints should we apply to it?)

The aim is to refine our dataset to ensure it is structured and ready for analysis. 

The cleaned data should meet the following criteria and constraints:

- Only relevant columns should be retained.
- All data types should be appropriate for the contents of each column.
- No column should contain null values, indicating complete data for all records.

Below is a table outlining the constraints on our cleaned dataset:

| Property         | Description |
|------------------|-------------|
| Number of Rows   | 100         |
| Number of Columns | 4           |

Here is a tabular representation of the expected schema for the clean data:

| Column Name        | Data Type | Nullable |
|--------------------|-----------|----------|
| channel_name       | VARCHAR   | NO       |
| total_subscribers   | INTEGER   | NO       |
| total_views        | INTEGER   | NO       |
| total_videos       | INTEGER   | NO       |

- What steps are needed to clean and shape the data into the desired format?

1. Remove unnecessary columns by only selecting the ones you need.
2. Extract YouTube channel names from the first column.
3. Rename columns using aliases.





### Transform the data

```sql
/*
# 1. Select the required columns
# 2. Extract the channel name from the 'NAME' column
*/

-- 1.

SELECT 
    CAST(SUBSTRING(NAME, 1, CHARINDEX('@', NAME) - 1) AS VARCHAR(100)) AS channel_name,
    total_subscribers,
    total_views,
    total_videos
FROM
    us_youtubers_2024;
```



```sql
/*
# 1. Create a view to store the transformed data
# 2. Cast the extracted channel name as VARCHAR(100)
# 3. Select the required columns from the us_youtubers_2024 SQL table 
*/

-- 1.
CREATE VIEW us_youtubers_2024 AS

-- 2.
SELECT
    CAST(SUBSTRING(NOMBRE, 1, CHARINDEX('@', NAME) - 1) AS VARCHAR(100)) AS channel_name, -- 2.
    total_subscribers,
    total_views,
    total_videos

-- 3.
FROM
    us_youtubers_2024;
```


# Testing

- What data quality and validation checks are you going to create?

Here are the data quality tests conducted:

## Row count check

/*
# Count the total number of records (or rows) are in the SQL view
*/

```sql
SELECT
    COUNT(*) AS no_of_rows
FROM
    view_uk_youtubers_2024;
```

