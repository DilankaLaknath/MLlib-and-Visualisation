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
