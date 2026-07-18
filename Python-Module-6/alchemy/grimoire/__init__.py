#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 19:49:19 by mozay           #+#    #+#               #
#  Updated: 2026/07/18 12:03:39 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .light_spellbook import light_spell_record
from .dark_spellbook import dark_spell_record

__all__ = ["light_spell_record", "dark_spell_record"]
