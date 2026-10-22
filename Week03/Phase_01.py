from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

texts = [

"I love this course",

"This course is excellent",

"I hate this course",

"This course is terrible",


]

labels = [

"positive",

"positive",

"negative",

"negative",

]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

model = MultinomialNB()

model.fit(X, labels)

new_text = ["I really love this course"]

new_X = vectorizer.transform(new_text)

prediction = model.predict(new_X)

print("Prediction:", prediction[0])