from functools import reduce

def modify_list(options, char):
    slice_point = int(len(options)/2)
    if char in ('F', 'L'):
        return options[0:slice_point]
    else:
        return options[slice_point:]

def find_value(dirs, size):
    return reduce(modify_list, dirs, range(0,size))[0]

def seat_id(row, seat):
    return row * 8 + seat

def find_seat(spec):
    row = find_value(spec[0:7], 128)
    seat = find_value(spec[7:], 8)
    return {"row": row,
            "seat": seat,
            "id": seat_id(row, seat)}

def solve(input):
    seats = [find_seat(spec) for spec in input]
    seat_ids = set([seat["id"] for seat in seats])
    all_seats = set(range(min(seat_ids), max(seat_ids) + 1))
    my_seat = all_seats - seat_ids

    return (max(seat_ids),my_seat)


