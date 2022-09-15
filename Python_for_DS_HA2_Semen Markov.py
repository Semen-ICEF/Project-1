#!/usr/bin/env python
# coding: utf-8

# In[10]:


class CountVectorizer():
    def fit_transform(self, lst):
        self.features = list(set(','.join(lst).lower().replace(',', ' ').split()))
        l1, l2 = [], []
        for i in lst:
            for j in self.features:
                l2.append(i.lower().split().count(j))
            l1.append(l2.copy())
            l2.clear()
        return l1
    
    
    def get_feature_names(self):
        return self.features

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(count_matrix)

