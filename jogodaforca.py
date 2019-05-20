from datetime import datetime, timedelta
class JogoDaForca(object):
	"""

	Class created by Gleyson Abreu

	"""


	"""
	atributos
	"""
	__secretWord = "Manchester"
	__maxErrors = 5
	__errors = 0
	__correctLetters = []
	__correctLettersNumber = 0
	__letterTyped = []
	__description = "Um clube de futebool europeu campeão da UEFA Champions League"


	def __init__(self, secretWord, maxErrors, description):
		
		if secretWord != None:
			self.__secretWord = secretWord
		if maxErrors != None:
			self.__maxErrors = maxErrors
		if description != None:
			self.__description = description

		for c, value in enumerate(self.__secretWord):

			if value == ' ':
				self.__correctLetters.append(" ")
				self.setCorrectLettersNumber()
				self.setLetterTyped(' ')
			else:
				self.__correctLetters.append("_")

	def getNow(self):
		return datetime.now()

	def getDescription(self):
		return self.__description
	def setDescription(self, description):
		self.__description = description

	def getLetterTyped(self):
		return self.__letterTyped
	def setLetterTyped(self, letter):
		self.__letterTyped.append(letter)

	def getSecretWord(self):
		return self.__secretWord
	def setSecretWord(self, secretWord):
		self.__secretWord = secretWord

	def getMaxErrors(self):
		return self.__maxErrors
	def setMaxErrors(self, maxErros):
		self.__maxErrors = maxErros

	def getErrors(self):
		return self.__errors
	def setErrors(self):
		self.__errors += 1

	def getCorrectLetters(self):
		return self.__correctLetters
	def setCorrectLetters(self, correctLetter, positon):
		self.__correctLetters[positon] = correctLetter

	def getCorrectLettersNumber(self):
		return self.__correctLettersNumber
	def setCorrectLettersNumber(self):
		self.__correctLettersNumber += 1