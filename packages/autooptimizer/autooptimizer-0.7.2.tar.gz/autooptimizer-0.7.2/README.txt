AutoOptimizer provides tools to automatically optimize machine learning model for a dataset with very little user intervention.

It refers to techniques that allow semi-sophisticated machine learning practitioners and non-experts 
to discover a good predictive model pipeline for their machine learning algorithm task quickly,
with very little intervention other than providing a dataset.


#Prerequisites:

jupyterlab(contains all sub packages except mlxtend) or: {sklearn,matplotlib,mlxtend,numpy}	


#Usage:


*Optimize scikit learn supervised and unsupervised learning models using python.


{DBSCAN, KMeans, MeanShift,  LogisticRegression, KNeighborsClassifier, SupportVectorClassifier, DecisionTree}


*Metrics for Your Regression Model


*Clear data by removing outliers



>#Running auto optimizer:


>>from autooptimizer.cluster import dbscan, meanshift, kmeans

 
>>from autooptimizer.neighbors import kneighborsclassifier


>>from autooptimizer.tree import decisiontreeclassifier


>>from autooptimizer.svm import svc


>>from autooptimizer.linear_model import logisticregression


>>dbscan(x)


>>kmeans(x)


>>meanshift(x)


>>logisticregression(x,y)


>>kneighborsclassifier(x,y)


>>svc(x,y)


>>decisiontreeclassifier(x,y)


'x' should be your independent variable or feature's values and 'y' is target variable or dependent variable.
The output of the program is the maximum possible accuracy with the appropriate parameters to use in model.

>#Evaluation Metrics for Your Regression Model

{root_mean_squared_error, root_mean_squared_log_error, root_mean_squared_precentage_error,
symmetric_mean_absolute_precentage_error, mean_bias_error, relative_squared_error, root_relative_squared_error
relative_absolute_error, median_absolute_percentage_error, mean_absolute_percentage_error}

>#Running for example


>>from autooptimizer.metrics import root_mean_squared_error


>>root_mean_squared_error(true, predicted)


>#Running outlier remover


>>from autooptimizer.outlier import interquartile_outlier_removal 

>>from autooptimizer.outlier import plot_interquartile_outlier_removal

>>from autooptimizer.outlier import zscore_outlier_removal

>>from autooptimizer.outlier import plot_zscore_outlier_removal

>>from autooptimizer.outlier import std_outlier_removal

>>from autooptimizer.outlier import plot_std_outlier_removal


>>interquartile_outlier_removal(array)


>>plot_interquartile_outlier_removal(array) #with plot charts for more details


>>zscore_outlier_removal(array)


>>plot_zscore_outlier_removal(array)


>>std_outlier_removal(array, threshold=value) #threshold default value is 3


>>std_outlier_removal(array, threshold=value) #threshold default value is 3



#Contact and Contributing:
Please share your good ideas with us. 
Simply letting us know how we can improve the programm to serve you better.
Thanks for contributing with the program.

>>https://github.com/mrb987/autooptimizer

>>www.Genesiscube.ir
>>info@Genesiscube.ir