class UserAccount:  
    def __init__(self, username, email, password):  
        self.username = username  
        self.email = email  
        self.__password = password
  
    def set_password(self, new_password):   
        if isinstance(new_password, str):  
            self.__password = new_password   
        
    def check_password(self, password):  
        return self.__password == password  
  
#Создание объекта
user = UserAccount("vadim_terekhov", "vadimterekhov.com", "old_password")  
  
#Проверка исходного пароля  
print(user.check_password("old_password"))  #True  
  
#Изменение пароля 
user.set_password("new_password")  
  
#Проверка нового пароля  
print(user.check_password("new_password"))  #True  
  
#Проверка старого пароля после изменения  
print(user.check_password("old_password"))  #False  
