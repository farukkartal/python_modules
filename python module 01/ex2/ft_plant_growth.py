# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/05/01 06:09:18 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/05/11 23:50:59 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def age(self) -> None:
        self.plant_age = self.plant_age + 1

    def grow(self, amount: float) -> None:
        self.height = round(self.height + amount, 1)


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30)
    plant1.show()

    for days in range(1, 8):
        print(f"=== Day {days} ===")
        plant1.age()
        plant1.grow(0.8)
        plant1.show()

    print(f"Growth this week: {round(plant1.height - 25.0, 1)}cm")
