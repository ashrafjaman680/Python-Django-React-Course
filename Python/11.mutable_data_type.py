# mutable data type
# 1.list
# 2.Dictonary
# 3.set
# list

a = [1,2,3,4,5]
first_lication = id(a)
print(first_lication)

a[0] = 10
sec_location = id(a)
print(sec_location)


# dictonery

b = {'a': 2, 'b':3}
first_lication = id(b)
print(first_lication)

b['a'] = 5
sec_location = id(b)
print(sec_location)

# set

s = {1,2,3,4}

first_lication = id(s)
print(first_lication)

s.add(7)
sec_location = id(s)
print(sec_location)
