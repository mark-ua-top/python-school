# Минулого уроку ми розглядали 
# 1. input() - функція для введення тексту
# 2. print() - функція виведення тексту в консоль

# Що таке функція? Функція - це іменований блок коду.
# Метод - це функція, що пов'язана з певним об'єктом.

# синтаксис функції в мові Python
# def <ім'я функції>(<параметри>):
#   <тіло функції>

def MyFirstFunction(text, num):
    for i in range(num): # цикл з лічильнико, повториться певну кількість разів
        print(text)
        
def PrintHello():
    MyFirstFunction("Привіт з іншої функції!", 2)
    
def GetUserInput():
    return input("Введи текст: ")

text = GetUserInput()
MyFirstFunction(text, 1)