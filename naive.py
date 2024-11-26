import random
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score


random.seed(40)


random_numbers = sorted([random.randint(0, 100) for _ in range(50)])
categories = ["low" if num < 50 else "high" for num in random_numbers]


category_labels = [0 if cat == "low" else 1 for cat in categories]


X = [[num] for num in random_numbers]  # Fitur
y = category_labels                    # Label


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


nb_model = GaussianNB()
nb_model.fit(X_train, y_train)


y_pred = nb_model.predict(X_test)
print("Bilangan asli (sorting):", [x[0] for x in X_test])
print("Kategori asli:", y_test)
print("Prediksi kategori:", y_pred)


print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
