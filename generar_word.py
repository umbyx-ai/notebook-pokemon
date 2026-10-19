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
    run_title = title_p.add_run('PROYECTO: ANÁLISIS DE UN CONJUNTO DE DATOS\nUNIVERSO POKÉMON')
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(24)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(130)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run('Memoria técnica del análisis exploratorio y resolución de preguntas de investigación mediante Python y Pandas')
    run_sub.font.name = 'Segoe UI'
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = COLOR_GRAY

    meta_p = doc.add_paragraph()
    meta_p.paragraph_format.space_after = Pt(6)
    meta_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = meta_p.add_run('Módulo: 0378 – Seguridad y Alta Disponibilidad (Tema 1: Alta Disponibilidad)\nProfesor: Josep Mª Ruiz Ríos\nAlumnos: [Nombre Alumno 1] & [Nombre Alumno 2]\nCiclo: ASIX 2 – Curso 2026/2027')
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
    add_h1('1. Introducción')
    add_p('El presente proyecto se enmarca dentro del módulo formativo 0378 – Seguridad y Alta Disponibilidad del ciclo de grado superior de Administración de Sistemas Informáticos en Red (ASIX2). El objetivo principal de la práctica consiste en aplicar metodologías de análisis y tratamiento masivo de datos mediante el lenguaje de programación Python y su ecosistema científico, adquiriendo competencias en inspección, limpieza, análisis descriptivo y visualización.')
    add_p('Como conjunto de datos de trabajo se ha seleccionado el universo de Pokémon. Este dataset resulta especialmente idóneo para un proyecto de analítica avanzada debido a la rica variedad de variables categóricas (tipos elementales, hábitats, generaciones) y numéricas continuas/discretas (estadísticas base de salud, ataque, defensa, velocidad y ratios de captura).')
    add_p('El entorno tecnológico configurado para el desarrollo integral del proyecto comprende:')
    add_p('• Python 3.14 como lenguaje de programación base.\n• Librerías Pandas y NumPy para la manipulación y álgebra matricial de datos.\n• Librerías Matplotlib y Seaborn para la generación de gráficos estáticos de alta calidad.\n• Jupyter Notebook como interfaz de programación interactiva y cuaderno de trabajo.\n• Git y GitHub Desktop como sistema de control de versiones y repositorio colaborativo en pareja.')

    # ----------------- 2. DESCRIPCIÓN DEL DATASET -----------------
    add_h1('2. Descripción del Dataset')
    add_p('El conjunto de datos original procede de la consolidación de información extraída de la PokéAPI y repositorios de Kaggle (pokemon_complete.csv). Tras el proceso de auditoría y depuración técnica, se ha consolidado un archivo definitivo denominado pokemon.csv.')
    add_p('El dataset consolidado presenta una estructura homogénea con 1.025 registros (cada uno correspondiente a una especie única de la Pokédex Nacional) y 15 variables de estudio:')

    # Tabla variables
    table_vars = doc.add_table(rows=1, cols=3)
    table_vars.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table_vars.rows[0].cells
    hdr_cells[0].text = 'Columna'
    hdr_cells[1].text = 'Tipo'
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
        ('pokedex_number', 'int64', 'Identificador numérico oficial en la Pokédex Nacional (1 a 1025).'),
        ('name', 'object', 'Nombre oficial de la especie en inglés.'),
        ('type_1', 'object', 'Tipo elemental principal del Pokémon (Fuego, Agua, Planta, etc.).'),
        ('hp', 'int64', 'Puntos base de salud (Hit Points).'),
        ('attack', 'int64', 'Puntos base de ataque físico.'),
        ('defense', 'int64', 'Puntos base de defensa física.'),
        ('sp_attack', 'int64', 'Puntos base de ataque especial.'),
        ('sp_defense', 'int64', 'Puntos base de defensa especial.'),
        ('speed', 'int64', 'Puntos base de velocidad de combate.'),
        ('base_stat_total', 'int64', 'Suma acumulada de las 6 estadísticas básicas de combate.'),
        ('generation', 'int64', 'Número entero de generación a la que pertenece (1 a 9).'),
        ('is_legendary', 'bool', 'Valor booleano que indica si el Pokémon es legendario (True/False).'),
        ('is_mythical', 'bool', 'Valor booleano que indica si el Pokémon es singular/mítico (True/False).'),
        ('habitat', 'object', 'Entorno ecológico asignado oficialmente (bosque, mar, cueva, etc.).'),
        ('capture_rate', 'int64', 'Ratio numérico de dificultad de captura (3 = mínimo, 255 = máximo).')
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
    add_h1('3. Limpieza y Gestión de Datos')
    add_p('Antes de proceder a la analítica, se aplicaron criterios metodológicos de calidad de datos:')
    add_h2('3.1. Reducción de dimensionalidad (16 columnas eliminadas)')
    add_p('El archivo sin depurar contenía 31 columnas. Se eliminaron 16 variables redundantes o puramente estéticas: sprites (sprite_url), textos de ambientación (flavor_text), medidas corporales (height_m, weight_kg), cadenas de evolución y habilidades de combate. Estas variables introducían ruido y consumo de memoria innecesario para los objetivos del proyecto.')

    add_h2('3.2. Normalización de especies (1.025 registros)')
    add_p('El archivo inicial contenía 1.350 filas debido a la inclusión de megaevoluciones, formas regionales (Alola, Galar, Hisui) y transformaciones temporales con numeraciones superiores a 10.000. Se procedió a filtrar estrictamente los números de Pokédex del 1 al 1.025. Esta decisión garantiza que cada especie esté representada una única vez, evitando sesgos que falsearían los análisis por tipo y hábitat.')

    add_h2('3.3. Tratamiento de valores nulos (columna habitat)')
    add_p('La auditoría de valores nulos reveló que todas las variables están completas al 100%, con la única excepción de la columna habitat, que presenta 639 valores faltantes (NaN).')
    add_p('Explicación técnica e histórica: La categorización por hábitats fue una funcionalidad introducida exclusivamente por Game Freak en la 3ª Generación (juegos Rojo Fuego y Verde Hoja de Game Boy Advance), en la que se clasificó exactamente a los 386 Pokémon existentes en ese momento (Generaciones 1 a 3). En las generaciones posteriores (4 a 9) la mecánica fue abandonada en la Pokédex oficial.')
    add_p('Solución aplicada: En lugar de imputar datos inventados o eliminar a los 639 Pokémon del dataset general, se implementó un filtrado selectivo mediante df.dropna(subset=["habitat"]) exclusivamente al abordar las Preguntas 1 y 2.')

    # ----------------- 4. ANÁLISIS EXPLORATORIO (EDA) -----------------
    add_h1('4. Análisis Exploratorio de Datos (EDA)')
    add_p('En el cuaderno 00_exploracion_inicial.ipynb se calcularon las estadísticas descriptivas de las variables cuantitativas de combate para los 1.025 Pokémon:')

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
        ('Media (mean)', '69.9', '78.8', '74.2', '71.7', '71.8', '68.0', '435.5'),
        ('Desv. Est. (std)', '26.1', '32.1', '30.7', '32.3', '27.7', '29.3', '120.9'),
        ('Mínimo (min)', '1.0', '5.0', '5.0', '10.0', '20.0', '5.0', '175.0'),
        ('Mediana (50%)', '68.0', '75.0', '70.0', '65.0', '70.0', '65.0', '450.0'),
        ('Máximo (max)', '255.0', '190.0', '250.0', '194.0', '250.0', '200.0', '720.0')
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

    add_p('Observaciones clave:')
    add_p('• La media global de fuerza (Base Stat Total) se sitúa en 435.5 puntos, con una mediana de 450.0 puntos.')
    add_p('• El Pokémon con menores estadísticas base registra 175 puntos, mientras que el techo estadístico estándar lo marca Arceus con 720 puntos.')

    # ----------------- 5. PREGUNTAS DE INVESTIGACIÓN -----------------
    add_h1('5. Análisis en Profundidad: Resolución de Preguntas')

    # --- 5.1 Pregunta 1 ---
    add_h2('5.1. Pregunta 1: Pokémon más fuerte por hábitat')
    add_p('Pregunta planteada: De cada hábitat, ¿cuál es el Pokémon con más puntos de estadística total (base_stat_total)?')
    add_p('Metodología: Se filtraron los Pokémon que tienen hábitat asignado (386 registros), se agruparon por la columna habitat y mediante idxmax() se obtuvo la fila correspondiente al valor máximo de base_stat_total en cada grupo. Por último, se ordenaron los resultados de forma descendente.')

    # Tabla exacta del notebook 01
    table_q1 = doc.add_table(rows=1, cols=3)
    table_q1.alignment = WD_TABLE_ALIGNMENT.CENTER
    q1_hdr = table_q1.rows[0].cells
    q1_hdr[0].text = 'Hábitat'
    q1_hdr[1].text = 'Pokémon'
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

    add_p('Análisis e interpretación del resultado:')
    add_p('El Pokémon líder absoluto resultante es Rayquaza con 680 puntos de estadística total en el hábitat "rare". Le siguen de cerca Kyogre (670 puntos en mar), Slaking (670 puntos en bosque) y Groudon (670 puntos en terreno accidentado).')
    add_p('Nota analítica sobre el dataset: En el hábitat "rare" existe un empate técnico a 680 puntos entre Rayquaza (#384) y Mewtwo (#150), destacando ambos como las cúspides de poder entre los Pokémon con hábitat catalogado en el juego.')

    # --- 5.2 Pregunta 2 ---
    add_h2('5.2. Pregunta 2: Hábitat con más puntos de fuerza')
    add_p('Pregunta planteada: ¿Cuál es el hábitat con más puntos de fuerza basándonos en los puntos de estadística?')
    add_p('Metodología: Se agruparon los Pokémon por habitat y se evaluó tanto la media de fuerza (mean()) como la suma total acumulada (sum()).')

    table_q2 = doc.add_table(rows=1, cols=3)
    table_q2.alignment = WD_TABLE_ALIGNMENT.CENTER
    q2_hdr = table_q2.rows[0].cells
    q2_hdr[0].text = 'Criterio de Evaluación'
    q2_hdr[1].text = 'Hábitat Ganador'
    q2_hdr[2].text = 'Puntos de Fuerza'
    for cell in q2_hdr:
        set_cell_background(cell, 'E53935')
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.name = 'Segoe UI'
                r.font.size = Pt(9.5)

    q2_rows = [
        ('Por Media de Fuerza', 'rare', '599.6 de media'),
        ('Por Suma Total Acumulada', 'grassland', '32.216 puntos totales')
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

    add_p('Análisis e interpretación:')
    add_p('Se evidencia una clara dualidad según la métrica empleada:')
    add_p('• Por promedio individual: El hábitat "rare" es el más fuerte de media (599.6 puntos), al concentrar casi exclusivamente a Pokémon legendarios y singulares.')
    add_p('• Por volumen total acumulado: El hábitat "grassland" (pradera) domina la suma global con 32.216 puntos gracias a su gran abundancia de especies (80 Pokémon).')

    # --- 5.3 Pregunta 3 ---
    add_h2('5.3. Pregunta 3: Tipo más fuerte de media')
    add_p('Pregunta planteada: De cada tipo de Pokémon, ¿cuál es el tipo más fuerte de media (basándonos en los puntos de estadística)?')
    add_p('Metodología: Se agruparon las 1.025 especies por su tipo principal (type_1), calculando la media de base_stat_total redondeada a 1 decimal y graficando la dispersión mediante un Boxplot.')

    table_q3 = doc.add_table(rows=1, cols=3)
    table_q3.alignment = WD_TABLE_ALIGNMENT.CENTER
    q3_hdr = table_q3.rows[0].cells
    q3_hdr[0].text = 'Posición / Categoría'
    q3_hdr[1].text = 'Tipo Elemental'
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
        ('#1 Más fuerte', 'Dragon (Dragón)', '490.2'),
        ('#2', 'Steel (Acero)', '475.1'),
        ('#3', 'Dark (Siniestro)', '454.7'),
        ('#4', 'Psychic (Psíquico)', '446.7'),
        ('#5', 'Fire (Fuego)', '446.2'),
        ('#17', 'Normal', '399.8'),
        ('#18 Más débil', 'Bug (Bicho)', '374.6')
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

    add_p('Análisis del Boxplot: El tipo Dragón encabeza el juego con 490.2 puntos de media, seguido de Acero (475.1) y Siniestro (454.7). En el extremo opuesto, el tipo Bicho presenta la media más baja con 374.6 puntos.')

    # --- 5.4 Pregunta 4 ---
    add_h2('5.4. Pregunta 4: Pokémon no legendario más fuerte')
    add_p('Pregunta planteada: De los Pokémon no legendarios ni míticos, ¿cuál es el más fuerte?')
    add_p('Metodología: Se filtraron las especies con is_legendary == False y is_mythical == False, ordenando descendentemente por base_stat_total y agrupando por escalones de fuerza.')

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
        ('1º (Líder Absoluto)', 'Slaking', 'Normal', '670'),
        ('2º (Empate a 600)', 'Hydreigon', 'Dark', '600'),
        ('2º (Empate a 600)', 'Kommo-O', 'Dragon', '600'),
        ('2º (Empate a 600)', 'Goodra', 'Dragon', '600'),
        ('2º (Empate a 600)', 'Baxcalibur', 'Dragon', '600')
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

    add_p('Análisis e interpretación: Slaking es el no-legendario más fuerte con 670 puntos base. En el escalón inmediatamente inferior se sitúan 11 Pokémon con exactamente 600 puntos (los conocidos como "pseudolegendarios", incluyendo a Dragonite, Tyranitar, Salamence, Metagross, Garchomp, Hydreigon, Goodra, Kommo-O, Dragapult y Baxcalibur).')
    add_p('Curiosidad de diseño: Slaking supera en estadísticas a leyendas como Kyogre o Groudon en estado base, pero los desarrolladores le asignaron la habilidad pasiva Ausente (Truant) para forzarlo a holgazanear un turno de cada dos.')

    # --- 5.5 Pregunta 5 ---
    add_h2('5.5. Pregunta 5: Legendarios con mayor ratio de captura')
    add_p('Pregunta planteada: De los legendarios, ¿cuál es el Pokémon con más capture rate (más fácil de capturar)?')
    add_p('Metodología: Se seleccionaron los 71 Pokémon legendarios (is_legendary == True), ordenando por capture_rate descendentemente.')

    table_q5 = doc.add_table(rows=1, cols=3)
    table_q5.alignment = WD_TABLE_ALIGNMENT.CENTER
    q5_hdr = table_q5.rows[0].cells
    q5_hdr[0].text = 'Capture Rate'
    q5_hdr[1].text = 'Cantidad'
    q5_hdr[2].text = 'Pokémon Legendarios Representativos'
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
        ('3 (Mínimo / Muy difícil)', '54', 'Articuno, Zapdos, Moltres, Mewtwo, Lugia, Ho-Oh, etc.')
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

    add_p('Análisis e interpretación: Necrozma, Eternatus y Terapagos son los legendarios más fáciles de capturar con un ratio de 255 (captura prácticamente automática). Esto responde a motivos narrativos del juego: su captura es un evento indispensable para completar la historia principal, a diferencia de los 54 legendarios clásicos que mantienen un restrictivo ratio de 3.')

    # ----------------- 6. CONCLUSIONES -----------------
    add_h1('6. Conclusiones')
    add_p('El desarrollo de este proyecto ha permitido extraer conclusiones de valor tanto en el ámbito analítico como en el metodológico:')
    add_p('1. Evidencia de diseño paramétrico: Los datos confirman que las estadísticas de Pokémon no se distribuyen al azar; responden a arquetipos deliberados donde los hábitats aislados y los tipos Dragón y Acero están sobrerrepresentados en la parte alta de la distribución.')
    add_p('2. Detección y resolución de sesgos: La depuración de megaevoluciones (filas > 10.000) y el tratamiento riguroso de los 639 nulos de hábitat evitaron distorsiones estadísticas que habrían invalidado las conclusiones.')
    add_p('3. Complementariedad de herramientas: La combinación de Pandas para el filtrado tabular con Seaborn/Matplotlib para la visualización ha permitido transformar tablas numéricas densas en respuestas directas y visuales.')
    add_p('4. Eficacia del flujo de trabajo en equipo: La partición modular de preguntas en cuadernos Jupyter independientes y la sincronización con Git/GitHub Desktop facilitó la resolución simultánea del proyecto sin colisiones de código.')

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
