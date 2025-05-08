# === # DEEPSEARCH # === #

import os
import tkinter as tk

def check_for_data_availability(target_str: list, root_dirs: list) -> None:
    """Проверяем, не бред ли ввёл пользователь"""

    if not target_str: # Проверяем, введена ли строка-цель
        print('Невозможно выполнить поиск без хотя бы одной строки, которую мы будем искать в файлах')
        exit()

    if not root_dirs: # Проверяем, введен ли хотя бы один путь
        print('Невозможно выполнить поиск без целевой директории. Укажите хотя бы одну')
        exit()

    for single_path in root_dirs: # Цикл для каждого представленного пути
        if not os.path.exists(single_path): # Проверяем, существует ли указанный путь
            print(f'Не существует указанного пути {single_path}')
            exit()


def search_for_files(target_str: list, root_dirs: list) -> set:
    """Ключевая функция программы. Проходится по каждому файлу в указанной директории и анализирует его содержимое (ищет совпадения с предоставленными словами для поиска)"""

    check_for_data_availability(target_str, root_dirs) # Проверяем, нет ли ошибочных входных данных

    any_file_counter = 0 # Счетчик всех проверенных файлов
    
    # Устанавливаем переменную общего словаря.
    result_dict = {}

    # === # Поиск # === #
    print('Please wait...')

    for single_path in root_dirs: # Цикл для каждого представленного пути

        for root, dirs, files in os.walk(single_path): # Пускаем цикл по файлам
            for file in files:

                if also_search_in_filenames:
                    for item in target_str: # Пытаемся найти в названии файла нужное слово
                        if (item in file and is_case_sensitive) or (item.lower() in file.lower() and not is_case_sensitive):

                            if os.path.join(root, file) not in result_dict: result_dict[os.path.join(root, file)] = [] # Создаем пустой список, если такового ещё нет
                            if item not in result_dict[os.path.join(root, file)]: result_dict[os.path.join(root, file)].append(item) # Добавляем элемент, если он ещё не добавлен

                with open(os.path.join(root, file), 'r', encoding='utf-8') as search_file:
                    any_file_counter += 1
                    try:
                        data = search_file.read() # Загружаем переменные из файла в переменную data
                        for item in target_str: # Цикл для каждого поискового слова
                            if (item in data and is_case_sensitive) or (item.lower() in data.lower() and not is_case_sensitive): # Проверка совпадений с учетом требований к регистру

                                if os.path.join(root, file) not in result_dict: result_dict[os.path.join(root, file)] = [] # Создаем пустой список, если такового ещё нет
                                if item not in result_dict[os.path.join(root, file)]: result_dict[os.path.join(root, file)].append(item) # Добавляем элемент, если он ещё не добавлен
                    except:
                        pass # Не удалось открыть - значит файл не текстовый и DeepSearch он не касается

    # Вывод списка из найденный файлов построчно
    for key in result_dict:
        print(f'{result_dict[key]} in {key}')

    # Сколько файлов найдено?
    print(f"{len(result_dict)} файлов с совпадениями обнаружено") if result_dict else print('Не обнаружено совпадений')
    # Сколько файлов проанализировано?
    print(f'{any_file_counter} файлов проанализировано')

    # Возварт (пока не имеет смысла, но может быть, в дальнейшим будет)
    return result_dict

def apply_dark_theme(window):

    # Определяем цвета для темной темы
    BACKGROUND_COLOR = "gray12"  # Очень темный серый
    FOREGROUND_COLOR = "white"

    """Применяет темную тему к указанному окну и его потомкам."""
    window.config(bg=BACKGROUND_COLOR)  # Устанавливаем цвет фона окна

    for widget in window.winfo_children(): # проходимся по всем виджетам в окне
        widget_class = widget.__class__.__name__
        if widget_class == "Label":  # Настраиваем только Label
            widget.config(bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
        elif widget_class == "Button":
            widget.config(bg="#333333", fg=FOREGROUND_COLOR, relief=tk.FLAT)
        elif widget_class == "Entry":
            widget.config(bg="#333333", fg=FOREGROUND_COLOR, insertbackground=FOREGROUND_COLOR) # insertbackground - цвет курсора

        # Рекурсивно применяем тему к потомкам (если есть)
        apply_dark_theme(widget)



# === # Запускаем поиск # === #



# Чувствителен ли поиск к РеГиСтРу? (указать ниже)
is_case_sensitive = False

# Искать ли в названиях файлов? (False - ищем только внутри, True - и внутри, и в названиях)
also_search_in_filenames = True

# Инициализируем UI
window = tk.Tk()
window.title('DeepSearch')
window.geometry("600x400")

apply_dark_theme(window)

label = tk.Label(window, text='Раз два три', background="black",  foreground="white")
label.pack(anchor='nw')

window.mainloop()

# Вводить данные сюда, сверху слово для поиска, снизу директория поиска (можно вводить списком)
# search_for_files([ 
#         'ModalFormData'
#     ], 
#     [
#         "C:/Users/arsen/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/ARX NAP BP"
#     ],
# )