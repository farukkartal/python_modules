# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_iterative.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/28 01:24:50 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/04/28 01:36:02 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    days = days + 1
    for days in range(1, days):
        print(f"Day {days}")
    print("Harvest time!")
