# === # DEEPSEARCH # === #

import os

def search_for_files(target_str: list, root_dirs: list) -> set:
    """Ключевая функция программы. Проходится по каждому файлу в указанной директории и анализирует его содержимое (ищет совпадения с предоставленными словами для поиска)"""

    any_file_counter = 0

    # Обработка исключений пустых переменных
    if not target_str: # Проверяем, введена ли строка-цель
        print('Невозможно выполнить поиск без строки-цели поиска')
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

        # === # Поиск # === #
        result_set = set()

        for root, dirs, files in os.walk(single_path):
            for file in files:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as search_file:
                    any_file_counter += 1
                    try:
                        data = search_file.read()
                        for item in target_str:
                            if item in data:
                                result_set.add(os.path.join(root, file))
                    except:
                        pass # Не удалось открыть - значит файл не текстовый и DeepSearch он не касается

    # Вывод списка из найденный файлов построчно
    for item in result_set:
        print(item)

    # Сколько файлов найдено?
    print(f"{len(result_set)} файлов обнаружено") if result_set else print('Не обнаружено совпадений')
    # Сколько файлов проанализировано?
    print(f'{any_file_counter} файлов проанализировано')

    # Возварт (пока не имеет смысла, но может быть, в дальнейшим будет)
    return result_set
    

# Запускаем поиск
search_for_files([ 
        'arxaco'
    ], 
    [
        'C:/Users/arsen/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang'
    ]
)