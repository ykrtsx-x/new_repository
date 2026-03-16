class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_first_name(self):
        print("мое имя ", self.first_name)

    def say_last_name(self):
        print("моя фамилия ", self.last_name)

    def say_full_name(self):
        print("меня зовут ", self.first_name, self.last_name)


alex = User("Alex", "Smith")
alex.say_first_name()
alex.say_last_name()
alex.say_full_name()
