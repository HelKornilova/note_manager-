titles = []  #создание списка для последуюшего хранения заголовков от пользователя

while 1 > 0:    #цикл для ввода нескольких заголовков
    title = input('Введите заголовок (или нажмите "Enter" для завершения): ')
    if not title:
        break   #завершение цикла, если нажали ввод
    titles.append(title) #сохранение заголовков, введенных пользователем

filtered_titles = list(set(filter(lambda x: x.strip(' '), titles)))  #убрать из вывода пустые строки и повторения

print("Заголовки заметки:")
for i in range(len(filtered_titles)): #использование цикла for для вывода списка в удобном формате
    print(filtered_titles[i])