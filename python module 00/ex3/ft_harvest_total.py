# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_harvest_total.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 21:36:53 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/04/27 21:43:51 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    harvest1 = int(input("Day 1 harvest: "))
    harvest2 = int(input("Day 2 harvest: "))
    harvest3 = int(input("Day 3 harvest: "))
    total_harvest = harvest1 + harvest2 + harvest3
    print(f"Total harvest: {total_harvest}")
