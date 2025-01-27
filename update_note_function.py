#Этап 3: Задание 2. update_note_function.py: Функция обновления заметки
#Функция update_note(note) принимает заметку (словарь) как аргумент.
#Позволяет пользователю выбрать поле для обновления.
#Проверяет корректность ввода и обновляет выбранное поле.

from datetime import datetime   #

def update_note():      #функция для обновления одного из значений в словаре
    note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
            'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
    print('Текущие данные заметки:')
    print(note)     #вывод текущей заметки, как показано в задании, для улучшения словарь можно распечатать, как показано в конце

    new_info = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
    if new_info != 'username' and new_info != 'title' and new_info != 'content' and new_info != 'status' and new_info != 'issue_date':
        print('Вы ввели неправильное значение или оставили поле пустым. пожалуйста, попробуйте ещё раз!')
        return update_note()
    if new_info == 'username':
        username = input('Введите новое значение для username: ')
        note['username'] = username
    if new_info == 'title':
        title = input('Введите новое значение для title: ')
        note['title'] = title
    if new_info == 'content':
        content = input('Введите новое значение для content: ')
        note['content'] = content
    if new_info == 'status':
        status = input('Введите новое значение для status (новая, в процессе, выполнено): ')
        note['status'] = status
    if new_info == 'issue_date':
        issue_date = input('Введите новое значение для issue_date (в формате ДД-ММ-ГГГГ): ')
        note['issue_date'] = issue_date
        try:  # использование try-except для обработки ошибок при неправильном формате даты
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y')  # переводим сразу в 'datetime.datetime'
        except ValueError:  # в случае неверного ввода сообщаем об ошибке и запускаем функцию заново
            print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')
            print('Пожалуйста, попробуйте еще раз!')
            return update_note()
    return note     #возвращаем обновленный словарь
note = update_note()

#вывод обновленной заметки, как показано в задании
print('Заметка обновлена:')
print(note)

#или вывод с помощью цикла для лучшего отображения
note_names = {'username': 'Имя:', 'title': 'Заголовок:', 'content': 'Описание:', 'status':
    'Статус:', 'created_date': 'Дата создания:', 'issue_date': 'Дедлайн:'}
print('Заметка обновлена:')
for key, value in note.items():   
    print(note_names[key], value)