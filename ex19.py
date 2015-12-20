def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheese!" % cheese_count
	print "you have %d boxes of crackers" % boxes_of_crackers
	print "man that's enough for a party!'"
	print "get a blanker.\n"
	

print "We can just give that fucntions numers direcrly :"
cheese_and_crackers(20, 30)

print "or, we can use variable from our script:"
amount_of_cheese = 10
amout_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amout_of_crackers)

print "we can do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "we can cobine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 100, amout_of_crackers + 1000)