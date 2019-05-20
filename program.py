from jogodaforca import *
class Program(JogoDaForca):
	"""
	Class created by Gleyson Abreu
	"""
	def __init__(self, secretWord, maxErrors, description):

		""" Iniciando o herança """
		JogoDaForca.__init__(self, secretWord, maxErrors, description)

	""" Metodo play para iniciar o game """
	def play(self):
		
		""" Enquando a quantidade erros do usuario for menor que o total de erros permitidos
		o programa continua sua execução.
		 """
		while self.getErrors() < self.getMaxErrors():

			"""Input para captura o que o usuario digita"""
			letter = str(input("Digite uma letra para o jogo da forca: "))

			""" Mais um while para verificar se o usuario digitou algo no input
			caso não ele exibi o mesmo input acima para captura o que usuario está digitando
			 """
			while letter == '':
				letter = str(input("Digite uma letra para o jogo da forca: "))

			"""
			Captura o que o usuario digita mas pega so a primeira letra da string e transforma ela em
			letra minuscula.
			"""
			firstLetter = letter[0].lower()

			"""
			Verificação para verificar se o usuario já digitou a letra que ele informou, caso essa
			letra esteja no list inidicando que ja foi enviada ele mostra a uma mensagem informando
			isso
			"""
			if firstLetter in self.getLetterTyped():
				print(self.getCorrectLetters())
				print("Você já digitou essa letra: {}".format(firstLetter))
			else:
				"""
				Caso não caia no if de cima, ele adiciona a letra ao list indicando que ja foi
				enviada e continua o codigio
				"""
				self.setLetterTyped(firstLetter)

				"""
				Pego a palavra secretra e transformo ela em totalmente em letras minusculas (sensitive case)
				"""
				__secretWord = self.getSecretWord().lower()

				"""
				Faço um FOR com uma chave e valor utilizando o enumerate e verifico se a letra informado
				ja está presente na palavra secreta;
				"""
				for c, value in enumerate(__secretWord):

					if value.lower() == firstLetter:

						"""Adiciono a letra na em sua posição original"""
						self.setCorrectLetters(firstLetter, c)

						"""
							Adiciono +1 no total de letras "achadas"
						"""
						self.setCorrectLettersNumber()

				"""
				Uma pequena veifica para informar se ele acertou a letra ou errou...
				"""
				if firstLetter in __secretWord:
					print("Parabéns você acertou uma letra!!")
					print("Você ainda pode errar {} vezes!".format(self.getAttempts()))
					print(self.getCorrectLetters())
				else:
					self.setErrors()
					print("Você errou a letra!!")
					print("Você tem {} chances..".format(self.getAttempts()))

				"""
				Atras o metodo para quando o usuario errar as 5 tentativas.
				"""
				self.getErrorMessage()


				"""
				Caso o usuario consiga informar todas as letras em sem exceder as 5 tentivas
				uma mensagem é mostrada
				"""
				if self.getCorrectLettersNumber() == len(self.getSecretWord()):
					print("=" * 40)
					print("{:^40}".format("WINNER WINNER CHICKEN DINNER"))
					print("{} era a palavra secreta, PARABÉNS!!".format(self.getSecretWord()))
					print("=" * 40)
					print("Jogo terminado às {}:{}".format(self.getNow().hour, self.getNow().minute))
					break

	"""
	Metodo para calcular as tentativas
	"""
	def getAttempts(self):
		return self.getMaxErrors() - self.getErrors()

	"""
		Metodo para mensagens de erro por excesso de tentativas erradas
	"""
	def getErrorMessage(self):
		if self.getErrors() == 5:
			print("=" * 40)
			print("{:^40}".format("GAME OVER"))
			print("A palavra secreta era: {}".format(self.getSecretWord()))
			print("=" * 40)
			print("Jogo terminado às {}:{}".format(self.getNow().hour, self.getNow().minute))
			