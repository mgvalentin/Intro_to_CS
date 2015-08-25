# print 3
# Unit 1 - Lesson 1 - How to Get Started

# print out number of minutes in 7 weeks
# print 60 * 24 * 7 * 7

# Grammar

# Speed of Light
# write code to printout how far light travels in centimeters in nanosecond
# speed of light = 299792458		meters per second
# centimeters = 100					one meter is 100 centimeters
# nanosecond = 1.0 / 1000000000 	one billionth of a second
print 299792458 * 100 * (1/1000000000) 
# above will print out as 0 since these are all INTs
# to get them to print out as a DECIMAL, change the values to decimals
print 299792458.0 * 100.0 * (1.0/1000000000.0) 
# however, only one value needs to be a decimal for the output to be decimal
print 299792458 * 100 * (1.0/1000000000) 


# 2.7 GHz is 2.7 billion operations per second
# light travels in 
print 299792458 * 100 * (1.0/1000000000) * 1/2.7
# on the mac with this CPU, the computer must complete an operation in a single nanosecond is less time than
# 11.1034243704 centimeters

# variables
# print the distance, in meters that light travels in one processor cycle
speed_of_light = 299792458.0				# meters per second
cycles_per_second = 2700000000.0			# 2.7 GHz
print speed_of_light / cycles_per_second

# or

speed_of_light = 299792458.0				# meters per second
cycles_per_second = 2700000000.0			# 2.7 GHz
cycle_distance = speed_of_light / cycles_per_second
print cycle_distance


# this code will result in an error since the variable minutes starts out undefined
# minutes = minutes +1
# seconds = minutes * 60
# print seconds

# to fix this, we could
minutes = 0
minutes = minutes +1
seconds = minutes * 60
print seconds
# thus, to use a variable, they must be defined in advance


# strings
# can be defined with single quotes or double quotes, but must finish with the same quote as the starts

print 'hello'
print "hello"


# concatenation
name = "Michael"
print 'Hello ' + name

# the following line will result in an error
# print 'My name is Michael' + 9
# as you can't contentatte strings with integers

# However, you can use some strings with multiplication
# e.g. print "!" * 12 will result in printing 12 exclamation points
print '!' * 12
# or
print 'Hello ' + name + '!' * 12


# Index Strings
# <string> [<expression>] 
# to get the 3 letter in the name variable, you would use name[2] to get the letter c in Michael

print name[2]

# to get the last character, use the [-1]
print name[-1]
# will print the l in michael


# String Sub-sequences
# so far we've pulled single characters using the expressions above
# to pull multiple characters, we need a start and end separated by a colon  :  UP TO but NOT inclusive of the end
# the following pulls characters from position 1 and stops before position 3
print name[1:3]
# thus this will pull i and c from Michael

# to pull from the beginning, leave the start position blank, e.g. print Mic
print name[:3]
# to pull all from a start position to the end, leave the end position blank, e.g. print hael
print name[3:]
# you COULD leave both sides blank to pull from beginning to end, but there isn't a good use case for this
print name[:]

# to pull all characters from beginning to the end EXCEPT the last character, e.g. Michae
print name[:-1]

# the following will result in an empty string since we are starting at zero and stopping before zero, thus empty
print name[0:-1+1]

# FIND strings in strings
# <string to searched>.find(<string to be found>)   results in the value of the start position for the first
# instance found in the <string to be searched> for the <string to be found>
# .find is a "method" or procedure that operations on strings
# 
pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres'
print pythagoras.find('the')
print pythagoras[21:]
print pythagoras.find('algebra')    # this will result in  -1  to indicate that the string was NOT FOUND



# the following will always evalue to zero
print ' '
print 'evaluate to zero quiz'
print name.find(name)
print 'name'.find('name')
print name.find('')					# empty string is always zero regardless of content of string to be searched
print name.find(name+'!!!') + 1     # the resulting finding string is longer and can never be found, hence -1 then we add 1


# to find from a starting position other than the beginning, we can use
# <string>find(<stringtofind>,<starting position>)
print pythagoras.find('the',30)
# will find the first instance of the word the after 30 and returns 36
# will return -1 if the string isn't found 

# Extracting links
# for the lesson, we'll assume links begin with <a href="<url>">
# start with a page variable that contains the content of a webpage

# if page = 'some website page content with <a href= embedded'
# start_link = page.find('<a href=') will return href position

# Link Quiz 
# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = page[start_quote+1:end_quote]
print url


# print page[start_link:]
# print start_link
# print page[start_quote:]
# print page[end_quote:]


# Homework 1
# Write Python code that prints out the number of hours in 7 weeks.
print 7 * 7 *24

s = ''
print ('a' + s)[1:]
print s[0:]
print s + ''
# print s[0] + s[1]    # will cause an error



# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
print s[0:1] + t[2:]
# or
print s[:-2] + t[-3:]


# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.
text = "first hoo" 
# ENTER CODE BELOW HERE
print text.find('hoo')




# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped' 
# >>> 18
text = 'all zip files are compressed'
# >>> -1
# text = "all zip files are zipped" 
#ENTER CODE BELOW HERE
print text.find('zip',(text.find('zip')+1))


# convert to string
# str(<number>) changes the type from number to string

# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
x = 3.5 
# >>> 4 (not 4.0)

# x = 3.14159

#ENTER CODE BELOW HERE
# just add .5 to help with rounding up and then strip off after the period
x = x + .5
y = str(x)
y = y[:y.find('.')]
print y






###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###

marker_loc = line.find(marker)
space_after_marker = line.find(' ',marker_loc+1)

#replaced = line[:marker_loc] + replacement + line[space_after_marker:]

line1 = line[:(line.find(marker))]
line2 = line[(line.find(marker)+(len(marker))):]
replaced = line1 + replacement + line2

print replaced
# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.




###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

#word = "madam"
# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###
word_backwards = word[::-1]

is_palindrome = word.find(word_backwards)

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"























