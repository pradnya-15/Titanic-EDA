
import nbformat
from nbconvert import HTMLExporter

# Read the Jupyter Notebook
notebook_file = "Titanic_EDA.ipynb"

with open(notebook_file, "r", encoding="utf-8") as file:
    notebook = nbformat.read(file, as_version=4)

# Convert notebook to HTML
html_exporter = HTMLExporter()

html_data, resources = html_exporter.from_notebook_node(notebook)

# Save HTML file
with open("Titanic_EDA.html", "w", encoding="utf-8") as file:
    file.write(html_data)

print("HTML exported successfully!")
print("File created: Titanic_EDA.html")
