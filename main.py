print("welcome praktikan KLS D")

# dictionary
name = {17: "andi", 18: "Rahmat", 19: "Rahman", 20: "upin"}

# loop through dictionary
for key, value in name.items():
    print(f"hello {value} with id {key}")

# adding dictionary from user input
name[21] = input("masukkan nama: ")

# print latest dictionary
print(name)

# adding ---
print("---".center(50, "-"))