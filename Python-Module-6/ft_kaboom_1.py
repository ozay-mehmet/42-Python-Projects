#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/18 11:59:55 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 12:07:00 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Fantasy", "Earth, wind and fire"))


if __name__ == "__main__":
    main()
