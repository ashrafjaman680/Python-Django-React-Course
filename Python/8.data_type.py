# Type of data types
#        ...
# 1.Numaric data type  
# 2.String data type
# 3.Sequence data type
# 4.Boolean data type
# 5.None data type
# 6.Dictonary data type
# 7.Set data type
# 8.Frozenset data type








# 1.Numaric data type

age = 34 #int data type
print(age)

marks = 52.8 # Float data type
print(marks)

complex_num = 10+2j # Complex data type
print(complex_num)


# 2.String data type

name = "MD ASHRAF JAMAN HRIDOY"
print(name)


# 3.type of sequence data type 
    #1.list data type
    # 2.Tuple data type
    # 3.Range data tupe

#1.list data type

# Ex 1 we can stote str

city = ["Dhaka", "Rangpur", "Khulna"]
print(city)


# Ex 2 we can stote str,float,int,complex num

list = [10, 20.3 , 10+2j, "Hello"]
print(list)


# Ex 3 we can store duplicate value

city = ["Dhaka", "Rangpur", "Khulna","Dhaka", "Rangpur", "Khulna"]
print(city)


# Ex 4 
# list maintain order
# this order start 0 to infinity
# if we call 0 no index

city = ["Dhaka", "Rangpur", "Khulna","Dhaka", "Rangpur", "Khulna"]
print(city[0])


# if we call 1 no index

city = ["Dhaka", "Rangpur", "Khulna","Dhaka", "Rangpur", "Khulna"]
print(city[1])


# 2.Tuple data type same as list

# Ex 1 we can stote str

city = ("Dhaka", "Rangpur", "Khulna")
print(city)


# Ex 2 we can stote str,float,int,complex num

list = (10, 20.3 , 10+2j, "Hello")
print(list)


# Ex 3 we can store duplicate value

city = ("Dhaka", "Rangpur", "Khulna","Dhaka", "Rangpur", "Khulna")
print(city)


# Ex 4 
# Tuple aslo maintain order
# this order start 0 to infinity
# if we call 0 no index

city = ("Dhaka", "Rangpur", "Khulna","Dhaka", "Rangpur", "Khulna")
print(city[0])


# if we call 1 no index

city = ("Dhaka", "Rangpur", "Khulna","Dhaka", "Rangpur", "Khulna")
print(city[1])


# 3.Range data type

# ex 1 print 0 to 10
number = range(0,10)
print(*number)

# ex 2 print 0 to 5
number2 = range(5)
print(*number2)

# ex 3 print even num 0 to 10
number3 = range(0,10,2)
print(*number3)

# ex 3 print odd num 0 to 10
number3 = range(0,10,3)
print(*number3)


# 4.Boolean data type

isBangladeshi = True
print(isBangladeshi)


# 5.None data type

money = None
print(money)


# 6.Dictonary data type

persion = {

    'name' : 'hridoy',
    'age' : 21,
    'isBangladeshi':True

}

print(persion)
print(persion['name'])
print(persion['age'])


# 7.Set data type

unique_num = {1,2,3,4,5}
print(unique_num)

# set only print unique items
unique_num = {1,2,3,4,5,1,2,1,3,4}
print(unique_num)


# 8.Frozenset data type

unique_num = ([1,2,3,4,5])
print(unique_num)