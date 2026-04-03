s = input("Enter a Sentence: ")
result = ""

print("Choose any one of the following options:")
print("1. Convert to UPPERCASE")
print("2. Convert to lowercase")
print("3. Convert to TOGGLE case")

choice = int(input("Enter your choice (1/2/3): "))

for i in s:
    if choice == 1:
        if "a" <= i <= "z":
            ans = chr(ord(i) - 32)
        else:
            ans = i

    elif choice == 2:
        if "A" <= i <= "Z":
            ans = chr(ord(i) + 32)
        else:
            ans = i

    elif choice == 3:
        if "A" <= i <= "Z":
            ans = chr(ord(i) + 32)
        elif "a" <= i <= "z":
            ans = chr(ord(i) - 32)
        else:
            ans = i

    else:
        print("Please choose from the given options")
        break

    result += ans   

print("Converted string:", result)