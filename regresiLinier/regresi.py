import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Data example
jam_belajar = np.random.rand(100, 1) * 10 # 100 nilai acak antara 0 dan 10
nilai_ujian = 3 * jam_belajar + np.random.randn(100, 1) * 2 
# Hubungan linear dengan sedikit noise
print (jam_belajar)
print ("Nilai Ujian:")
print (nilai_ujian)