list1 = []
fruits = ["apple", "grapes", "mango", "orange", "banana"]
num = [1, 2, 3, 4, 5, 6]
mixed = [1, 2, "donut", "false"]

print ("fruits = ", fruits)

print (len(mixed))

print (mixed [0])
print (mixed [-2])

print (fruits)

#replace element
fruits [1] = "wateh melonn"
print (fruits)

#remove element
fruits.remove ("mango")
print (fruits)

#to check if an element is present
print ("apple" in fruits)
print ("grapes" in fruits)

#itaration
for i in fruits:
    print (i)

#to add an element
fruits.append ("apple")
print (fruits)

#to count the amount of the element
print (fruits.count("apple"))

#to find wich index is the element
print (fruits.index("apple"))

#reverse
fruits.reverse
print (fruits)

#sorting
fruits.sort ()
print (fruits)

meow = ["q", "w", "e", "r", "t", "y", "u"]

#slicy slicy

#slicy from start
print (meow[2:])

# slicy from end
print (meow[:-3])
print (meow[:3])

# slicey from smth to smth
print (meow[1:5])
print (meow[1:-1])

#slicey slicey from smth to smth with stepsss
print (meow[1:5:2])
print (meow[:-1:5])
print (meow[-5:-1:2])
