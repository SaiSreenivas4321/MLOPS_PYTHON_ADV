class social_network_chat:
    def __init__(self):
        self.username = ''  #username 
        self.password = ''
        self.loggedIn = False
        self.menu()
        #pass
    def menu(self):
        user_input = input("""Welcome to socialnetwork and give me a your opnion ? 
                           1. Press 1 for signup
                           2. press 2 for signin
                           3. press 3 to write a post
                           4. press 4 to message a friend 
                           5. press any other key to exit """)
        
        if user_input == "1":
            self.signup()
            pass
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.Send_message()
        else: 
            exit()

        #pass
    def signup(self):
        email = input("Enter your email here ->")
        password = input(" setup your Password ")
        self.username = email
        self.password = password
        print("You have signedup Sucessfully {self.username} and {self.password}")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password =='':
            print("Please signup first by Pressing")
            # self.my_post()
            #pass
        else:
            uname = input("enteryour email/username here ->")
            passwd = input("enter your password here ->")
            if self.username == uname and self.password == passwd:
                print("You have signed Sucessfully")
                self.loggedIn = True
                self.my_post()
            else:
                print("Please input correct credentals..")
                self.loggedIn = False
                self.menu()


    def my_post(self):
        if self.loggedIn == True:
            txt = input("Enter your message here ")
            print(f" following the txt{txt}")
        else:
            print("Please login First to some post something")
            self.menu()

    def Send_message(self):
        if self.loggedIn == True:
            txt = input("Enter Your messsage here ->")
            message = input("Enter your message here ")
            print(message)
            self.menu()
        else:
            print("Please login First to some post something")
            self.menu()

            #pass
obj = social_network_chat()

