
# Unit 2




#Procedures
#def <procedure name> (<parm1>,<parm2>,etc.):
#	<code block>   # always indented, usually 4 spaces by default
# 	variables defined in the procedure are not accessible outsife of the procedure
#	thus we need to output some variable(s)
#	return <output1>, <output2>, etc.
#	side-effects are things that can print, do some work, etc., but aren't 
#	returned to the calling program
# 	while you can pass a variable to a procedure, you're really passing its value
# 	and NOT the actual variable
# 	try to use input parm names that give a good idea of what the inputs are 
# 	supposed to be vs. simply a,b,c, etc.

page =('<div id="top_bin"><div id="top_content" class="width960">' '<div class="udacity float-left"><a href="http://udacity.com">')
# page = contents of a web page


def get_next_target (s):
	start_link = s.find('<a href=')
	start_quote = s.find('"',start_link)
	end_quote = s.find('"',start_quote+1)
	url = s[start_quote+1:end_quote]
	return url, end_quote

print get_next_target(page)

# to call the procedure, the inputs or arguments or operands must match the number
# of inputs expected by the procedures definition



def rest_of_string(s):
	return s[1:]

print rest_of_string('audacity')

# the following does nothing as it doesn't return any value.  
# calling this procedure will return "None" 
def sum (a,b):
	a = a + b

def square(n):
	n = n * n
	return n

print square(5)
print square(square(5))
 
def sum3(a,b,c):
	sum = a + b + c
	return sum

print sum3(1,2,3)


def abbaize(a, b):
	abba = a+b+b+a
	return abba

print abbaize('dog', 'cat')

# return the position of the 2nd occurance of a target within the search string
danton = "De l'audace, encore de l'audace, toujours de l'audace"

def find_second (strToSearch, strToFind):
	firstOccur = strToSearch.find(strToFind)
	secondOccur = strToSearch.find(strToFind,firstOccur+1)
	return secondOccur

print find_second(danton,'audace')

twister = "she sells seashells by the seashore"
print find_second(twister,'she')


#comparisons
# operations can return true or false based on logic
print 2 < 3  # will return "True"
print 3 < 2  # will return "False"

# Conditions
# if <test expression>:
#	<block run if expression is true
#	don't forget indentation

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a,b):
	if a > b :
		return a
	if b > a :
		return b
	if b == a :
		return a

print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3


# above would be better if we use the else statement

def bigger2(a,b):
	if a > b :
		r = a
	else :
		r = b
	return r

print bigger2(2,7)
#>>> 7

print bigger2(3,2)
#>>> 3

print bigger2(3,3)
#>>> 3


# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
	if (name[0] == 'D') or (name[0] == 'N'):
		return True
	else :
		return False

# or you can write it with a return based on return of true or false evaluation
# e.g.   return name[0] == 'D'    would evaluate to true without the need for IF
# also	 return name[0] == 'D' or name[0] == 'N'


print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False

print is_friend('Ned')


# important to note that in an OR expression, if the first item evaluates to TRUE
# then python will not try to evaluate the 2nd item


# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#def biggest(a,b,c):
#	if a >= b :
#		if a >= c :
#			return a
#		else :
#			return c
#	elif b >= c :
#		return b
#	else :
#		return c

def biggest(a,b,c):
	if a > b :
		if a > c :
			return a
		else :
			return c
	else :
		if b > c :
			return b
		else :
			return c


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

print biggest(3,3,3)
#>>> 3

print biggest(9,9,3)
#>>> 9

print ">>>>>>>>>>>>>>>"
# or you can use the bigger procedure defined earlier and next the use of that 
# in our biggest procedure


def biggest2(a,b,c):
	return bigger(bigger(a,b),c)
	

print biggest2(3, 6, 9)
#>>> 9

print biggest2(6, 9, 3)
#>>> 9

print biggest2(9, 3, 6)
#>>> 9

print biggest2(3, 3, 9)
#>>> 9

print biggest2(9, 3, 9)
#>>> 9

print biggest2(3,3,3)
#>>> 3

print biggest2(9,9,3)
#>>> 9

print ">>>>>>>>>>>>>>>"

# of course, we can use the built in "max" function that does this for us

print max(3,3,3,4)

print ">>>>>>>>>>>>>>>"

# while
i = 0
while i<10:
	print i
	i = i + 1

print ">>>>>>>>>>>>>>>"

i = 0
while i<10:
	i = i + 1
	print i

print ">>>>>>>>>>>>>>>"

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.
              
def print_numbers(s):
	i = 1
	while i <= s:
		print i
		i = i + 1

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3
print ">>>>>>>>>>>>>>>"

# factorial

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
	x = 1
	while n > 0:
		x = x * n
		n = n - 1
	return x

print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
print factorial(52)

print ">>>>>>>>>>>>>>>"



def factorial2(n):
	x = 1
	while True:
		if i > 0 :
			break
		x = x * n
		n = n - 1
	return x

print factorial2(4)
#>>> 24
print factorial2(5)
#>>> 120
print factorial2(6)
#>>> 720
print factorial2(52)

print ">>>>>>>>>>>>>>>"











