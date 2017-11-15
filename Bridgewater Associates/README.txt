Time Taken: 3 Hours

Setup Instructions
    nltk package should be installed: pip install nltk

Program Steps:
    1. Download and install the punkt nltk package if necessary
    2. Setup additional abbreviations for the nltk package to be aware of when detecting sentences
    3. Get the file to process and the save file to post results to
    4. Analyze the given file for word occurrences for each sentence
    5. Print and write the concordance to the console and save file

Issues:
    The program will incorrectly split on abbreviations.
        This is due to limitations of the natural language processing package as it can't determine if an abbreviation is the end of a sentence or not.
        To solve this, abbreviations will need to be hard coded and added to the sentence tokenizer to properly setup the sentence tokenizer or train the sentence tokenizer on similar files.
    The original output formatting doesn't scale with files that have >1000 unique words
        The bullet lettering of increasing number of letters pushes the word beyond what the padded spacing can allow
        As such, I've removed the bullet lettering to keep the formatting consistent. If the bullet lists are truly necessary, then numerical indicators could be used as those will not increase in character size too much.
