# Spam-Email-Classifier
Hey! I am Arnav. I made this spam classifier using NLP, in it I use **Bag of words** for text vectorizing and for prediction I use **Naive Bayes Classifier**.  
##
For downloading dataset [Click Here](https://www.kaggle.com/datasets/nitishabharathi/email-spam-dataset?select=completeSpamAssassin.csv). \
Then download '*completeSpamAssassin.csv*' in it.
##
Now as per NLP pipeline :
1. Data Acquisition
2. Text Preprocessing
3. Feature Engineering
4. Model Evaluation
5. Model Deployment
##
* **Data Acquisition** : Import the dataset that we downloaded earlier in your Google Colab.
```python
import pandas
table = pd.read_csv('completeSpamAssassin.csv')
```
* **Text Preprocessing** : I had done Basic-Text Preprocessing, in which I had done text cleaning by doing lowercasing, removing newline character (\n), removing url links, removing '@', removing all punctuation marks, removing digits, removing all the stopwords and using stemming in all words in all the texts.
* **Feature Engineering** : For finding the feature of of the text I used Bag of Words.
```python
from sklearn.feature_extraction import CountVectorizer
cv = CountVectorizer()
#fitting and transforming the training data using this code
cv.fit_transform(train).toarray()
#transforming the testing data using ths code
cv.transform(test).toarray()
```
* **Model Evaluation** :  Split the data into training and testing data. I had choosen Naive Bayes Classifier for prediction. By fitting and checking the accuracy of training and testing data I got that in out of 3 Naive Bayes Classifier, Multinomial has its training data and testing data accuracy more 97%. Hence, I had choosen **Multinomial Naive Bayes Classifier** as our final model.
```python
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
gnb = GaussianNB()
bnb = BernoulliNB()
mnb = MultinomialNB()
```
##
Comparing all the classsifier after fitting the data,
1. **Gaussian Naive Bayes Classifier :**
 * Training Data Accuracy
```python
0.9063492063492063
```
 * Testing Data Accuracy
```python
0.8884859474161378
```
2. **Bernoulli Naive Bayes Classifier :**
 * Training Data Accuracy
```python
0.9607709750566893
```
 * Testing Data Accuracy
```python
0.958295557570263
```
3. **Multinomial Naive Bayes Classifier :**
 * Training Data Accuracy
```python
0.9807256235827665
```
 * Testing Data Accuracy
```python
0.970988213961922
```
##
After Choosing the best model, now we export the vectorizer and model using pickle library. \
Now, as per the NLP pipeline only one step is left to do which is **Model Deployment**. \
I used **Streamlit library** for model deployment in **PyCharm**. \
All the step for deployment is written in *pycharm.py* file.
