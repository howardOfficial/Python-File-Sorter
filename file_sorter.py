import os
import shutil
import datetime

def organize_files(folder_path):
    """
    Переименовывает файлы (добавляет дату) и сортирует по папкам (по расширению).
    """
    if not os.path.exists(folder_path):
        print("Папка не найдена!")
        return

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Пропускаем папки (обрабатываем только файлы)
        if os.path.isfile(file_path):
            # 1. Получаем расширение файла (без точки)
            extension = filename.split('.')[-1].lower()
            
            # 2. Создаем папку для этого расширения (если нет)
            ext_folder = os.path.join(folder_path, extension)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            
            # 3. Формируем новое имя (добавляем дату изменения файла)
            mtime = os.path.getmtime(file_path)
            date_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            new_name = f"{date_str}_{filename}"
            
            # 4. Перемещаем и переименовываем
            new_path = os.path.join(ext_folder, new_name)
            shutil.move(file_path, new_path)
            print(f"Перемещен: {filename} -> {new_path}")

if __name__ == '__main__':
    # Укажи путь к папке, которую нужно отсортировать (например, 'C:/Downloads')
    target_folder = input("Введите путь к папке для сортировки: ")
    organize_files(target_folder)
    print("Готово!")
