# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_data.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/05/01 05:24:20 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/05/11 23:50:25 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant1.show()

    plant2 = Plant("Sunflower", 80, 45)
    plant2.show()

    plant3 = Plant("Cactus", 15, 120)
    plant3.show()
