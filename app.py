import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Create main window
root = tk.Tk()
root.title("Multilingual Translator")
root.geometry("600x400")
root.resizable(False, False)

# Language options
languages = list(LANGUAGES.values())
lang_codes = {v: k for k, v in LANGUAGES.items()}

# Functions
def translate_text():
    try:
        src_lang = lang_codes[source_lang.get()]
        dest_lang = lang_codes[target_lang.get()]
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Widgets
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, width=70)
input_text.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
source_lang = ttk.Combobox(frame, values=languages, width=20)
source_lang.set("english")
source_lang.grid(row=0, column=1)

tk.Label(frame, text="To:", font=("Arial", 10)).grid(row=0, column=2, padx=5)
target_lang = ttk.Combobox(frame, values=languages, width=20)
target_lang.set("hindi")
target_lang.grid(row=0, column=3)

translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 12))
translate_btn.pack(pady=10)

tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=70)
output_text.pack()

# Run the app
root.mainloop()
