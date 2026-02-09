# TODO: Generate Different Routes from Successful Ones

## Information Gathered
- Successful routes are stored in `attempts/succesfull/` with JSON files containing inputs and results.
- Existing successful routes:
  - route1.json: ["a", "a", "14210"] -> escaped
  - route2.json: ["b", "y", "b", "a"] -> unsafe
  - route3.json: ["b", "y", "a", "a", "b", "b", "b", "b"] -> unsafe
  - escaped_route_1_4_2_10.json: escaped
  - unsafe_route_1_7_4_2.json: unsafe
  - unsafe_route_1_7_5_9_2.json: unsafe
- Failed routes are in `attempts/failed/` with various errors.
- The game logic is in `game.py`, dungeon rooms in `dungeon.py`, and test scripts like `final_routes.py` run different input combinations.
- Routes are defined by room order ('1', '7', '4', '5', '8', '3', '9', '6', '2', '10') and user inputs that determine the path.

## Plan
- Create a new script to generate and test multiple input combinations that differ from existing successful routes.
- Focus on inputs that lead to different outcomes: failed, lost, rescued, forced, cheated.
- Run the script to simulate routes and save results to `attempts/failed/` or new categories if different.
- Ensure new routes are not identical to existing successful ones.

## Dependent Files to be edited
- Create new script: `module_5/generate_different_routes.py`
- No changes to existing files needed initially.

## Followup steps
- Run the new script to generate routes.
- Review generated JSON files for different outcomes.
- If needed, adjust inputs in the script for more variety.
