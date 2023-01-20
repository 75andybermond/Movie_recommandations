# Movie_recommandations

## _Overview_
This project is an end-to-end machine learning project that utilizes the Mflix dataset to create a movie recommendation web app. The project includes feature engineering, data cleaning, and the creation of a SQLite database. The model was trained using the pandas and scikit-learn libraries, and the web app was built using Flask.

### Data Cleaning and Feature Engineering
The first step in this project was to clean and prepare the data for modeling. This involved removing missing or duplicate values, and transforming the data into a format that could be used for training. The following cleaning steps were performed:

- Removing duplicate rows
- Removing rows with missing values
- Rep
- Stripping and replacing multiple spaces in the fields
- The following feature engineering steps were performed:
- Text cleaning (removing caps, capitals, non textual caracters)
- Concatenating the columns (directors, fullplot, casting, countries, genres, languages) to create a combined feature for vectorization.

### Data Viz 
Data visualization were added to help in the understanding of the dataset and the metadata.

## Model Training
The model was trained using the `TfidfVectorizer` method from the scikit-learn library to convert the text data into numerical vectors. Cosine similarity was used to calculate the similarity between the vectors and to recommend the movies.

## SQLite Database

The cleaned data was stored in an SQLite database for easy retrieval during the web app development.

## Flask API
The final step was to create a web app using Flask. The web app allows users to input a movie title, and the app will return a list of recommended movies based on the trained model. The web app also uses a HTML template and a stylesheet to present the results in a user-friendly format.

## Tech

We use a number of open source projects to work properly:

- [SqlLite](https://www.sqlite.org/index.html/) - Light Database easy to use 
- [Sklearn](https://scikit-learn.org/stable/) - Machine learning library
- [Pandas](https://pandas.pydata.org/) - Data processing
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Python framework for Web App 


# Conclusion
This project shows how machine learning can be used to create a movie recommendation web app using the Mflix dataset. The project demonstrates the importance of data cleaning and feature engineering in preparing data for modeling, as well as the ease of creating web apps using Flask.
