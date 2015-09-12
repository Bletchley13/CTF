


def gen(cur, charset, i, target):
	if i > 5:
		return
	for c in charset:
		ns = cur + c
		#print "try:",ns
		hv = hash(ns)
		if hv == target:
			print ns
			return
		gen(ns, charset, i+1, target)
		
		


def mm(a,b):
	if b == 0:
		return 0
	ret = mm(2*a, b/2)
	if b % 2 == 1:
		ret += a
	#print "%x, %x => %x" % (a,b,ret)
	return ret % 1000000000000037

def mm2(a,b):
        ret = 0
        for i in xrange(0,64):
                ret += ((b >> i) & 0x1) * (a << i )
                ret = ret % 1000000000000037
        return ret


def hash(string):
	value = 0
	for x in string:
		ch = ord(x)
		value = mm(value, 0x241) + ch
	return value 

def hash2(string):
        value = 0
        for x in string:
                ch = ord(x)
                value = mm2(value, 0x241) + ch
        return value



#print mm(0x0, 0x241) 
#print mm(0x31, 0x241)

#s = ""
#for i in xrange(0,50):
#	s+= "0" 
#	val = hash(s)
#	if val > 0x1e1eab437eeb0:
#		print i
#		break

#target = 0x1e1eab437eeb0
#while target != 0:
#	cur = target % 241
#	target = target/241
#	print cur 

#size 5


#valid = []
#for i in xrange(0x0,0xff):
#	if chr(i).isalnum():
#		valid.append(chr(i))

#print valid
#print hash("78y9O")
#print hash("O9y87")
string = "oihTiCor"
print hex(hash(string))
print hex(hash2(string))
#print hex(hash("AH800"))

#base = [1, 577, 332929, 192100033, 110841719041, 63955671886657, 36902422678601089]

ret = 0
index = 0
base = 1
for i in string[::-1]:
	#print ord(i)
	ret = (ret +mm(ord(i),base)) % 1000000000000037
	index += 1	
	#base *= 0x241 
	base = mm(base, 0x241)
	base = base % 1000000000000037	
print hex(ret)



