name = 'Donan M. Jackson'
age = 22 # not a lie
height = 68 # inches
weight = 190 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "They're %d inches tall." % height
print "They're %d pounds heavy" % weight
print "Actually that's not too heavy."
print "They've gpt %s eyes and %s hair." % (eyes, hair)
print "Their teeth are usually %s depending on the tea." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)