import hw1_map


def main():

    sheer_map = hw1_map.create_sheer_map()

    for location in sheer_map:
        location.print_short_info()  

    # print(frodo_house.linked_locations)
    # print(east_road.linked_locations)

    # print(dead_forest.linked_locations)
    # print(north_marsh.linked_locations)
    # print(nearby_river.linked_locations)

if __name__ == '__main__':
    main()



