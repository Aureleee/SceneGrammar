# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aurele <aurele@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 21:31:40 by aurele            #+#    #+#              #
#    Updated: 2026/02/08 12:39:57 by aurele           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import importlib
import utils 
importlib.reload(utils)


generator = utils.SemanticPromptGenerator()
prompt = generator.generate_prompt()
print(prompt)

with open("saved_prompts.txt", "a") as f:
    f.write(prompt + "\n")