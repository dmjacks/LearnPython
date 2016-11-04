# variable x is equal to a string
x = "There are %d types of people." % 10

# variable binary is equal to a string
binary = "binary"

# variable do_not is equal to a string
do_not = "don't"

# variable y is equal to a string
y = "Those who know %s and those who %s." % (binary, do_not)

# this line prints x
print x

# this line prints y
print y

# this line prints a string with x interpolated
print "I said: %r." % x

# this line prints a string with y interpolated
print "I also said: '%s'." % y

# variable hilarious equals False
hilarious = False

# variable joke_evaluation equals a string
joke_evaluation = "Isn't that joke so funny?! %r"

# this line prints joke_evaluation with hilarious interpolated
print joke_evaluation % hilarious

# variable w equals a string
w = "This is the left side of..."

#variable e equals a string
e = "a string with a right side."

# this line prints a concatenation of w and e
print w + e