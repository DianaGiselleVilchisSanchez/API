document.addEventListener('DOMContentLoaded', () => {
    const notebookContent = document.getElementById('notebook-content');

    // Función para ejecutar un notebook según su id
    function executeNotebook(id) {
        fetch(`/notebook/${id}`)
            .then(response => response.text())  // Cambiado a .text() para recibir HTML
            .then(data => {
                notebookContent.innerHTML = data;
            })
            .catch(err => console.error('Error:', err));
    }

    // Asignamos la función a cada botón en el HTML
    const buttons = document.querySelectorAll('button');
    buttons.forEach((button, index) => {
        button.addEventListener('click', () => executeNotebook(index + 1));  // +1 porque el ID empieza desde 1
    });
});
