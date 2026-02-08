# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aurele <aurele@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 21:31:40 by aurele            #+#    #+#              #
#    Updated: 2026/02/08 11:33:49 by aurele           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils import *

generator = SemanticPromptGenerator()
prompt = generator.generate_prompt()
print(prompt)