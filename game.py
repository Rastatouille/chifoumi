import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)


class Game:
    def __init__(self, rounds, idplayer1, idplayer2):
        self.r = rounds
        self.id1 = idplayer1
        self.id2 = idplayer2
		self.score_1 = 0
		self.score_2 = 0
		self.nb_null = 0
		self.code=get_random_string(8)

	def playRound(self,player1,player2):
		if self.r<1:
			return 0
		res= whoWin(player1,player2)
		if res==1:
			self.score_1 += 1
		elif res==-1:
			self.score_2 += 1	
		else
			self.nb_null += 1
		self.r+=-1
		return 1

	def whoWin(self,player1,player2):

		if player1=='p' and player2=='p':
			return 0
		elif player1=='p' and player2=='f':
			return -1
		else player1=='p' and player2=='c':
			return 1
		if player1=='f' and player2=='p':
			return 1
		elif player1=='f' and player2=='f':
			return 0
		else player1=='f' and player2=='c':
			return -1
		if player1=='c' and player2=='p':
			return -1
		elif player1=='c' and player2=='f':
			return 1
		else player1=='c' and player2=='c':
			return 0

		def getCode(self):
			return self.code
		def getScore1(self):
			return self.score_1 
		def getScore2(self):
			return self.score_2 
		def getScoreNul(self):
			return self.nb_null 
