# Music Classification using MLlib and Visualization

In this project, we aim to classify music into three genres: "Pop," "Metal," and "Hip-Hop," using MLlib in Apache Spark.

Taras Matyashovskyy has a [YouTube video](https://www.youtube.com/watch?v=szpcW-SEJK4&t) demonstrating how to use MLlib to classify music into the two classes "Pop" and "Metal." You can access his code on his [GitHub repository](https://github.com/tmatyashovsky/spark-ml-samples) and read further details from his [blog post](https://dzone.com/articles/distingish-pop-music-from-heavy-metal-using-apache).

However, in his demo, his system was unable to properly categorize "Hip-Hop" because his model was not trained for it. In this project, we will build a better system that can classify music into all three genres. We can use his code as a starting point, but we will need to make some changes to it for it to work for this task. 

## Step 1: Download the Mendeley Music Dataset

### Task
1. Download the Mendeley music dataset (26MB) from [here](https://data.mendeley.com/datasets/3t9vbwxgr5/2).
2. Note that it has multiple classes: pop, country, blues, jazz, reggae, rock, hip hop.
3. Let's call this dataset "Mendeley dataset."
4. Note: In this dataset they have a release_date column. But it is actually not an actual date but just the released year. We will continue this convention. 

### Answer
# Running Scala Code in Terminal
To run Scala code in the terminal, follow these steps:

1. Install Scala and set up your environment. You can follow the instructions provided on the official Scala website: https://www.scala-lang.org/download/
2. Create a new Scala file with the code you want to run. Let's say you named the file "MyCode.scala".
3. Open a terminal window and navigate to the directory where your Scala file is located using the `cd` command. For example, if your file is located in the "Documents" folder, you can run the command `cd ~/Documents`.
4. Compile your Scala code using the `scalac` command. For example, you can run the command `scalac MyCode.scala`.
5. Run your Scala code using the `scala` command. For example, you can run the command `scala MyCode`.
6. If your code requires any external dependencies, make sure to add them to the classpath using the `-cp` option. For example, you can run the command `scala -cp /path/to/dependency MyCode`.

Note that these steps assume that you have Scala installed and set up properly on your system. If you encounter any issues, refer to the official Scala documentation or seek help from the Scala community.
