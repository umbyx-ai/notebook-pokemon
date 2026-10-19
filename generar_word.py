import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_report():
    doc = Document()

    # Configuración de márgenes estándar
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Paleta de colores
    COLOR_PRIMARY = RGBColor(229, 57, 53)    # Rojo Pokémon
    COLOR_SECONDARY = RGBColor(21, 101, 192) # Azul
    COLOR_GRAY = RGBColor(100, 100, 100)

    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    # ----------------- PORTADA -----------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(80)
    title_p.paragraph_format.space_after = Pt(12)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title_p.add_run('PROYECTO: ANÁLISIS DE DATOS POKÉMON')
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(24)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(130)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run('Memoria del proyecto de análisis de datos con Python, Pandas, Matplotlib y Seaborn')
    run_sub.font.name = 'Segoe UI'
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = COLOR_GRAY

    meta_p = doc.add_paragraph()
    meta_p.paragraph_format.space_after = Pt(6)
    meta_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = meta_p.add_run('Módulo: 0378 – Seguridad y Alta Disponibilidad\nProfesor: Josep Mª Ruiz Ríos\nAlumnos: [Nombre Alumno 1] & [Nombre Alumno 2]\nCiclo: 2º ASIX – Curso 2026/2027')
    r.font.name = 'Segoe UI'
    r.font.size = Pt(11)

    doc.add_page_break()

    # Funciones de utilidad para títulos y párrafos
    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(20)
        h.paragraph_format.space_after = Pt(8)
        run = h.add_run(text)
        run.font.name = 'Segoe UI'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = COLOR_PRIMARY
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
        run = h.add_run(text)
        run.font.name = 'Segoe UI'
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = COLOR_SECONDARY
        return h

    def add_p(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = 'Segoe UI'
        run.font.size = Pt(10.5)
        return p

    # ----------------- 1. INTRODUCCIÓN -----------------
    add_h1('1. Introducción y elección del tema')
    add_p('Este proyecto forma parte de la asignatura 0378 – Seguridad y Alta Disponibilidad en 2º de ASIX. El objetivo era trabajar en pareja utilizando Python, Jupyter Notebooks y librerías de análisis de datos (Pandas, NumPy, Matplotlib y Seaborn), subiendo todo el trabajo a un repositorio compartido en GitHub.')
    add_p('Escogimos este tema principalmente porque es una saga que nos gusta mucho a los dos y sobre la que ya teníamos bastante conocimiento previo. Al conocer bien los juegos, los tipos, las estadísticas y las mecánicas, sabíamos que podíamos plantear preguntas con sentido y entender fácilmente si los datos que nos devolvía el código eran correctos o si había algún error. Además, es un dataset muy completo para trabajar, ya que combina números (vida, ataque, defensa, velocidad...) con categorías (tipos, hábitats, generaciones).')
    add_p('Repartirnos las preguntas no tuvo ninguna complicación: lo echamos a suertes. A uno le tocó hacer la exploración inicial y las preguntas 1 y 3, y al otro las preguntas 2, 4 y 5. Para coordinarnos usamos GitHub Desktop, con el que ya habíamos trabajado anteriormente en otras prácticas, por lo que el flujo de hacer commits, pull y push fue cómodo y sin conflictos.')

    # ----------------- 2. DESCRIPCIÓN DEL DATASET -----------------
    add_h1('2. Descripción del Dataset')
    add_p('El archivo original procede de Kaggle (pokemon_complete.csv). Después de revisarlo y limpiarlo, generamos nuestro propio archivo definitivo: pokemon.csv, que contiene 1.025 filas (una por cada Pokémon de la Pokédex Nacional) y 15 columnas:')

    # Tabla variables
    table_vars = doc.add_table(rows=1, cols=3)
    table_vars.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table_vars.rows[0].cells
    hdr_cells[0].text = 'Columna'
    hdr_cells[1].text = 'Tipo de dato'
    hdr_cells[2].text = 'Descripción'
    for cell in hdr_cells:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    vars_data = [
        ('pokedex_number', 'int64', 'Número oficial en la Pokédex (del 1 al 1025).'),
        ('name', 'object', 'Nombre del Pokémon.'),
        ('type_1', 'object', 'Tipo principal del Pokémon (Fuego, Agua, Planta, Dragón...).'),
        ('hp', 'int64', 'Puntos de vida base.'),
        ('attack', 'int64', 'Puntos de ataque físico.'),
        ('defense', 'int64', 'Puntos de defensa física.'),
        ('sp_attack', 'int64', 'Puntos de ataque especial.'),
        ('sp_defense', 'int64', 'Puntos de defensa especial.'),
        ('speed', 'int64', 'Velocidad de combate.'),
        ('base_stat_total', 'int64', 'Suma de todas las estadísticas de combate anteriores.'),
        ('generation', 'int64', 'Generación en la que se introdujo (del 1 al 9).'),
        ('is_legendary', 'bool', 'Si es legendario (True o False).'),
        ('is_mythical', 'bool', 'Si es singular o mítico (True o False).'),
        ('habitat', 'object', 'Hábitat asignado (bosque, mar, cueva, etc.).'),
        ('capture_rate', 'int64', 'Facilidad de captura (cuanto más alto, más fácil).')
    ]

    for row_idx, data in enumerate(vars_data):
        row_cells = table_vars.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(9)

    # ----------------- 3. LIMPIEZA Y GESTIÓN DE DATOS -----------------
    add_h1('3. Limpieza y tratamiento de los datos')
    add_p('Antes de ponernos a responder las preguntas, revisamos el archivo y tomamos varias decisiones de limpieza:')
    add_h2('3.1. Eliminar columnas irrelevantes (de 31 a 15 columnas)')
    add_p('El dataset original venía con 31 columnas. Borramos directamente todas aquellas que no aportaban nada a las preguntas que íbamos a responder o que eran solo datos cosméticos, como las URLs de las imágenes (sprite_url), los textos de la Pokédex (flavor_text), las alturas, pesos, grupos de huevo o habilidades.')

    add_h2('3.2. Filtrar a las 1.025 especies base (de 1.350 a 1.025 filas)')
    add_p('El archivo original tenía 1.350 filas porque incluía megaevoluciones y formas regionales con números de Pokédex superiores a 10.000. Decidimos quedarnos únicamente con los 1.025 Pokémon oficiales de la Pokédex Nacional para que cada especie contara una sola vez y no falseara las medias de los tipos ni de los hábitats.')

    add_h2('3.3. El paréntesis sobre la columna habitat')
    add_p('Al revisar los valores nulos (df.isnull().sum()), vimos que la única columna con datos faltantes era habitat, con 639 nulos. Investigando el motivo, vimos que la función de hábitats solo existió oficialmente en los juegos de la 3ª Generación (Rojo Fuego y Verde Hoja para Game Boy Advance), donde se catalogaron los 386 Pokémon que existían en ese momento. A partir de la 4ª generación, Game Freak dejó de usar esta clasificación.')
    add_p('Como era un tema interesante para responder a las dos primeras preguntas, decidimos seguir adelante aunque no cubriera todo el dataset, haciendo un breve paréntesis explicativo y utilizando dropna(subset=["habitat"]) solo cuando analizamos los hábitats para no tener que descartar al resto de Pokémon en las demás preguntas.')

    # ----------------- 4. ANÁLISIS EXPLORATORIO (EDA) -----------------
    add_h1('4. Exploración inicial (EDA)')
    add_p('En el notebook 00_exploracion_inicial.ipynb cargamos el dataset y sacamos las estadísticas descriptivas generales de todos los Pokémon con .describe():')

    # Tabla describe
    table_desc = doc.add_table(rows=1, cols=8)
    table_desc.alignment = WD_TABLE_ALIGNMENT.CENTER
    desc_headers = ['Métrica', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'BST Total']
    for c_idx, h_text in enumerate(desc_headers):
        cell = table_desc.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, '1565C0')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9)

    desc_data = [
        ('Media', '69.9', '78.8', '74.2', '71.7', '71.8', '68.0', '435.5'),
        ('Desv. estándar', '26.1', '32.1', '30.7', '32.3', '27.7', '29.3', '120.9'),
        ('Mínimo', '1.0', '5.0', '5.0', '10.0', '20.0', '5.0', '175.0'),
        ('Mediana (50%)', '68.0', '75.0', '70.0', '65.0', '70.0', '65.0', '450.0'),
        ('Máximo', '255.0', '190.0', '250.0', '194.0', '250.0', '200.0', '720.0')
    ]

    for row_idx, data in enumerate(desc_data):
        row_cells = table_desc.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(8.5)

    add_p('Viendo la tabla, la media general de estadísticas de un Pokémon se queda en unos 435 puntos, con una mediana de 450. El mínimo del juego son 175 puntos y el máximo de esta lista base llega a 720 puntos (Arceus).')

    # ----------------- 5. PREGUNTAS DE INVESTIGACIÓN -----------------
    add_h1('5. Resolución de las 5 preguntas planteadas')
    add_p('A continuación explicamos cómo resolvimos cada pregunta en su respectivo notebook y los resultados obtenidos. Como conocemos la franquicia, la mayoría de conclusiones salieron tal y como nos esperábamos.')

    # --- 5.1 Pregunta 1 ---
    add_h2('5.1. Pregunta 1: Pokémon más fuerte por hábitat')
    add_p('Pregunta planteada: De cada hábitat, ¿cuál es el Pokémon con más puntos de estadística total (base_stat_total)? (Notebook: 01_pokemon_mas_fuerte_por_habitat.ipynb)')
    add_p('Para responderla, filtramos los Pokémon que sí tenían hábitat asignado, agrupamos por habitat y nos quedamos con el valor máximo de cada grupo mediante idxmax().')

    table_q1 = doc.add_table(rows=1, cols=3)
    table_q1.alignment = WD_TABLE_ALIGNMENT.CENTER
    q1_hdr = table_q1.rows[0].cells
    q1_hdr[0].text = 'Hábitat'
    q1_hdr[1].text = 'Pokémon más fuerte'
    q1_hdr[2].text = 'Base Stat Total'
    for cell in q1_hdr:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    q1_rows = [
        ('rare', 'Rayquaza', '680'),
        ('sea', 'Kyogre', '670'),
        ('forest', 'Slaking', '670'),
        ('rough-terrain', 'Groudon', '670'),
        ('waters-edge', 'Dragonite', '600'),
        ('mountain', 'Tyranitar', '600'),
        ('cave', 'Regirock', '580'),
        ('grassland', 'Raikou', '580'),
        ('urban', 'Blissey', '540')
    ]

    for row_idx, data in enumerate(q1_rows):
        row_cells = table_q1.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(9)

    add_p('')
    if os.path.exists('graficos/pregunta_1.png'):
        doc.add_picture('graficos/pregunta_1.png', width=Inches(5.8))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    add_p('Comentario de los resultados:')
    add_p('En el gráfico horizontal pusimos a cada Pokémon con un color representativo suyo. El más fuerte resultó ser Rayquaza con 680 puntos en el hábitat raro, seguido de Kyogre en el mar (670), Slaking en el bosque (670) y Groudon en terreno accidentado (670). Cabe mencionar que en el hábitat raro Mewtwo también tiene 680 puntos, empatando en la máxima puntuación.')

    # --- 5.2 Pregunta 2 ---
    add_h2('5.2. Pregunta 2: Hábitat con más puntos de fuerza')
    add_p('Pregunta planteada: ¿Cuál es el hábitat con más puntos de fuerza basándonos en los puntos de estadística? (Notebook: 02_habitat_con_mas_fuerza.ipynb)')
    add_p('Aquí analizamos dos cosas: qué hábitat tiene la media de fuerza más alta y cuál tiene más puntos sumando todos sus Pokémon.')

    table_q2 = doc.add_table(rows=1, cols=3)
    table_q2.alignment = WD_TABLE_ALIGNMENT.CENTER
    q2_hdr = table_q2.rows[0].cells
    q2_hdr[0].text = 'Criterio'
    q2_hdr[1].text = 'Hábitat ganador'
    q2_hdr[2].text = 'Puntuación'
    for cell in q2_hdr:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    q2_rows = [
        ('Por media de fuerza', 'rare', '599.6 puntos de media'),
        ('Por suma total de puntos', 'grassland', '32.216 puntos totales')
    ]
    for row_idx, data in enumerate(q2_rows):
        row_cells = table_q2.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(9)

    add_p('')
    if os.path.exists('graficos/pregunta_2.png'):
        doc.add_picture('graficos/pregunta_2.png', width=Inches(5.5))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    add_p('Comentario de los resultados:')
    add_p('Si miramos la media, el hábitat más fuerte es claramente rare con casi 600 puntos de media, lo cual es normal porque casi todos los que viven ahí son legendarios (Mewtwo, las aves legendarias, Rayquaza...). Pero si miramos la suma total acumulada, gana grassland (pradera) con más de 32.000 puntos porque es el hábitat donde más Pokémon hay metidos (80 especies).')

    # --- 5.3 Pregunta 3 ---
    add_h2('5.3. Pregunta 3: Tipo de Pokémon más fuerte de media')
    add_p('Pregunta planteada: De cada tipo de Pokémon, ¿cuál es el tipo más fuerte de media (basándonos en los puntos de estadística)? (Notebook: 03_tipo_mas_fuerte_de_media.ipynb)')
    add_p('Agrupamos los 1.025 Pokémon por su tipo principal (type_1), calculamos la media de cada uno y además hicimos un diagrama de caja (Boxplot) para ver cómo se reparten las estadísticas dentro de cada tipo.')

    table_q3 = doc.add_table(rows=1, cols=3)
    table_q3.alignment = WD_TABLE_ALIGNMENT.CENTER
    q3_hdr = table_q3.rows[0].cells
    q3_hdr[0].text = 'Posición'
    q3_hdr[1].text = 'Tipo'
    q3_hdr[2].text = 'Media Base Stat Total'
    for cell in q3_hdr:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    q3_rows = [
        ('1º', 'Dragon (Dragón)', '490.2'),
        ('2º', 'Steel (Acero)', '475.1'),
        ('3º', 'Dark (Siniestro)', '454.7'),
        ('4º', 'Psychic (Psíquico)', '446.7'),
        ('5º', 'Fire (Fuego)', '446.2'),
        ('17º', 'Normal', '399.8'),
        ('18º', 'Bug (Bicho)', '374.6')
    ]
    for row_idx, data in enumerate(q3_rows):
        row_cells = table_q3.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(9)

    add_p('')
    if os.path.exists('graficos/pregunta_3.png'):
        doc.add_picture('graficos/pregunta_3.png', width=Inches(6.0))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    add_p('Comentario de los resultados:')
    add_p('Como ya nos esperábamos, el tipo más fuerte de media es el Dragón (490.2), seguido de cerca por el tipo Acero (475.1). Son tipos pensados en el juego para ser poderosos y con muchos Pokémon finales y legendarios. En cambio, el tipo Bicho es el más débil de media (374.6) porque la mayoría son los primeros bichos que te encuentras al inicio de la aventura y evolucionan rápido pero con estadísticas bajas.')

    # --- 5.4 Pregunta 4 ---
    add_h2('5.4. Pregunta 4: Pokémon no legendario más fuerte')
    add_p('Pregunta planteada: De los Pokémon no legendarios ni míticos, ¿cuál es el más fuerte? (Notebook: 04_no_legendarios_mas_fuertes.ipynb)')
    add_p('Filtramos para quitar legendarios y míticos (is_legendary == False y is_mythical == False) y ordenamos de mayor a menor fuerza.')

    table_q4 = doc.add_table(rows=1, cols=4)
    table_q4.alignment = WD_TABLE_ALIGNMENT.CENTER
    q4_hdr = table_q4.rows[0].cells
    q4_hdr[0].text = 'Posición'
    q4_hdr[1].text = 'Pokémon'
    q4_hdr[2].text = 'Tipo'
    q4_hdr[3].text = 'Base Stat Total'
    for cell in q4_hdr:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    q4_rows = [
        ('1º', 'Slaking', 'Normal', '670'),
        ('2º (Empate a 600)', 'Hydreigon', 'Siniestro', '600'),
        ('2º (Empate a 600)', 'Kommo-o', 'Dragón', '600'),
        ('2º (Empate a 600)', 'Goodra', 'Dragón', '600'),
        ('2º (Empate a 600)', 'Baxcalibur', 'Dragón', '600')
    ]
    for row_idx, data in enumerate(q4_rows):
        row_cells = table_q4.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(9)

    add_p('')
    if os.path.exists('graficos/pregunta_4.png'):
        doc.add_picture('graficos/pregunta_4.png', width=Inches(5.6))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    add_p('Comentario de los resultados:')
    add_p('El Pokémon no legendario más fuerte de todos es Slaking con 670 puntos. Ya sabíamos que esto saldría así: Slaking tiene más estadísticas que muchos legendarios, pero el juego lo compensa dándole su habilidad obligatoria Ausente (Truant), que hace que pierda un turno de cada dos sin atacar. Justo detrás de él están los 11 "pseudolegendarios" habituales empatados con 600 puntos exactos (Dragonite, Tyranitar, Salamence, Garchomp...).')

    # --- 5.5 Pregunta 5 ---
    add_h2('5.5. Pregunta 5: Legendarios con mayor ratio de captura')
    add_p('Pregunta planteada: De los legendarios, ¿cuál es el Pokémon con más capture rate (más fácil de capturar)? (Notebook: 05_legendarios_capture_rate.ipynb)')
    add_p('Filtramos los 71 Pokémon legendarios del dataset y ordenamos por su ratio de captura (capture_rate).')

    table_q5 = doc.add_table(rows=1, cols=3)
    table_q5.alignment = WD_TABLE_ALIGNMENT.CENTER
    q5_hdr = table_q5.rows[0].cells
    q5_hdr[0].text = 'Capture Rate'
    q5_hdr[1].text = 'Cantidad de Legendarios'
    q5_hdr[2].text = 'Ejemplos'
    for cell in q5_hdr:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    q5_rows = [
        ('255 (Máximo posible)', '3', 'Necrozma, Eternatus, Terapagos'),
        ('45', '7', 'Rayquaza, Xerneas, Yveltal, Cosmog, Cosmoem, Solgaleo, Lunala'),
        ('10', '2', 'Zacian, Zamazenta'),
        ('6', '4', 'Wo-Chien, Chien-Pao, Ting-Lu, Chi-Yu'),
        ('5', '1', 'Ogerpon'),
        ('3 (Mínimo / Muy difícil)', '54', 'Mewtwo, Lugia, Ho-Oh, Articuno, Zapdos, etc.')
    ]
    for row_idx, data in enumerate(q5_rows):
        row_cells = table_q5.add_row().cells
        bg = 'F8F9FA' if row_idx % 2 == 0 else 'FFFFFF'
        for c_idx, text in enumerate(data):
            row_cells[c_idx].text = text
            set_cell_background(row_cells[c_idx], bg)
            for p in row_cells[c_idx].paragraphs:
                for r in p.runs:
                    r.font.name = 'Segoe UI'
                    r.font.size = Pt(9)

    add_p('')
    if os.path.exists('graficos/pregunta_5.png'):
        doc.add_picture('graficos/pregunta_5.png', width=Inches(5.4))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    add_p('Comentario de los resultados:')
    add_p('Los más fáciles son Necrozma, Eternatus y Terapagos con un ratio de 255 (el máximo del juego). Esto tiene una explicación muy sencilla que cualquier jugador conoce: son Pokémon que el juego te obliga a capturar como parte de la historia para poder avanzar, así que el ratio está puesto para que no se te escapen. En cambio, la gran mayoría (54 legendarios) tienen un ratio de 3, que es lo estándar para que atraparlos cueste bastante.')

    # ----------------- 6. CONCLUSIONES -----------------
    add_h1('6. Conclusiones')
    add_p('• Los datos respaldan lo que sabíamos del juego: Al conocer la franquicia de antemano, los resultados no nos han sorprendido, pero ha sido muy interesante comprobar con datos y gráficos reales cosas como la superioridad de los Dragones, la anomalía de Slaking o los ratios de captura según la historia.')
    add_p('• La importancia de limpiar el dataset: Pasar de 31 a 15 columnas y quitar las formas duplicadas con IDs raros nos facilitó mucho la vida a la hora de trabajar con los notebooks sin liarnos.')
    add_p('• Manejo de nulos: Descubrir por qué faltaban datos en habitat nos enseñó que antes de borrar nulos a lo loco hay que entender el motivo por el cual faltan esos datos en el dataset original.')
    add_p('• Trabajo en equipo con GitHub: Como ya habíamos utilizado Git y GitHub Desktop en otras prácticas, repartirnos el trabajo a suertes y sincronizar los notebooks no nos dio ningún problema.')

    output_path = 'Memoria_Proyecto_Pokemon.docx'
    try:
        doc.save(output_path)
        print(f'Documento Word generado exitosamente: {output_path}')
    except PermissionError:
        fallback_path = 'Memoria_Proyecto_Pokemon_v2.docx'
        doc.save(fallback_path)
        print(f'Memoria_Proyecto_Pokemon.docx esta abierto en Word. Se ha guardado como: {fallback_path}')

if __name__ == '__main__':
    create_report()
