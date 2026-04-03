str = input("Enter a sentence: ")

print("Forward sentence: ")
for i in range(len(str)):
    print(str[i], end="")

print("\nBackward sentence: ")
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
    
    