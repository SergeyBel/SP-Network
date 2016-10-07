from SPCipher import *

class Present(SPCipher):

	
	def __init__(self):
		sbox = [0xc,0x5,0x6,0xb,0x9,0x0,0xa,0xd,0x3,0xe,0xf,0x8,0x4,0x7,0x1,0x2]
		self.sboxes = [sbox] * 16
		self.invSboxes = [InvMapping(sbox)] * 16
		self.pTransform = [0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,
        4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,
        8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,
        12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]
		self.invPTransform = InvMapping(self.pTransform)
		self.blockSize = 64
		self.rounds = 32
		self.sboxSize = 4
		
	def ExpandKey(self, key):
		self.roundKeys = []
		key = self.KeyFormat(key)
		for i in range(self.rounds):
			self.roundKeys.append(key[0:64])
			key = key[61:] + key[0:61]
			t = key[0:4]
			t = self.Sbox(self.sboxes[0], string2number(t))
			key = number2string(t, 4) + key[4:]
			t = string2number(key[60:65])
			t = t ^ (i + 1)
			key = key[0:60] + number2string(t, 5) + key[65:]


