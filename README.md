# Machine Learning Voyage: Predicting Survival on the Titanic  
## Collaborators  
**Fullname / Github Username**  
Kerim Celik / kcelik369  
Nancy Zheng / zhengn95  
Kylie Li / xyr3n  
Thanushree Palanivale / tanvale  
Elizabeth Morgan / elizabethmorgan26  
Nick Nath / earthreveals  

## Table of Contents 
1. **Dataset**
   - Resources folder
   - Original Kaggle Dataset is [HERE](https://www.kaggle.com/competitions/titanic)  
2. **Data Visualization**
   - `Titanic_Visualizations.twbx`
4. **Data Model Implementation**
   - `DataProcessing.ipynb`
   - `SQLCode.ipynb`
5. **Data Model Optimization**
   - `ModelEvaluation.ipynb`

## Outline - Tableau - Elizabeth
We will attempt to use a variety of machine learning applications and network types to solve the classic problem of determining if a passenger on the Titanic survived or not.  
Tableau Analysis for the ReadMe file:
Most passengers on the Titanic perished.
Passengers were mostly adults and mostly male. The largest class aboard 
was third class.
Women aboard the ship had significantly higher chances of survival. Even 
when considering boarding class distinctions, survival rates among first-class
men were only 35%, whereas over 97% of first-class women survived. 
Interestingly, third-class women had a higher survival rate than first-class 
men.
Gender also played a crucial role in the survival of children on board. While 
sadly only 21% of boys in the third class survived, 51% of girls in the same class 
did. Despite boys faring worse than adult women, their survival rate was 
double that of adult men.
Class was a significant factor as well, with women in first and second-class 
being around twice as likely to survive as men in first class, while still 
unlikely to survive, were three times as likely to survive compared to men in 
lower classes.
 
Another way of looking at class is to observe the points of embarkation. 
Cherbourg, France boarded the highest proportion of first-class passengers 
and unsurprisingly saw the highest rates of survival. The passengers who 
boarded at Queenstown, Ireland were mostly third class and consequently, 
the rate of survival is lower than passengers who boarded at Cherbourg. 
Passengers who boarded at Southampton, England were the least likely to 
survive, mostly because Southampton had the highest proportion of male 
passengers and also due to more than 50% of passengers coming from third 
class.
Having relatives aboard the Titanic indeed slightly improved the chances of 
survival for all classes and genders of adults and children, except for first-
class women, where the difference was negligible.

**Data Model Implementation (25 points) - Kerim**
A Python script initializes, trains, and evaluates a model (10 points)  
The data is cleaned, normalized, and standardized prior to modeling (5 points)  
The full ETL process is contained within the "DataProcessing" Jupyter notbook, while model testing and analysis is in "ModelEvaluation". The "SQLCode" notebook contains more data transformation and analysis utilizing SQL.
All notebooks were run in Google Colab; as a result, there are segments of redundant code present to make running the code as simple as possible without too many file uploads. You'll need to add the relevant files in a "Resources" folder in Colab, which can be found near the top of the Jupyter notebooks. Output files such as refined datasets and a tree diagram will need to be downloaded from Colab.
Our best performance was around 86% from the CatBoost model.

**The model utilizes data retrieved from SQL (5 points) - Nancy**

**The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared. (5 points) - Tan**
Data Model Optimization (25 points)  
The model optimization and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (15 points)  
I have done two classifications and one neural network model.
For the two classifications I used the CatBoost and AdaBoost classifiers. CatBoost is 
a gradient boosting library that's particularly effective for categorical data. 
AdaBoost is short for Adaptive Boosting, and is a machine learning algorithm used 
for classification tasks. It is an ensemble learning method that combines multiple 
weak learners to create a strong learner.
CatBoost was initialized and iterations were set to 500. I also try to control the step
size at each iteration during the gradient boosting process. I then train, predict and 
evaluate the model to get an accuracy of 0.86. This turns out to be our best 
performing model.
AdaBoost is later implemented using sci-kit learn as well.    I generate a synthetic 
classification dataset which creates 1000 samples with 4 features, 2 of which are 
informative for classification. I then train, predict and evaluate the model to get an 
accuracy of 0.84.
Neural network model using TensorFlow's Keras API
I set up input features, layer sizes and create a new sequential neural network 
model.
I then add the first layer and set the activation to ReLu (Rectified Linear Unit), which
is commonly used in hidden layers to introduce non-linearity. I then set the second, 
third and output layer and set all their activations to sigmoid. Sigmoid functions are 
often used in hidden layers for binary classification problems. Sigmoid is also 
chosen in the output layer because the problem is a binary classification, where the 
output needs to be between 0 and 1.
I print a summary of the model, including the layers, their output shapes, and the 
number of trainable parameters in the model. It provides a concise overview of the 
model architecture.
I then compile and fit the model to get an accuracy of 0.83

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
