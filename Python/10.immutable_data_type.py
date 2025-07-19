#immutable = (innitaial location != final location )
# list of immutable data type
# int,flot,tuple,Frozenset etc

# ex 
num = 10 
initial_location=id(num)
print(initial_location)

num = 12
second_location=id(num)
print(second_location)  # not same initial_location

