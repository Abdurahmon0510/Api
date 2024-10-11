
class Talaba:
    company = ('https://lms.tuit.uz/')

    def __init__(self, username, password, age, email, address, gender):
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.address = address
        self.gender = gender

    def set_username(self, new_username):
        self.username = new_username
        return self.username

    def respected_username(self):
        if self.gender == 'male':
            self.username = 'Hello Mr. ' + self.username
            print(self.username)
        elif self.gender == 'female':
            self.username = 'Hello Ms. ' + self.username
            print(self.username)
        else:
            print('Sorry, gender must be male or female')

    def set_age(self, new_age):
        self.age = new_age
        return self.age

    def course(self):
        self.course = self.age - 18
        return self.course

    def password(self, new_password):
        self.password = new_password
        return self.password

    def control_password(self):
        belgilar = "~`!@#$%^&*()_+/*-?><\":|}{[];/.,'"
        A = False
        B = False
        C = False
        D = False
        E = False
        for item in self.password:
            if item.isalpha():
                A = True
            if item.isnumeric():
                B = True
            if item.islower():
                C = True
            if item.isupper():
                D = True
            if item in belgilar:
                E = True
        if A == True and B == True and C == True and D == True and E == True and len(self.password) >= 8:
            print('Your password is valid')
        else:
            print('Your password is invalid')
            return

    def set_email(self, new_email):
        self.email = new_email
        return self.email

    def control_email(self):
        if '@gmail.com' in self.email:
            print('Your email is valid')
        elif 'email.ru' in self.email:
            print('Your email is valid')
        else:
            print('Your email is invalid')
            return

        def set_address(self, new_address):
            self.address = new_address
            return self.address

        def control_address(self):
            if 'street' in self.address:
                print('Your address is valid')
            else:
                print('Your address is invalid')

talaba1 = Talaba('Avf', '5102005Aa!', 18, 'Abdurahmon5102005@gmail.com', 'Xiyobon street 40', 'male')
print(Talaba.company)
print(talaba1.email)
talaba1.control_password()
talaba1.control_email()

