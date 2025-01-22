#5. delete_note.py: Удаление заметок
#Функциональность:
#Удаляет заметку по имени пользователя или заголовку.
#Выводит сообщение, если заметка не найдена.
#Обновляет список заметок.

note_1 = {'name': 'Елена', 'title': 'Список покупок', 'content': 'Купить продукты на неделю'}
note_2 = {'name': 'Мария', 'title': 'Учёба', 'content': 'Подготовиться к экзамену'}
note_3 = {'name': 'Алексей', 'title': 'Книги', 'content': 'Составить список книг в поездку'}
notes = [note_1, note_2, note_3]  # сохранение списка словарей

print("Текущие заметки:")
for i, item in enumerate(notes, start=1):  #вывод списка словарей с нумерацией
    print(f'{i}. Имя: {item['name']}')
    print(f'Заголовок: {item['title']}')
    print(f'Описание: {item['content']}')

while True:     #удаление заметки через цикл по имени или заголовку
    delete_ = input('Введите имя пользователя или заголовок для удаления заметки: ')
    if delete_ == note_1['name'] or delete_ == note_1['title']:
        delete_1 = input('Вы уверены, что хотите удалить заметку? (да/нет): ')
        if delete_1.lower() == 'да':
            notes.remove(note_1)
            break
        else:
            continue
    if delete_ == note_2['name'] or delete_ == note_2['title']:
        delete_2 = input('Вы уверены, что хотите удалить заметку? (да/нет): ')
        if delete_2.lower() == 'да':
            notes.remove(note_2)
            break
        else:
            continue
    if delete_ == note_3['name'] or delete_ == note_3['title']:
        delete_3 = input('Вы уверены, что хотите удалить заметку? (да/нет): ')
        if delete_3.lower() == 'да':
            notes.remove(note_3)
            break
        else:
            continue
    else:
        print('Заметок с таким именем пользователя или заголовком не найдено. Попробуйте еще раз.')
        continue

print('Успешно удалено!')
print('Остались следующие заметки: ')
for i, item in enumerate(notes, start=1):  #вывод списка словарей с нумерацией
    print(f'{i}. Имя: {item['name']}')
    print(f'Заголовок: {item['title']}')
    print(f'Описание: {item['content']}')