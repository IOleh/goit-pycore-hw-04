import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація бібліотеки colorama
init(autoreset=True)

def print_directory_tree(path, indent=""):
    try:
        path = Path(path)
        if not path.exists():
            print(Fore.RED + "Шлях не існує.")
            return
        if not path.is_dir():
            print(Fore.RED + "Вказаний шлях не веде до директорії.")
            return

        for item in path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + indent + "📂 " + item.name)
                print_directory_tree(item, indent + "    ")
            else:
                print(Fore.GREEN + indent + "📜 " + item.name)
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: [python HW3_Script.py ""D:/My documents/PyCharm/goit-pycore-hw-04/HW3_Script.py""]")
        return
    
    directory_path = sys.argv[1]
    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()
