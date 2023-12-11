# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:19:28 2023

@author: mysticmarks
"""

import tkinter as tk
from tkinter import ttk
import nltk
import os

# Ensure the NLTK data (e.g., tokenizers, taggers) is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class CodeConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        if not os.path.exists("output"):
            os.mkdir("output")
            print("Created output directory")
        else:
            print("Output directory already exists")

        self.title("Natural Language to Code Converter")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Input Entry widget
        self.input_label = ttk.Label(self, text="Enter your instruction:")
        self.input_label.pack(pady=5)
        self.input_entry = ttk.Entry(self, width=50)
        self.input_entry.pack(pady=5, padx=5)

        # Convert Button
        self.convert_button = ttk.Button(self, text="Convert to Code", command=self.convert_to_code)
        self.convert_button.pack(pady=5)

        # Output Text widget
        self.output_text = tk.Text(self, height=10, width=50)
        self.output_text.pack(pady=5, padx=5)

        # Save Button
        self.save_button = ttk.Button(self, text="Save", command=self.save_output)
        self.save_button.pack(pady=5)

    def convert_to_code(self):
        user_input = self.input_entry.get()
        tokens = nltk.word_tokenize(user_input)
        tagged = nltk.pos_tag(tokens)

        # Basic rule-based conversion (you can extend it as per your requirements)
        code = ""
        for word, tag in tagged:
            if tag.startswith("VB"):  # Verb
                code += f"{word}()"  # Example conversion rule: Verb -> Function
            elif tag.startswith("NN"):  # Noun
                code += f"{word}"  # Example conversion rule: Noun -> Variable/Object
            code += " "  # Adding space for readability

        self.output_text.delete(1.0, tk.END)  # Clearing previous output
        self.output_text.insert(tk.END, code)  # Inserting new converted code

    def save_output(self):
        filenames = os.listdir("output")
        code = self.output_text.get(1.0, tk.END)
        with open(f'output/{len(filenames)}.py', "w") as file:
            file.write(code)

if __name__ == "__main__":
    app = CodeConverterApp()
    app.mainloop()
