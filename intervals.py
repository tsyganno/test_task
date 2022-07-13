import itertools


def all_events(task):
    for v in task.values():
        yield from zip(v, itertools.cycle((-1, 1)))


def presence_events(task):
    c_prev = 0
    for time, border in sorted(all_events(task)):
        c_next = c_prev + border
        if c_prev == -2 and c_next == -3:
            yield time, border
        if c_prev == -3 and c_next == -2:
            yield time, border
        c_prev = c_next


def presence(task):
    return sum(t * b for t, b in presence_events(task))


test_1 = {'data': {'lesson': [1594663200, 1594666800], 'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}}
test_2 = {'data': {'lesson': [1594702800, 1594706400], 'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641], 'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}}
test_3 = {'data': {'lesson': [1594692000, 1594695600], 'pupil': [1594692033, 1594696347], 'tutor': [1594692017, 1594692066, 1594692068, 1594696341]}}


print(presence(test_1['data']))
print(presence(test_2['data']))
print(presence(test_3['data']))
