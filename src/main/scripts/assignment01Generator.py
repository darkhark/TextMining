# This script writes out the homework one file

from Assignment01 import MobyTokens
from Assignment01.SpellChecker import SpellCheckerWindow
from Writer.HomeworkWriter import HomeworkWriter
import tkinter as tk

answersList = []
fileLocation = MobyTokens.getMobyTxtLocation()
stringFile = MobyTokens.getFileAsRawString(fileLocation)
mobyTokens = MobyTokens.getAllTokens(stringFile)

question1 = MobyTokens.wordAndPunctuationTokenCounter(mobyTokens)
answersList.append(question1)

verbLemmatizedTokens = MobyTokens.getVerbLemmatizations(mobyTokens)
question2 = MobyTokens.wordAndPunctuationTokenCounter(verbLemmatizedTokens)
answersList.append(question2)

question3 = MobyTokens.getWordPercentage(["HISTORY", "history"], mobyTokens)
answersList.append(question3)

question4 = MobyTokens.getMostFrequentTokens(mobyTokens, 10)
answersList.append(question4)
HomeworkWriter.writeHomework(answersList, "Assignment01")

root = tk.Tk()
my_gui = SpellCheckerWindow(root)
root.mainloop()
