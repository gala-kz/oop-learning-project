# class-instance-attributes-1.py

# This code shows that an Instance can access it's own
# attributes as well as Class attributes.

# We have a class attribute named 'count', and we add 1 to
# it each time we create an instance. This can help count the
# number of instances at the time of instantiation.


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        print(self.val)

    def get_count(self):
        print(InstanceCounter.count)


a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print("value of obj: %s" % obj.get_val())
    print("Count : %s" % obj.get_count())
    
# a = InstanceCounter(5)
# val = 5
# InstanceCounter = 1

# b = InstanceCounter(10) 
# val = 10    
# InstanceCounter = 2

# c = InstanceCounter(15) 
# val = 15    
# InstanceCounter = 3

# prints:
# value of obj: 5
# count:1

# value of obj: 10
# count:2

# value of obj: 15
# count:3
    
    
    
    
    
    
    
    
    
    
    
    

'''
O/P-
5
value of obj: None
3
Count : None
10
value of obj: None
3
Count : None
15
value of obj: None
3
Count : None
'''