class Hello:
    def upperCase(self, a):
        return a.upper()

word = input("Enter a word:").strip()
object = Hello()
print("The upper case of the string is:", object.upperCase(word))

        
        