# Enter your code here. Read input from STDIN. Print output to STDOUT
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

ab = (a*b)/100.0
ac = (a*c)/100.0

#print round(a+ab+ac)
print "The total meal cost is %d dollars."%round(a+ab+ac)
