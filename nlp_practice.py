import nltk

# opening the sermon text
f = open("a_divine_and_supernatural_light.txt", "r")
text = f.read()
text = text.lower()

tokens = [t for t in text.split()]

# removing stopwords from the text
from nltk.corpus import stopwords
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

# plotting the 20 most frequestly used words
freq = nltk.FreqDist(clean_tokens)
freq.plot(20, cumulative=False)

# opening the sermon text
f = open("sinners_in_the_hands_of_an_angry_god.txt", "r")
text = f.read()
text = text.lower()

tokens = [t for t in text.split()]

# removing stopwords from the text
from nltk.corpus import stopwords
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

# plotting the 20 most frequestly used words
freq = nltk.FreqDist(clean_tokens)
freq.plot(20, cumulative=False)


 
