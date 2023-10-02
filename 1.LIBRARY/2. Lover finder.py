import random
lover = ["Davit","Chhinkeo","Votey","Phanit","Veasna","Tiv","Neardey","Rady"]
name = input("What is your name? ")
print(name+ " secret lover is "+ lover[random.randint(1,len(lover))])
