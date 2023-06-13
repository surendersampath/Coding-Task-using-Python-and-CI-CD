
def test_func(a, b):
    return a + b


def decode_seat_number_from_boarding_pass(boarding_pass_string):
    # Decode the row number
    row_string = boarding_pass_string[:7]
    row_binary = row_string.replace("F", "0").replace("B", "1")
    row_number = int(row_binary, 2)
    
    # Decode the column number
    col_string = boarding_pass_string[7:]
    col_binary = col_string.replace("L", "0").replace("R", "1")
    col_number = int(col_binary, 2)
    
    # Calculate the seat ID
    seat_id = row_number * 8 + col_number

    return seat_id


def find_seat_from_scanned_boarding_pass ( scanned_boarding_pass_data ):
    return -1