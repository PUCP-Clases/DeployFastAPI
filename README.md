# 🚀 Despliegue de modelos de ML en una Aplicación Web 🚀

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![fastapi](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](https://img.shields.io/badge/FastAPI-3776AB?style=for-the-badge&logo=fastapi&logoColor=white)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

<div align='center'> 
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"/>
</div>

## Descripción del Proyecto
Este proyecto combina el aprendizaje automático y FastAPI para desarrollar una aplicación potente y escalable para el análisis predictivo y el procesamiento de datos en tiempo real.

## Tabla de Contenidos
1. [Resumen del Proyecto](#resumen)
  - [Descripción del conjunto de datos](#conjunto-de-datos)
2. [Stack de Tecnología](#tecnologia)
3. [Entregables](#entregables)
4. [Instalación](#instalacion)
5. [Ejecución](#ejecucion)
6. [API Endpoints](#puntos-de-extremo)
7. [Uso de la Aplicación](#uso)
8.  [Información de Contacto](#contacto)

## 1. Resumen del Proyecto <a name="resumen"></a>
- El proyecto de predicción de sepsis gira en torno a un modelo de aprendizaje automático diseñado para predecir con precisión la sepsis en pacientes de unidades de cuidados intensivos (UCI). El modelo ha sido sometido a un riguroso entrenamiento y evaluación para garantizar su eficacia en la identificación de pacientes en riesgo de sepsis.

- El proyecto proporciona una solución integral que incluye un FastAPI bien documentado alojado en una plataforma como el Hugging Face Model Hub y Heroku. Esta API permite la integración sin problemas del modelo de predicción de sepsis en sistemas de atención médica existentes, proporcionando a los profesionales de la salud información valiosa para mejorar la atención al paciente.

- Para simplificar la implementación y el uso, el proyecto incluye un archivo Docker que agiliza el proceso de configuración y garantiza la instalación de las dependencias necesarias. Esto facilita la implementación del modelo de predicción de sepsis en diversos entornos, tanto locales como en la nube.

- Se proporciona documentación detallada y ejemplos prácticos para guiar a los usuarios en la utilización efectiva del modelo de predicción de sepsis. La documentación cubre instrucciones de instalación, pautas de uso de la API y destaca las posibles aplicaciones del modelo en escenarios de atención médica reales, empoderando a los proveedores de atención médica para tomar decisiones informadas y mejorar los resultados de los pacientes.

### i. Descripción del conjunto de datos <a name="conjunto-de-datos"></a>
| Nombre de la Columna | Atributo/Objetivo | Descripción |
| -------------------- | ----------------- | ----------- |
| ID                   | N/A               | Número único para representar el ID del paciente |
| PRG                  | Atributo1         | Glucosa en plasma |
| PL                   | Atributo 2        | Resultado del análisis de sangre-1 (mu U/ml) |
| PR                   | Atributo 3        | Presión arterial (mm Hg) |
| SK                   | Atributo 4        | Resultado del análisis de sangre-2 (mm) |
| TS                   | Atributo 5        | Resultado del análisis de sangre-3 (mu U/ml) |
| M11                  | Atributo 6        | Índice de masa corporal (peso en kg / (altura en m)^2) |
| BD2                  | Atributo 7        | Resultado del análisis de sangre-4 (mu U/ml) |
| Age                  | Atributo 8        | Edad de los pacientes (años) |
| Insurance            | N/A               | Si un paciente tiene una tarjeta de seguro válida |
| Sepsis               | Target            | Positivo: si un paciente en la UCI desarrollará sepsis, y Negativo: en caso contrario |


## 2. Stack de Tecnología <a name="tecnologia"></a>
| Tecnología   | Versión   |
| ------------ | --------- |
| Python       | 3.9       |
| FastAPI      | 0.95.2    |
| Uvicorn      | 0.22.0    |
| Scikit-learn | 0.24.1    |
| Pandas       | 1.2.4     |
| Jinja2       | 3.1.2     |
| pandas-profiling       | 3.6.6     |

## 3. Entregables <a name="entregables"></a>
1. Un Jupyter notebook para entrenar un modelo de clasificación
2. Un modelo de clasificación
3. Una aplicación de API construida con FastApi
4. Una aplicación de Streamlit que realiza llamadas a la API construida
5. Un archivo Docker para facilitar la implementación

## 4. Instalación <a name="instalacion"></a>
Clona el repositorio en tu máquina local:

        git clone https://github.com/PUCP-Clases/DeployFastAPI.git

Navega al directorio del proyecto:

        cd DeployFastAPI
Crea un nuevo entorno virtual y actívalo:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux y MacOs:

        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

## 5. Ejecución <a name='ejecucion'></a>
1. Notebooks

Para ejecutar cualquier notebook:
- Navega a la carpeta del proyecto en la terminal de Anaconda.
- Ejecuta el comando 'jupyter notebook' o abre desde tu IDE favorito.
- Navega al notebook 'Sepsis_prediction_with_ml.ipynb'.
- Ejecuta las celdas en el notebook.

2. API

Para ejecutar la API, sigue estos pasos: Después de haber instalado todos los requisitos

En la raíz de tu repositorio en tu terminal:
`root :: <DeployFastAPI> ...` ejecuta el comando:

            uvicorn src.app.app:app --reload 

O

            python src/app/app.py

Abre tu navegador e ingresa a http://127.0.0.1:8000/docs para acceder a la documentación de la API.

3. Aplicación Streamlit

Para ejecutar la aplicación, sigue estos pasos: Después de haber instalado todos los requisitos

En la raíz de tu repositorio en tu terminal:
`root :: <DeployFastAPI> ...` ejecuta el comando:

            streamlit src/streamlit_app/main.py

Abre tu navegador e ingresa a http://localhost:8501 o http://172.20.10.12:8501 para acceder a la aplicación.

## 6. API Endpoints <a name="api-endpoints"></a>
1. **/**: Este endpoint muestra un mensaje de bienvenida: "Welcome to the Sepsis API...".
2. **/health**: Comprueba el estado de la API.
3. **model-info**: Devuelve información sobre el modelo.
4. **/predict**: Recibe entradas y devuelve una única predicción.
5. **/predict-batch**: Recibe múltiples entradas y devuelve múltiples predicciones.
5. **/upload-data**: Recibe un archivo JSON o CSV, lo procesa y devuelve predicciones.

## 7. Uso de la Aplicación <a name="usage"></a>
Para probar los diversos endpoints de la API utilizando la documentación proporcionada, sigue estos pasos:

1. Comienza accediendo a la documentación de la API, que proporciona información detallada sobre los endpoints disponibles y sus funcionalidades.

2. Encuentra la sección que describe los campos de entrada y los parámetros necesarios para cada endpoint. Especificará el formato de datos esperado, como JSON o datos de formulario, y los campos de entrada necesarios.

3. Introduce los datos de entrada requeridos en los campos de entrada correspondientes o en los parámetros según se especifique en la documentación.

4. Envía la solicitud haciendo clic en el botón "Ejecutar" o utilizando el método adecuado en tu herramienta elegida. La API procesará la solicitud y generará la salida en función de los datos proporcionados.

5. Recupera la respuesta de la API, que contendrá la salida generada. Esta salida puede incluir predicciones, puntuaciones de probabilidad u otra información relevante relacionada con la predicción de sepsis.

6. Repite el proceso para probar diferentes endpoints o varía los datos de entrada para explorar las capacidades de la API. Asegúrate de seguir las pautas de la documentación para cada endpoint para obtener resultados precisos.

## 8. Información de Contacto <a name="contact"></a>

<table>
  <tr>
    <th>Nombre</th>
    <th>LinkedIn</th>
    <th>GitHub</th>
    <th>Hugging Face</th>
  </tr>
  <tr>
    <td>Juan Carlos Tovar</td>
    <td><a href="https://www.linkedin.com/in/juan-carlos-tovar-galarreta/">@juan-carlos-tovar-galarreta</a></td>
    <td><a href="https://github.com/JuanTovarGalarreta">@JuanTovarGalarreta</a></td>
    <td><a href="https://huggingface.co/JuanCarlosA">@JuanCarlosA</a></td>
  </tr>
</table>
