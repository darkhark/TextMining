from pathlib import Path
import nltk as nltk


def getMobyTxtLocation():
    return str(Path(__file__).parent.parent.parent.parent.parent / "data") + "/moby.txt"


def getAllTokensSorted(fileAsString: str):
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
    print("Unique number of tokens: " + str(len(uniqueTokenList)))


def getFileAsRawString(filePath: str) -> str:
    with open(filePath, "r") as file:
        fileAsString = file.read()
    return fileAsString


def getVerbLemmatizations(tokens) -> list:
    """
    Takes in a list of tokens and finds all the verbs then
    lemmatizes them.

    @param tokens: A list of tokens
    @return: The list of tokens after lemmatization.
    """
    nltk.download('wordnet')
    lemmatizer = nltk.WordNetLemmatizer()
    lemmaTokens = nltk.pos_tag(tokens)
    verbArray = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    results = []
    for token in lemmaTokens:
        if token[1] in verbArray:
            resultingToken = lemmatizer.lemmatize(token[0], pos='v')
        else:
            resultingToken = token[0]
        results.append(resultingToken)
    return results


fileLocation = getMobyTxtLocation()
stringFile = getFileAsRawString(fileLocation)
mobyTokens = getAllTokensSorted(stringFile)
wordAndPunctuationTokenCounter(mobyTokens)
verbLemmatizedTokens = getVerbLemmatizations(mobyTokens)
wordAndPunctuationTokenCounter(verbLemmatizedTokens)

