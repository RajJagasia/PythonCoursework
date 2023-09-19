# PUT YOUR NAME HERE             Raj Dinesh Jagasia    <--- so we know who you are
# PUT YOUR UserID HERE             rj2011 , H00376443  <--- so we know who you are
# F28PL Coursework 1, Python         <--- leave this line unchanged 

# Deadline is Wednesday 27 October 2021 at 15:30, local time for your campus (Edinburgh or Dubai).

# It is not your marker's role to debug basic syntax errors.
# Therefore, if your script won't compile then it might not be marked.
# In other words: if `python3 py_cw.py` won't execute, then your marker is not obliged to mark your answers. 

# To do this coursework, FORK, THEN CLONE the gitlab project.

# If you do it the other way around, then you'll have cloned *my* project (which you can't `git push` to), rather than cloned *your fork* of the project (which you can `git push` to).  
# Any questions, don't guess: ask.

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# The test file test_cw.py is not exhaustive. 
# Just because your answer passes it does not mean it's correct.
# You would do well to consider where errors might be lurking and to add these to test_cw.py.   
# You are not marked directly on the quality of additional tests, however your marker may be
# able to assign marks for understanding as demonstrated in any tests you may write, 
# even if the code itself isn't quite right. 


# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  


# Do not delete the text from here ... 
################################################################################
# Question 1   


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here


#####################################
# Question 1a
'''
Before Writing the code for every function I have written a General Description as to prevent writing more comments beside the code
as it will make it harder to read,
So the comments besides the code will very less as the main explaination is done in General Description
'''
'''
General Description

c1-->This parameter gives us a tuple with 2 elements
c2-->This parameter also gives us a tuple with 2 elements
ans_cadd-->I created this tuple which stores the answer.(I declared this as it makes the code more readable)

'''
def cadd(c1, c2):
    ans_cadd=(c1[0]+c2[0],c1[1]+c2[1])  # I did basic complex number addition by using indexing 
    return ans_cadd

'''
General Description

c1-->This parameter gives us a tuple with 2 elements
c2-->This parameter also gives us a tuple with 2 elements
ac,adi,bci,bdi2---> there was no need to declare these but I did it to make the code mode readable
ans_cmult-->I created this tuple which stores the answer.(I declared this as it makes the code more readable)

'''

def cmult(c1,c2):
    ac=c1[0]*c2[0]
    adi=c1[0]*c2[1]
    bci=c1[1]*c2[0]
    bdi2=c1[1]*c2[1]*-1
    anscmult=(ac+bdi2,adi+bci)     # I did basic complex number multiplication by using indexing 
    return anscmult
    


#####################################
# Question 1b

'''
General Description

x1-->This parameter gives us an integer (this should be converted to the real part)
x2-->This parameter also gives us an integer (but this should be converted to the imaginary part)
There was no need to declare any variable as the code is very readable.

'''

def tocomplex(x1, y1):
    return x1 + y1 * 1j    # returning x1(as it is as it is the real part) and y1(multiplying it to 1j to make it the imaginary part)

'''
General Description

c-->This parameter gives us a complex number which should be converted to a tuple with 2 elements
There was no need to declare any variable as the code is very readable.

'''

