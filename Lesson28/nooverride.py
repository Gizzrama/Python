class India():
    def capitalcity(self):
        print("The capital city of India is New Delhi.")

    def language(self):
        print("Hindi is primarily spoken in India.")

    def type(self):
        print("India is a developing nation.")

class USA():
    def capitalcity(self):
        print("The capital city of the United States is Washington D.C.")

    def language(self):
        print("English is primarily spoken in the US.")

    def type(self):
        print("USA is a developed nation.")


india = India()
usa = USA()

for i in (india, usa):
    i.capitalcity()
    i.language()
    i.type()

