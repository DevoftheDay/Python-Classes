class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter a word here")

    def print_message(self):
        print("Message in uppercase: ", self.message.upper())


word_text = DailyMessage()
word_text.get_message()
word_text.print_message()

class HelperSession:
    def __init__(self):
        print("Session created")

    def __del__(self):
        print("Session deleted")

    def create_session():
        print("Helper session created")
        session = HelperSession()
        print("Session ready.")
        return session

session_obj = create_session()

class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}

        for index, number in enumerate(numbers):
            needed_number = target - number

            if needed_number in lookup:
                return(lookup[needed_number], index)
            lookup[number] = index

        return None

number = {10,20,30,40,50,60}

target_value = int(input("Enter a number here"))
result = PairFinder().find_pair(numbers, target_value)

if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found")

del session_obj
print("Program End")