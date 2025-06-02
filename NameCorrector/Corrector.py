class Corrector:
  """Класс для обработки входного поля."""

def _init_(self, user):
    self.user = user

def starter(user):
    outStr = []
    for char in user:
       if char == " ":
          outStr.append(char)
       elif char.isalpha() == True:
            outStr.append(char)
       else:
           outStr.clear()
           print("Недопустимое значение!")
           break
           
    for s in outStr:
      if outStr[0].isupper() == True:
            print(s, end='')
      else:
          print("Введите имя с большой буквы.")
          break



          
          
          