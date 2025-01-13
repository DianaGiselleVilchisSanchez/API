from flask import Flask, render_template
import nbformat
from nbconvert import HTMLExporter
import os

app = Flask(__name__)

# Directorio de notebooks
NOTEBOOKS_PATH = './notebooks'


def convert_notebook_to_html(notebook_path):
    """
    Convierte un archivo .ipynb a HTML, manteniendo las salidas (gráficos incluidos).
    """
    if not os.path.exists(notebook_path):
        return "<h1>Error: Notebook no encontrado</h1>"

    try:
        with open(notebook_path, 'r', encoding='utf-8') as nb_file:
            notebook_content = nbformat.read(nb_file, as_version=4)

        html_exporter = HTMLExporter()
        html_exporter.exclude_input = True  # Excluir entradas, incluir salidas (gráficas)
        html_exporter.template_name = 'classic'
        body, _ = html_exporter.from_notebook_node(notebook_content)
        return body
    except Exception as e:
        return f"<h1>Error al cargar el notebook: {str(e)}</h1>"


@app.route('/')
def index():
    """
    Página principal que lista las opciones disponibles.
    """
    return render_template('index.html')


@app.route('/notebook/<int:notebook_id>')
def show_notebook(notebook_id):
    """
    Muestra un notebook específico según su ID.
    """
    notebooks = {
        1: '3501_Regresion_Lineal.ipynb',
        2: '3501_Regresion_Logistica.ipynb',
        3: '3501_Preparacion-del-DataSet.ipynb',
        4: '3501_Visualizacion-de-datos.ipynb',
        5: '3501_Creacion-de-transformadores-y-pipelines-personalizados.ipynb',
        6: '3501_Evaluacion-de-Resultados.ipynb',
        7: '3501_Support-Vector-Machine.ipynb',
        8: '3501_Arboles-De-Decision.ipynb'
    }

    # Validar que el notebook_id sea válido
    notebook_name = notebooks.get(notebook_id)
    if not notebook_name:
        return "<h1>Error: Notebook no encontrado</h1>"

    notebook_path = os.path.join(NOTEBOOKS_PATH, notebook_name)
    return convert_notebook_to_html(notebook_path)


if __name__ == '__main__':
    # Usar el puerto dinámico asignado por Render, por defecto 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
