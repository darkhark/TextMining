from datetime import datetime
from pathlib import Path


class HomeworkWriter:
    _docsPath = str(Path(__file__).parent.parent.parent.parent.parent / "docs") + "/"
    _separator = "\n------------------------------\n"

    @staticmethod
    def writeHomework(answersList: list, fileName: str) -> None:
        """
        Writes answer to homework in a formatted way so I don't have to keep writing it.

        @param answersList: A list of all the answers for the assignment as strings, where each
        value is the answer to one question.

        @param fileName: A string for the name of the txt file to be generated.
        @return: None, but it writes to a file in the docs directory.
        """
        with open(HomeworkWriter._docsPath + fileName + ".txt", "x") as homework:
            count = 1
            separator = HomeworkWriter._separator
            homework.write("Name: Josh Harkness\nClass: CAP6307-TextMining\n")
            homework.write("Date: " + datetime.today().strftime('%Y-%m-%d') + "\n")
            for answer in answersList:
                answersString = "\nQuestion " + str(count) + ":" + separator
                answersString += answer + separator
                homework.write(answersString)
                count += 1
