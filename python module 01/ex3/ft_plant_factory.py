# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_factory.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/05/11 23:23:05 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/05/12 00:28:30 by fakartal@student.4###   ########.fr       #
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
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25.0, 30)
    print("Created: ", end="")
    plant1.show()
    plant2 = Plant("Oak", 200.0, 365)
    print("Created: ", end="")
    plant2.show()
    plant3 = Plant("Cactus", 5.0, 90)
    print("Created: ", end="")
    plant3.show()
    plant4 = Plant("Sunflower", 80.0, 45)
    print("Created: ", end="")
    plant4.show()
    plant5 = Plant("Fern", 15.0, 120)
    print("Created: ", end="")
    plant5.show()
