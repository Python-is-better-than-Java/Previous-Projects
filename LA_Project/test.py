import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import cv2
import pickle

img_file = open('img_file', 'rb')     
db = pickle.load(img_file)
print(db)