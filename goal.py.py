import datetime
class Goal:
    def __init__(self, name, target_sum, category):
        self.name = name
        self.target_sum = float(target_sum)
        self.current_balance = 0.0
        self.category = category
        self.status = "В процессе"
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_funds(self, amount):
        """Пункт 1.2: Увеличение баланса с проверкой на превышение"""
        if amount <= 0:
            print("Сумма пополнения должна быть больше нуля.")
            return False
        
        if self.current_balance + amount > self.target_sum:
            print(f"Ошибка: Баланс не может превышать итоговую сумму ({self.target_sum}).")
            return False

        self.current_balance += amount
        self.check_status() # Проверяем, не достигли ли цели (Пункт 1.4)
        return True

    def subtract_funds(self, amount):
        """Пункт 1.2: Уменьшение баланса"""
        if amount <= 0:
            print("Сумма списания должна быть больше нуля.")
            return False
        
        if self.current_balance - amount < 0:
            print("Ошибка: Баланс не может быть отрицательным.")
            return False

        self.current_balance -= amount
        self.check_status()
        return True

    def get_progress(self):
        """Пункт 1.3: Вычисление процента выполнения"""
        progress = (self.current_balance / self.target_sum) * 100
        return round(progress, 2)

    def check_status(self):
        """Пункт 1.4: Изменение статуса при достижении цели"""
        if self.current_balance >= self.target_sum:
            self.status = "Выполнена"

    def to_dict(self):
        """Для сохранения в JSON"""
        return {
            "name": self.name,
            "target_sum": self.target_sum,
            "current_balance": self.current_balance,
            "category": self.category,
            "status": self.status,
            "created_at": self.created_at
        }