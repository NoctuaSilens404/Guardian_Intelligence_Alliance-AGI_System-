# GIA - Guardian Intelligence Alliance

## Modelos de IA

### Clasificador de Riesgo de Fatiga

**Algoritmo**: RandomForestClassifier
**Features**:
- pulso (latidos/minuto)
- temperatura (°C)
- spo2 (saturación de oxígeno, %)
- horas_trabajadas

**Etiquetas**: bajo, medio, alto

**Pipeline**:
1. StandardScaler (normalización)
2. RandomForestClassifier (n_estimators=100, max_depth=5)

**Umbrales**:
- Riesgo alto: >= 0.7 probabilidad
- Riesgo medio: >= 0.4 probabilidad
- Riesgo bajo: < 0.4 probabilidad

### Entrenamiento
Ejecutar:
```bash
python src/ia/entrenamiento/entrenar_modelo.py
```
