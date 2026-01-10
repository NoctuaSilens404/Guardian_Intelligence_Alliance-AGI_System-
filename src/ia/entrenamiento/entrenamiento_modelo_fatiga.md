import pandas as pd

# Cargar el dataset
df = pd.read_csv("src/ia/entrenamiento/datos_fatiga.csv")

# Ver las primeras filas
df.head()

df = df.dropna()

X = df[["pulso", "temperatura", "spo2", "horas_trabajadas"]]
y = df["etiqueta_riesgo"]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split

# Dividir datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print("Tamaño entrenamiento:", len(X_train))
print("Tamaño prueba:", len(X_test))
