from pathlib import Path
import nltk as nltk


def getMobyTxtLocation():
    return str(Path(__file__).parent.parent.parent.parent.parent / "data") + "/moby.txt"


def getTokens(fileAsString: str):
    """
    The tokens will be created using the nltk
    library.

    @param fileAsString: A file's contents as a string
    @return: A sorted list of all tokens
    """
    nltk.download("punkt")
    return sorted(nltk.word_tokenize(fileAsString))


def wordAndPunctuationTokenCounter(tokens) -> list:
    """
    Counts tokens in a document.
    @param tokens: The tokens from
    """
    print("Total number of tokens: " + str(len(tokens)))
    uniqueTokenList = nltk.FreqDist(tokens)
    print(len(uniqueTokenList))


def getFileAsRawString(filePath: str) -> str:
    with open(filePath, "r") as file:
        fileAsString = file.read()
    return fileAsString


fileLocation = getMobyTxtLocation()
mobyTokens = getTokens(getFileAsRawString(fileLocation))
wordAndPunctuationTokenCounter(mobyTokens)
