# Для приклада
# p v ~q, ~q v s v ~p, ~s, q, r v s
# p v q, q v s v ~p, ~q

# Програма яка реалізує метод резолюцій пропозиційної логіки

# Функція прибирає зі списку елементи які повторюються
def function (A):
  for i in A:
    f = list(set(i))
    i.clear()
    i.extend(f)

import copy
print("Введіть набір диз'юнктів через кому, використовуючи 'v'")
print("для запису диз'юнкції, та '~' для заперечення:")
a = input()                         # Записуємо строку вводу у змінну
Arr = a.split(", ")                 # Вилучаємо зі строки лексеми розділені комою
B = []                              # Створюємо пустий список, якій будемо заповнювати окремими змінними
for i in Arr:
  temp = i.split(' ')               # Відокремлюємо змінні які розділені пробілом і записуємо у список
  while 'v' in temp:
    temp.remove('v')                # Якщо мається символ 'v' видаляємо його
  B.append(temp)                    # Додаэмо кожний список до загального списку

lenB = len(B)
lenLast = len(B[lenB-1])
temp = ''                           # Створюємо пусту змінну строки
P = copy.deepcopy(B)                # Копіюємо список
# Змінні для керування списками
c1 = 0
c2 = 0
c3 = 0
# Лічильник циклів
count1 = 0
count2 = 0
# У циклі перебираємо всі варіанти поки не знайдеться пустий диз'юнкт
while (([] in P) == False):
  print('==================================================')
  print(B)                          # Виводимо зміст загального списку
  while (([] in P) == False):
    copyP = list(P)                 # Копіюємо список
    flag1 = False                   # Флаг для керування
    c1=count1
    c2=count2
    while c1 < len(P):              # Рухаємось по зовнішньому списку
      while c2 < len(P[c1]):        # Рухаємось по внутрішньому списку
        temp = P[c1][c2]            # Вибор змінної для якої шукаємо контрарну пару
        while c3 < len(P):          # Знову йдемо з початку списка шукаючи контрарну пару
          contr = (temp[1:] if '~' in temp else '~'+temp) # Змінна яку шукаємо
          if contr in P[c3]:        # Якщо знайшли пару
            P[c3].remove(contr)     # Видаляємо ту що знайшли
            P[c1].remove(temp)      # Видаляємо ту для якої шукали
            P[c1].extend(P[c3])     # Додаємо диз'юнкт в якому знайшли до першого диз'юнкту
            if len(P) != 1:         # Видаляэмо той диз'юнкт в якому найшли якщо він не останній
              P.remove(P[c3])
            function(P)             # Видаляємо елементи, що повторюються
            print(P)                # Виводимо новий вигляд списку
            flag1 = True            # Виходимо з циклу
            break
          # Якщо не знайшли, збільшуємо індекс для роботи з наступним елементом
          c3+=1
        c3=0
        if flag1:                   # Якщо знашли, виходимо з циклу
          break
        # Якщо не знайшли, збільшуємо індекс для роботи з наступним елементом
        c2+=1
      c2=0
      if flag1:                     # Якщо знашли, виходимо з циклу
        break
      c1+=1
    # Якщо загальний список перестав змінюватися, то значить пройшли всі елементи, виходимо з циклу
    if copyP == P:
      break
  # Блок керування лічильниками для початку кожної нової ітерації з наступного члена внутрішнього списка
  if (([] in P) == False):
    P = copy.deepcopy(B)
  if count2 == len(B[count1])-1:
    count1 +=1
    count2 = 0
  else:
    count2 +=1
  # Вихід з циклу у разі незнаходження порожнього диз'юнкта
  if ((count1 == lenB) and (count2 == lenLast-1)):
    break

if [] in P:
  print('True!')
else:
  print('False!')
