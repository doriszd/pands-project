#Doris Zdravkovic, April, 2019 


#Import numpy and pandas
import numpy as np 
import pandas as pd 

#Read iris_1 file
iris_1 = pd.read_csv("iris_1.csv")
#Printing first 10 rows
iris_1.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
iris_1.head(10)
print (iris_1.head (10))
#Size of each species
iris_1["species"]. unique()
print(iris_1.groupby ("species").size())
#Count, mean, std, min, max
summary = iris_1.describe()
summary = summary.transpose()
print (summary.head())

#Graphics
# 1. Comparison of Sepal Length Distributions
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

# 2. Comparison of Sepal Width Distributions
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

# 3. Comparison of Petal Length Distributions
#Set style, colours (standard) and plot size
sns.set(style="whitegrid", palette="GnBu_d", rc={"figure.figsize": (11.7, 8.27)})
#Title
title="Comparison of Petal Length Distributions"
#x = species, y = petal length
sns.boxplot(x="species", y="petal_length", data=iris_1)
#Increased fontsize
plt.title(title, fontsize=26)
plt.show()

# 4. Comparison of Petal Width Distributions
#Set style, colours (standard) and plot size
sns.set(style="whitegrid", palette="GnBu_d", rc={"figure.figsize": (11.7, 8.27)})
#Title
title="Comparison of Petal Width Distributions"
#x = species, y = petal width
sns.boxplot(x="species", y="sepal_width", data=iris_1)
#Increased fontsize
plt.title(title, fontsize=26)
plt.show()


# 5. Pairplot
#Background color
import seaborn as sns
sns.set(style="whitegrid")
sns.pairplot(iris_1, hue="species", palette="GnBu_d", diag_kind="kde", markers=["o", "s", "D"])
#Remove the top and right spines from plot
sns.despine()
import matplotlib.pyplot as plt
plt.show()

# 6. plotting regression and confidence intervals
import seaborn as sns
sns.pairplot(iris_1,hue="species", kind='reg', palette="GnBu_d")
#Remove the top and right spines from plot
sns.despine()
#show plot
import matplotlib.pyplot as plt
plt.show()

# 7. Swarm plot
import seaborn as sns
#setting the background color and size of graph
sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
# "Melt" the dataset
iris2 = pd.melt(iris_1, "species", var_name="measurement")
# Draw a categorical scatterplot
sns.swarmplot(x="measurement", y="value", hue="species",palette="GnBu_d", data=iris2)
#Remove the top and right spines from plot
sns.despine()
#show plot
import matplotlib.pyplot as plt
plt.show()

# 8. Violin plot 1
import seaborn as sns
#setting the background color and size of graph
sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
sns.violinplot(x="species", y="petal_length", palette="GnBu_d", data=iris_1)
#Remove the top and right spines from plot
sns.despine()
#show plot
import matplotlib.pyplot as plt
plt.show()


# 9. Violin plot 2
import seaborn as sns
#setting the background color and size of graph
sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})
sns.violinplot(x="species", y="petal_width", palette="GnBu_d", data=iris_1)
#Remove the top and right spines from plot
sns.despine()
#show plot
import matplotlib.pyplot as plt
plt.show()

# 10. Box plot
import matplotlib.pyplot as plt
iris_1.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

