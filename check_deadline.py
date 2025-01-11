#3. check_deadline.py: Обработка дедлайнов
#Функциональность:
#Запрашивает дату дедлайна и сравнивает её с текущей датой.
#Сообщает, истёк ли дедлайн или сколько дней осталось.
#Проверяет корректность формата ввода.

print('Здравствуйте! Давайте проверим, сколько ещё есть времени на выполнение задания!')

from datetime import datetime  #получение текущей даты с помощью библиотеки datetime
current_date = datetime.now()
print("Текущая дата:", current_date.strftime("%d-%m-%Y"))   #текущая дата для пользователя в формате дд-мм-гггг, строка.

while True:    # использование цикла для ввода даты пользователем
    issue_date = input("Введите дату дедлайна (в формате день-месяц-год): ")
    try:    #использование try-except для обработки ошибок при неправильном формате даты
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y')      #переводим сразу в 'datetime.datetime'
        break
    except ValueError:      # в случае неверного ввода сообщаем об ошибке и запускаем цикл заново
        print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')
        print('Пожалуйста, попробуйте еще раз!')

#анализ введенной даты и вывод результата пользователю:
time_difference = issue_date - current_date     #получение разницы в днях, <class 'datetime.timedelta'>
days_difference = time_difference.days + 1  #получение разницы в днях, <class 'int'>
if days_difference == 1:
    print("Дедлайн уже завтра!")
if days_difference == 2 or days_difference == 3 or days_difference == 4:
    print(f"До дедлайна осталось {days_difference} дня.")
if days_difference >= 5:
    print(f"До дедлайна осталось {days_difference} дней.")
if days_difference == 0:
    print("Дедлайн уже сегодня!")
if days_difference == -1:       #КАК УБРАТЬ МИНУС ПРИ ВЫВОДЕ ДАТЫ?
    print(f"Внимание! Дедлайн истёк {days_difference} день назад!")
if days_difference == -2 or days_difference == -3 or days_difference == -4:
    print(f"Внимание! Дедлайн истёк {days_difference} дня назад!")
if days_difference <= -5:
    print(f"Внимание! Дедлайн истёк {days_difference} дней назад!")