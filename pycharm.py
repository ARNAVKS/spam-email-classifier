#now deploying the model using pycharm

#importing libraries
import streamlit as st
import pickle
import string
import re

st.title('Spam Email Classifier')

remove_url = re.compile(r'https?://\S+|www\.\S+')
newline_rem=re.compile(r'\n')
mail_rem=re.compile(r'[^\@]\@[^\@]')
def num_remover(text):
    for i in string.digits:
        text = text.replace(i,'')
    return text
def punc(text):
    for i in string.punctuation:
        text = text.replace(i,'')
    return text

def transform_text(text):
  text = text.lower()
  text = newline_rem.sub('',text)
  text = remove_url.sub('',text)
  text = mail_rem.sub('',text)
  text = punc(text)
  text = num_remover(text)
  return text

cv = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('mnb_model.pkl','rb'))

input = st.text_input('**Write the mail content here :**')

if st.button('Predict'):
    input_vec = cv.transform([input])

    pred = model.predict(input_vec)[0]

    if pred == 1:
        st.header('Spam')
    else:
        st.header('Not spam')
