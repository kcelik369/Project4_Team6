from flask import Flask, redirect, url_for, render_template, send_from_directory
import pandas as pd

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
# app.config['TEMPLATES_AUTO_RELOAD'] = True  # Optional: Auto-reload templates during development

# Root endpoint with links to api1, api2, and api3
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to redirect to Titanic ML Project Repository
@app.route('/endpoint1')
def endpoint1():
    return redirect("https://github.com/kcelik369/Project4_Team6")

# API endpoint to redirect to original kaggle dataset
@app.route('/endpoint2')
def endpoint2():
    return redirect("https://www.kaggle.com/competitions/titanic")

# API endpoint to redirect to jupyter notebook on Python
@app.route('/endpoint3')
def endpoint3():
    return redirect("https://github.com/kcelik369/Project4_Team6/blob/main/ModelEvaluation.ipynb")

# API endpoint to redirect to Titanic Data Visualization on Github
@app.route('/endpoint4')
def endpoint4():
    return redirect("https://public.tableau.com/app/profile/elizabeth.morgan4663/viz/Project4Team6-TitanicVisualizations/TitanicPassengerDataAnalysis")

# Serve static files like CSS, JS, and images
# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)