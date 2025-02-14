# Flask Web Application

This project is a Flask web application that enables navigation between different pages, including a home page, FAQ page, and contact page. The application utilizes a structured template system for consistent design and layout.

## Project Structure

```
flask-app
├── app
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── assets
│   │       └── favicon.ico
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── faq.html
│   │   └── contact.html
│   ├── __init__.py
│   └── routes.py
├── venv
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```
   flask run
   ```

## Usage

- Navigate to `http://127.0.0.1:5000/` to access the home page.
- Use the navigation links to access the FAQ and contact pages.

## Dependencies

- Flask
- Any other libraries specified in `requirements.txt`.

## License

This project is licensed under the MIT License.