from typing import List
import re
import numpy as np

class CountVectorizer():
    def fit_transform(self, collection: List[str]) -> List[List[int]]:
        '''transforms list of str into a matrix consisting of nested lists to create term-document matrix'''
        self.features = list(set(re.sub(r'[\.,?!:^;-_+=&$%`]', ' ', ','.join(collection).lower()).split()))
        return np.array([[re.sub(r'[\.,?!:^;-_+=&$%`]', '',collection[i].lower()).split().count(j) for j in self.features] for i in range(len(collection))]).reshape(-1, len(self.features))


    def get_feature_names(self) -> List[str]:
        '''returns a list of unique words containing in the input'''
        return self.features

corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
    ]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

if __name__ == "__main__":
    print(vectorizer.get_feature_names())
    print(count_matrix)
    print(CountVectorizer.fit_transform.__doc__)
    print(CountVectorizer.get_feature_names.__doc__)

