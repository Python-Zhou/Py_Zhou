x = "There ard %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilasrious = False
joke_evalution = "Isn't that joke so funny?! %r"

print(joke_evalution % hilasrious)

w = "This is the left side of ..."
e = "a string with a right side"

print(w+e)

formatter = "%r %r %r %r"
print(formatter % ("aa", "bb", "cwerwerwerc", "dd"))
