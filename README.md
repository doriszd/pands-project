# pands-project




# Iris flower dataset

The Iris flower data is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in the paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis.  It is sometimes called Anderson’s Iris data set as Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species (Setosa, Versicolor and Virginica) from the same pasture, and picked on the same day and measured at the same time by the same person with the same tools. The sepals of a flower are the outer structures that protect the more fragile parts of the flower, such as the petals. In many flowers, the sepals are green, and only the petals are colorful. For Irises, however, the sepals are also colorful (medium.com). Picture taken from medium.com. 

Picture 1. Iris flowers
![iris pic](https://github.com/doriszd/pands-project/blob/master/iris_pic1.jpg "Picture 1. Iris flowers")


The data consists of continuous numeric values which describe the dimensions of the respective features.  Iris dataset if often used as training model based on different algorithms (dakokohler.com) which signifies the importance of machine learning.  It is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning (stats.stackexchange.com)
In this project I will not be discussing different algorithms that could be applied as the aim of this project is to summarise the data set and write Python code to investigate it. Python libraries like matplotlib, seaborn, numpy and pandas will be used in order to present supporting tables and graphics. In the research paper data set will be analysed using Python data libraries, and based on the tables and graphics obtained its results will be discussed. 

## Data set

The data set contains three classes of 50 instances each where each class refers to a type of iris plant. Data set consists of 

    • 150 samples
    • 3 labels: species of Iris (Iris setosa, Iris virginica and Iris versicolor)
    • 5 features: Sepal length, Sepal width, Petal length, Petal width in cm and Species

Data set was downloaded from the Internet (www.machinelearningmastery.com)

## Python Libraries

#### Matplotlib 
It is a Python 2D plotting library which produces publication quality figures in a  variety of hardcopy format and interactive environments across platforms.
#### Seaborn
Python data visualization library based on matplotlib. It provides a high level interface for drawing attractive and informative statistical graphics. 
#### NumPy
Fundamental package for scientific computing with Python.
#### Pandas
Open source library providing high-performance, easy to use data structures and data tools for the Python programming language. 

## Preview of data 

There are 150 observations with 5 features describing sepal length, sepal width, petal length, petal width and species. The number of each species is 50. 

In the next few tables some data set characteristics are shown.  In the table data.head() the first 10 rows of data set are shown. Next table gives information about the dataset. It gives the number of each group ( Iris setosa, Iris virginica and Iris versicolor). Furthermore, the last table gives us description of statistical features – count, mean, std, min, max of each iris species. Count is 150 which refers to the number of iris flowers. Mean gives arithmetical average number and STD represents the percentage of flowers in each species that are far from the average. 

data.head()
#Printing first 10 rows
iris_1.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
iris_1.head(10)
print (iris_1.head (10))

![data_head](https://github.com/doriszd/pands-project/blob/master/head.JPG "data.head()")


data.count()
#Size of each species
iris_1["species"]. unique()
print(iris_1.groupby ("species").size())

![data_count](https://github.com/doriszd/pands-project/blob/master/count.JPG "data.count()")

data.describe()
#Count, mean, std, min, max
summary = iris_1.describe()
summary = summary.transpose()
print (summary.head())

![data.describe](https://github.com/doriszd/pands-project/blob/master/STD.JPG "data.describe()")

## Data visualization

Boxplots are standardized way of displaying the distribution of data based on a five number summary (“minimum”, “first quartile”, “median, “third quartile” and “maximum”). 





