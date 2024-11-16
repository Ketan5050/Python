import nltk 
from nltk.tokenize import *
nltk.download('punkt_tab')
text="Hello, I am Ketan Patil from Kolhapur"
print(word_tokenize(text))

sentences=sent_tokenize(text)
print(sentences)