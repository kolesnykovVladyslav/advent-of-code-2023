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
        print("Subtask2: Lowest location number: ", find_lowest_location_b(_maps, seeds))


def find_lowest_location_b(maps, seeds):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    ranges_to_check = seed_ranges
    for mapping in maps.values():
        ranges = mapping.values()
        _next = []
        while len(ranges_to_check) > 0:
            found = False
            start_range, end_range = ranges_to_check.pop()
            for destination, source, _range in ranges:
                start_overlap = max(start_range, source)
                end_overlap = min(end_range, source + _range)
                if start_overlap < end_overlap:
                    _next.append((start_overlap - source + destination, end_overlap - source + destination))
                    found = True
                    if start_overlap > start_range:
                        ranges_to_check.append((start_range, start_overlap))
                    if end_range > end_overlap:
                        ranges_to_check.append((end_overlap, end_range))
            if not found:
                _next.append((start_range, end_range))
        ranges_to_check = _next
    return min(ranges_to_check)[0]


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
