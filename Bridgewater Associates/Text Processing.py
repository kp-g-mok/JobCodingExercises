import os
import nltk
import string
import tkinter as tk

from tkinter import filedialog


def get_filenames():
    """
    Use Tkinter file dialog screens to select files to read from and save to
    Read file is the text file you want to process
    Save file is the text file you want the word count results to be logged to
    :return: the file path to read from and save file for results
    """
    root = tk.Tk()
    root.withdraw()
    initial_dir = os.getcwd()
    read_file = filedialog.askopenfilename(initialdir=initial_dir, title="Select file to process",
                                           filetypes=[("Text Files", "*.txt")])
    save_file = filedialog.asksaveasfilename(initialdir=initial_dir, title="Save file for word occurrences",
                                             filetypes=[("Text Files", "*.txt")], defaultextension='.txt')
    return read_file, save_file


def get_words(file):
    """
    Returns a list of the words that occur in the given text file and the sentences they occur in
    :return: Dictonary of words : sentence list
    """
    words_dict = {}
    with open(file, 'r') as f:
        for num, sentence in enumerate(nltk.sent_tokenize(f.read())):
            line = num + 1
            for token in nltk.word_tokenize(sentence):
                if token in string.punctuation or not token.replace('.', '').isalpha():
                    continue
                low_word = token.lower()
                if low_word not in words_dict:
                    words_dict[low_word] = []
                words_dict[low_word].append(line)
    return words_dict


def print_and_save_words(save_file, words_dict):
    """
    Print and save each word found in the text file in this format:
        {Word}(Spacing){Number of Occurrences}:{Sentence of Occurrence}
        Spacing will be a max width of 25 spaces between the word and the occurrence values
    :return: Nothing
    """
    with open(save_file, 'w') as s:
        max_width = 25
        for i, word in enumerate(sorted(words_dict)):
            sentence_lines = ','.join([str(line) for line in words_dict[word]])
            line = '{word: <{width}} {{{length}:{sentence_list}}}'.format(
                word=word,
                width=max_width,
                length=len(words_dict[word]),
                sentence_list=sentence_lines)
            print(line)
            s.write(line + '\n')


if __name__ == '__main__':
    # Setup NLTK for abbreviations
    nltk.download('punkt')
    extra_abbreviations = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e', 'phd', 'etc', 'al', 'ak', 'az', 'ar', 'ca',
                           'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me',
                           'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd',
                           'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn',
                           'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']
    sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentence_tokenizer._params.abbrev_types.update(extra_abbreviations)

    file_path, save_path = get_filenames()
    words = get_words(file_path)
    print_and_save_words(save_path, words)
