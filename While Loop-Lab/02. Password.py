user_name = input()
password = input()
enter_password = input()
while password != enter_password:
    enter_password = input()
print(f"Welcome {user_name}!")