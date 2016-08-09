def without_while(x,y,numbers):
  if x < y:
    print "At the top i is %d" % x
    numbers.append(x)

    x += 1
    print "Numbers now", numbers
    print "At the bottom is %d" % x
    without_while(x,y,numbers)

  return numbers

numbers = without_while(0,6,[])

print "The Numbers: "

for num in numbers:
  print num
