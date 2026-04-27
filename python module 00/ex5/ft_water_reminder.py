# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_water_reminder.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 21:52:11 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/04/28 01:17:18 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:

    last_time = int(input("Days since last watering: "))
    if last_time > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
