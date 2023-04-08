// Import libraries
import org.apache.spark.sql.SparkSession

// Create Spark session
val spark = SparkSession.builder.appName("SongGenreClassifier").getOrCreate()

// Load Mendeley dataset
val data = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Users/dilanka/Documents/MSc/Big Data Analytics/MLlib-and-Visualisation/Mendeley_dataset.csv")

// Split data into training and test sets
val Array(trainingData, testData) = data.randomSplit(Array(0.8, 0.2))

// Import libraries
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.feature.{HashingTF, IDF, StringIndexer, Tokenizer}
import org.apache.spark.sql.SparkSession

// create a label indexer to convert genre string labels to numerical indices
val labelIndexer = new StringIndexer().setInputCol("genre").setOutputCol("label").fit(data)

// tokenize the lyrics column into words
val tokenizer = new Tokenizer().setInputCol("lyrics").setOutputCol("words")

// apply TF-IDF feature extraction
val hashingTF = new HashingTF().setInputCol("words").setOutputCol("rawFeatures").setNumFeatures(1000)
val idf = new IDF().setInputCol("rawFeatures").setOutputCol("features")

// create a logistic regression model
val lr = new LogisticRegression().setMaxIter(100).setRegParam(0.01)

// create a pipeline with the stages in the order they should be executed
val pipeline = new Pipeline().setStages(Array(labelIndexer, tokenizer, hashingTF, idf, lr))

// split the data into training and testing sets (80/20)
val Array(trainingData, testData) = data.randomSplit(Array(0.8, 0.2))

// fit the pipeline on the training data
val model = pipeline.fit(trainingData)

// make predictions on the testing data
val predictions = model.transform(testData)

// show the predicted labels and their corresponding probabilities
predictions.select("lyrics", "genre", "prediction", "probability").show()





import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator

// evaluate the model accuracy
val evaluator = new MulticlassClassificationEvaluator().setLabelCol("label").setPredictionCol("prediction").setMetricName("accuracy")
val accuracy = evaluator.evaluate(predictions)

// show the predicted labels and their corresponding probabilities
predictions.select("lyrics", "genre", "prediction", "probability").show()

// print the model accuracy
println("Accuracy: " + accuracy)


// save the trained model to a file
model.save("/Users/dilanka/Documents/MSc/Big Data Analytics/MLlib-and-Visualisation/model")


// load the trained model from a file
val loadedModel = PipelineModel.load("/Users/dilanka/Documents/MSc/Big Data Analytics/MLlib-and-Visualisation/model")
