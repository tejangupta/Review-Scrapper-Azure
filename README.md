# Flipkart Review Scrapping
#### Description:
Flipkart Review Scrapping is a project that aims to gather and analyze customer reviews from the Flipkart online marketplace. Flipkart is a popular e-commerce platform in India that sells a wide range of products including electronics, fashion, books, and more. The project involves scraping customer reviews from various products on Flipkart.

The review scraping process involves the use of web scraping tools and techniques to extract reviews from Flipkart's website. The extracted data is then processed, cleaned, and stored in a structured format such as a CSV file or a database.

This can further use, and is not implemented by me, various natural language processing techniques to analyze the reviews and extract useful information such as sentiment analysis, key topics, and user preferences.

##### Technologies Used
- Python
-Flask framework
- BeautifulSoup library
- Requests library
- HTML, CSS, and JavaScript


##### Modules and packages used:

- flask
- flask_cors
- requests
- bs4
- urllib.request
- logging
- csv

Depending on the environment in which you're running the application you're required to download the following packages from the **requirements.txt** either using conda or pip.

#### Project Structure
The project consists of the following files and folders:
- `app.py`: This file contains the main Flask application. It has two endpoints - / and /review. The / endpoint renders the index.html template, which displays a form for the user to input the product they want to search for. The /review endpoint handles the form submission, scrapes the reviews for the given product, and returns the results as a table.
- `static`: Here we have two files inside the css folder namely **main.css** and **style.css** that deal with the aesthetics of web pages that is rendered.
- `templates`: Here we have three html files namely - **base.html**, **index.html**, **results.html** which describes how the content is to be structured.
- `requirements.txt`: Mentions the list of packages that are supposed to be installed inside your workspace or project.
- `csv file` : You only have this file once the user has inputed a product and clicked the Search button. All the reviews are then stored in a csv file.
- `scrapper.log`: Generates a log of the execution of each and every step, which can be inspected to figure out where it all went wrong.

#### How the project and web app works?
The process of scraping reviews involves the use of web scraping techniques such as sending HTTP requests and parsing HTML content using libraries like Requests and BeautifulSoup. Once the reviews are scraped, they are cleaned and processed to remove unwanted characters and noise. The cleaned reviews are then stored in a structured format such as a CSV file or a database.

The web app is designed to handle multiple requests simultaneously, and the reviews are scraped in real-time. The web app provides users with the ability to filter the reviews based on various criteria such as the rating, the date, and the number of words in the review.

The web app also has a feature where users can download the scraped reviews in CSV format. This feature is useful for users who wish to perform further analysis on the data using external tools.

#### Design Choices
One of the main design choices made in this project was the choice of web scraping tools and techniques used to extract reviews from Flipkart's website. We decided to use the BeautifulSoup library for parsing HTML and the Requests library for making HTTP requests to Flipkart's website. This choice was made because these libraries are widely used in the Python community and are well-documented, making it easier for developers to work with them.

Another design choice was the decision to store the extracted data in a structured format such as a CSV file or a database. We chose to use a CSV file for storing the data because it is a simple and widely used format that can be easily processed by other applications.

We also chose to use the Flask framework for building the web application. Flask is a lightweight and easy-to-use framework that is ideal for building small web applications like this one. We used Flask to define two endpoints - / and /review. The / endpoint renders the index.html template, which displays a form for the user to input the product they want to search for. The /review endpoint handles the form submission, scrapes the reviews for the given product, and returns the results as a table.

We also used a framework to make the web application look more modern and professional. Provides a wide range of pre-built CSS styles and components that can be easily integrated into any web application.

In terms of natural language processing techniques, we did not implement them in this project. However, these techniques can be used to analyze the reviews and extract useful information such as sentiment analysis, key topics, and user preferences. This can provide valuable insights into customer behavior and preferences, which can be used to improve the products and services offered by businesses.

### Thank you!
