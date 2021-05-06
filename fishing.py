#First page should contain the user profile creation and store it in a list

print("Welcome to the fishing tournament!")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
date_of_birth = input("Enter your date of birth (DD/MM/YYYY): ")

def register_user():
username_info = username.get()
password_info = username.get()

file = open("userinfo.txt", "w")
file.write(username_info+"\n")
file.write(password_info+"\n")
file.flush()
file.close()


new_username.delete(0, END)
new_password.delete(0, END)

Label(screen1, text="You're registered!", fg="green", font=("Calibri", 11)).pack()