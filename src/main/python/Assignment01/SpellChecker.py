from concurrent.futures.thread import ThreadPoolExecutor
from nltk.corpus import words
import tkinter as tk
import nltk


class SpellCheckerWindow(tk.Frame):

    executor = ThreadPoolExecutor(8)

    def __init__(self, inRoot, **kw):
        super().__init__(**kw)
        self.root = inRoot
        self.root.title("Spell Checker Window")
        self.root.geometry("500x200")

        # Creates the op Label
        self.label = tk.Label(
            self.root,
            text="Spell Checker"
        )

        # Creates the box above the buttons for entering the word
        self.entryBox = tk.Entry(self.root)
        self.entryBox.insert(0, "Enter word here...")

        # Creates the check button which will call the spell checker on the word in the entry
        self.check_button = tk.Button(
            self.root,
            text="Check",
            width=10,
            height=2,
            command=lambda: self.checkPressed(self.entryBox.get())
        )

        # Creates the clear button to clear the text entry
        self.clear_button = tk.Button(
            self.root,
            text="Clear",
            width=10,
            height=2,
            command=lambda: self.clearAll()
        )

        self.textBox = tk.Text(
            self.root,
            height=10,
            width=40
        )

        self.defineLayout()

    def defineLayout(self):
        """
        Uses the grid layout manager to make the display prettier.
        """
        self.label.grid(row=0, column=0, columnspan=3)
        self.entryBox.grid(row=1, column=0, columnspan=2)
        self.check_button.grid(row=2, column=0, sticky="N")
        self.clear_button.grid(row=2, column=1, padx=5, sticky="N")
        self.textBox.grid(row=1, column=2, rowspan=2, sticky="E")

    def clearAll(self):
        if len(self.entryBox.get()) > 0:
            self.entryBox.delete(0, 'end')
        if len(self.textBox.get("1.0", "end-1c")) > 0:
            self.textBox.delete("1.0", "end-1c")

    def checkPressed(self, word):
        self.executor.submit(self.checkSpelling, word)

    def checkSpelling(self, word: str) -> None:
        """
        Used by the Check button to return the results of the spell
        check to the textBox. If the word contains anything outside
        of letter, it will not be allowed and a message will be displayed
        in the textbox.

        @param word: An alphaetic string
        """
        nltk.download("words")
        word = word.strip()
        if len(self.textBox.get("1.0", "end-1c")) > 0:
            self.textBox.delete("1.0", "end-1c")
        if word.isalpha():
            top15 = self.getTop15Results(word)
        else:
            top15 = ["Please enter an alphabetic string."]
        for word in top15:
            self.textBox.insert('end', word + "\n")

    def getTop15Results(self, word: str) -> list:
        self.after(0, self.textBox.insert, 'end', "Loading...")
        distDict = {}
        for correctWord in words.words():
            editDist = nltk.edit_distance(word, correctWord)
            distDict[correctWord] = editDist
        distDict = {keyWord: dist for keyWord, dist in sorted(distDict.items(), key=lambda item: item[1])}
        count = 0
        top15 = []
        for key in distDict:
            if count < 15:
                top15.append(key)
                count += 1
            else:
                break
        self.textBox.delete("1.0", "end-1c")
        return top15
