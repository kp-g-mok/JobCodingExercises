import nltk
nltk.download('punkt')

# # Time: 15 min research
#
# import os
# import tkinter as tk
#
# from tkinter import filedialog
# from nltk import sent_tokenize
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=[("Text Files", "*.txt")])
#
#     print(file_path)
#     with open(file_path) as f:
#         for sentence in sent_tokenize(f):
#             print(sentence)
