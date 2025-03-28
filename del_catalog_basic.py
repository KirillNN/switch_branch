import os
import shutil
import stat

def remove_readonly(func, path, _):
    """Снимаем атрибут 'только для чтения' и повторяем удаление"""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def delete_git_and_folder(folder_path):
    git_path = os.path.join(folder_path, ".git")  # Полный путь к .git

    # Удаляем .git, если он есть
    if os.path.exists(git_path):
        shutil.rmtree(git_path, onerror=remove_readonly)
        print(f"Удален .git в {git_path}")

    # Удаляем сам каталог
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path, onerror=remove_readonly)
        print(f"Удален каталог {folder_path}")

# Задайте путь к каталогу, где нужно удалить .git и сам каталог
delete_git_and_folder(r"..\Python_Basic")
