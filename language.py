import tkinter as tk
from tkinter import messagebox, filedialog
from googletrans import Translator

# Function to perform translation
def translate_text():
    try:
        # Get the input text and target language
        text = entry_input.get("1.0", "end-1c")
        target_language = lang_to.get()

        # Initialize the Translator
        translator = Translator()

        # Detect the source language automatically
        detected_language = translator.detect(text).lang

        # Perform translation from detected language to the selected target language
        translated = translator.translate(text, src=detected_language, dest=target_language)

        # Display the translated text and detected language
        entry_output.delete("1.0", "end")
        entry_output.insert("1.0", f"Detected Language: {detected_language}\n\nTranslated Text:\n{translated.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open and translate file content
def open_and_translate_file():
    try:
        # Ask user to select a file
        file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        
        if file_path:
            # Open and read the content of the file
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()

            # Detect language and translate
            translator = Translator()
            detected_language = translator.detect(file_content).lang
            target_language = lang_to.get()

            translated = translator.translate(file_content, src=detected_language, dest=target_language)

            # Display the translated text
            entry_output.delete("1.0", "end")
            entry_output.insert("1.0", f"Detected Language: {detected_language}\n\nTranslated Text:\n{translated.text}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while translating the file: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x600")

# Add title label
label_title = tk.Label(root, text="Language Translator", font=("Arial", 20))
label_title.pack(pady=20)

# Create input text area
label_input = tk.Label(root, text="Enter Text or Translate File:")
label_input.pack()

entry_input = tk.Text(root, height=5, wrap="word")
entry_input.pack(pady=10)

# List of more than 100 languages with their full names (alphabetically sorted)
languages = {
    "en": "English", "es": "Spanish", "fr": "French", "de": "German", "it": "Italian", "pt": "Portuguese",
    "ru": "Russian", "hi": "Hindi", "ar": "Arabic", "zh": "Chinese", "ja": "Japanese", "ko": "Korean",
    "tr": "Turkish", "nl": "Dutch", "sv": "Swedish", "pl": "Polish", "cs": "Czech", "da": "Danish",
    "af": "Afrikaans", "sq": "Albanian", "am": "Amharic", "hy": "Armenian", "bn": "Bengali", "bs": "Bosnian",
    "bg": "Bulgarian", "ca": "Catalan", "hr": "Croatian", "eo": "Esperanto", "et": "Estonian", "tl": "Filipino (Tagalog)",
    "fi": "Finnish", "el": "Greek", "gu": "Gujarati", "hu": "Hungarian", "is": "Icelandic", "id": "Indonesian",
    "kn": "Kannada", "km": "Khmer", "la": "Latin", "lv": "Latvian", "lt": "Lithuanian", "mk": "Macedonian",
    "ml": "Malayalam", "mr": "Marathi", "ne": "Nepali", "no": "Norwegian", "ro": "Romanian", "si": "Sinhala",
    "sr": "Serbian", "sk": "Slovak", "sl": "Slovenian", "sw": "Swahili", "ta": "Tamil", "te": "Telugu",
    "th": "Thai", "ur": "Urdu", "vi": "Vietnamese", "cy": "Welsh", "xh": "Xhosa", "zu": "Zulu"
}

# Sort languages alphabetically by their full names
sorted_languages = sorted(languages.items(), key=lambda x: x[1])



# Create target language dropdown (displaying full names)
label_to = tk.Label(root, text="Translate To:")
label_to.pack()

lang_to = tk.StringVar()
lang_to.set("es")  # Default to Spanish

dropdown_to = tk.OptionMenu(root, lang_to, *[lang[1] for lang in sorted_languages])
dropdown_to.pack()

# Create translate button
button_translate = tk.Button(root, text="Translate", command=translate_text)
button_translate.pack(pady=20)

# Create file translate button
button_file_translate = tk.Button(root, text="Translate File", command=open_and_translate_file)
button_file_translate.pack(pady=20)

# Create output text area
label_output = tk.Label(root, text="Translated Text:")
label_output.pack()

entry_output = tk.Text(root, height=10, wrap="word", state="normal")
entry_output.pack(pady=10)

# Start the GUI
root.mainloop()
