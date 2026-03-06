import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Data example
jam_belajar = np.random.rand(100, 1) * 10 # 100 nilai acak antara 0 dan 10
nilai_ujian = 3 * jam_belajar + np.random.randn(100, 1) * 2 
# Hubungan linear dengan sedikit noise
# print (jam_belajar)
# print ("Nilai Ujian:")
# print (nilai_ujian)

# Split data into training and testing sets
Xtrain, X_test, y_train, y_test = train_test_split(jam_belajar, nilai_ujian, test_size=0.2, random_state=42)

# Initialize model linier regression
model = LinearRegression()

# Train model using training data
model.fit(Xtrain, y_train)

# Predict using testing data
y_pred = model.predict(X_test)

# visualize the results
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=3)
plt.title("Regresi Linier Sederhana")
plt.xlabel("Jam Belajar")
plt.ylabel("Nilai Ujian")   
plt.show()  

# Hitung dan cetak metrik evaluasi
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)     

# Gunakan model untuk membuat prediksi baru
new_hours = np.array([[8]]) # contoh: prediksi nilai ujian untuk 8 jam belajar
new_prediction = model.predict(new_hours)
print("Prediksi nilai ujian untuk 8 jam belajar:", new_prediction[0][0])  
belajar: {new_prediction[0][0]}