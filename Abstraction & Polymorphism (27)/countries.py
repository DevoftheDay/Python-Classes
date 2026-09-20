class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the national language of India")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of the USA.")

    def language(self):
        print("English is the national language of the USA")

    def type(self):
        print("USA is a developed country")


obj_india = India()
obj_USA = USA()

for country in (obj_india, obj_USA):
    country.capital()
    country.language()
    country.type()