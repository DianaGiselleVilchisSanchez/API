from flask import Flask, render_template
import nbformat
from nbconvert import HTMLExporter
import os

app = Flask(__name__)

NOTEBOOKS_PATH = './notebooks'

def convert_notebook_to_html(notebook_path):
    """Convierte un archivo .ipynb a HTML, manteniendo las salidas (gráficos incluidos)."""
    with open(notebook_path, 'r', encoding='utf-8') as nb_file:
        notebook_content = nbformat.read(nb_file, as_version=4)

    html_exporter = HTMLExporter()
    html_exporter.exclude_input = True # Asegura incluir salidas de las celdas (gráficas)
    html_exporter.template_name = 'classic'  # Usar un template que soporte gráficos
    body, _ = html_exporter.from_notebook_node(notebook_content)
    return body

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notebook/1')
def regression_linear():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Regresion_Lineal.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

@app.route('/notebook/2')
def regression_logistic():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Regresion_Logistica.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

@app.route('/notebook/3')
def dataset_preparation():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Preparacion-del-DataSet.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

@app.route('/notebook/4')
def data_visualization():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Visualizacion-de-datos.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

@app.route('/notebook/5')
def transformers_and_pipelines():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Creacion-de-transformadores-y-pipelines-personalizados.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

@app.route('/notebook/6')
def results_evaluation():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Evaluacion-de-Resultados.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content


@app.route('/notebook/7')
def new_notebook():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Support-Vector-Machine.ipynb') 
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

@app.route('/notebook/8')
def results_evaluation():
    notebook_path = os.path.join(NOTEBOOKS_PATH, '3501_Arboles.ipynb')
    try:
        html_content = convert_notebook_to_html(notebook_path)
    except Exception as e:
        return f"Error al cargar el notebook: {str(e)}"
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
