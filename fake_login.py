import time


username = 'Mr.join'
password = 'secret-password'


user = input("User: ")
Pass = input("Password: ")


if user == username and Pass == password:
  time.sleep(1)
  print("Please wait")
  time.sleep(2)
  print("OK...")
  time.sleep(3)
  print("Loading.....")
  time.sleep(4)
  print(".....")
  time.sleep(5)
  print("Access Granted")

elif user != username:
  print("incorrect username")

elif Pass != password:
  print("incorrect password")

else:
  print("incorrect username and password")  
