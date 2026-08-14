

 Book Data Analysis using Web Scraping

 Project Overview

This project demonstrates the complete data analysis process, starting from web scraping to data visualization. The dataset was collected from the Books to Scrape website using Scrapy, cleaned using Pandas, and analyzed using Matplotlib. The objective was to collect book information, preprocess the data, identify patterns, and present meaningful insights through visualizations.

 Website Used

https://books.toscrape.com/

 Technologies Used

- Python
- Scrapy
- Pandas
- NumPy
- Matplotlib
- JSON
- CSV

```

 Task 1: Web Scraping

The dataset was collected from the Books to Scrape website using Scrapy. Exactly 100 books were scraped from the first five pages of the website. For each book, the following information was extracted:

- Title
- Category
- Price
- Rating
- Availability
- Product Description
- UPC
- Number of Reviews
- Product URL

The scraped data was exported in both CSV and JSON formats.

 Task 2: Data Preprocessing

The collected dataset was cleaned and prepared for analysis using Pandas. The preprocessing steps included:

- Checking and removing duplicate records
- Identifying missing values
- Cleaning the Price column
- Converting ratings into numerical values
- Extracting stock count from the Availability column
- Converting columns to appropriate data types
- Saving the cleaned dataset in CSV and JSON formats

 Task 3: Data Visualization

The cleaned dataset was analyzed using Matplotlib. The following visualizations were created:

- Price Distribution
- Rating Distribution
- Average Price by Category
- Price vs Rating

Summary statistics were also used to examine price patterns, category distribution, ratings, stock availability, and missing values.

 Task 4: Analysis and Interpretation

The analysis focused on identifying:

- Distribution of book prices
- Rating patterns
- Categories with the highest average prices
- Relationship between price and rating
- Most represented categories
- Books offering better value for their price
- Limitations of the dataset

 Dataset Information

- Total Books Scraped: 100
- Total Pages Scraped: 5

Output Files

Raw Dataset

- books_100.csv
- books_100.json

Cleaned Dataset

- books_cleaned.csv
- books_cleaned.json

Visualizations

- price_distribution.png
- rating_distribution.png
- average_price_by_category.png
- price_vs_rating.png

Conclusion

This project demonstrates the complete workflow of web scraping, data preprocessing, exploratory data analysis, and visualization using Python. It provides practical experience in collecting real-world data, cleaning it, analyzing trends, and presenting meaningful insights through graphical representations.
