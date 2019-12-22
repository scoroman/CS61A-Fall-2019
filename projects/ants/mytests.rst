This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *
	>>> beehive, layout = Hive(AssaultPlan()), dry_layout
	>>> dimensions = (1, 9)
	>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
	>>> thrower = ThrowerAnt()
	>>> ant_place = colony.places["tunnel_0_0"]
	>>> ant_place.add_insect(thrower)

	Case Example
		>>> x = 5
		>>> x
		5

	Case Ex 1 
	>>> near_bee = Bee(2) # A Bee with 2 armor
	>>> far_bee = Bee(3)  # A Bee with 3 armor
	>>> near_place = colony.places['tunnel_0_3']
	>>> far_place = colony.places['tunnel_0_6']
	>>> near_place.add_insect(near_bee)
	>>> far_place.add_insect(far_bee)
	>>> nearest_bee = thrower.nearest_bee(colony.beehive)
	>>> thrower.nearest_bee(colony.beehive) is far_bee
	#False
	>>> thrower.nearest_bee(colony.beehive) is near_bee
	#True
	>>> nearest_bee.armor
	#2