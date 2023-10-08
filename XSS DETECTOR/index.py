import pickle
from keras.models import load_model

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

model = load_model('xss_model.h5')

user_input = input("Lütfen kontrol edilecek metni girin: ")
vectorized_input = vectorizer.transform([user_input])

# Dönüştürülen veriyi modelin beklediği boyuta uygun hale getirme
if vectorized_input.shape[1] > 100:
    vectorized_input = vectorized_input[:, :100]

prediction = model.predict(vectorized_input)

if prediction[0][0] > 0.5:
    print("Bu metin XSS saldırısı olarak tespit edildi!")
else:
    print("Bu metin güvenli görünüyor.")
