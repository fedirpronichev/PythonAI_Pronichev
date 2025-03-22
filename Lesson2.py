import random


class Student:
    amount_of_student = 0

    def __init__(self, name, scholarship=50, money=500):
        self.name = name
        self.scholarship = scholarship
        self.money = money
        self.height = 170
        self.knowledge = 0
        self.stress = 0
        Student.amount_of_student += 1

    def work(self):
        earnings = random.randint(200, 500)
        self.money += earnings
        self.stress += 10
        print(f"{self.name} працював і заробив {earnings}. Гроші: {self.money}, Стрес: {self.stress}")

    def study(self):
        self.knowledge += random.randint(5, 15)
        self.stress += 5
        print(f"{self.name} вчився. Знання: {self.knowledge}, Стрес: {self.stress}")

    def relax(self):
        expenses = random.randint(50, 150)
        self.money -= expenses
        self.stress -= 10
        print(f"{self.name} відпочивав. Витрати: {expenses}, Гроші: {self.money}, Стрес: {self.stress}")

    def live_month(self):
        print(f"\nМісяць почався для {self.name}")
        self.money += self.scholarship
        print(f"Стипендія отримана. Гроші: {self.money}")

        for _ in range(4):
            if self.money < 100:
                self.work()
            elif self.knowledge < 50:
                self.study()
            elif self.stress > 30:
                self.relax()
            else:
                self.study()

        print(f"Місяць закінчився для {self.name}. Гроші: {self.money}, Знання: {self.knowledge}, Стрес: {self.stress}")

    def live_year(self):
        for month in range(1, 13):
            print(f"\n========== Місяць {month} ==========")
            self.live_month()
        print(f"\nРік закінчився! {self.name}: Гроші: {self.money}, Знання: {self.knowledge}, Стрес: {self.stress}")


# запускається симуляція життя студента на один рік
tom = Student(name="Tom", scholarship=100, money=300)
tom.live_year()
