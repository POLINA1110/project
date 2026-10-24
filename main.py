import json
import os
from goal import Goal

DATA_FILE = "goals.json"

def load_goals():
    """Загрузка целей из файла JSON"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            goals = []
            for item in data:
                goal = Goal(item['name'], item['target_sum'], item['category'])
                goal.current_balance = item['current_balance']
                goal.status = item['status']
                goal.created_at = item['created_at']
                goals.append(goal)
            return goals
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def save_goals(goals):
    """Сохранение целей в файл JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump([goal.to_dict() for goal in goals], file, ensure_ascii=False, indent=4)

def show_all_goals(goals):
    """Просмотр всех целей"""
    if not goals:
        print("\nУ вас пока нет целей.")
        return
    
    print("\n--- Ваши цели ---")
    for i, goal in enumerate(goals, 1):
        print(f"{i}. [{goal.category}] {goal.name}")
        print(f"   Статус: {goal.status} | Прогресс: {goal.get_progress()}%")
        print(f"   Баланс: {goal.current_balance} / {goal.target_sum}")
        print("-" * 30)

def main():
    goals = load_goals()

    while True:
        print("\n=== КОПИЛКА ===")
        print("1. Добавить новую цель")
        print("2. Посмотреть все цели")
        print("3. Пополнить баланс цели")
        print("4. Списать средства с цели")
        print("5. Удалить цель")
        print("0. Выход")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Название цели: ")
            category = input("Категория (например, Работа, Здоровье): ")
            try:
                target_sum = float(input("Итоговая сумма: "))
                goals.append(Goal(name, target_sum, category))
                save_goals(goals)
                print("Цель успешно добавлена!")
            except ValueError:
                print("Ошибка: Сумма должна быть числом.")

        elif choice == "2":
            show_all_goals(goals)

        elif choice == "3":
            show_all_goals(goals)
            if not goals: continue
            try:
                idx = int(input("Введите номер цели для пополнения: ")) - 1
                amount = float(input("Сумма пополнения: "))
                if 0 <= idx < len(goals):
                    if goals[idx].add_funds(amount):
                        save_goals(goals)
                        print("Баланс обновлен!")
                else:
                    print("Неверный номер цели.")
            except ValueError:
                print("Ошибка ввода.")

        elif choice == "4":
            show_all_goals(goals)
            if not goals: continue
            try:
                idx = int(input("Введите номер цели для списания: ")) - 1
                amount = float(input("Сумма списания: "))
                if 0 <= idx < len(goals):
                    if goals[idx].subtract_funds(amount):
                        save_goals(goals)
                        print("Баланс обновлен!")
                else:
                    print("Неверный номер цели.")
            except ValueError:
                print("Ошибка ввода.")

        elif choice == "5":
            show_all_goals(goals)
            if not goals: continue
            try:
                idx = int(input("Введите номер цели для удаления: ")) - 1
                if 0 <= idx < len(goals):
                    deleted_goal = goals.pop(idx)
                    save_goals(goals)
                    print(f"Цель '{deleted_goal.name}' удалена.")
                else:
                    print("Неверный номер цели.")
            except ValueError:
                print("Ошибка ввода.")

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()