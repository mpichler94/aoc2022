import re
from collections import namedtuple
import numpy as np

Sensor = namedtuple('Sensor', ['pos', 'distance', 'beacon'])

def parse_input():
    f = open('input.txt')
    #f = open('example.txt')
    lines = f.readlines()
    f.close()

    sensors = []
    for i in range(0, len(lines), 1):
        line = lines[i].strip()
        match = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        pos = [int(match.group(1)), int(match.group(2))]
        beacon = [int(match.group(3)), int(match.group(4))]
        distance = abs(pos[0] - beacon[0]) + abs(pos[1] - beacon[1])
        sensors.append(Sensor(pos, distance, beacon))

    return sensors


def covered_tiles(sensors, target_row):
    row = set()
    beacons = set()

    for sensor in sensors:

        if sensor.beacon[1] == target_row:
            beacons.add(sensor.beacon[0])

        y_distance = abs(target_row - sensor.pos[1])
        x_distance = sensor.distance - y_distance

        if x_distance < 0:
            continue

        x_min = sensor.pos[0] - x_distance
        x_max = sensor.pos[0] + x_distance + 1

        for x in range(x_min, x_max):
            row.add(x)

    for beacon in beacons:
        row.remove(beacon)

    return len(row)


def free_tile(sensors):
    max = 4000000

    beacons = set()

    for sensor in sensors:
        beacons.add((sensor.beacon[0], sensor.beacon[1]))

    for sensor in sensors:
        top_y = sensor.pos[1] + sensor.distance - 1
        bottom_y = sensor.pos[1] - sensor.distance - 1


        for i in range(sensor.distance):
            for x, y in (
                    (sensor.pos[0] + i, top_y - i),
                    (sensor.pos[0] - i, top_y - i),
                    (sensor.pos[0] + i, bottom_y + i),
                    (sensor.pos[0] - i, bottom_y + i),
            ):
                if x < 0 or y < 0 or x > max or y > max:
                    continue
                elif (x, y) in beacons:
                    continue

                for sensor2 in sensors:
                    s_dist = abs(sensor2.pos[0] - x) + abs(sensor2.pos[1] - y)
                    if s_dist <= sensor2.distance:
                        break
                else:
                    return x, y


def part_a(sensors):

    target_row = 2000000
    num_covered = covered_tiles(sensors, target_row)
    print(f'[a] Covered tiles in row {target_row} = {num_covered}')


def part_b(sensors):

    x, y = free_tile(sensors)
    print(f'[b] tuning frequency = {x * 4000000 + y}')


def main():
    sensors = parse_input()

    part_a(sensors)

    part_b(sensors)


if __name__ == '__main__':
    main()
