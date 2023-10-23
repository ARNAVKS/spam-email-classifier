# Spam-Email-Classifier
Hey! I am Arnav. I made this spam classifier using NLP, in it I use **Bag of words** for text vectorizing and for prediction I use **Naive Bayes Classifier**.  
##
For downloading dataset [Click Here](https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset?select=completeSpamAssassin.csv). \
Then download '**completeSpamAssassin.csv**' in it.
##
Now as per NLP pipeline :
1. Data Acquisition
2. Text Preprocessing
3. Feature Engineering
4. Model Evaluation
##
* **Data Acquisition** : Import the dataset that we downloaded earlier in your Google Colab.
* **Text Preprocessing** : I had done Basic-Text Preprocessing, in which I had done text cleaning by doing lowercasing, removing newline character (\n), removing url links, removing '@', removing all punctuation marks and removing digits in all the texts.
* **Feature Engineering** : For finding the feature of of the text I used Bag of Words.
* **Model Evaluation** :  Split the data into training and testing data. I had choosen Naive Bayes Classifier for prediction. By fitting and checking the accuracy of training and testing data I got that in out of 3 Naive Bayes Classifier, Multinomial has its training data and testing data accuracy more 98%. Hence, I had choosen **Multinomial Naive Bayes Classifier** as our final model.
