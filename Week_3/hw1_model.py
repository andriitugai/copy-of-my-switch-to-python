import itertools

class Location(object):
    ''' Base class for location.
    '''

    # Location usually is a safe place. We can as come in such as go out of it.
    safe_place = True

    @classmethod
    def is_safe_here(cls):
        return cls.safe_place
    

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
            if location not in self.locations_container and self.is_safe_here():
                self._linked_locations.append(location)
                self.locations_container.add(location)
            if self not in location :
                location.add_link(self)

    def remove_link(self, location):
        if isinstance(location, Location):
            if location in self.locations_container:
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

    def print_short_info(self):
        print()
        print(self.name)
        link_template0 = '    |'
        link_template1 = '    +----->  {0}'
        for link in self.linked_locations:
            # print(link_template0)
            print(link_template1.format(link))


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
