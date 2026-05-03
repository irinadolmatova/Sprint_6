import random

class OrderDataHelper:
    @staticmethod
    def generate_order_data():
        names = ["Кими", "Алекс", "Макс", "Джени", "Женевьева"]
        surnames = ["Ли", "Ким", "Мун", "Россини", "Квят"]
        name = random.choice(names)
        surname = random.choice(surnames)
        address = f"Москва, ул. Пушкинская, д. {random.randint(100, 200)}"
        phone = f"79{random.randint(100000000, 999999999)}"
        date = f"{random.randint(10, 28)}.{random.randint(10, 12)}.2026"
        comment = "комментарий"
        return name, surname, address, phone, date, comment