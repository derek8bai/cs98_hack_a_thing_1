import nltk

# opening the sermon text
f = open("a_divine_and_supernatural_light.txt", "r")
text1 = f.read()
text1 = text1.lower()

tokens = [t for t in text1.split()]

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
text2 = f.read()
text2 = text2.lower()

tokens = [t for t in text2.split()]

# removing stopwords from the text
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

# plotting the 20 most frequestly used words
freq = nltk.FreqDist(clean_tokens)
freq.plot(20, cumulative=False)

  
# api-endpoint 
  
import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = ""
url = ""
authenticator = IAMAuthenticator(api_key)
tone_analyzer = ToneAnalyzerV3(
    version='2020-01-08',
    authenticator=authenticator
)

tone_analyzer.set_service_url(url)

tone_analysis = tone_analyzer.tone(
    {'text': text1},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))

tone_analysis = tone_analyzer.tone(
    {'text': text2},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
 
