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

        print("Seeds: ", seeds)


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
