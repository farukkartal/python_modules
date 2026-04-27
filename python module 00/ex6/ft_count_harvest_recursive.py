# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_recursive.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 01:36:46 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/04/28 02:03:37 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive() -> None:
    target = int(input("Days until harvest: "))

    def ft_days_counter(counter, target) -> None:
        if counter > target:
            print("Harvest time!")
        else:
            print(f"Day {counter}")
            counter = counter + 1
            ft_days_counter(counter, target)
    ft_days_counter(1, target)
