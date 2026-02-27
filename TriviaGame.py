import math

class TriviaGame:
    def __init__(self, player, questions):
        self.player = player
        self.questions = questions
        self.score = 0

    def askQuestion(self, questions):


    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer:
            print("Correct answer! Next question: \n")
            self.score += 1
        else:
            print("Incorrect answer! Next question: \n")

    def calcPercent(self):
        percentRight = (self.score / len(self.questions)) * 100
        return math.ceil(percentRight)

    def startGame(self):

    def newGame(self):
