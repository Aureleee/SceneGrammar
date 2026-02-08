## SceneGrammar

This repository provides a **lightweight Python** tool to generate structured semantic scene prompts.
You define what appears in the image and how much of it, and the tool automatically builds clean prompts for image generation pipelines

--- 
No compilation.  
No environment setup.  
Just Python :D

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repo_url> scenegrammar
````

```bash
cd scenegrammar
```

---

### 2. Run the code

The project uses **only standard Python**.
No external libraries are required.

```bash
python main.py
```

That’s it.

---

## Project Structure

```text
scenegrammar/
├── utils.py      # SemanticPromptGenerator class
├── main.py       # Example usage
└── README.md
```

---

## How it works (quick insight)

The core logic is contained in the `SemanticPromptGenerator` class.

It is based on three elements:

1. **Semantic vocabulary**

```python
self.semantic_vocabulary = {
    "vegetation_forest": [...],
    "roads_ground": [...],
    "buildings_urban": [...],
    "infrastructure": [...],
    "vehicles": [...]
}
```

2. **Semantic coverage ranges (in percent)**

```python
self.semantic_coverage_ranges = {
    "vegetation_forest": (35, 55),
    "roads_ground": (20, 35),
    "buildings_urban": (10, 20),
    "infrastructure": (5, 10),
    "vehicles": (2, 5)
}
```

3. **Prompt generation**
   The generator:

* samples vocabulary terms
* samples realistic percentages
* combines them into a structured sentence

---

## Example Output

```text
Semantic background composed of dense forest, vegetation cover forming about 48% of the background,
road network, ground surface occupying around 27% of the image,
residential blocks, built-up regions representing roughly 15% of the scene,
infrastructure accounting for about 7% of the overall area,
vehicles spanning nearly 3% of the image.
```

---

## Reproducibility

You can control randomness using a seed:

```python
generator = SemanticPromptGenerator(seed=42)
```

* same seed → same prompt
* no seed → random generation

---