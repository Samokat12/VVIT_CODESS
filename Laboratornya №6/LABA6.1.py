class UserAccount:
   def __init__(self,username,email,password):
       self.username=username
       self.email=email
       self.__password=password
   def set_password(self,new_password):
        self.__password=new_password
   def check_password(self,password):
       return self.__password==password
user1=UserAccount('uglyfromyoung','ugly@example','London')
print(user1.check_password('London'))
user1.set_password('Paris')
print(user1.check_password('London'))
print(user1.check_password('Paris'))