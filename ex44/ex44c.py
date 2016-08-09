class Parent(object):

  def altered(self):
    print "PARENT altered()"

class Child(Parent):

  def altered(self):
    print "CHILD, Before PARENT altered()"
    super(Child, self).altered()
    print "CHILD, After PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
