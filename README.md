# Music Classification using MLlib and Visualization

In this project, we aim to classify music into three genres: "Pop," "Metal," and "Hip-Hop," using MLlib in Apache Spark.

Taras Matyashovskyy has a [YouTube video](https://www.youtube.com/watch?v=szpcW-SEJK4&t) demonstrating how to use MLlib to classify music into the two classes "Pop" and "Metal." You can access his code on his [GitHub repository](https://github.com/tmatyashovsky/spark-ml-samples) and read further details from his [blog post](https://dzone.com/articles/distingish-pop-music-from-heavy-metal-using-apache).

However, in his demo, his system was unable to properly categorize "Hip-Hop" because his model was not trained for it. In this project, we will build a better system that can classify music into all three genres. We can use his code as a starting point, but we will need to make some changes to it for it to work for this task. 

## Step 1: Download the Mendeley Music Dataset

### Task
1. Download the Mendeley music dataset (26MB) from [here](https://data.mendeley.com/datasets/3t9vbwxgr5/2). Note that it has multiple classes: pop, country, blues, jazz, reggae, rock, hip hop.
* Let's call this dataset "Mendeley dataset."
* Note: In this dataset they have a release_date column. But it is actually not an actual date but just the released year. We will continue this convention. 

## Step 2: Use a training/test split of 80/20

### Answer
1. Load the Mendeley dataset into a Spark DataFrame using the following commands:
```import org.apache.spark.sql.SparkSession```

```val spark = SparkSession.builder.appName("MusicClassification").getOrCreate()```

```val data = spark.read.option("header", "true").option("inferSchema", "true").csv("/Users/dilanka/Documents/MSc/Big Data Analytics/MLlib-and-Visualisation/Mendeley_dataset.csv")```

```data.show() ```

* This code creates a SparkSession and reads the CSV file into a DataFrame named "data". The "header" option is set to true to treat the first row of the file as column names, and the "inferSchema" option is set to true to infer the data types of each column. The data.show() statement is used to display the first few rows of the DataFrame.

2. Split the data into training and testing sets using the 'randomSplit' method:

```val Array(trainingData, testData) = data.randomSplit(Array(0.8, 0.2))```

* Here, I am using the 'randomSplit' method to split the data into training and testing sets. We are specifying the split ratios as an array of doubles where the first element represents the fraction of the data to use for training and the second element represents the fraction of the data to use for testing.

## Step 3: Create and train an MLlib pipeline to classify song lyrics to the above 7 classes. (We can alter Taras Matyashovskyy's code or write new code from the ground up).