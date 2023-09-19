"""
These are NOT property-based tests, and as such, passing them does not mean that your code is fully correct.
Your mark will ultimately depend on how you have coded your answers.

You can and probably should write your own additional test code to test your answers.  Such additional test code will not be marked and it's fine if they are submitted to your fork, whether as part of the py_cw.py file or in a separate file.

To run these tests, type `pytest-3` within this directory.
"""
import py_cw
from random import randint


def test_q1a():
	s = py_cw.cadd((1, 0), (0, 1))
	p = py_cw.cmult((3, 2), (9, 6))
	assert s == (1, 1) and p == (15, 36)
	# Below are the tests which I added
	s = py_cw.cadd((3,5), (4,-3))
	p = py_cw.cmult((3, 2), (1,7))
	assert s == (7,2) and p == (-11,23)
	s = py_cw.cadd((-5, 4), (2, -4))
	p = py_cw.cmult((1,1), (1,1))
	assert s == (-3, 0) and p == (0,2)    #Checking negative
	s = py_cw.cadd((0, 0), (0, 0))
	p = py_cw.cmult((0,0), (0,0))
	assert s == (0, 0) and p == (0,0)    #Checking all zeros
	s = py_cw.cadd((24,31), (-32, -44))
	p = py_cw.cmult((13,-20), (56,-26))
	assert s == (-8, -13) and p == (208, -1458)    #Checking mre than 1 digit

def test_q1b():
	assert py_cw.tocomplex(1, 2) == (1 + 2j) and py_cw.fromcomplex(1 + 1j) == (1, 1)
	# Below are the tests which I added
	assert py_cw.tocomplex(208, -1458) == (208-1458j) and py_cw.fromcomplex(208 -1458j) == (208, -1458) #Checking mre than 1 digit
	assert py_cw.tocomplex(15, 36) == (15+36j) and py_cw.fromcomplex(15+36j) == (15, 36)  #Checking mre than 1 digit
	assert py_cw.tocomplex(0,0) == (0j) and py_cw.fromcomplex(0j) == (0,0)               #Checking all zeros

