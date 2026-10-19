# Proyecto: Análisis de un Conjunto de Datos — Universo Pokémon 🔴⚪

> **Memoria técnica y resultados del proyecto de análisis exploratorio de datos mediante Python y Pandas.**

---

## 📌 Ficha del Proyecto

| Parámetro | Detalle |
| :--- | :--- |
| **Módulo Formativo** | 0378 – Seguridad y Alta Disponibilidad (Tema 1: Alta Disponibilidad) |
| **Ciclo Formativo** | Administración de Sistemas Informáticos en Red (ASIX 2) |
| **Profesor** | Josep Mª Ruiz Ríos |
| **Autores** | [Nombre Alumno 1] & [Nombre Alumno 2] |
| **Curso Académico** | 2026 – 2027 |
| **Repositorio GitHub** | [notebook-pokemon](https://github.com/umbyx-ai/notebook-pokemon) |

---

## 📑 Tabla de Contenidos
1. [Introducción](#1-introducción)
2. [Descripción del Dataset](#2-descripción-del-dataset)
3. [Limpieza y Gestión de Datos](#3-limpieza-y-gestión-de-datos)
4. [Análisis Exploratorio de Datos (EDA)](#4-análisis-exploratorio-de-datos-eda)
5. [Análisis en Profundidad: Resolución de las 5 Preguntas](#5-análisis-en-profundidad-resolución-de-las-5-preguntas)
   - [5.1. Pregunta 1: Pokémon más fuerte por hábitat](#51-pregunta-1-pokémon-más-fuerte-por-hábitat)
   - [5.2. Pregunta 2: Hábitat con más puntos de fuerza](#52-pregunta-2-hábitat-con-más-puntos-de-fuerza)
   - [5.3. Pregunta 3: Tipo más fuerte de media](#53-pregunta-3-tipo-más-fuerte-de-media)
   - [5.4. Pregunta 4: Pokémon no legendario más fuerte](#54-pregunta-4-pokémon-no-legendario-más-fuerte)
   - [5.5. Pregunta 5: Legendarios con mayor ratio de captura](#55-pregunta-5-legendarios-con-mayor-ratio-de-captura)
6. [Conclusiones Generales](#6-conclusiones-generales)
7. [Estructura del Repositorio](#7-estructura-del-repositorio)

---

## 1. Introducción

El presente proyecto se enmarca dentro del módulo formativo **0378 – Seguridad y Alta Disponibilidad** del ciclo de grado superior **ASIX2**. El objetivo fundamental consiste en aplicar metodologías rigurosas de análisis, tratamiento y visualización de datos mediante el lenguaje de programación Python y su ecosistema de librerías científicas, adquiriendo competencias clave en inspección técnica, depuración de anomalías, cálculo descriptivo y formulación de preguntas de investigación.

### ¿Por qué el universo Pokémon?
Se ha seleccionado este conjunto de datos debido a su enorme riqueza analítica:
* **Variables cuantitativas continuas y discretas**: Atributos numéricos de combate (`hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed`), la suma total de poder (`base_stat_total`) y ratios de probabilidad (`capture_rate`).
* **Variables cualitativas / categóricas**: Tipologías elementales (`type_1`), entornos biológicos (`habitat`) y marcas booleanas de categoría especial (`is_legendary`, `is_mythical`).
* **Relaciones no triviales**: Permite plantear hipótesis sobre el diseño paramétrico de videojuegos, balance competitivo y narrativa lúdica.

### Pila Tecnológica
* **Python 3.14**: Motor de computación base.
* **Pandas & NumPy**: Carga de DataFrames, filtrado vectorial, agregaciones y álgebra de tablas.
* **Matplotlib & Seaborn**: Generación de visualizaciones gráficas estadísticas de alta calidad.
* **Jupyter Notebook**: Entorno de desarrollo interactivo modular por notebooks.
* **Git & GitHub Desktop**: Control de versiones, ramas y trabajo colaborativo en pareja.

---

## 2. Descripción del Dataset

El conjunto de datos original procede de la consolidación de información extraída de la **PokéAPI** y repositorios abiertos de **Kaggle** (`pokemon_complete.csv`). Tras un proceso exhaustivo de auditoría y depuración técnica, se ha consolidado un archivo definitivo denominado **`pokemon.csv`**, compuesto por **1.025 registros** y **15 variables de estudio**.

### Diccionario de Datos

| Campo | Tipo | Descripción |
| :--- | :---: | :--- |
| `pokedex_number` | `int64` | Identificador numérico oficial en la Pokédex Nacional (1 al 1025). |
| `name` | `object` | Nombre oficial de la especie en inglés. |
| `type_1` | `object` | Tipo elemental principal de la criatura (Fuego, Agua, Dragón, etc.). |
| `hp` | `int64` | Puntos base de salud (*Hit Points*). |
| `attack` | `int64` | Puntos base de ataque físico. |
| `defense` | `int64` | Puntos base de defensa física. |
| `sp_attack` | `int64` | Puntos base de ataque especial. |
| `sp_defense` | `int64` | Puntos base de defensa especial. |
| `speed` | `int64` | Puntos base de velocidad de combate. |
| `base_stat_total` | `int64` | Puntuación total acumulada de las 6 estadísticas básicas. |
| `generation` | `int64` | Generación a la que pertenece la especie (1 a 9). |
| `is_legendary` | `bool` | Indicador booleano de si es un Pokémon legendario. |
| `is_mythical` | `bool` | Indicador booleano de si es un Pokémon singular/mítico. |
| `habitat` | `object` | Entorno biológico asignado oficialmente (bosque, mar, cueva, etc.). |
| `capture_rate` | `int64` | Coeficiente de dificultad de captura (de 3 a 255). |

---

## 3. Limpieza y Gestión de Datos

Para asegurar la calidad y consistencia de los análisis, se adoptaron tres decisiones metodológicas clave:

### 3.1. Reducción de dimensionalidad (16 columnas eliminadas)
El CSV original contaba con 31 columnas. Se descartaron 16 variables puramente cosméticas o prescindibles para las preguntas planteadas:
`type_2`, `height_m`, `weight_kg`, `base_experience`, `abilities`, `hidden_ability`, `is_baby`, `color`, `shape`, `egg_groups`, `growth_rate`, `base_happiness`, `genus`, `evolution_chain_id`, `flavor_text` y `sprite_url`.
> *Motivación*: Eliminar ruido analítico y optimizar el uso de memoria en Pandas.

### 3.2. Normalización de especies (1.025 especies base)
El archivo crudo contenía 1.350 filas debido a formas alternativas, megaevoluciones y formas regionales con identificadores superiores a 10.000 (ej. *Mega-Charizard*, *Deoxys-Attack*).
> *Motivación*: Se filtró estrictamente el rango `pokedex_number <= 1025`, garantizando que cada especie única esté representada exactamente una vez y evitando sesgos estadísticos de duplicidad.

### 3.3. Tratamiento de valores nulos (columna `habitat`)
La verificación con `df.isnull().sum()` demostró que todas las variables están completas al 100%, salvo `habitat`, que presenta **639 valores faltantes (`NaN`)**:
* **Contexto técnico e histórico**: El sistema de hábitats fue una función introducida exclusivamente en la 3ª Generación (*Pokémon Rojo Fuego y Verde Hoja* de Game Boy Advance, año 2004) para catalogar a los **386 Pokémon** existentes en esa época (Gen 1 a 3). A partir de la Generación 4 en adelante, la Pokédex oficial abandonó esta función.
* **Solución aplicada**: No se eliminaron las filas ni se imputaron valores sintéticos. Se aplicó un filtrado puntual mediante `dropna(subset=['habitat'])` únicamente en las Preguntas 1 y 2, manteniendo intactos los 1.025 Pokémon para el resto del estudio.

---

## 4. Análisis Exploratorio de Datos (EDA)

En el cuaderno `00_exploracion_inicial.ipynb` se procesaron las estadísticas descriptivas globales de las variables de combate para el total de 1.025 Pokémon:

| Métrica | HP | Attack | Defense | Sp. Atk | Sp. Def | Speed | BST Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Media (`mean`)** | 69.9 | 78.8 | 74.2 | 71.7 | 71.8 | 68.0 | **435.5** |
| **Desv. Est. (`std`)** | 26.1 | 32.1 | 30.7 | 32.3 | 27.7 | 29.3 | **120.9** |
| **Mínimo (`min`)** | 1.0 | 5.0 | 5.0 | 10.0 | 20.0 | 5.0 | **175.0** |
| **Mediana (`50%`)** | 68.0 | 75.0 | 70.0 | 65.0 | 70.0 | 65.0 | **450.0** |
| **Máximo (`max`)** | 255.0 | 190.0 | 250.0 | 194.0 | 250.0 | 200.0 | **720.0** |

### Observaciones clave
* **Fuerza media global**: La media de poder se sitúa en **435.5 puntos**, con una mediana de **450.0 puntos**, lo que demuestra una distribución bastante simétrica centrada en la evolución intermedia.
* **Rango de poder**: El valor mínimo es de **175 puntos** y el techo estándar lo marca Arceus con **720 puntos**.

---

## 5. Análisis en Profundidad: Resolución de las 5 Preguntas

A continuación se detalla la resolución técnica de cada una de las 5 preguntas planteadas, incluyendo metodología, tabla de resultados, gráfico generado e interpretación.

---

### 5.1. Pregunta 1: Pokémon más fuerte por hábitat

> **Pregunta:** *De cada hábitat, ¿cuál es el Pokémon con más puntos de estadística total (`base_stat_total`)?*

* **Cuaderno**: [`01_pokemon_mas_fuerte_por_habitat.ipynb`](01_pokemon_mas_fuerte_por_habitat.ipynb)
* **Metodología**: Filtrado de registros válidos de hábitat (386 filas), agrupamiento por `habitat` y extracción del índice máximo con `idxmax()` sobre `base_stat_total`.

#### Tabla de Resultados

| Hábitat | Pokémon Líder | Base Stat Total |
| :--- | :--- | :---: |
| 🥇 **rare** | **Rayquaza** | **680** |
| 🥈 **sea** | Kyogre | 670 |
| 🥈 **forest** | Slaking | 670 |
| 🥈 **rough-terrain** | Groudon | 670 |
| 🥉 **waters-edge** | Dragonite | 600 |
| 🥉 **mountain** | Tyranitar | 600 |
| **cave** | Regirock | 580 |
| **grassland** | Raikou | 580 |
| **urban** | Blissey | 540 |

#### Visualización
![Pokémon más Fuerte por Hábitat](graficos/pregunta_1.png)

#### Interpretación
* El líder absoluto resultante en el cuaderno es **Rayquaza** con **680 puntos** en el hábitat `rare`.
* Le siguen de forma destacada las deidades climáticas **Kyogre (670)** en el mar y **Groudon (670)** en terreno accidentado, junto al sorprendente **Slaking (670)** en bosque.
* *Nota analítica*: En el hábitat `rare` se produce un empate técnico exacto a 680 puntos entre **Rayquaza (#384)** y **Mewtwo (#150)**, situándose ambos en la cima absoluta de poder para especies con hábitat catalogado.

---

### 5.2. Pregunta 2: Hábitat con más puntos de fuerza

> **Pregunta:** *¿Cuál es el hábitat con más puntos de fuerza basándonos en los puntos de estadística?*

* **Cuaderno**: [`02_habitat_con_mas_fuerza.ipynb`](02_habitat_con_mas_fuerza.ipynb)
* **Metodología**: Agrupamiento por `habitat` evaluando tanto la media aritmética (`mean()`) como la suma total acumulada (`sum()`) de `base_stat_total`.

#### Tabla de Resultados

| Criterio de Evaluación | Hábitat Ganador | Puntos de Fuerza |
| :--- | :---: | :---: |
| **Por Media de Fuerza** | `rare` | **599.6 de media** |
| **Por Suma Total Acumulada** | `grassland` | **32.216 puntos totales** |

#### Visualización
![Puntos Totales de Fuerza por Hábitat](graficos/pregunta_2.png)

#### Interpretación
Se observa una clara divergencia según la métrica analizada:
1. **Por promedio individual**: El hábitat **`rare`** lidera de forma aplastante con **599.6 puntos de media**, debido a que está compuesto prácticamente en exclusiva por criaturas legendarias (Articuno, Zapdos, Moltres, Mewtwo, Rayquaza).
2. **Por volumen acumulado total**: El hábitat **`grassland`** (pradera) lidera el total absoluto acumulado con **32.216 puntos** debido a su alta concentración poblacional (80 especies catalogadas).

---

### 5.3. Pregunta 3: Tipo más fuerte de media

> **Pregunta:** *De cada tipo de Pokémon, ¿cuál es el tipo más fuerte de media (basándonos en los puntos de estadística)?*

* **Cuaderno**: [`03_tipo_mas_fuerte_de_media.ipynb`](03_tipo_mas_fuerte_de_media.ipynb)
* **Metodología**: Agrupamiento de las 1.025 especies por `type_1`, cálculo de media de `base_stat_total` redondeada a 1 decimal y representación de distribución completa mediante diagrama de caja (*Boxplot*).

#### Tabla de Resultados

| Posición / Categoría | Tipo Elemental | Media Base Stat Total |
| :---: | :--- | :---: |
| 🏆 **#1 Más fuerte** | **Dragon (Dragón)** | **490.2** |
| 🥈 **#2** | Steel (Acero) | 475.1 |
| 🥉 **#3** | Dark (Siniestro) | 454.7 |
| **#4** | Psychic (Psíquico) | 446.7 |
| **#5** | Fire (Fuego) | 446.2 |
| ... | ... | ... |
| **#17** | Normal | 399.8 |
| 📉 **#18 Más débil** | **Bug (Bicho)** | **374.6** |

#### Visualización
![Distribución de Fuerza Total por Tipo de Pokémon](graficos/pregunta_3.png)

#### Interpretación
* El tipo **Dragón** lidera holgadamente el juego con una media de **490.2 puntos**, seguido de **Acero (475.1)** y **Siniestro (454.7)**.
* En el extremo opuesto, el tipo **Bicho** presenta la media más baja de la franquicia (**374.6 puntos**), debido a que concentra multitud de especies de rutas iniciales con evoluciones muy tempranas y stats reducidos.
* El *Boxplot* evidencia que la caja intercuartílica de Dragón y Acero está claramente desplazada hacia arriba en comparación con el resto, reflejando su diseño deliberado como tipos de élite competitiva.

---

### 5.4. Pregunta 4: Pokémon no legendario más fuerte

> **Pregunta:** *De los Pokémon no legendarios ni míticos, ¿cuál es el más fuerte?*

* **Cuaderno**: [`04_no_legendarios_mas_fuertes.ipynb`](04_no_legendarios_mas_fuertes.ipynb)
* **Metodología**: Doble filtrado booleano (`is_legendary == False` y `is_mythical == False`), ordenación descendentemente por `base_stat_total` y categorización por escalones de poder.

#### Tabla de Resultados

| Posición | Pokémon | Tipo Principal | Base Stat Total |
| :---: | :--- | :---: | :---: |
| 🥇 **1º (Líder Absoluto)** | **Slaking** | Normal | **670** |
| 🥈 **2º (Empate a 600)** | Hydreigon | Siniestro | 600 |
| 🥈 **2º (Empate a 600)** | Kommo-o | Dragón | 600 |
| 🥈 **2º (Empate a 600)** | Goodra | Dragón | 600 |
| 🥈 **2º (Empate a 600)** | Baxcalibur | Dragón | 600 |

#### Visualización
![Escalones de Fuerza en Pokémon No Legendarios](graficos/pregunta_4.png)

#### Interpretación
* **Slaking** es el Pokémon no legendario más fuerte de la historia con **670 puntos base**, una cifra superior a la de la mayoría de criaturas legendarias estándar.
* **La paradoja de diseño**: Para compensar este descomunal poder numérico, Game Freak le otorgó la habilidad pasiva negativa **Ausente (*Truant*)**, que le impide ejecutar movimientos en turnos consecutivos.
* Inmediatamente por debajo se sitúan los denominados **pseudolegendarios** con exactamente **600 puntos** (Dragonite, Tyranitar, Salamence, Metagross, Garchomp, Hydreigon, Goodra, Kommo-o, Dragapult y Baxcalibur).

---

### 5.5. Pregunta 5: Legendarios con mayor ratio de captura

> **Pregunta:** *De los legendarios, ¿cuál es el Pokémon con más capture rate (más fácil de capturar)?*

* **Cuaderno**: [`05_legendarios_capture_rate.ipynb`](05_legendarios_capture_rate.ipynb)
* **Metodología**: Filtrado del subconjunto de Pokémon legendarios (`is_legendary == True`, 71 registros), análisis de frecuencias de `capture_rate` y ordenación descendente.

#### Tabla de Resultados

| Ratio de Captura (`capture_rate`) | Cantidad de Legendarios | Especies Representativas |
| :---: | :---: | :--- |
| **255 (Máximo posible)** | **3** | **Necrozma, Eternatus, Terapagos** |
| **45** | 7 | Rayquaza, Xerneas, Yveltal, Cosmog, Cosmoem, Solgaleo, Lunala |
| **10** | 2 | Zacian, Zamazenta |
| **6** | 4 | Wo-Chien, Chien-Pao, Ting-Lu, Chi-Yu |
| **5** | 1 | Ogerpon |
| **3 (Mínimo / Muy difícil)** | **54** | Articuno, Zapdos, Moltres, Mewtwo, Lugia, Ho-Oh, etc. |

#### Visualización
![Distribución de Capture Rate en Pokémon Legendarios](graficos/pregunta_5.png)

#### Interpretación
* **Necrozma**, **Eternatus** y **Terapagos** poseen un ratio de **255**, el valor máximo posible del algoritmo de captura (captura casi matemática con cualquier Pokéball estándar).
* **Justificación narrativa**: Estos tres legendarios forman parte obligatoria del clímax de la historia en sus respectivos títulos (Sol/Luna, Espada/Escudo y Escarlata/Púrpura); facilitar su captura al 100% evita que el jugador quede atascado en el avance cinemático del juego.
* Por el contrario, el **76% de los legendarios (54 especies)** mantienen el icónico ratio de **3**, exigiendo el uso de Ultra Balls, estados alterados o la Master Ball.

---

## 6. Conclusiones Generales

1. **Diseño paramétrico estructurado**: Los datos demuestran que las estadísticas de Pokémon responden a patrones de diseño industrial muy medidos: tipos elementales dominantes (Dragón, Acero) frente a tipos introductorios (Bicho, Normal), así como hábitats fuertemente correlacionados con la jerarquía de poder.
2. **Relevancia del preprocesamiento y limpieza**: La decisión de descartar megaevoluciones (> 10.000) y de gestionar selectivamente los 639 nulos de `habitat` evitó distorsiones graves que habrían arruinado las medias por tipo y hábitat.
3. **Equilibrio entre estadística y mecánicas jugables**: El caso de Slaking (670 BST pero limitado por *Truant*) y el de los legendarios con ratio de captura 255 demuestran que los números en un dataset deben interpretarse siempre en conjunto con las reglas del dominio de estudio.
4. **Validación del flujo de trabajo científico**: El uso combinado de Pandas para el tratamiento matricial, Seaborn/Matplotlib para la comunicación gráfica y Jupyter Notebooks para la reproducibilidad permitió estructurar una investigación rigurosa, reproducible y modular.

---

## 7. Estructura del Repositorio

```text
notebook-pokemon/
│
├── 00_exploracion_inicial.ipynb          # Cuaderno de carga, limpieza, gestión de nulos y EDA general
├── 01_pokemon_mas_fuerte_por_habitat.ipynb # Pregunta 1: Pokémon más fuerte por hábitat (Rayquaza / Mewtwo)
├── 02_habitat_con_mas_fuerza.ipynb       # Pregunta 2: Hábitat con más fuerza (media y suma total)
├── 03_tipo_mas_fuerte_de_media.ipynb     # Pregunta 3: Tipo elemental más fuerte de media (Boxplot)
├── 04_no_legendarios_mas_fuertes.ipynb   # Pregunta 4: Pokémon no legendario más fuerte (Slaking)
├── 05_legendarios_capture_rate.ipynb     # Pregunta 5: Legendarios con mayor ratio de captura
│
├── pokemon.csv                           # Dataset depurado y ordenado por Pokédex (1.025 filas x 15 columnas)
│
├── graficos/                             # Gráficos estadísticos exportados en alta resolución
│   ├── pregunta_1.png
│   ├── pregunta_2.png
│   ├── pregunta_3.png
│   ├── pregunta_4.png
│   └── pregunta_5.png
│
├── presentacion/                         # Presentación interactiva HTML/CSS/JS (9 diapositivas)
│   └── index.html
│
├── Memoria_Proyecto_Pokemon.docx         # Informe técnico en formato Microsoft Word (.docx)
└── README.md                             # Memoria técnica completa visible en la raíz de GitHub
```