from program import *

"""
Primeiro Campo diz respeito a palavra secreta pra o jogo da forca; Se 'None' é colocada uma palavra pré definida no codigo
Segundo Campo diz respeito a quantidade de erros que você pode cometer; Se 'None' é coloda um limite padrão de 5
Terceiro campo diz respeito a descrição da palavra secrete, uma dica.
"""
jogo_da_forca = Program(None, None, None)

""" Aparencia inicil do programa """
print("=" * 40)
print("{:^40}".format("JOGO DA FORCA"))
print("{:^40}".format("Criado por Gleyson Abreu"))
print("=" * 40)

""" Informações iniciais """
print("{:^40}".format("PALAVRA SECRETA \n"))
print("Jogo iniciado às {}:{}".format(jogo_da_forca.getNow().hour, jogo_da_forca.getNow().minute))
print("Dica: {}".format(jogo_da_forca.getDescription()))
print(jogo_da_forca.getCorrectLetters())
print("Total de letras: {} ".format(len(jogo_da_forca.getSecretWord())))
print("Total de erros permitidos: {}".format(jogo_da_forca.getMaxErrors()))
print("Total de erros cometidos: {}".format(jogo_da_forca.getErrors()))

""" Vamos jogar... """
jogo_da_forca.play()