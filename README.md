# Machine Learning Voyage: Predicting Survival on the Titanic  
## Outline 
We will attempt to use a variety of machine learning applications and network types to solve the classic problem of determining if a passenger on the Titanic survived or not. Please follow this [link](https://docs.google.com/presentation/d/1BwgvJUFh5OM1lqclEAVu_NhSxfGTTEGm/edit?usp=drive_link&ouid=118052364722070729043&rtpof=true&sd=true) to view out project on PPT.

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

## Data Visualization
Based on our Tableau visualization and data analysis, most passengers on the Titanic perished. Passengers were mostly adults and mostly male and the largest class aboard 
was the third class. Women aboard the ship had significantly higher chances of survival. Even when considering boarding class distinctions, survival rates among first-class men were only 35%, whereas over 97% of first-class women survived. Interestingly, third-class women had a higher survival rate than first-class men.  

Gender also played a crucial role in the survival of children on board. While sadly only 21% of boys in the third class survived, 51% of girls in the same class did. Despite boys faring worse than adult women, their survival rate was double that of adult men. Having relatives aboard the Titanic slightly improved the chances of survival for all classes and genders of adults and children, except for first-class women, where the difference was negligible.  
  
Class was a significant factor as well, with women in first and second class being around twice as likely to survive as men in first class. While still having a low survival rate, men in first class were three times as likely to survive compared to men in lower classes.  
  
Another way of looking at class is to observe the points of embarkation. Cherbourg, France boarded the highest proportion of first-class passengers and unsurprisingly saw the highest rates of survival. The passengers who boarded at Queenstown, Ireland were mostly third class and consequently, the rate of survival was lower than passengers who boarded at Cherbourg. 
Passengers who boarded at Southampton, England were the least likely to survive, mostly because Southampton had the highest proportion of male passengers and also due to more than 50% of passengers coming from third class.  

See the full Tableau Visualization on [Tableau Public](https://public.tableau.com/app/profile/elizabeth.morgan4663/viz/Project4Team6-TitanicVisualizations/TitanicPassengerDataAnalysis) or download the `Titanic_Visualizations.twbx` found in this github repository.
  
## Data Model Implementation  
The first step of the data processing stage was to merge the test CSV files and then assign the files to a train or test variable. Next null values were dropped from the "Embarked" column since there was no significant loss in the data by doing so. To ensure that data types were correct, the `.astype()` function was used to convert appropriate columns to strings. The "Age" column contains 177 null values out of 891 entries, therefore a significant amount of data would be lost if we dropped null values. Instead, estimated median values for "Age" were replaced across sets of "Pclass" and "Gender" feature combinations with null values...  

The full ETL process is contained within the `DataProcessing.ipynb`, while model testing and analysis is in `ModelEvaluation.ipynb`. The `SQLCode.ipynb` contains more data transformation and analysis utilizing SQL. All notebooks were run in [Google Colab](https://colab.research.google.com/); as a result, there are segments of redundant code present to make running the code as simple as possible without too many file uploads. You'll need to add the relevant files in a "Resources" folder in Colab, which can be found near the top of the Jupyter notebooks. Output files such as refined datasets and a tree diagram will need to be downloaded from Colab.

## Data Model Optimization  
Summary of Model Performance in Supervised Machine Learning
Logistic Regression:
The confusion matrix of the logistic regression model revealed that the model accurately classified 541 instances of non-survival and 302 instances of survival in the training data.
In the testing data, it correctly identified 193 instances of non-survival and 80 instances of survival.
Achieving an 83% accuracy in testing, the logistic regression model demonstrated slightly better performance in predicting class 0 compared to class 1.

K Nearest Neighbors Classifier:
The KNN classifier accurately predicted 218 instances of non-survival and 109 instances of survival in the testing data.
Achieving an accuracy of 88% in training and 83% in testing, the K Nearest Neighbors Classifier Model showcased robust predictive capabilities.

Random Forest Classifier:
The random forest model accurately predicted all instances for both class 0 and class 1 in the training data. The testing data yielded a similar outcome, with correct predictions of 218 instances of non-survival and 109 instances of survival.
It achieved an accuracy of 100% in training and 83% in testing, and the model exhibited consistent performance in predicting both non-survival and survival cases.

Decision Tree Classifier:
The decision tree classifier accurately predicted 184 instances of non-survival and 76 instances of survival. 
While achieving 100% accuracy in the training data, its performance decreased slightly to 80% in testing.

Gradient Boosting Classifier Model:
The gradient boosting classifier correctly identified 218 instances of non-survival and 109 instances of survival in the testing data.
With an 83% accuracy in testing, the model demonstrated a slightly stronger capability towards predicting class 0 compared to class 1.

Overall, the models evaluated showed strong predictive capabilities in training data, where they demonstrated higher accuracy rates. However, they tend to perform better at predicting class 0 (non-survival) instances compared to class 1 (survival) instances across all models. This discrepancy could be attributed to several factors, including class imbalance, feature representation, and model complexity.

Interestingly, both the random forest and decision tree classifiers achieved a remarkable 100% accuracy on the training data. This outcome suggests that these models may have overfit the training data. As a result, they may struggle to perform as well on unseen data, leading to lower accuracy rates in testing.  

**Classification & Neural Network Model**
Two classifications and one neural network model were used in Data Model Optimization. The `CatBoost` and `AdaBoost` classifiers were used. `CatBoost` is a gradient-boosting library that's particularly effective for categorical data. `AdaBoost` is short for Adaptive Boosting and is a machine-learning algorithm used for classification tasks. It is an ensemble learning method that combines multiple weak learners to create a strong learner.  
  
`CatBoost` was initialized and iterations were set to 500. Step size was controlled at each iteration during the gradient boosting process. We then train, predict, and 
evaluate the model to get an accuracy of *0.86 or 85%. This turns out to be our best-performing model.*  
  
`AdaBoost` is later implemented using sci-kit learn as well. We generate a synthetic classification dataset that creates 1000 samples with 4 features, 2 of which are informative for classification. We then train, predict, and evaluate the model to get an accuracy of 0.84. 

The neural network model using TensorFlow's Keras API was used. We set up input features, layer sizes and created a new sequential neural network model. We then added the first layer and set the activation to ReLu (Rectified Linear Unit), which is commonly used in hidden layers to introduce non-linearity. The second, third, and output layers activations were all set to sigmoid. Sigmoid functions are often used in hidden layers for binary classification problems. Sigmoid is also chosen in the output layer because the problem is a binary classification, where the output needs to be between 0 and 1.  
  
We print a summary of the model, including the layers, their output shapes, and the number of trainable parameters in the model. It provides a concise overview of the model architecture. We then compile and fit the model to get an accuracy of 0.83.

**TO DO**
GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)  