def fromcomplex(c):
    return (c.real,c.imag)   # returning the real and imaginary part in a tuple


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions 
* seqaddi and 
* seqmulti 
that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[-1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqaddlc and seqmultlc.
"""

#####################################
# Question 2a

'''
General Description

l1--> A list with some integers
l2--> Also a list with some integers
Assuming that the length of l1 and l2 is same
ansSeqAddi--> This is a list which will contain the answer
The is done by using a 'for loop'.
'''
def seqaddi(l1, l2):
    ansSeqAddi=[]
    for i in range(len(l1)):         #As the length of both list are same we can use len(l1) or len(l2)
        ansSeqAddi+=[l1[i]+l2[i]]    #Appending the the sum of each of the integers(based on the index) to ansSeqAddi

    return ansSeqAddi    # Returning the Answer

'''
General Description

l1--> A list with some integers
l2--> Also a list with some integers
Assuming that the length of l1 and l2 is same
ansSeqMulti--> This is a list which will contain the answer
The is done by using a 'for loop'.
'''

def seqmulti(l1, l2):
    ansSeqMulti=[]
    for i in range(len(l1)):          #As the length of both list are same we can use len(l1) or len(l2)
        ansSeqMulti+=[l1[i]*l2[i]]    #Appending the the product of each of the integers(based on the index) to ansSeqMulti

    return ansSeqMulti    # Returning the Answer
   


#####################################
# Question 2b

'''
General Description

l1--> A list with some integers
l2--> Also a list with some integers
Assuming that the length of l1 and l2 is same
ansSeqAddr--> This is a list which will contain the answer for the specific recursion
The is done by using 'Recursion'.-->Recursion basically means calling the function within itself 
'''

def seqaddr(l1, l2):
    ansSeqAddr=[]
    if len(l1)==1:             #Base case
        return [l1[0] + l2[0]]
    else:                     #Step case
        ansSeqAddr += [l1.pop(0)+l2.pop(0)]    #Appending the the sum of each of the popped (based on the index) integers to ansSeqAddr
        return ansSeqAddr + seqaddr(l1,l2)     # Returning the sum of ansSeqAddr and calling the function 'seqaddr(l1,l2)' again.

'''
General Description

l1--> A list with some integers
l2--> Also a list with some integers
Assuming that the length of l1 and l2 is same
ansSeqMultr--> This is a list which will contain the answer for the specific recursion
The is done by using Recursion'.-->Recursion basically means calling the function within itself 
'''

def seqmultr(l1, l2):
    ansSeqMultr=[]
    if len(l1)==1:             #Base case
        return [l1[0] * l2[0]]
    else:                     #Step case
        ansSeqMultr += [l1.pop(0)*l2.pop(0)]    #Appending the the product of each of the popped (based on the index) integers to ansSeqMultr
        return ansSeqMultr + seqmultr(l1,l2)     # Returning the sum of ansSeqMultr and calling the function 'seqmultr(l1,l2)' again.



#####################################
# Question 2c
'''
General Description

l1--> A list with some integers
l2--> Also a list with some integers
Assuming that the length of l1 and l2 is same
ansSeqAddlc--> This is a list which will contain the answer
The is done by using 'List Comprehension'.-->It is basically using a for loop and the conditional test inside with one line of code
                                          --->This makes the code look neat and shorter 
'''

def seqaddlc(l1,l2):
    ansSeqAddlc=[x+l2[l1.index(x)] for x in l1 ]    #Appending the the sum (of x(it is element of l1 the index is on) and l2(index is the index of x in l1)) to ansSeqAddlc
    return ansSeqAddlc    # Returning the Answer

'''
General Description

l1--> A list with some integers
l2--> Also a list with some integers
Assuming that the length of l1 and l2 is same
ansSeqMultlc--> This is a list which will contain the answer
The is done by using 'List Comprehension'.-->It is basically using a for loop and the conditional test inside with one line of code
                                          --->This makes the code look neat and shorter 
'''


def seqmultlc(l1,l2):
    ansSeqMultlc=[x*l2[l1.index(x)] for x in l1 ]   #Appending the the product (of x(it is element of l1 the index is on) and l2(index is the index of x in l1)) to ansSeqMultlc
    return ansSeqMultlc    # Returning the Answer




# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3

"""
Write functions
* ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
* matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have it the other way around that's fine; just make sure to clearly explain your code).
* matrixadd
Matrix addition, which is simply pointwise addition.
* matrixmult
Matrix multiplication, which is not simply pointwise multiplication.

In the programs above, you do not need to write error-handling code, e.g. for the cases that 
inputs do not represent matrices or represent matrixes of the wrong shapes.
So for instance your matrixshape may assume that the argument has successfully passed the test 
ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.

You would do well to carefully comment your code, so your marker might award some marks
even for imperfect results. 
"""

'''
General Description

m--> this is a 2D list or a matrix
In this we have to check if m is in the correct format of a matrix(all the columns are of equal length in every row)
ans_ismatrix-->This is a boolean will hold True or False
check--->This is a list that will hold the length of all the rows.
chk--> This will hold the 1st element of the list check
Then I will run a for loop and check if all the elements of check is equal to chk (which is the first element).
If all the elements of the check are equal to chk (It means that all rows are of equal length thus there are a equal number of columns in each row)
 it will set ans_ismatrix to True  and later on return ans_ismatrix
If anyone of the elements is not equal to chk it will return False 
'''
def ismatrix(m):
    check=[]
    ans_ismatrix=False
    for i in m:        
        check+=[len(i)]    #Appending the length of each row to check 
    chk=check[0]           #it is equal to the 1st element of the list
    for i in check:        #iterating through check
        if chk==i:          
            ans_ismatrix=True
        else:
            return False  #If chk is not equal to the m[index] it will return False 
    return ans_ismatrix 

        
'''
General Description

m--> this is a matrix
In this we have to return rows and cols of a matrix in the form of a tuple.
rows---> Number of rows 
cols---> Number of columns
'''


def matrixshape(m):
    # Number of rows first, and number of columns second
    if m==[]:        # If m is a empty list 
        return (0,0)   #Both rows and cols would be 0
    else:
        rows=len(m)    
        cols=len(m[0])   # length of the first list of m as length of all the rows are same
        return (rows,cols)

'''
General Description

m1--> this is a matrix
m2--> this is also a matrix
In this we have to add 2 matrix 
ansMatrixAdd---> will contain the answer of the addition

We start by iterating through the rows of m1, then we iterate through the elements of each row.
We also create a temp list which will contain the sum of the element at indexes of l1 and l2  for each row 
after iterating through the whole rows(while appending the sum to temp) the list temp will be added to ansMatrixAdd
After this the temp value will again be equal to a empty list so that it can hold the elements for the next row

this will keep on repeating unill we have iterated through all the rows and then when we are done we will return ansMatrixAdd

'''  

def matrixadd(m1,m2):
    ansMatrixAdd=[]

    for i in range(len(m1)):        # iterating by row of m1
        temp=[]

        for j in range(len(m1[i])):        # iterating by columns of m1
            temp+=[m1[i][j]+m2[i][j]]   # Appending the sum of the elements of the ith row in a list temp

        ansMatrixAdd+=[temp]         #Appending the temp list to the final list for every row

    return ansMatrixAdd


'''
General Description

m1--> this is a matrix
m2--> this is also a matrix
In this we have to multiply 2 matrix 
ansMatrixMult---> will contain the answer 

We start by creating the proper dimensions for ansMatrixMult as the rows and cols would be different compared to both the original matrix
The rows of ansMatrixMult will be same as the rows of m1 and the cols of ansMatrixMult will be same as m2---> For this I will use matrixshape function that i had declared before
Then I will use 'List Comprehension' 2 for loops and make ansMatrixMult with the dimension rows,cols with each element initially set to zero 
Then I will run for loops again to find the answer for each multiplication and keep on appending to ansMatrixMult

This will keep on repeating unill we have iterated through all the rows and cols of m1 and m2. 
After the whole multiplication is done i will return ansMatrixMult


'''  


def matrixmult(m1,m2):

    rows=matrixshape(m1)
    cols=matrixshape(m2)

    # We Start by creating a a matrix with required dimensions a all elements 0. Later on we change the value of each element
    ansMatrixMult=[[0 for j in range(cols[1])]for i in range(rows[0])]  #List Comprehension

    for i in range(len(m1)):       # iterating by row of m1
        for j in range(len(m2[0])):     # iterating by column by m2

            for k in range(len(m2)):    # iterating by rows of m2
                ansMatrixMult[i][j] += m1[i][k] * m2[k][j]  # Adding the values to the same element until when the whole row is multiplied to the whole column
                                                            #After that it will go to the next element
    return ansMatrixMult



# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
* Mutable vs immutable types. Give at least two examples of each, with explanation.
* Integer vs float types.
* Assignment = vs equality == vs identity is.
* The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
* Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""

#Answer To Question Q4

#1)Mutable vs immutable types
'''
    Whenever an object is instantiated in python, it is assigned a unique object id.
    If it is a Mutable Type we can change it's contents without changing its object id.
    If it is a Immutable Type we can't change it's contents without changing its object id. 
    Thus when we change a immutable type we are creating a new object.


    Mutable Types -----> It can be changed after creating it.

    Examples-->List, Sets, etc.

    Proof 1
    
    Code

    name = ["Raj"]
    id_of_name= id(name)
    name += ["Jagasia"]
    new_id_of_name = id(name)
    if new_id_of_name == id_of_name:
        print ("List is Mutable")
    else:
        print("List is Immutable")


    Output

    List is Mutable

    Proof 2

    Code

    name = ["Raj","","Jagasia"]
    name[1]="D"
    print(name)


    Output

    ['Raj', 'D', 'Jagasia']

    From Proof 1, we get to know that if we add a new element to a list it's id won't change.
    From Proof 2, we get to know that if we want change the the value for any index for a list we can do it 


    Immutable Types -----> It cannot be changed after creating it.

    If we change the value of a immutable type it will create a new object.

    Examples-->Tuples, Strings, FrozenSet, int, float, etc.

    Proof 1
    
    Code

    name = "Raj"
    id_of_name= id(name)
    name += " Jagasia"
    new_id_of_name = id(name)
    if new_id_of_name == id_of_name:
        print ("String is Mutable")
    else:
        print("String is Immutable")


    Output

    String is Immutable

    Proof 2

    Code

    name = "Raj Jagasia"
    name[3]="D"
    print(name)

    Output

    TypeError: 'str' object does not support item assignment

    From Proof 1, we get to know that if we add a new element to a string it's id will change.
    From Proof 2, we get to know that if we want change the the value for any index for a string we can't do it 
'''



#2)Integer vs float types.

'''
Integer Types ----->
->They are Whole Numbers(Thus they are without decimal values)
->They can be Positive or Negative
->Can convert to integer by using int()
>>> int(5.5)#5.5 is a floating point number (can't be used for string,list,tuple,etc.)
5 
->They are infinite precision


Proof 1

Code
>>> def example1(n): # Recursive function
        if n==0: 
            return 3
        else:
            return 3**(example1(n-1))

>>>example1(0)
3
>>>example1(1)
27
>>>example1(2)
7625597484987
>>>example1(3)
# It crashes my machine

->Python eats memory, trying to calculate an extremly large number to infinite precision as integers are infinite precision.



Float Types ----->
->They are Floating Point Numbers(Thus they are with decimal values)
->They can be Positive or Negative
->Can convert to Floating Point Number by using float()
>>> float(5)#5 is a Integer Type number (can't be used for string,list,tuple,etc.)
5.0 
->They aren't infinite precision

Proof 1

Code
>>> def example1(n): # Recursive function
        if n==0: 
            return 3.0
        else:
            return 3.0**(example1(n-1))

>>>example1(0)
3.0
>>>example1(1)
27.0
>>>example1(2)
7625597484987.0
>>>example1(3)
#OverflowError: (34, 'Result too large')

->Python doesn't eat memory, trying to calculate an extremly large number to infinite precision as floats aren't infinite precision.
->But if you want arbitrary precision floats you can use a package -- 'mpmath'
'''
#Assignment = vs equality == vs identity is.
'''
3)Assignment '='
The “=” is an assignment operator is used to assign the value on the right to the variable on the left.

Code

>>> n=10          # Assigning 10 to a variable n
>>> n=[1,2]       # Assigning a list to a variable n
>>> m=n           # Making m and n point to the same object(their ids would be same)

Equality '=='
The ‘==’ operator checks whether the two given operands are equal or not. If so, it returns true. Otherwise it returns false
It only checks if the value of both is equal, It doesn't check if the id is equal.

Code

>>> n=[1,2]       # Assigning a list to a variable n
>>> m=n           # Making m and n point to the same object(their ids would be same)
>>> id(m)
1700517935816
>>> id(n)
1700517935816
# id of m and n is same
>>> m==n
True
>>> x=[1,2]   
>>> y=[1,2]
>>> id(x)
1700517933768
>>> id(y)
1700517387016
# id of x and y is not same
>>> x==y
True


Identity 'is'
An 'is' expression evaluates to True if two variables point to the same (identical) object.Otherwise it returns false
It only checks if the id of both is equal(They should point to the same object), even if the value is same but the id is different it will return false

>>> n=[1,2]       # Assigning a list to a variable n
>>> m=n           # Making m and n point to the same object(their ids would be same)
>>> id(m)
1700517935816
>>> id(n)
1700517935816
# id of m and n is same
>>> m is n
True
>>> x=[1,2]   
>>> y=[1,2]
>>> id(x)
1700517933768
>>> id(y)
1700517387016
# id of x and y is not same
>>> x is y
False
'''
#The computational effects of a call to list on an element of range type, as in list(range(5**5**5)).
'''
4) This gives the following error---> OverflowError: Python int too large to convert to C ssize_t

This is because we will get an OverflowError if the list has more elements than can be fit into a signed long:[1]
Maximum Elements in a list
On 32bit Python: 2**31 - 1
On 64 bit Python: 2**63 - 1
You can get a MemoryError even for values just under that.

5*5*5 = 19110125979454775203564045597039645991980810489900.....(it continues )
2*63 = 9223372036854775808 

2*63 is much much smaller than 5*5*5 thus it shows an error

Referenced Sites
[1]-->https://stackoverflow.com/
'''

# Slices, with examples. Including an explanation of the difference in execution between
 #list(range(10**10)[10:10]) and
 #list(range(10**10))[10:10]
'''
5)Slicing to used to extract parts from list, strings, tuples, etc
There are 2 ways to slice
->Indexing
->Using slice() function
The slice() function returns a slice object.
A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. 
You can also specify the step, which allows you to e.g. slice only every other item. [1]

Examples

By Slice Function
>>> a = ("a", "b", "c", "d", "e", "f", "g", "h")
>>> x = slice(0, 8, 3)
>>> print(a[x])
('a', 'd', 'g')

By Indexing
>>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> nums[2:7]
[30, 40, 50, 60, 70]
>>> nums[slice(2,7)]
[30, 40, 50, 60, 70]


>>> list(range(10**10)[10:10])  # Slices the range before converting in into a list , It runs very fast
[]                              #It doesnt show memory error as it has to 1st slices the range then covert it into a list thus a lot of memory is saved
>>> list(range(10**10))[10:10]  # Slices the range after converting in into a list , It runs very very slow 
MemoryError                     #It shows memory error as it has to 1st convert the elments to a list then slice it 

Referenced Sites
[1]-->www.w3schools.com



'''




# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5
print()
print('Question 5')

"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
* encdat(-5) should return '-5'
* encdat(5.0) should return '5.0'
* encdat(5+5j) should return '5+5j' -- NOTE: not '(5+5j)'.
* encdat('(5))(') should return '(5))('

Do not just immediately hit the input with `str`, using it as a function that inputs an integer, float, complex number or string, and returns a string, since that guts the question. 
"""
'''
General Description

dat--->This is any data type -- integer, float, complex number or string.
In this we have to take dat and return it as a string
type_dat---> This holds the type of that

I will start by checking if type_dat is a string, if it is I will return dat itself as a string is already in string format, 
there is no need to waste any resources converting a string to a string.

Then I will check if it is a complex Number, if it is I will use f"{}" to convert it to a string and 
then slice it in such a way that it returns the string without the brackets.

At last if it is any other data type they all will be returned back as a string as there is no need 
to declare for every other individual data type and make the code unnecessarily long and complex

**In this code I used f"{}" but instead of this I could also use the str() function or the format() function.

'''  

def encdat(dat):
    type_dat=type(dat)           #Checking the type of dat
    if type_dat == str:      
        return dat                  #If it is a string just returning the same thing back
    elif type_dat == complex:
        return f"{dat}"[1:-1]     #Returning the sliced version of the string of a complex number (sliced means without the brackets over here)
    else: 
        return f"{dat}"             #If it is any other data type just returning the string of the data type
    



# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""
'''
General Description

i--> This is an integer
We have to basically take in an integer and encode it using this ---> f(n+1) = [f(n),[f(n)]] 
So I declared a base case that if i is equal to 0 it will return [] (an empty list)

Step Case-> If 'i' is not equal to 0 then we call the same function again while decrementing i by 1 in this way [fenc(i-1),[fenc(i-1)]]
(This is a recursive function)
''' 

def fenc(i):
    if i==0:  # Base Case 
        return []
    else:        #Step Case
        return [fenc(i-1),[fenc(i-1)]]   # Taken from the question

'''
General Description

l--> This is a list which contains more lists in the form of  f(n+1) = [f(n),[f(n)]] 
We have to basically decode the list back to an integer 
count-->I declared this to count which integer we are on and return the final integer

Then I will start an infinite loop 

list--> I declared this variable as this will contain the encoding of the current value of count, it's value will change on every loop

Then I will check if my 'list' is equal to the given 'l' 
If Yes then it will return the current count

If it is not equal it will increment count by 1 and continue looping


''' 


def fdec(l):
    count=0    
    while True:      #Infinite loop
        list=fenc(count)   #Encoding the list bast on integer count
        if l==list:         # Checking if it is equal to the l 
            return count 
        else:
            count+=1





# END ANSWER TO Question 6
################################################################################


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can't manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""


'''
General Description

In this we have implement a generator and returns the text for any finite number of calls 

colbaselist-->This is a list which contains the 3 'cycle of life' text ---> eat, sleep, code 
colanslist--->This is a list which will contain the answer of the finite calls
**There is no actual need for this according to the test case and I am also not returning colanslist 
but if we need the list not the current element needed we can return this by changing the code a bit

We Start an infinite loop
Then we use a for loop to iterate through the colbaselist

i-->It is the current index it will contain either eat,sleep or code

Then for every iteration our colanslist will be appended with the current value of 'i'(the index) 
And at the same time it will also yield 'i'(The index )

'''


def cycleoflife():
    colbaselist=['eat','sleep','code']    # Our base list
    colanslist=[]                         # I made this as this contain the list
    while True:
        for i in colbaselist:
            colanslist+=[i]              #Adds the value to our anslist
            yield i                      #It will yield the current element
    




# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""


'''
General Description

datum-->List of data
In this we have convert datum to a list of integers

We will do this by recursion
Base Case --> If the type of datum is not a list
it will return datum

Step Case--> it will use a recursive function
Instead of using 2 for loops and making the code look larger I used List Comprehension as this makes the code look neat and shorter

'''

def gendat(datum):
    if type(datum) != list:       # Base Case 
        return [datum]  
    else:                         #Step Case
        return [data for l in datum for data in gendat(l)] # Using Recursion 



# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""

'''
General Description

In this we have implement a generator and returns the nth prime number for n number of calls (where n is the given number )

num---> We will set this value to 2 first as the 1st prime mumber is true 

We Start an infinite loop
x-->A
Then we use a for loop to iterate through the colbaselist
checker--> A boolean that stores True or False 
Then we will run a for loop to go from 2 till the number berfore the current number  --- We do this to check whether the current value of num is a prime number or not
We will use if statement to check whether the number gives us a remainder as 0 when divided by the range of numbers in the for loop 
If it gives the remainder as 0 then it is not a prime number and the value of checker will be set to false
If it does then ut is a prime number

Then outside the for loop we will check if our checker value is true or not -- if it is true we will yield that number

Regardless if checker is true or false at the end we will increment our num by 1 

**I have commented the reference code 
'''

def eratosthenes():
    num=2
    while True:
        checker=True
        for i in range(2,num):
            if num % i == 0:      #If the remainder is equal to 0, checker will be set to false
                checker=False
        if checker==True :
            yield num             #If the value of checker is true it will yield the number
        num+=1                    #Incrementing the value of num by 1


'''
# For reference, here is an implementation of the sieve of Eratosthenes, 
# whose argument acts as a bound on the returned generator (40000, by default). 
# Your answer should take no argument, and should return an unbounded generator.
def eratosthenes(z=40000):
    # create an array of true values the size of z
    A = [True] * z
    # iterate over each value to z squared
    for x in range(2, int(z ** 0.5)):
        # if A[x] has a true value
        if A[x]:
            # iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                # set anything in the range to false
                A[z] = False
    # iterate over the array
    for y in range(2, len(A)):
        # if a value is true that index is a prime number
        if A[y]:
            # yield the current iterator location as it is a prime
            yield y
'''



# END ANSWER TO Question 9
################################################################################


################################################################################
# Question 10

"""
Following on from Question 3, invertible matrices are explained here:
   https://en.wikipedia.org/wiki/Invertible_matrix
   https://en.wikipedia.org/wiki/Minor_(linear_algebra)#Inverse_of_a_matrix

Write and test an algorithm to calculate the inverse of an n x n matrix (i.e. a square matrix) using Cramer's rule, for n>=1.

* Your answer should include helper functions (and tests for them) to calculate the
* *determinant*,
* *minors*,
* *cofactors*, and
* *adjoint* of a matrix, all of which are described here:
   https://en.wikipedia.org/wiki/Minor_(linear_algebra)
   https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
* Your code will be marked on clarity as well as correctness.  Code that is "correct" but unreadable, is bad code and therefore may get bad marks.

Writing, documenting, and testing helper functions is generally good practice, and you will likely find other helper functions are required, such as for matrix transpose, computing a sub-matrix, multiplying a matrix by a scalar, and perhaps others.  

Whatever you do, just make sure you explain what you're doing and why. 
"""

'''
General Description

m--> this is a matrix
In this we have to transpose the given matrix -- It means the rows will become cols and cols will be rows
ansMatrixTranspose---> will contain the answer 
dim-->contains the length of the rows (In n x n matrix rows and cols are equal)

We start by creating the proper dimensions for ansMatrixTranspose but as we are considering a n x n matrix rows will be equal to cols

Then I will use 'List Comprehension' with 2 for loops and make ansMatrixTranspose with dim with each element initially set to zero 

Then I will run for loops to find the answer ansMatrixTranspose[rows][cols]==m[cols][rows] and keep on appending to ansMatrixMult

This will keep on repeating until we have iterated through all the rows and cols of m and appended everything to ansMatrixTranspose
After rows is cols and cols is rows will return ansMatrixMult


'''  

def matrixtranspose(m):
    dim=len(m)                       # dimensions of the matrix to make a new empty matrix (rows=cols for n x n matrix)
    ansMatrixTranspose=[[0 for j in range(dim)]for i in range(dim)] #Creating matrix with all elements as 0 by List Comprehension

    for i in range(dim):            #Iterating through rows
        for j in range(dim):            #Iterating through cols
            ansMatrixTranspose[i][j]=m[j][i]    #ansMatrixTranspose[rows][cols]==m[cols][rows] rows is cols and cols is rows

    return ansMatrixTranspose
    
'''
General Description

m--> this is a matrix
p-->This is a row
q-->This is a col
In this we have to delete given row and col from the matrix -- It means that if we had an nxn matrix now the new size will be n-1 x n-1
And then we have to return the sub matrix

ansMatrixsub---> will contain the answer 
lenm-->contains the length of the rows of the original matrix (In n x n matrix rows and cols are equal)

We start will use 'List Comprehension' with 2 for loops and make ansMatrixsub with lenm with each element initially set to zero 

Then I will use 2 for loops and make ansMatrixsub equal to our given matrix
We do it this way instead of directly assigning 'ansMatrixsub=m' 
because if we do 'ansMatrixsub=m' it will result in both ansMatrixsub and m pointing to the same object,
so if we change 'ansMatrixsub' our m will also change and we don't want to do that so thus I made a matrix with identical elements but pointing to different objects


Then I will remove the row to be removed directly by .remove() function

After that I will itertate through each row and remove the column by .remove() function

After this I will return the answer
'''  

def matrixsub(m, p, q):  #m is matrix, p is the row, q is the col

    lenm=len(m)                         # dimensions of the matrix
    ansMatrixsub=[[0 for j in range(lenm)]for i in range(lenm)]  #Creating matrix with all elements as 0 by List Comprehension

    # Iterating through each element of the matrix
    for i in range(lenm):
        for j in range(lenm):
            ansMatrixsub[i][j]=m[i][j]   # Making every element of ansMatrixsub identical to m
            
    ansMatrixsub.remove(ansMatrixsub[p])   # Removing the row


    for i in range(len(ansMatrixsub)):     #Iterating through rows
        ansMatrixsub[i].remove(ansMatrixsub[i][q])       # Removing the mentioned column

    return ansMatrixsub   

'''
General Description

m--> this is a matrix
In this we have to find and return the determinant of the matrix 

We will use 'Recursion' for this

if it is a 0x0 matrix it determinant is 1 thus it will return 1
if it is a 1x1 matrix it will return the number itself
if it is a 2x2 matrix it will do the determinant calculation and return it  ----> This is also my base case
if it is a 3x3 matrix I will find the sum of the cofators of each element in 1st row(0th index) for this I will use 'recursion'--->This is my step case
for the rest nxn matrix it will follow same as the explaination of 3x3 matrix  

I will use matrixsub function for which I wrote the code before.

matrixsub-->Using this to detete the row and col and get a smaller matrix(Determinant calculation)
sumcofactor-->This will contain my answer for 3x3 or larger matrix

After this I will return the answer

'''  

def matrixdeterminant(m):
    if len(m)<1:
        return 1    #for 0x0 matrix determinant is 1

    elif len(m)==1:
        return m[0][0]              #for 1x1 matrix determinant is the number itself

    elif len(m)==2:                    #Base Case
        two_by_two_ans=(m[0][0]*m[1][1])-(m[0][1]*m[1][0])
        return two_by_two_ans               #for 2x2 matrix determinant is by the calculation

    else:                       #Step Case
        sumcofactor=0    
        for i in range(len(m)):      
            # Will go through all the elements in the 1st row and add them to sumcofactor
            sumcofactor+= ((-1)**(0+i)) * m[0][i] * matrixdeterminant(matrixsub(m,0,i))     #Recursive Function
            # matrixsub-->Using this to detete the row and col and get a smaller matrix(Determinant calculation)

        return sumcofactor

'''
General Description

m--> this is a matrix

In this we have to return minors of the given matrix
ansMatrixMinors---> will contain the answer 
lenm-->contains the length of the rows of the original matrix (In n x n matrix rows and cols are equal)

We start will use 'List Comprehension' with 2 for loops and make ansMatrixMinors with lenm with each element initially set to zero 

Then I will use 2 for loops and make ansMatrixMinors equal to it's determinant 
by using the matrixdeterminant and matrixsub function for which I wrote the code before.

After this I will return the answer
'''  

def matrixminors(m):
    lenm=len(m)
    ansMatrixMinors=[[0 for j in range(lenm)]for i in range(lenm)]  #Creating matrix with all elements as 0 by List Comprehension

    # Iterating through each element of the matrix
    for i in range(lenm):
        for j in range(lenm):

            ansMatrixMinors[i][j]= matrixdeterminant(matrixsub(m,i,j))  
            # matrixdeterminant-->Using this to find determinant(Determinant calculation)
            # matrixsub-->Using this to detete the row and col and get a smaller matrix(Determinant calculation)
    
    return ansMatrixMinors

'''
General Description

m--> this is a matrix

In this we have to return cofactors of the given matrix
ansMatrixCofactor---> will contain the answer 
lenm-->contains the length of the rows of the original matrix (In n x n matrix rows and cols are equal)

We start will use 'List Comprehension' with 2 for loops and make ansMatrixCofactor with lenm with each element initially set to zero 

Then I will use 2 for loops and make ansMatrixCofactor equal to it's determinant * -1**(i+j) 
(i and j is the row and column it depend on this whether the element will be multiplied by -1 or 1)

by using the matrixdeterminant and matrixsub function for which I wrote the code before.

After this I will return the answer
'''  

def matrixcofactors(m):
    lenm=len(m)
    ansMatrixCofactor=[[0 for j in range(lenm)]for i in range(lenm)]  #Creating matrix with all elements as 0 by List Comprehension

    # Iterating through each element of the matrix
    for i in range(lenm):
        for j in range(lenm):

            ansMatrixCofactor[i][j]= ((-1)**(i+j)) * matrixdeterminant(matrixsub(m,i,j)) 
            # matrixdeterminant-->Using this to find determinant(Determinant calculation)
            # matrixsub-->Using this to detete the row and col and get a smaller matrix(Determinant calculation)

    return ansMatrixCofactor

'''
General Description

m--> this is a matrix

In this we have to return Adjoint of the given matrix

Adjoint is the transpose of the cofactors of the matrix and as I have already typed the code those functions before I will call them

Thus I will return the transpose of the cofactors of the matrix
'''  

def matrixadjoint(m):
    return matrixtranspose(matrixcofactors(m))  

'''
General Description

m--> this is a matrix
s--> A number
In this we have to multiply s with each element of the matrix

ansMatrixScale---> will contain the answer 
lenm-->contains the length of the rows of the original matrix (In n x n matrix rows and cols are equal)

We start will use 'List Comprehension' with 2 for loops and make ansMatrixsub with lenm with each element initially set to zero 

Then I will use 2 for loops and make ansMatrixScale equal to our given matrix * s(the provided number)

After this I will return the answer
'''  


def matrixscale(s, m):
    lenm=len(m)
    ansMatrixScale=[[0 for j in range(lenm)]for i in range(lenm)]  #Creating matrix with all elements as 0 by List Comprehension

    # Iterating through each element of the matrix
    for i in range(len(m)):
        for j in range(len(m)):
            ansMatrixScale[i][j]=m[i][j]*s     # Making every element of ansMatrixScale equal to m * s
         
    return ansMatrixScale

'''
General Description

m--> this is a matrix

In this we have to find inverse of the matrix

ansMatrixScale---> will contain the answer 
adjoint_matrix---> will contain the adjoint
det_to_multiply--> will contain the 1/Determinant value

There was no need to create the above 3 variables but did this to make the code more readable

We will check first if the determinant of matrix is 0, if it is 0, it has no inverse. Thus returning None.

If it is not equal to 0
then we will use the formula for inverse
I have already type code for the helper funnctions before and i will call them and then return the answer

'''

def matrixinverse(m):
    if matrixdeterminant(m)==0:
        return None   # As no inverse possible
    else:
        adjoint_matrix=matrixadjoint(m)     #Finding Adjoint
        det_to_multiply=1/matrixdeterminant(m)        #Finding 1/Determinant value
        ansMatrixInverse=matrixscale(det_to_multiply,adjoint_matrix)      #Multiplying 1/Determinant value to adjoint and thus finding the inverse
        return ansMatrixInverse
        #Can also write it this way in 1 line --> return matrixscale(1/matrixdeterminant(m),matrixadjoint(m))
        #But I wrote in the above way so that even if the code is a bit long its more readable

# END ANSWER TO Question 10
################################################################################


###############################################################################
# Question 11

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""


"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious[1], tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 

#Answer
'''
Python has many modern uses and Applications. It’s perfect for web development, the Internet of Things, machine learning, startups, and fintech among many others.[3]

Python is such a stable, flexible, and simple programming language, it’s perfect for various machine learning (ML) and artificial intelligence (AI) projects. [1]
It has Amazing Libraries. Whether you’re looking to create a simple graphical representation or a more interactive plot, you can find a library to match your needs. Examples include Pandas Visualization and Plotly. [1]

The language is easy-to-learn, flexible, and well-supported, meaning it’s relatively quick and easy to use for analyzing data. [1]
You can program all kinds of applications using Python. Whether it’s blockchain applications, audio and video apps, or machine learning applications, you can build them all with Python. It has also inspired the creation of new programming languages. It can also be used to develop graphic design applications.[1]
The applications of Python are numerous and so are its benefits. [3]



Python is quickly ascending to the forefront of the most popular programming languages in the world.[2]
According to the TIOBE index, which measures the popularity of programming languages, Python is the third most popular programming language in the world, behind only Java and C. [1]

There are many reasons for the ubiquity of Python, including Its versatility, its ease of use, Its simple syntax, Its thriving community, its Great Corporate Sponsors, its Amazing Libraries, its Reliability and Efficiency, Accessibility, its Healthy, Active and Supportive Community, etc. [1][3]
Python is both object-oriented and functional and it is a high-level programming language.

For those who are new to coding and programming, Python can be an excellent first step. It’s relatively easy to learn, making it a great way to start building your programming knowledge. Python is relatively easy to read and understand, as its syntax is more like English.
As it’s an open-source language, anyone can use Python to code. Python has a healthy community of enthusiasts that strive every day to make the language better by fixing bugs and opening new possibilities. And, as mentioned before, it also enjoys strong support from the world’s largest corporations. One of them is Google. They are actively working on guides, tutorials, and other resources to get the most out of Python.[3]
Python is portable and highly flexible, meaning, a Python code written for a Windows machine, or a Linux machine can also run-on iOS, and vice versa – you don’t need to make any alterations in the code.[2]



Based on the previous elaborations, we could imagine that Python will stay on top for ages to come. But like every technology, Python has its own weaknesses. [4]
Some of them are Speed, Whitespaces, Scope, Lambdas, Runtime Errors, etc.[4]

Python is slow. Like, really slow. On average, we need about 2–10 times longer to complete a task with Python than with any other language.[4]
In Python, we use whitespaces and indentations to indicate different levels of code. This makes it optically appealing and intuitive to understand.Other languages, for example C++, rely more on braces and semicolons. While this might not be visually appealing and beginner-friendly, it makes the code a lot more maintainable. For bigger projects, this is a lot more useful.[4]

A Python script isn’t compiled first and then executed. Instead, it compiles every time you execute it, so any coding error manifests itself at runtime. This leads to poor performance, time consumption, and the need for a lot of tests.[4]
Despite all of the flexibility within Python, the usage of Lambdas is rather restrictive. In Python, inner scopes can only see outer scopes, but not change them. This leads to a lot of confusion.[4]

There are a few new competitors on the market of programming languages like Rust, Julia, Go. While there are other languages on the market, these three are the ones that fix weak patches of Python.

Thus, I think python is not the programming language for the future but I am talking about the far future, in the near future Python will still be one of the most popular programming language. 


Referenced Sites

[1]-www.futurelearn.com
[2]-www.upgrad.com
[3]-www.stxnext.com
[4]-thenextweb.com



'''







# END ANSWER TO Question 11 
###############################################################################

###############################################################################
# Question 12

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""
'''
General Description

n--> An integer

In this we have to convert the integer to a list with the least significant digit first

ans_iint--> It is a list that will contain the answer

Running a loop until n is not equal to 0

current_digit--->This will store the digit that is in the ones place 
then we add current_digit to our ans_iint
then we do integer division by 10 to remove the digit we have added in the list from our number n

the while loop keeps on running until our n is equal to 0 

Then we return the answer

'''
# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    ans_iint=[]       
    while n!=0:              # While n is not equal to 0
        current_digit=n%10       #We will store the digit that is in the ones place
        ans_iint+=[current_digit]     #Append the list with current_digit
        n=n//10               #Removed the digit added so the next didit will be add to the list in the next loop
    return ans_iint

'''
General Description

I--> An list of digits

In this we have to convert the list of numbers back to the integer

place--> this is the place value it is multiplied with 10 in every loop. 
initially its set to 1 as the 1st value will be in the ones place then multiplied by 10 as the next value will be in the tens place and so on.....

ans_pint--> It is an integer that will contain the answer

Running a loop trough each element of the list
In this the product of the place value and i(this is the digit) is added to ans_pint
Then we multiply place with 10

This loop will keep on running until it has completely iterated through the whole list and then we'll return the answer

'''

# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    place=1
    ans_pint=0
    for i in I:
        ans_pint+=i*place
        place*=10

    return ans_pint

'''
General Description

This part is really hard to explain so I will write more inline comments over here

I--> An list of digits
J-->Also an list of digits
In this we have to add both the infinite integers

place--> this is the place value it is multiplied with 10 in every loop. 
initially its set to 1 as the 1st value will be in the ones place then multiplied by 10 as the next value will be in the tens place and so on.....

ans_iadd--> It is an list that will contain the answer


'''
# add two infinite integers
def iadd(I,J):

    ans_iadd=[]
    Len_of_I=len(I)
    Len_of_J=len(J)

    if Len_of_I>Len_of_J:
        difference=Len_of_I-Len_of_J    # Checking how many extra digits I has compared to J
        for i in range(difference):
            J+=[0]      #So we can add 0's at the end of J so that it wont show index out of range error and our also won't be affected
    
    elif Len_of_I<Len_of_J:
        difference=Len_of_J-Len_of_I    # Checking how many extra digits J has compared to I
        for i in range(difference):
            I+=[0]      #So we can add 0's at the end of I so that it wont show index out of range error and our also won't be affected

    for i in range(len(I)):   #Instead of len(I) we can also write len(J) as both are the same
        ans_iadd+=[I[i]+J[i]]   #This will contain the sum 
    
    return pint(ans_iadd)        #This will return the integer form of the answer

'''
General Description

This part is really hard to explain so I will write more inline comments over here

I--> An list of digits
J-->Also an list of digits
In this we have to multiply both the infinite integers

place--> this is the place value it is incremented by 1 in every loop
initially its set to 0 as the 1st value will be in the ones place so there is no need to insert a zero at the start of the list

temp_list_imult--> This list will store the list of each element of J multiplied with the whole I list

I am using Multiplication is reapeated addition logic here


'''

# multiply two infinite integers
def imult(I,J):

    temp_list_imult=[]      #This list will store the list of each element of J multiplied with the whole I list
    place=0                 #this is the place where the element is

    for i in I:   #Iterating through list I
        temp=[]
        for j in J:   #Iterating through list J
            temp+=[j*i]       #This is where each individual element will multiply and be stored
            
        for k in range(place):  
            temp.insert(0,0)            #This is where 0's are added based on place
        #After 0's are added then then list is ready to be put in temp_list_imult where the lists of it will be add to each other later.
        temp_list_imult+=[temp]    
        place+=1                    #Incrementing place by 1 each time it loops
        
    ans_imult=0
    for i in temp_list_imult:     
        ans_imult=iadd(iint(ans_imult),i)   #This is where all the lists in temp_list_imult are being added to ans_imult
                                            #I am using Multiplication is reapeated addition logic here

    return ans_imult               #This will return the integer form of the answer 
                                   #If we want in list form we can use pint function                    


'''
General Description

In this I have done 2 codes 
The one I have commented is a shorter version but in it I converted J back to a integer,ran a loop and multiplied I to I till the loop ended.
I am not sure if we can do it this way but I think we cant thus I have commented it below.

The 2nd code

This part is really hard to explain so I will write more inline comments over here

I--> An list of digits
J-->Also an list of digits
In this we have to raise I to the power of J





'''
# raise I to the power of J
def ipow(I,J):
    if J==[0]:         #Any Number raised to 0 is always 1
        return 1
    elif J==[1]:
        return pint(I)    #Any number raised to 1 is the number itself
    else:
        ans_ipow=imult(I,I) 
        place=1                     #This is the place it is multiplied br 10 for every loop
        checker=False             # This is used for checking that I have done 2 less I x I multiplications in the next part 
        for i in range(len(J)+1):
            try:                        #It was showing some random error when I was iterating but I was getting my answer thus I used try and catch
                pl=J[i]*place
            except:
                return ans_ipow
            if (checker!=True) and (J[i]>=2):  # I did this because i am multiplying I x I in ans_ipow at the start
                pl-=2
                checker=True
                
            place*=10            #place it is multiplied by 10
                    
                
            for j in range(pl):    #It is multiplied current number * it place times
                ans_ipow=imult(iint(ans_ipow),I)           #It is multiplied the the previous ans x (current number * it place) times
                
        return ans_ipow                 #This will return the integer form of the answer 
                                    #If we want in list form we can use pint function     

'''
def ipow(I,J):
    if J==[0]:
        return 1
    elif J==[1]:
        return pint(I)
    else:
        ans_ipow=imult(I,I)
        for i in range(pint(J)-2):
            ans_ipow=imult(iint(ans_ipow),I)
                
        return ans_ipow

'''