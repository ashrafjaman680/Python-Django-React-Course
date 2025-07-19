# type conversion
# Explicit => int(),flot(),str()
# Implicit => x =10 y =50.2

# Explicit conversion

x = int(10)
y = float(10.5)
print(x)
print(y)

# implicit conversion

a = 10
b = 10.5

print(a)
print(b)


# exception handeling

try:
    name =int("Hridoy")
    print(name)
except Exception as p:
    print(p)    
