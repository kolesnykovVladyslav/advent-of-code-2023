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
        seeds = list(map(int, lines[0].split()[1:]))
        _maps = build_data(lines[2:])
        print("Subtask1: Lowest location number: ", find_lowest_location(_maps, seeds))

        '''
        seed_to_soil_map = _maps[Maps.seed_to_soil.value]
        seeds_ranges = set()
        for i in range(0, len(seeds), 2):
            _seed_start = seeds[i]
            _seed_end = _seed_start + seeds[i + 1] - 1

            for values in seed_to_soil_map.values():
                source_start = values[1]
                source_end = source_start + values[2] - 1

                intersection_start = max(_seed_start, source_start)
                intersection_end = min(_seed_end, source_end)
                if intersection_start <= intersection_end:
                    _range = range(max(_seed_start, source_start), min(_seed_end, source_end))
                    seeds_ranges.update(set(_range))

        print("Subtask2: Lowest location number: ", find_lowest_location(_maps, seeds_ranges))
        '''


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
