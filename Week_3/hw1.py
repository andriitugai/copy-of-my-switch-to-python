class Location(object):
    ''' Base class for location.
    '''

    # Location usually is a safe place. We can as come in such as go out of it.
    safe_place = True

    def __init__(self, name, description):
        self._name = name
        self._description = description
        self.locations_container = set()
        self._linked_locations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def linked_locations(self):
        return self._linked_locations

    @linked_locations.setter
    def linked_locations(self, lst):
        for location in lst:
            if location not in self.locations_container:
                self._linked_locations.append(location)
                self.locations_container.add(location)


    def add_link(self, location):
        if isinstance(location, Location):
            if location not in self.locations_container and location.__class__.safe_place:
                print("adding {location}. Safe place")
                self._linked_locations.append(location)
                self.locations_container.add(location)
            if self not in location and location.__class__.safe_place:
                location.add_link(self)

    def remove_link(self, location):
        if isinstance(location, Location):
            if location in self.locations_container and location.__class__.safe_place:
                self._linked_locations.remove(location)
                self.locations_container.remove(location)
            if self in location:
                location.remove_link(self)

    def __contains__(self, location):
        return location in self.locations_container

    def __str__(self):
        return(f'<{self.__class__.__bases__[0].__name__}: {self.__class__.__name__} "{self._name}">')

    def __repr__(self):
        return str(self)


class DangerLocation(Location):
    '''Class for dangerous locations, you can only enter in.
    Where are only incoming ways to such places, and no ways out'''

    safe_place = False


class House(Location):
    pass


class Road(Location):
    pass


class Field(Location):
    pass


class Forest(Location):
    pass


class River(Location):
    pass


    
def main():

    # Create objects on the map
    frodo_house = House("Frodo's house", 
                '''Frodo lives here. a little house with yard and other stuff''')

    nearby_river = River('River', "Nearby river")
    bilbo_house = House("Bilbo's house", 
                '''Bilbo lives here. a little house with yard and other stuff''')

    east_road = Road("East Road", 
                '''The road from Bilbo's and Frodo's houses to the Forest''')

    north_marsh = DangerLocation("Marsh", '''The marsh on the north''')
    dead_forest = DangerLocation("Dead Forest", '''The very dangerous forest''')
    forest = Forest("Sunny forest", '''Safe forest in the middle of the map''')

    frodo_house.add_link(bilbo_house)
    bilbo_house.add_link(east_road)
    east_road.add_link(frodo_house)
    frodo_house.add_link(nearby_river)
    frodo_house.add_link(north_marsh)
    east_road.add_link(dead_forest)
    dead_forest.add_link(forest)
    east_road.add_link(forest)

    north_marsh.add_link(nearby_river)

    print(frodo_house.linked_locations)
    print(east_road.linked_locations)

    print(dead_forest.linked_locations)
    print(north_marsh.linked_locations)

    print(nearby_river.linked_locations)



if __name__ == '__main__':
    main()



