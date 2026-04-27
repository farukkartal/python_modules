# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plot_area.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fakartal@student.42istanbul.com.tr <fakartal+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/27 20:54:51 by fakartal@student.42#+#    #+#             #
#   Updated: 2026/04/27 21:30:16 by fakartal@student.4###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    total_area = width * length
    print(f"Plot area: {total_area}")
