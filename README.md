# Text Translation Application

This project is a web-based text translation application that utilizes a pre-trained model for bidirectional translation. Users can select languages and input text to receive translations.

## Project Structure

```
text-translation-app
├── src
│   ├── app.py                # Entry point of the application
│   ├── model
│   │   └── translator.py     # Contains the Translator class for translation
│   ├── web
│   │   ├── routes.py         # Defines web routes for the application
│   │   ├── templates
│   │   │   └── index.html    # HTML template for the main web page
│   │   └── static
│   │       └── style.css     # CSS styles for the web application
│   └── utils
│       └── languages.py      # Contains supported languages and utility functions
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd text-translation-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python src/app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- Select the source and target languages from the dropdown menus.
- Enter the text you wish to translate in the provided text area.
- Click the "Translate" button to receive the translated text.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.