# Copilot Instructions for AI Agents

## Project Overview
This is a simple Python CLI application for managing and displaying recipes (receptenboek). The codebase is organized into clear modules for models and UI logic.

## Architecture
- **models/**: Contains core data classes:
  - `ingredient.py`: Defines `Ingrediënt` (ingredient with name, amount, unit)
  - `stap.py`: Defines `Stap` (a single recipe step)
  - `recept.py`: Defines `Recept` (recipe with name, description, ingredients, steps)
- **ui/cli.py**: Main CLI interface. Handles user input, displays recipes, and manages the main loop.
- **main.py**: (Not shown) Likely entry point; may import and run `ui.cli.start()`.

## Key Patterns & Conventions
- **Dutch Naming**: Class and variable names use Dutch (e.g., `Ingrediënt`, `Stap`, `Recept`, `recepten`). Maintain this convention for new features.
- **Data Flow**: Recipes are seeded in `seed_recepten()` and passed to the CLI loop. All user interaction is via the terminal.
- **No External Dependencies**: The project uses only standard Python, no third-party packages.
- **Simple OOP**: Each model is a simple class with attributes; no inheritance or advanced patterns.

## Developer Workflows
- **Run the app**: Execute `python main.py` from the project root (assumed standard entry point).
- **Add a recipe**: Update `seed_recepten()` in `ui/cli.py` to add new recipes, ingredients, or steps.
- **Extend models**: Add new fields or methods in the relevant file in `models/`.
- **No tests or build system**: There are no automated tests or build scripts. Manual testing via CLI is expected.

## Example: Adding a New Ingredient
To add a new ingredient to a recipe, update the `ingrediënten` list in `seed_recepten()`:
```python
ingrediënten = [Ingrediënt("Spaghetti", 75, "g"), Ingrediënt("Pesto", 20, "g"), Ingrediënt("Kaas", 10, "g")]
```

## File References
- `models/ingredient.py`, `models/stap.py`, `models/recept.py`: Core data structures
- `ui/cli.py`: Main CLI logic and user interaction

## AI Agent Guidance
- Follow Dutch naming and keep CLI logic simple and linear
- Place new models in `models/`, new UI logic in `ui/`
- Avoid introducing external dependencies unless explicitly requested
- Keep user interaction text in Dutch

---
For questions or unclear conventions, ask for clarification or examples from the user.
