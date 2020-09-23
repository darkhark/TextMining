from pathlib import Path
import nltk as nltk


def getMobyTxtLocation():
    """
    Gets the path for the mobyText file specific to ths repo.

    @return: the string representation of the path
    """
    return str(Path(__file__).parent.parent.parent.parent.parent / "data") + "/moby.txt"


def getAllTokens(fileAsString: str) -> list:
    """
    The tokens will be created using the nltk
    library.

    @param fileAsString: A file's contents as a string
    @return: A sorted list of all tokens
    """
    nltk.download("punkt")
    return nltk.word_tokenize(fileAsString)


def wordAndPunctuationTokenCounter(tokens) -> list:
    """
    Counts tokens in a document.

    @param tokens: The tokens from
    """
    resultsList = []
    totalNumber = "Total number of tokens: " + str(len(tokens))
    uniqueTokenList = nltk.FreqDist(tokens)
    uniqueNumber = "Unique number of tokens: ", str(len(uniqueTokenList))
    resultsList.append(totalNumber)
    resultsList.append(uniqueNumber)
    return resultsList


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


def getWordPercentage(wordList: list, tokens) -> str:
    """
    Calculates the percentage of a list of tokens for the given tokens.

    @param wordList: A list of the words that you want to figure out the percentage of.
    @param tokens: The total list of tokens.
    @return: A string of the percentage the entire wordList takes up in the tokens.
    """
    tokenList = nltk.FreqDist(tokens)
    sumOfFreq = 0.0
    wordListAsString = ""
    count = 1
    for word in wordList:
        wordListAsString += word
        if count != len(wordList):
            wordListAsString += ", "
            count += 1
        sumOfFreq += tokenList.freq(word)
    percentWord = round(sumOfFreq * 100, 5)
    return "Percentage of (" + wordListAsString + ") is " + "{:5f}".format(percentWord)


def getMostFrequentTokens(tokens, numOfTop: int) -> str:
    """
    Determines the top n terms and converts the values into a string.

    @param tokens: The tokens to determine the frequency for.
    @param numOfTop: How many top tokens should be considered.
    @return: A string consisting of the top n tokens and their frequencies.
    """
    tokenList = nltk.FreqDist(tokens)
    topWordsList = tokenList.most_common(numOfTop)
    topWordsString = ""
    for pair in topWordsList:
        topWordsString += "\n------\nToken: " + pair[0] + "\nFreq: " + str(pair[1])
    return topWordsString


fileLocation = getMobyTxtLocation()
stringFile = getFileAsRawString(fileLocation)
mobyTokens = getAllTokens(stringFile)
wordAndPunctuationTokenCounter(mobyTokens)
verbLemmatizedTokens = getVerbLemmatizations(mobyTokens)
wordAndPunctuationTokenCounter(verbLemmatizedTokens)
print(getWordPercentage(["HISTORY", "history"], mobyTokens))
print(getMostFrequentTokens(mobyTokens, 10))

