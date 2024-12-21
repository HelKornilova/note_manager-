name = input("Введите Ваше имя: ")
title_1 = input("Основные темы: ")
title_2 = input("Персонажи: ")
title_3 = input("Рекомендации для чтения: ")
titles = [title_1, title_2, title_3]
print(titles)
content = input("О чем Ваша заметка? ")
status = input("Какой статус заметки? ")
created_date = input("Укажите дату создания (в формате ДД-ММ-ГГГГ) ")
issue_date = input("Укажите дату истечения (в формате ДД-ММ-ГГГГ) ")

note = {"Имя пользователя": name,
        "Содержание заметки": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дата изменения": issue_date,
        "Заголовки": titles}
print(note)