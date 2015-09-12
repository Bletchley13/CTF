from z3 import *

def mm2(a,b):
	ret = 0
	for i in xrange(0,64):
		#if ((b >> i) & 0x1):
		ret += ((b >> i) & 0x1)*(a << i )
 			#ret = ret % 1000000000000037
			#ret += (a << i )
	return ret

def calchash(x, k):
	ret = 0
	for i in xrange(0,k-1):
		ret = mm2(ret, 0x241) + x[i]
	return ret % 1000000000000037

def try_k(k, target):
        s = Solver()
        xs = []
        ys = []
	# base is the power of 0c241
        base = 1
        zs = []
        #z = BitVec("z0" , 64) 
        #s.add(z==0) #initial sum is 0
        #zs.append(z)
       
        for i in xrange(1, k):
		x = BitVec("x%d" % i, 64) # this character
		z = BitVec("z%d" % i, 64) # hash value of this character (x * 0x241^i)
		#value range
		s.add( 48 <= x )
                s.add( x <= 122 )

                for i in xrange(91, 97):
                        s.add(x != i)

                for i in xrange(58, 65):
                        s.add(x != i)

		#hash
		s.add( mm2(x , base)  % 1000000000000037 == z )
		xs.append(x)
                zs.append(z)
		base =mm2(base , 0x241)% 1000000000000037
	#s.add(calchash(xs, k)==target)
	s.add(Sum(zs)%1000000000000037 ==target)
	if s.check() == sat:
                m = s.model()
                r = [ m.evaluate(xs[i]) for i in range( k-1) ]
                msg = ""
                for re in r:
                        msg += chr(int(str(re)))
                        #print chr(int(str(re)))
                #print msg
                print msg[::-1]
                return True
        return False


def tryn(k, target):
	s = Solver()
	xs = []
	ys = []
	base = 1
	zs = []
	z = BitVec("z0" , 64) # z to save current sum
	s.add(z==0) #initial sum is 0
	zs.append(z)
	#print zs[0]
	for i in xrange(1, k):
		#print i, base
		#print zs[-1]
		x = BitVec("x%d" % i, 64)
		#y = BitVec("y%d" % i, 64)
		z = BitVec("z%d" % i, 64)
		
		s.add( 48 <= x )		
		s.add( x <= 122 )

		for i in xrange(91, 97):
                        s.add(x != i)

		for i in xrange(58, 65):
			s.add(x != i)

		#s.add( (zs[-1]+ ((x*base)% 1000000000000037  ) ) % 1000000000000037 == z )
		s.add( (zs[-1]+ (mm2(x, base)  ) ) % 1000000000000037 == z )
		xs.append(x)
		zs.append(z)
		base = (base * 0x241) % 1000000000000037
	#add = BitVec("add")
	s.add(zs[k-1]==target)
	#print Sum([ v for y in ys ])
	#s.add( Sum([ v for y in ys ]) == 10 )
	#s.add(sumv)
	if s.check() == sat:
		m = s.model()
		print m
		r = [ m.evaluate(xs[i]) for i in range( k-1) ] 
    		print r
		msg = ""
		for re in r:
			msg += chr(int(str(re)))
			print chr(int(str(re))) 
		print msg
		print msg[::-1]
		return True
	return False


target = 0x1e1eab437eeb0

for i in xrange(9,20):
	print i
	if try_k(i, target):
		break


