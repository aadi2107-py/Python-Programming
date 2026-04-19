sentence = input("Enter an Setence: ")
def count_vc(sentence):
    vowels = "aeiouAEIOU"
    vowels = sum(1 for ch in s if ch in vowels )
    consonents = sum(1 for ch in s if ch not in vowels)
    return (vowels,consonents)

    print(count_vc(sentence))