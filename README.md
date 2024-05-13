# Machine Learning Voyage: Predicting Survival on the Titanic
## Collaborators
Kerim Celik / kcelik369  
Nancy Zheng / zhengn95  
Kylie Li / xyr3n  
Thanushree Palanivale / tanvale  
Elizabeth Morgan / elizabethmorgan26  
Nick Nath / earthreveals  

## Dataset
The Resources folder contains the datasets used in this analysis  
Source is [HERE](https://www.kaggle.com/competitions/titanic)

## Outline - Tableau - Elizabeth
We will attempt to use a variety of machine learning applications and network types to solve the classic problem of determining if a passenger on the Titanic survived or not.  

**Data Model Implementation (25 points) - Kerim**
A Python script initializes, trains, and evaluates a model (10 points)  
The data is cleaned, normalized, and standardized prior to modeling (5 points)  

**The model utilizes data retrieved from SQL or Spark (5 points) - Nancy**

**The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared. (5 points) - Tan**
Data Model Optimization (25 points)  
The model optimization and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (15 points)  

**Overall model performance is printed or displayed at the end of the script (10 points) - Kylie**
Summary of Model Performance
Logistic Regression:
The confusion matrix of the logistic regression model revealed that the model accurately classified 541 instances of non-survival and 302 instances of survival in the training data.
In the testing data, it correctly identified 193 instances of non-survival and 80 instances of survival.
Achieving an 83% accuracy in testing, the logistic regression model demonstrated slightly better performance in predicting class 0 compared to class 1.

K Nearest Neighbors Classifier:
The KNN classifier accurately predicted 218 instances of non-survival and 109 instances of survival in the testing data.
Achieving an accuracy of 88% in training and 83% in testing, the K Nearest Neighbors Classifier Model showcased robust predictive capabilities.

Random Forest Classifier:
The random forest model accurately predicted all instances for both class 0 and class 1 in the training data. The testing data yielded a similar outcome, with correct predictions of 218 instances of non-survival and 109 instances of survival.
It achieved an accuracy of 100% in training and 83% in testing, the model exhibited consistent performance in predicting both non-survival and survival cases.

Decision Tree Classifier:
The decision tree classifier accurately predicted 184 instances of non-survival and 76 instances of survival. 
While achieving 100% accuracy in the training data, its performance decreased slightly to 80% in testing.

Gradient Boosting Classifier Model:
The gradient boosting classifier correctly identified 218 instances of non-survival and 109 instances of survival in the testing data.
With an 83% accuracy in testing, the model demonstrated a slightly stronger capability towards predicting class 0 compared to class 1.

Overall, the models evaluated showed strong predictive capabilities in training data, where they demonstrate higher accuracy rates. However, they tend to perform better at predicting class 0 (non-survival) instances compared to class 1 (survival) instances across all models. This discrepancy could be attributed to several factors, including class imbalance, feature representation, and model complexity.

Interestingly, both the random forest and decision tree classifiers achieved a remarkable 100% accuracy on the training data. This outcome suggests that these models may have overfit the training data. As a result, they may struggle to perform as well on unseen data, leading to lower accuracy rates in testing.


**TO DO**
GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)  
