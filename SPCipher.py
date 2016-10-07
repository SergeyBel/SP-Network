def string2number(str):
	return int(str, 2)

def number2string(i, n):
	s = bin(i)[2:]
	s  = "0" * (n - len(s)) + s
	return s
		
def ArrayToBitString(a, n):
	s = ""
	for i in range(len(a)):
		s = s + number2string(a[i], n)
	return s
	
def BitStringToArray(s, n):
	p = []
	for i in range(0, len(s), n):
		p.append(string2number(s[i:i + n]))
	return p
	
def InvMapping(f):
	inv = [f.index(i) for i in range(len(f))]
	return inv

class SPCipher:
	blockSize = 0
	rounds = 0
	sboxes = []
	invSboxes = []
	roundKeys = []
	pTransform = []
	invPTransform = []
	sboxSize = 0
	
	def __init__(self, sboxes, pTransform, blockSize = 64, rounds = 32, sboxSize = 4):
		self.sboxes = sboxes
		self.pTransform = pTransform
		self.blockSize = blockSize
		self.rounds = rounds
		self.sboxSize = sboxSize
	
	def ExpandKey(self, key):
		return True
	
	def Encrypt(self, text, key):
		p = self.PlainTextFormat(text)
		
		self.ExpandKey(key)
		for i in range(self.rounds - 1):
			p = self.Round(p, self.roundKeys[i])
		p = self.AddKey(p, self.roundKeys[self.rounds - 1])

		return self.CipherTextFormat(p)
		
		
		
	def Decrypt(self, text, key):
		p = self.PlainTextFormat(text)
		
		self.ExpandKey(key)
		self.roundKeys = self.roundKeys[::-1]
		p = self.AddKey(p, self.roundKeys[0])
		for i in range(1, self.rounds):
			p = self.InvRound(p, self.roundKeys[i])
			
		return self.CipherTextFormat(p)
		
	def Round(self, p, key):
		p = self.AddKey(p, key)
		p = self.SboxLayer(self.sboxes, p)
		p = self.PLayer(self.pTransform, p)
		return p
		
	def InvRound(self, p, key):
		p = self.PLayer(self.invPTransform, p)
		p = self.SboxLayer(self.invSboxes, p)
		p = self.AddKey(p, key)
		return p
	
	def AddKey(self, p, key):
		res = ""
		for i in range(len(p)):
			res += str(int(p[i]) ^ int(key[i]))
		return res
	
	def SboxLayer(self, sboxes, p):
		r = BitStringToArray(p, self.sboxSize)
		res = ""
		for i in range(len(sboxes)):
			part = self.Sbox(sboxes[i], r[i])
			res += number2string(part, self.sboxSize)
		return res
		
	def Sbox(self, sbox, x):
		return sbox[x]
	
	def PLayer(self, pFunc, p):
		r = [0] * len(p)
		for i in range(len(pFunc)):
			r[pFunc[i]] = p[i:i+1]
		return ''.join(r)
	
	#functions to convert plaintext, ciphertext and key from/to internal format 
	#internal format - strings of 1 and 0
	
	def PlainTextFormat(self, text):
		p = [int(t, 16) for t in text]
		return ArrayToBitString(p, 4)
		
	def CipherTextFormat(self, text):
		p = BitStringToArray(text, 4)
		res = ""
		for t in p:
			res += format(t, 'x')
		return res

	def KeyFormat(self, key):
		a = [int(k, 16) for k in key]
		return ArrayToBitString(a, 4)
		



	

	
	