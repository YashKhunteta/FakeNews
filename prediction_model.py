from nltk.corpus import stopwords
import joblib
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
<<<<<<< HEAD
import os
=======
>>>>>>> 6097e93ed80df465389b2c6a559379f9ed973fbf

ps = PorterStemmer()
nltk.data.path.append('./nltk_data')


model = joblib.load('model2.pkl')
print('=> Pickle Loaded : Model ')
tfidfvect = joblib.load('tfidfvect2.pkl')
print('=> Pickle Loaded : Vectorizer')


class PredictionModel:
    output = {}

<<<<<<< HEAD
    # Load the model and vectorizer once at the start
    model = None
    tfidfvect = None

    @staticmethod
    def load_model():
        if PredictionModel.model is None or PredictionModel.tfidfvect is None:
            # Load the model and vectorizer only once
            model_path = os.getenv('MODEL_PATH', 'model2.pkl')
            vectorizer_path = os.getenv('VECTORIZER_PATH', 'tfidfvect2.pkl')

            PredictionModel.model = joblib.load(model_path)
            PredictionModel.tfidfvect = joblib.load(vectorizer_path)

            print('=> Pickle Loaded : Model and Vectorizer')

    # constructor
    def __init__(self, original_text):
        self.output['original'] = original_text
        # Load model when the object is created
        PredictionModel.load_model()
=======
    # constructor
    def __init__(self, original_text):
        self.output['original'] = original_text

>>>>>>> 6097e93ed80df465389b2c6a559379f9ed973fbf

    # predict
    def predict(self):
        review = self.preprocess()
<<<<<<< HEAD
        text_vect = PredictionModel.tfidfvect.transform([review]).toarray()
        self.output['prediction'] = 'FAKE' if PredictionModel.model.predict(text_vect) == 0 else 'REAL'
        return self.output

=======
        text_vect = tfidfvect.transform([review]).toarray()
        self.output['prediction'] = 'FAKE' if model.predict(text_vect) == 0 else 'REAL'
        return self.output


>>>>>>> 6097e93ed80df465389b2c6a559379f9ed973fbf
    # Helper methods
    def preprocess(self):
        review = re.sub('[^a-zA-Z]', ' ', self.output['original'])
        review = review.lower()
        review = review.split()
<<<<<<< HEAD
        review = [ps.stem(word) for word in review if word not in stopwords.words('english')]
        review = ' '.join(review)
        self.output['preprocessed'] = review
        return review
=======
        review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)
        self.output['preprocessed'] = review
        return review
>>>>>>> 6097e93ed80df465389b2c6a559379f9ed973fbf
