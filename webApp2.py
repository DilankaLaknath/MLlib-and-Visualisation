from flask import Flask, request, render_template
from pyspark.ml import PipelineModel
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from pyspark.ml.linalg import Vectors
from pyspark.sql.functions import first, udf
from pyspark.ml.linalg import DenseVector
from pyspark.sql.types import ArrayType, DoubleType


# initialize SparkSession
spark = SparkSession.builder.appName('my_app_name').getOrCreate()

app = Flask(__name__)
model = PipelineModel.load('/Users/dilanka/Documents/MSc/Big Data Analytics/MLlib-and-Visualisation/updated-model')

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for handling the lyrics form submission
@app.route('/classify', methods=['POST'])
def classify():
    # Get the lyrics from the form
    lyrics = request.form['lyrics']

    # Define a schema for the input data
    input_schema = StructType([
        StructField('lyrics', StringType(), True)
    ])

    # Convert the input data to a Spark DataFrame
    input_df = spark.createDataFrame([(lyrics,)], schema=input_schema)

    # Use the model to classify the lyrics into one of the seven classes
    result = model.transform(input_df)
    prob =result.select(first("probability")).collect()[0][0]
    list_probs = prob.toArray().tolist()

    # Create a bar chart of the genre probabilities
    fig, ax = plt.subplots()
    genres = ['pop', 'country', 'blues', 'jazz', 'reggae', 'rock', 'hip hop', 'Indie']
    genre_probs = {genre: list_probsz for genre, list_probsz in zip(genres, list_probs)}
    ax.bar(genres, list_probs)
    ax.set_ylim([0, 1])
    ax.set_ylabel('Probability')
    ax.set_xlabel('Genre')
    plt.xticks(rotation=45, ha='right')

    # Convert the chart to a PNG image and encode it as a base64 string
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    # Render the results page with the predicted genre and the bar chart
    return render_template('results.html',
                           genre=genre_probs,
                           chart_data=chart_data)

if __name__ == '__main__':
    app.run(debug=True)
