import traceback
import Corrector

try:
  def main():
      
      print("\n", "Введите своё имя:")
      Corrector.starter(input())
      main()
except Exception as e:
   exception_traceback = traceback.format_exc()
   print(exception_traceback)
   
main()


