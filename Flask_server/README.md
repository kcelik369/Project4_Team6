# Serving Static Files in Flask

Serving static files in Flask involves making sure that your CSS, JavaScript, images, and other static assets are accessible to your web application. Flask provides a convenient way to serve these files using its `static` folder. Here's how you can serve static files in Flask:

## Directory Structure

First, ensure that you have a directory structure similar to the following:

```
├── app.py
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── script.js
│   └── images
│       └── logo.png
└── templates
    └── index.html
```

- `app.py`: Your Flask application file.
- `static`: Folder containing static assets like CSS, JavaScript, and images.
- `templates`: Folder containing your HTML templates.

## Linking Static Files in HTML Templates

In your HTML templates (e.g., `index.html`), use Flask's `url_for` function to generate URLs for static files. This ensures that Flask can correctly handle static file paths, even if your application's URL structure changes.

For example, to link a CSS file located in `static/css/style.css`, you would write:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

Similarly, for JavaScript files in `static/js/script.js`:

```html
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

And for images like `logo.png` in `static/images/logo.png`:

```html
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

## Configuring Static Folder in Flask

In your Flask application (`app.py`), you need to configure Flask to use the `static` folder for serving static files. By default, Flask looks for static files in a folder named `static` in the root directory of your application.

You don't need to explicitly define the static route; Flask handles it internally. However, make sure you don't create routes with the same names as your static folders or files to avoid conflicts.

Here's a minimal example of how you might configure your Flask application to serve static files:

```python
from flask import Flask, render_template

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Run Your Flask Application

Start your Flask application using `python app.py` in your terminal. Flask will automatically serve static files from the `static` folder when referenced in your HTML templates using `url_for`.

When you access your Flask application in a web browser, the static files will be loaded correctly and applied to your web pages.

By following these steps, you can ensure that static files like CSS, JavaScript, images, etc., are properly served and integrated into your Flask web application.

---

## Reference:
https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
