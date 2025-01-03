status = 'в процессе'   #текущий статус заметки
from time import sleep  #при желании использовать задержку программы до того, как предложить сменить статус
print('Текущий статус заметки:', status)
sleep(1.5)
print('Введите новый статус заметки, указав его название:')    #предложение поменять статус с указанными вариантами
print('1. выполнено')
print('2. в процессе')
print('3. отложено')

while True:     #использование цикла для ввода нового статуса заметки
    status = input('Ваш выбор: ')
    if status == 'выполнено':
        print('Статус заметки успешно обновлён на: "выполнено"!')
        break
    if status == ('в процессе'):
        print('Статус заметки успешно обновлён на: "в процессе"!')
        break
    if status == ('отложено'):
        print('Статус заметки успешно обновлён на: "отложено"!')
        break
    else:   #подсказки в случае ввода некорректных данных
        print('Вы указали некорректные данные. Пожалуйста, введите название нового статуса еще раз.')
        print('Статус заметки может быть: выполнено, в процессе или отложено.')

update_status = {"status": status}     #сохранение нового статуса в словарь
#print(update_status)