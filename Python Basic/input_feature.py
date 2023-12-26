name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
college = input("Enter your college: ")
profession = input("Enter your profession: ")
pet_name = input("Enter your pet name: ")

# 1st solution 1 line but not neat
print("There once was a person named", name, "who lived in", city + ". At the age of", age+ ",", name, "went to college at", college + ".", name, "graduated and went to work as a", profession + ". Then,", name, "adopted an animal named", pet_name + ". The both lived happily ever after!")

# 2nd solution using end=""
print ("There once was a person named",name, end="")
print (" who lived in", city, end="")
print (". At the age of", age, end="")
print (",",name, end="")
print (" went to college at" ,college, end="")
print (".", name, end="")
print (" graduated and went to work as a",profession, end="")
print (". Then,", name, end="")
print (" adopted an animal named", pet_name, end="")
print (". They both lived happily ever after!")