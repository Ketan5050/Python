import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_word=set(stopwords.words("english"))
text="This is a sample sentence, showing off the stop word filteration"
words=word_tokenize(text)
filtered_word=[ word for word in words if word.lower() not in stop_word]
print(filtered_word)
