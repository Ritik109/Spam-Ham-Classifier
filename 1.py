import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle as c

direc = "emails/"
files = os.listdir(direc)
emails = [direc + email for email in files]
words = []
c = len(emails)
for email in emails:
	print("reading "+email)
	f = open(email)
	blob = f.read()
	words += blob.split(" ")
	print(c)
	c -= 1


