# === # DEEPSEARCH # === #

import os

def check_for_data_availability(target_str: list, root_dirs: list) -> None:
    """Проверяем, не бред ли ввёл пользователь"""

    if not target_str: # Проверяем, введена ли строка-цель
        print('Невозможно выполнить поиск без хотя бы одной строки, которую мы будем искать в файлах')
        input()
        exit()

    if not root_dirs: # Проверяем, введен ли хотя бы один путь
        print('Невозможно выполнить поиск без целевой директории. Укажите хотя бы одну')
        input()
        exit()

    for single_path in root_dirs: # Цикл для каждого представленного пути
        if not os.path.exists(single_path): # Проверяем, существует ли указанный путь
            print(f'Не существует указанного пути {single_path}')
            input()
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

                            if os.path.join(root, file) not in result_dict: result_dict[os.path.join(root, file)] = [] # Создаем пустое множество, если такового ещё нет
                            if item not in result_dict[os.path.join(root, file)]: result_dict[os.path.join(root, file)].append(item) # Добавляем элемент, если он ещё не добавлен

                with open(os.path.join(root, file), 'r', encoding='utf-8') as search_file:
                    any_file_counter += 1
                    try:
                        data = search_file.read() # Загружаем переменные из файла в переменную data
                        for item in target_str: # Цикл для каждого поискового слова
                            if (item in data and is_case_sensitive) or (item.lower() in data.lower() and not is_case_sensitive): # Проверка совпадений с учетом требований к регистру

                                if os.path.join(root, file) not in result_dict: result_dict[os.path.join(root, file)] = [] # Создаем пустое множество, если такового ещё нет
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
    


# === # Запускаем поиск # === #



# Чувствителен ли поиск к РеГиСтРу? (указать ниже)
is_case_sensitive = False

# Искать ли в названиях файлов? (False - ищем только внутри, True - и внутри, и в названиях)
also_search_in_filenames = True

# Вводить данные сюда, сверху слово для поиска, снизу директория поиска (можно вводить списком)
search_for_files([ 
        'sk_a_',
        'sk_b_',
        'sk_c_',
        'sk_d_'
    ], 
    [
        "C:/Users/arsen/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang"
    ],
)