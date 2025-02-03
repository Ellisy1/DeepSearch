# === # DEEPSEARCH # === #

import os

def search_for_files(target_str: list, root_dir: str) -> set:
    """Ключевая функция программы. Проходится по каждому файлу в указанной директории и анализирует его содержимое (ищет совпадения с предоставленными словами для поиска)"""

    # === # Обработка исключений # === #
    if not os.path.exists(root_dir): # Проверяем, существует ли указанный путь
        raise ValueError(f'Не существует указанного пути {root_dir}')

    if not target_str: # Проверяем, введена ли строка-цель
        raise ValueError('Невозможно выполнить поиск без строки-цели поиска')

    # === # Поиск # === #
    result_set = set()

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as search_file:
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
    print(f"{len(result_set)} файлов обнаружено")

    # Возварт (пока не имеет смысла, но может быть, в дальнейшим будет)
    return result_set
    

# Запускаем поиск
search_for_files(['arxaco'], 'C:/Users/arsen/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang')