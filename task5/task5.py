import enum


class Maps(enum.Enum):
    seed_to_soil = 1
    soil_to_fertilizer = 2
    fertilizer_to_water = 3
    water_to_light = 4
    light_to_temperature = 5
    temperature_to_humidity = 6
    humidity_to_location = 7


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        # Parse seeds
        seeds = set(map(int, lines[0].split()[1:]))
        _maps = build_data(lines[2:])
        lowest_location = find_lowest_location(_maps, seeds)
        print("Lowest location number: ", lowest_location)


def find_lowest_location(maps, seeds):
    source = seeds
    successors = None
    for _map in maps.values():
        successors = []
        for source_value in source:
            successor = source_value
            for key in _map:
                values = _map[key]
                source_start = values[1]
                destination_start = values[0]
                _range = values[2]
                if source_start <= source_value < source_start + _range:
                    successor = destination_start + (source_value - source_start)
                    break
            successors.append(successor)
        source = successors

    return min(successors)


def build_data(lines):
    data = {}
    map_index = None

    for line in lines:
        # Check if line is a map_caption
        if line[0].isdigit():
            values = list(map(int, line.split()))
            _dict = data.get(map_index, dict())
            _dict[values[1]] = values
            data[map_index] = _dict
            continue

        for map_caption in Maps:
            if line.startswith(map_caption.name.replace("_", "-")):
                map_index = map_caption.value
                break

    return data


if __name__ == "__main__":
    main()
