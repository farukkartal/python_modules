# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 02:06:27 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/04/28 02:22:35 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    edited = seed_type.capitalize()
    if unit == "packets":
        print(f"{edited} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{edited} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{edited} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
