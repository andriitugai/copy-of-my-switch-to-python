from hw1_model import *

def create_sheer_map():
     # Create objects on the map
    frodo_house = House("Frodo's house", 
                '''Frodo lives here. a little house with yard and other stuff''')

    nearby_river = River('River', "Nearby river")
    bilbo_house = House("Bilbo's house", 
                '''Bilbo lives here. a little house with yard and other stuff''')
    bilbo_garden = Field("Bilbo Garden", "Bilbo is working here...")
    east_road = Road("East Road", 
                '''The road from Bilbo's and Frodo's houses to the Forest''')

    north_marsh = DangerLocation("Marsh", '''The marsh on the north''')
    dead_forest = DangerLocation("Dead Forest", '''The very dangerous forest''')
    forest = Forest("Sunny forest", '''Safe forest in the middle of the map''')
    west_road = Road("West Road", '''The road from Harfoots House to the Forest''')
    harfoots_house = House("Harfoots's House", '''A lot of Herfoots live here''')
    harfoots_field = Field("Harfoots's Field", "Big field, where Harfoots grows their plants.")


    # Create links between the objects
    frodo_house.add_link(bilbo_house)
    bilbo_house.add_link(east_road)
    bilbo_house.add_link(bilbo_garden)
    east_road.add_link(frodo_house)
    frodo_house.add_link(nearby_river)
    frodo_house.add_link(north_marsh)
    east_road.add_link(dead_forest)
    dead_forest.add_link(forest)
    east_road.add_link(forest)
    north_marsh.add_link(nearby_river)
    forest.add_link(west_road)
    west_road.add_link(harfoots_field)
    west_road.add_link(harfoots_house)

    return [
            bilbo_house,
            frodo_house,
            nearby_river,
            bilbo_garden,
            east_road,
            north_marsh,
            dead_forest,
            forest,
            west_road,
            harfoots_house,
            harfoots_field
    ]
