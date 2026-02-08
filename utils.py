# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aurele <aurele@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 19:36:23 by aurele            #+#    #+#              #
#    Updated: 2026/02/08 11:32:23 by aurele           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

class SemanticPromptGenerator:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.semantic_vocabulary = {
            "vegetation_forest": [
                "dense forest",
                "vegetation cover",
                "tree canopy",
                "natural terrain",
                "green areas",
                "foliage",
                "wooded regions"
            ],
            "roads_ground": [
                "road network",
                "asphalt roads",
                "ground surface",
                "paths",
                "open areas",
                "terrain"
            ],
            "buildings_urban": [
                "urban area",
                "buildings",
                "residential blocks",
                "built-up regions"
            ],
            "infrastructure": [
                "infrastructure",
                "industrial structures"
            ],
            "vehicles": [
                "vehicles"
            ]
        }
        self.semantic_coverage_ranges = {
            "vegetation_forest": (35, 55),
            "roads_ground": (20, 35),
            "buildings_urban": (10, 20),
            "infrastructure": (5, 10),
            "vehicles": (2, 5)
        }
        self.coverage_patterns = [
            "covering approximately {p}% of the scene",
            "occupying around {p}% of the image",
            "representing roughly {p}% of the scene",
            "accounting for about {p}% of the overall area",
            "spanning nearly {p}% of the image",
            "forming about {p}% of the background"
        ]

    def _sample_percentage(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def _sample_vocabulary(self, words, k=2):
        return ", ".join(random.sample(words, min(k, len(words))))

    def _sample_coverage_phrase(self, percentage):
        pattern = random.choice(self.coverage_patterns)
        return pattern.format(p=percentage)

    def generate_prompt(self):
        components = []

        for category, words in self.semantic_vocabulary.items():
            min_p, max_p = self.semantic_coverage_ranges[category]
            percentage = self._sample_percentage(min_p, max_p)
            vocab = self._sample_vocabulary(words)
            coverage_phrase = self._sample_coverage_phrase(percentage)

            components.append(f"{vocab} {coverage_phrase}")

        return "Semantic background composed of " + ", ".join(components) + "."
