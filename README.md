# Proyecto 1 - Machine Learning

## 📌 Descripción
Este proyecto tiene como objetivo desarrollar un flujo de **Machine Learning** desde la carga y análisis de datos hasta la construcción y evaluación de un modelo de regresión.  
El trabajo se centra en aplicar conceptos fundamentales de **preprocesamiento**, **pipeline**, **visualización** y **evaluación de métricas**, siguiendo buenas prácticas de estructuración de proyectos en Python.

---

## 📂 Estructura del Proyecto
```bash
Proyecto1/
│── data/               # Datos de entrada (crudos y procesados)
│── notebooks/          # Notebooks exploratorios (EDA, pruebas)
│── src/                # Código fuente del proyecto
│   ├── preprocessing.py # Limpieza y preparación de datos
│   ├── modeling.py      # Definición y entrenamiento de modelos
│   ├── evaluation.py    # Métricas de evaluación
│── reports/            # Resultados, gráficas y análisis
│── requirements.txt    # Dependencias del proyecto
│── README.md           # Documentación principal



---

## Librerías Utilizadas

- **Procesamiento de datos**: `numpy`, `pandas`, `os`, `h5py`
- **Extracción de features de series temporales**: `tsfresh`
- **Selección de features**: `sklearn.feature_selection`
- **Normalización de datos**: `sklearn.preprocessing.StandardScaler`
- **Balanceo de clases**: `imblearn.over_sampling.SMOTE`
- **Visualización**: `matplotlib`, `seaborn`

---

## Flujo de Trabajo

### 1. Carga y Exploración de Datos
- Se cargan los datasets de entrenamiento y prueba desde archivos `.h5`.
- Se inspecciona la forma de los datos y se visualizan las primeras muestras.
- Se analiza la distribución de clases y se identifica desbalance entre `Control (0)` y `Alcohólicos (1)`.

### 2. Conversión de Series Temporales
- Los datos de EEG se convierten a formato “long” (`id`, `time`, `value`) compatible con `tsfresh`.
- Se crean `long_train_df` y `long_test_df` para extracción de características.

### 3. Extracción de Features
- Se extraen automáticamente estadísticas de las series temporales usando `tsfresh`.
- Se procesan los datos en bloques para optimizar memoria y tiempo de cómputo.
- Se guarda cada bloque como CSV y se combinan en un dataset final.
- Se realiza selección de features relevantes usando `select_features` (basado en la variable objetivo).

### 4. Selección de Features y Reducción de Dimensionalidad
- Se aplica **ANOVA F-test** para evaluar relevancia de cada feature con respecto a la clase.
- Se seleccionan las **top 20 features** más discriminativas.
- Se eliminan features redundantes basadas en análisis de correlación.

### 5. Balanceo de Clases
- Se aplica **SMOTE** para generar muestras sintéticas de la clase minoritaria.
- Se verifica la distribución equilibrada (50%-50%) de clases para entrenamiento.

### 6. Guardado de Datasets Finales
- `x_train_final.csv` y `x_test_final.csv` contienen las features depuradas y listas para el entrenamiento.
- `X_train_top20_features.csv` y `X_test_top20_features.csv` contienen únicamente las top 20 features seleccionadas.

---

## Análisis Exploratorio (EDA)

1. **Distribución de clases**:
   - La clase `Control` representa ~75% del dataset.
   - La clase `Alcohólicos` representa ~25%.
   - Se recomienda balancear antes del entrenamiento.

2. **Matriz de correlación**:
   - Se visualiza la correlación entre features y con el target.
   - Se identifican features redundantes o altamente correlacionadas.

3. **Visualización de features importantes**:
   - Se generan gráficos de dispersión entre las features más relevantes y la clase objetivo.
   - Esto permite identificar separación entre clases y posibles patrones discriminativos.

---

## Cómo Ejecutar

1. Instalar dependencias:

```bash
pip install numpy pandas h5py tsfresh scikit-learn imbalanced-learn matplotlib seaborn

2. Ejecutar el notebook de preprocesamiento y EDA:

```bash
jupyter notebook notebooks/EDA_Preprocessing.ipynb


3. Los datasets finales (x_train_final.csv y x_test_final.csv) estarán listos para entrenar modelos de machine learning como SVM, Random Forest, XGBoost, etc.


## Notas Importantes

- Los datos de EEG tienen 18,530 registros por sujeto.
- La extracción de features se realiza sobre el primer canal de EEG, aunque puede extenderse a todos los canales.
- Mantener nombres y orden de features consistentes entre entrenamiento y prueba.