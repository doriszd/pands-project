# pands-project




# Iris flower dataset

The Iris flower data is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in the paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis.  It is sometimes called Anderson’s Iris data set as Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species (Setosa, Versicolor and Virginica) from the same pasture, picked on the same day and measured at the same time by the same person with the same tools. The sepals of a flower are the outer structures that protect the more fragile parts of the flower, such as the petals. In many flowers, the sepals are green, and only the petals are colorful. For Irises, however, the sepals are also colorful (medium.com). Picture taken from medium.com. 

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


#### 1. Comparison of Sepal Length Distributions  
#Import seaborn and matplotlib  
import seaborn as sns  
import matplotlib.pyplot as plt   
#Set style, colours (standard) and plot size  
sns.set(style="whitegrid", palette="GnBu_d", rc={"figure.figsize": (11.7, 8.27)})  
#Title  
title="Comparison of Sepal Length Distributions"  
#x = species, y = sepal length  
sns.boxplot(x="species", y="sepal_length", data=iris_1)  
#Increased fontsize  
plt.title(title, fontsize=26)  
plt.show()   

![sepal_len](https://github.com/doriszd/pands-project/blob/master/sepal.png "sepal_leng")

From the above graph we can see that virginica has the longest sepal length while setosa has the shortest one. The difference is significant as virginica’s sepal length is around 6.5 cm and setosa’s sepal length is 5 cm. 

#### 2. Comparison of Sepal Width Distributions   
#Import seaborn and matplotlib  
import seaborn as sns  
import matplotlib.pyplot as plt   
#Set style, colours (standard) and plot size  
sns.set(style="whitegrid", palette="GnBu_d", rc={"figure.figsize": (11.7, 8.27)})  
#Title  
title="Comparison of Sepal Width Distributions"  
#x = species, y = sepal width  
sns.boxplot(x="species", y="sepal_width", data=iris_1)  
#Increased fontsize  
plt.title(title, fontsize=26)  
plt.show()

![sepal_width](https://github.com/doriszd/pands-project/blob/master/Figure_2_sepal%20width%20dist.png "sepal_width")

The graph shows that setosa has the widest sepal (median – 3.4 cm), while there is no big difference between versicolor (median - 2.8 cm), and virginica (median – 3 cm). 

#### 3. Comparison of Petal Length Distributions  
#Set style, colours (standard) and plot size  
sns.set(style="whitegrid", palette="GnBu_d", rc={"figure.figsize": (11.7, 8.27)})  
#Title  
title="Comparison of Petal Length Distributions"  
#x = species, y = petal length  
sns.boxplot(x="species", y="petal_length", data=iris_1)  
#Increased fontsize  
plt.title(title, fontsize=26)  
plt.show()  

![petal_leng](https://github.com/doriszd/pands-project/blob/master/Figure_3_petal%20leng%20dist.png "petal_leng")

It can be seen that virginica’s petal length distribution is spread from 5 to 6 cm with median, 5. 6 cm. Virginica is followed by versicolor with median, around 4.4 cm and finally there is a big difference when it comes to setosa whose median is around 1.5 cm. Setosa’s petal length makes setosa divergent from other species. 

#### 4. Comparison of Petal Width Distributions
#Set style, colours (standard) and plot size  
sns.set(style="whitegrid", palette="GnBu_d", rc={"figure.figsize": (11.7, 8.27)})  
#Title  
title="Comparison of Petal Width Distributions"  
#x = species, y = petal width  
sns.boxplot(x="species", y="sepal_width", data=iris_1)  
#Increased fontsize  
plt.title(title, fontsize=26)  
plt.show()  

![petal_width](https://github.com/doriszd/pands-project/blob/master/Figure_4_petal%20width%20dist.png "petal_width")

While setosa’s petal length is the shortest, setosa’s petal width is the widest of all, followed by virginica (median 3cm) and versicolor (median 2.7cm). 

#### 5. Pairplot  
#Background color  
import seaborn as sns  
sns.set(style="whitegrid")  
sns.pairplot(iris_1, hue="species", palette="GnBu_d", diag_kind="kde", markers=["o", "s", "D"])  
#Remove the top and right spines from plot  
sns.despine()  
import matplotlib.pyplot as plt  
plt.show()  

![pairplot](https://github.com/doriszd/pands-project/blob/master/Figure_5_pairplot.png "pairplot")

The density plots on the diagonal make it easy to compare distributions between the species. 
After using pair plots it is clear that the relationship between pairs of features of a iris-setosa is distinctly different from those of the other two species. There is some overlap in the pairwise relationships of the other two species, iris-versicolor and iris-virginica. According to Kohler as plot suggests that Iris-setosa is the most separable, it would be a good idea to explore some of that data by itself (dakokohler.com). 




