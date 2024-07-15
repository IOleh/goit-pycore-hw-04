def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats

# Приклад використання функції:
cats_info = get_cats_info("HW2_cats_file.txt")
print(cats_info)
