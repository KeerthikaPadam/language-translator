# Language Translator with File Translation

This is a simple **Language Translator** application built with **Python** using the **Tkinter** library for the graphical user interface (GUI) and **Google Translate API** for translating text and files. The application can automatically detect the language of the input text and translate it into a selected target language. Additionally, it supports translating text files by reading their content and then performing the translation.

## Features

- **Text Translation**: Translate text from one language to another.
- **File Translation**: Upload and translate the content of `.txt` files.
- **Language Detection**: Automatically detects the language of the input text.
- **Multiple Languages**: Supports translation between over 100 languages, including popular languages like English, Spanish, French, Chinese, and more.
- **Interactive GUI**: A user-friendly interface built with Tkinter for easy translation.

## Prerequisites

- Python 3.x
- `googletrans` library (Python wrapper for Google Translate API)
- Tkinter (comes pre-installed with Python)

## Installation

1. **Clone the repository** or download the script:
   ```bash
   git clone https://github.com/KeerthikaPadam/language-translator.git
   cd language-translator
   ```

2. **Install dependencies**:
   - Install `googletrans`:
     ```bash
     pip install googletrans==4.0.0-rc1
     ```

   - Tkinter is usually included with Python, but if it's not installed, you can install it based on your operating system.

## Usage

1. **Run the application**:
   - To start the Language Translator, open a terminal and navigate to the directory where the script is located.
   - Run the script:
     ```bash
     python file_language_translator.py
     ```

2. **Text Translation**:
   - Enter the text you want to translate in the **"Enter Text"** area.
   - Select the source language (automatically detected) and the target language from the dropdown menus.
   - Click the **"Translate"** button to see the translated text in the output area.

3. **File Translation**:
   - Click the **"Translate File"** button.
   - A file dialog will open. Select a `.txt` file to upload.
   - The application will read the file's content, detect the language, and translate it into the selected target language.
   - The translated text will appear in the output area.

## Example

- **Text Translation**:
  - Input text: "Hello, how are you?"
  - Source language: Automatically detected (English)
  - Target language: Spanish
  - Translated text: "Hola, ¿cómo estás?"

- **File Translation**:
  - Input file: A text file containing "Hello, world!"
  - Source language: Automatically detected (English)
  - Target language: French
  - Translated text: "Bonjour le monde!"

## Supported Languages

The application supports over 100 languages. Here are some of the most common:

- English
- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Hindi
- Arabic
- Chinese
- Japanese
- Korean
- Turkish
- Dutch
- Swedish
- Polish
- Czech
- Danish
- And many more...

For a full list of supported languages, refer to the [Google Translate API documentation](https://cloud.google.com/translate/docs).

## Troubleshooting

- **File Format**: The application currently supports `.txt` files. Other formats such as `.pdf` or `.docx` are not supported.
- **Language Detection Issues**: The application automatically detects the language of the input text. If the detection isn't accurate, you may manually set the source language in the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Translate API**: The translation feature uses the `googletrans` Python library, which is a wrapper for the Google Translate API.
- **Tkinter**: Tkinter is used to create the graphical user interface (GUI) for this application.