def test_q2a():
	assert py_cw.seqaddi([1, 2, 3, 4], [2, 3, 4, 5]) == [3, 5, 7, 9] and py_cw.seqmulti([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 6, 12, 20]
	# Below are the tests which I added
	assert py_cw.seqaddr([1, 2, 3, 4], [5, 4, 3, 2]) == [6, 6, 6, 6] and py_cw.seqmultr([1, 2, 3, 4], [5, 4, 3, 2]) == [5, 8, 9, 8]
	assert py_cw.seqaddi([9, 8, 7, 6], [4, 5, 6, 9]) == [13, 13, 13, 15] and py_cw.seqmulti([9, 8, 7, 6], [4, 5, 6, 9]) == [36, 40, 42, 54]
	assert py_cw.seqaddi([6, 8, -4, 8], [4, -5, 6, -9]) == [10, 3, 2, -1] and py_cw.seqmulti([6, 8, -4, 8], [4, -5, 6, -9]) == [24, -40, -24, -72] #Checking negative


def test_q2b():
	assert py_cw.seqaddr([1, 2, 3, 4], [5, 4, 3, 2]) == [6, 6, 6, 6] and py_cw.seqmultr([1, 2, 3, 4], [5, 4, 3, 2]) == [5, 8, 9, 8]
	# Below are the tests which I added
	assert py_cw.seqaddi([1, 2, 3, 4], [2, 3, 4, 5]) == [3, 5, 7, 9] and py_cw.seqmulti([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 6, 12, 20]	
	assert py_cw.seqaddi([9, 8, 7, 6], [4, 5, 6, 9]) == [13, 13, 13, 15] and py_cw.seqmulti([9, 8, 7, 6], [4, 5, 6, 9]) == [36, 40, 42, 54]
	assert py_cw.seqaddi([6, 8, -4, 8], [4, -5, 6, -9]) == [10, 3, 2, -1] and py_cw.seqmulti([6, 8, -4, 8], [4, -5, 6, -9]) == [24, -40, -24, -72] #Checking negative



def test_q2c():
	assert py_cw.seqaddlc([1, 2, 3, 4], [5, 4, 3, 2]) == [6, 6, 6, 6] and py_cw.seqmultlc([1, 2, 3, 4], [5, 4, 3, 2]) == [5, 8, 9, 8]
	# Below are the tests which I added
	assert py_cw.seqaddi([1, 2, 3, 4], [2, 3, 4, 5]) == [3, 5, 7, 9] and py_cw.seqmulti([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 6, 12, 20]
	assert py_cw.seqaddi([9, 8, 7, 6], [4, 5, 6, 9]) == [13, 13, 13, 15] and py_cw.seqmulti([9, 8, 7, 6], [4, 5, 6, 9]) == [36, 40, 42, 54]
	assert py_cw.seqaddi([6, 8, -4, 8], [4, -5, 6, -9]) == [10, 3, 2, -1] and py_cw.seqmulti([6, 8, -4, 8], [4, -5, 6, -9]) == [24, -40, -24, -72] #Checking negative



def test_q3_ismatrix():
	assert (not py_cw.ismatrix([[2,3,4], [3,2,6,7], [2,3,4]])) and py_cw.ismatrix([[1,2,3], [3,4,6]])
	# Below are the tests which I added
	assert (py_cw.ismatrix([[2,3,4], [2,6,7], [2,3,4]])) and not py_cw.ismatrix([[1,5,2,3], [3,4,6]])
	assert (not py_cw.ismatrix([[2], [], [2]])) and py_cw.ismatrix([[1], [3]])

	
def test_q3_matrixshape():
	m = [[1,2,3], [3,4,6]]
	assert py_cw.matrixshape(m) == (2, 3)
	# Below are the tests which I added
	m = [[1,2], [3,4]]
	assert py_cw.matrixshape(m) == (2, 2)
	m = [[1,2,3]]
	assert py_cw.matrixshape(m) == (1, 3)
	m = [[], []]
	assert py_cw.matrixshape(m) == (2, 0)
	m = []
	assert py_cw.matrixshape(m) == (0, 0)


def test_q3_matrixadd():
	m1 = [[1,2,3], [3,4,6]]
	m2 = [[5,6,7], [7,6,4]]
	assert py_cw.matrixadd(m1, m2) == [[6, 8, 10], [10,10,10]]
	# Below are the tests which I added
	m1 = [[2,3], [-5,7]]
	m2 = [[4,6], [2,-11]]
	assert py_cw.matrixadd(m1, m2) == [[6,9], [-3,-4]]	# Checking negative
	m1 = [[1,4], [2,3]]
	m2 = [[-4,-1], [-3,-2]]
	assert py_cw.matrixadd(m1, m2) == [[-3,3], [-1,1]] 
	m1 = [[0,0], [0,0]]
	m2 = [[-4,-1], [-3,-2]]
	assert py_cw.matrixadd(m1, m2) == [[-4,-1], [-3,-2]] # checking m1 full zeros
	m1 = [[1,4], [2,3]]
	m2 = [[0,0], [0,0]]
	assert py_cw.matrixadd(m1, m2) == [[1,4], [2,3]] # checking m2 full zeros
	m1 = [[0,0], [0,0]]
	m2 = [[0,0], [0,0]]
	assert py_cw.matrixadd(m1, m2) == [[0,0], [0,0]] # checking both m1 and m2 full zeros





def test_q3_matrixmult():
	m1 = [[2,3,4], [7,8,9]]
	m2 = [[1,0], [3,6], [8,2]]
	assert py_cw.matrixmult(m1, m2) == [[43,26], [103,66]]
	# Below are the tests which I added
	m1 = [[4,5]]
	m2 = [[1,6,9], [5,2,4]]
	assert py_cw.matrixmult(m1, m2) == [[29,34,56]] # Checking random
	m1 = [[1,-2,1], [2,1,3]]
	m2 = [[2,1], [3,2], [1,1]]
	assert py_cw.matrixmult(m1, m2) == [[-3,-2], [10,7]] # Checking negative
	m1 = [[2,3,4], [7,8,9]]
	m2 = [[0,0], [0,0]]
	assert py_cw.matrixmult(m1, m2) == [[0, 0], [0, 0]] # checking m2 full zeros



def test_q5():
	assert py_cw.encdat(-10)=='-10' and py_cw.encdat(10.4) == '10.4' and py_cw.encdat(5+4.5j)=='5+4.5j' and py_cw.encdat(345)=='345' and py_cw.encdat(5+5j)=='5+5j' and py_cw.encdat('(5+5j)')=='(5+5j)' and py_cw.encdat('({))') == '({))'
	# Below are the tests which I added
	assert py_cw.encdat(-5000.6479)=='-5000.6479'# Checking negative float
	assert py_cw.encdat(145+37j)=='145+37j'   # Checking complex
	assert py_cw.encdat(5432)=='5432'          # Checking int
	assert py_cw.encdat('abcdefghijklmnopqrstuvwxyz')=='abcdefghijklmnopqrstuvwxyz' # Checking string of alphabets
	assert py_cw.encdat('!@#$%^&*()')=='!@#$%^&*()'              # Checking string of special character
	


def test_q6_fenc():
	assert py_cw.fenc(4)==[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]
	# Below are the tests which I added
	assert py_cw.fenc(0)==[]               # Testing for 0
	assert py_cw.fenc(1)==[[], [[]]]               # Testing for 1
	assert py_cw.fenc(2)==[[[], [[]]], [[[], [[]]]]]               # Testing for 2
	assert py_cw.fenc(3)==[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]               # Testing for 3
	assert py_cw.fenc(5)==[[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]], [[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]]]	       # Testing for 5






def test_q6_fdec():
	assert py_cw.fdec([[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]])==4
	# Below are the tests which I added
	assert py_cw.fdec([]) == 0         # Testing for 0
	assert py_cw.fdec([[], [[]]])==1         # Testing for 1
	assert py_cw.fdec([[[], [[]]], [[[], [[]]]]]) == 2         # Testing for 2
	assert py_cw.fdec([[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]])==3         # Testing for 3
	assert py_cw.fdec([[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]], [[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]]])==5         # Testing for 5


def test_q7():
	n = randint(100, 1000)
	li = ['eat', 'sleep', 'code']
	g = py_cw.cycleoflife()
	y = None
	for _ in range(n):
		y = next(g)
	assert y == li[(n % 3) - 1]
	# Below are the tests which I added, they are the same as the first one but as n is random it changes everytime
	n = randint(100, 1000)
	li = ['eat', 'sleep', 'code']
	g = py_cw.cycleoflife()
	y = None
	for _ in range(n):
		y = next(g)
	assert y == li[(n % 3) - 1]
	n = randint(100, 1000)
	li = ['eat', 'sleep', 'code']
	g = py_cw.cycleoflife()
	y = None
	for _ in range(n):
		y = next(g)
	assert y == li[(n % 3) - 1]
	n = randint(100, 1000)
	li = ['eat', 'sleep', 'code']
	g = py_cw.cycleoflife()
	y = None
	for _ in range(n):
		y = next(g)
	assert y == li[(n % 3) - 1]


def test_q8():
	assert py_cw.gendat([5,5,[5,[]],[],[5],[[5]]]) == [5,5,5,5,5]
	# Below are the tests which I added
	assert py_cw.gendat([10,-5,[9,[]],[],[79],[[26]]]) == [10,-5,9,79,26]       # Checking random
	assert py_cw.gendat([-7,[-85,[]],[],[-333],[[-104]]]) == [-7,-85,-333,-104]       # Checking all negative
	assert py_cw.gendat([[[]],[],[],[[]]]) == []       # Checking empty
	


def test_q9():
	p = None
	e = py_cw.eratosthenes()
	for _ in range(22):
		p = next(e)
	assert p == 79
	# Below are the tests which I added
	p = None
	e = py_cw.eratosthenes()
	for _ in range(1):
		p = next(e)
	assert p == 2           #Checking if the 2nd Prime Number is correct or not
	p = None
	e = py_cw.eratosthenes()
	for _ in range(3):
		p = next(e)
	assert p == 5            #Checking if the 3rd Prime Number is correct or not
	p = None
	e = py_cw.eratosthenes()
	for _ in range(1000):  
		p = next(e)
	assert p == 7919       #Checking if the 1000th Prime Number is correct or not

def test_q10_transpose():    # I added this test
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixtranspose(m) == [[1,4,7],[2,5,8],[3,6,9]]   # Checking 3x3 
	m = [[1,2],[3,4]]
	assert py_cw.matrixtranspose(m) == [[1,3],[2,4]]    # Checking 2x2
	m = [[1,2],[3,4]]
	assert py_cw.matrixtranspose(m) == [[1,3],[2,4]]    # Checking negative

def test_q10_matrixsub():    # I added this test
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixsub(m,1,2) == [[1, 2], [7, 8]]    # Checking 3x3 -> 2x2
	m = [[1,2,3,4], [5,6,7,8], [4,3,2,1], [9,8,7,6]]
	assert py_cw.matrixsub(m,0,1) == [[5,7,8],[4,2,1],[9,7,6]] # Checking 4x4 -> 3x3


def test_q10_determinant():
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	assert py_cw.matrixdeterminant(m) == -406
	# Below are the tests which I added
	m = [[1,2],[3,4]]
	assert py_cw.matrixdeterminant(m) == -2  # All positive 2x2
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixdeterminant(m) == 0  # All positive 3x3
	m = [[1,2,3,4], [5,6,7,8], [4,3,2,1], [9,8,7,6]]
	assert py_cw.matrixdeterminant(m) == 0  # All positive 4x4
	m = []
	assert py_cw.matrixdeterminant(m)==1   #Testing 0x0 matrix
	m = [[5]]
	assert py_cw.matrixdeterminant(m)==5       # Testing 1x1 matrix



def test_q10_minors():
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	assert py_cw.matrixminors(m) == [[-47, 13, 11], [28, 70, 28], [26, 36, -32]]
	# Below are the tests which I added
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixminors(m) == [[-3,-6,-3],[-6,-12,-6],[-3,-6,-3]] # Checking all positive 
	m = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
	assert py_cw.matrixminors(m) == [[-3,-6,-3],[-6,-12,-6],[-3,-6,-3]] # Checking all negative 


def test_q10_cofactors():
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	assert py_cw.matrixcofactors(m) == [[-47, -13, 11], [-28, 70, -28], [26, -36, -32]]
	# Below are the tests which I added
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixcofactors(m) == [[-3,6,-3],[6,-12,6],[-3,6,-3]] # Checking all positive 
	m = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
	assert py_cw.matrixcofactors(m) == [[-3,6,-3],[6,-12,6],[-3,6,-3]] # Checking all negative 

def test_q10_adjoint():
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	assert py_cw.matrixadjoint(m) == [[-47, -28, 26], [-13, 70, -36], [11, -28, -32]]
	# Below are the tests which I added
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixadjoint(m) == [[-3,6,-3],[6,-12,6],[-3,6,-3]] # Checking all positive 
	m = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
	assert py_cw.matrixadjoint(m) == [[-3,6,-3],[6,-12,6],[-3,6,-3]] # Checking all negative 


def test_q10_scale():    # I added this test
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	s=2
	assert py_cw.matrixscale(s,m) == [[16, 8, 4], [4, -6, 10], [2, 8, 18]]
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	s=-2
	assert py_cw.matrixscale(s,m) == [[-16, -8, -4], [-4, 6, -10], [-2, -8, -18]]  # Checking Multiplying by negative
	m = [[0,0,0], [0,0,0], [0,0,0]]
	s=2
	assert py_cw.matrixscale(s,m) == [[0,0,0], [0,0,0], [0,0,0]]  # Checking Multiplying a 0 matrix


def test_q10_inverse():
	m = [[8,4,2], [2,-3,5], [1,4,9]]
	assert round(py_cw.matrixdeterminant(py_cw.matrixmult(m, py_cw.matrixinverse(m)))) == 1
	# Below are the tests which I added
	m = [[1,2,3],[4,5,6],[7,8,9]]
	assert py_cw.matrixinverse(m) == None # Checking if determinant is 0 so no matrix exsits





# I added all the test below


def test_q12_iint():
	n=0
	assert py_cw.iint(n)==[]  #Checking 0 to Empty List
	n=1
	assert py_cw.iint(n)==[1]    #Checking 1 digit number
	n=12
	assert py_cw.iint(n)==[2,1]     #Checking 2 digit number
	n=123
	assert py_cw.iint(n)==[3,2,1]     #Checking 3 digit number
	n=1234
	assert py_cw.iint(n)==[4,3,2,1]    #Checking 4 digit number
	n=12345
	assert py_cw.iint(n)==[5,4,3,2,1]      #Checking 5 digit number

def test_q12_pint():
	l=[]
	assert py_cw.pint(l)==0  #Checking Empty List to zero 
	l=[1]
	assert py_cw.pint(l)== 1  #Checking 1 digit number
	l=[2,1] 
	assert py_cw.pint(l)==12     #Checking 2 digit number
	l=[3,2,1] 
	assert py_cw.pint(l)==123     #Checking 3 digit number
	l=[4,3,2,1] 
	assert py_cw.pint(l)==1234     #Checking 4 digit number
	l=[5,4,3,2,1] 
	assert py_cw.pint(l)==12345     #Checking 5 digit number


def test_q12_iadd():
	I=[3,2,1]
	J=[6,5,4]
	assert py_cw.iadd(I,J)==579   # length of I=J
	I=[4,3,2,1]
	J=[6,5,4]
	assert py_cw.iadd(I,J)==1690  # length of I>J
	I=[3,2,1]
	J=[7,6,5,4]
	assert py_cw.iadd(I,J)==4690  # length of I<J
	I=[0]
	J=[0]
	assert py_cw.iadd(I,J)==0  # length of I=J=0
	I=[]
	J=[]
	assert py_cw.iint(py_cw.iadd(I,J))==[]   # Adding empty list and coverting the answer back to a number
	assert py_cw.iadd(I,J)==0					# Adding empty list





def test_q12_imult():
	I=[3,2,1]
	J=[6,5,4]
	assert py_cw.imult(I,J)==56088   # length of I=J
	I=[4,3,2,1]
	J=[6,5,4]
	assert py_cw.imult(I,J)==562704  # length of I>J
	I=[3,2,1]
	J=[7,6,5,4]
	assert py_cw.imult(I,J)==561741 # length of I<J
	I=[0]
	J=[0]
	assert py_cw.imult(I,J)==0  # length of I=J=0
	I=[]
	J=[]
	assert py_cw.iint(py_cw.imult(I,J))==[]   # Multiplying empty list and coverting the answer back to a number
	assert py_cw.imult(I,J)==0					# Multiplying empty list


def test_q12_ipow():
	# if J = [0]
	I=[1,2]
	J=[0]
	assert py_cw.ipow(I,J)==1 
	# J = [1]
	I=[1,2]
	J=[1]
	assert py_cw.ipow(I,J)==21
	# length of I=J
	I=[2,1]
	J=[5,4]
	assert py_cw.ipow(I,J)==3657261988008837196714082302655030834027437228032 
	# length of I>J 
	I=[3,2,1]
	J=[1,2]
	assert py_cw.ipow(I,J)==77269364466549865653073473388030061522211723
	# length of I>J
	I=[2,1,2,8]
	J=[5,4]
	assert py_cw.ipow(I,J)==141319577848423534816985530004935988154464775265690467168900925290886240746147681471703424434391508063007158167767107082269902059132866566858300451951657998031186099739172012032
	# length of I<J
	I=[3,2]
	J=[3,2,1]
	assert py_cw.ipow(I,J)==310830645388221229862399853154632371436178147989403533068374140330232726646012654829356036792658947360110570975113008772299548005313894389199908475841673438748632602567




	




