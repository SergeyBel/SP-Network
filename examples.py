from Present import *

def test(text, key):
	ciph = Present()
	c = ciph.Encrypt(text, key)
	print "plainttext:"
	print text
	print "key:"
	print key
	print "ciphertext:"
	print c
	print "decrypt:"
	print ciph.Decrypt(c, key)
	print 
			
def tests():
	test("0000000000000000", "00000000000000000000")
	test("0000000000000000", "FFFFFFFFFFFFFFFFFFFF")
	test("FFFFFFFFFFFFFFFF", "00000000000000000000")
	test("FFFFFFFFFFFFFFFF", "FFFFFFFFFFFFFFFFFFFF")

	
tests()