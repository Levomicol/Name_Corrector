class Corrector:
  """Класс для обработки входного поля."""

def _init_(self, user):
    self.user = user

def starter(user):
    outStr = []

    for char in user:
       if char == " ":
          ind = user.index(char)+1
          if user[ind].isupper() == True:
             outStr.append(char)

          elif user[ind].isupper() == False:
              print("\n После пробела должно стоять большой букве")
              break

       elif char.isalpha() == True:
            outStr.append(char)

       else:
           outStr.clear()
           print("\n Недопустимое значение!")
           break
       
    output(outStr)

def output(user):        
    for s in user:
          print(s, end='')



          
          
          