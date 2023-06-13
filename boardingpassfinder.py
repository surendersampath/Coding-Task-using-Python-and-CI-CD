import logging

logging.basicConfig(filename='coding_Challenge.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)


def decode_seat_number_from_boarding_pass(boarding_pass_string):

    if boarding_pass_string == "":
        logging.critical("Incorrect boarding pass data.")

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


def find_seat_from_scanned_boarding_pass(scanned_boarding_pass_data):
    try:
        seats = set()
        highest_seat_id = 0
        missing_seat_id = 0

        seats = set(map(decode_seat_number_from_boarding_pass, scanned_boarding_pass_data))
        highest_seat_id = max(seats)

        # Find the missing seat by checking consecutive seat IDs
        missing_seat_id = next(filter(lambda seat_id: seat_id not in seats and (seat_id + 1) in seats and (seat_id - 1) in seats,
                                range(highest_seat_id + 1)))

        logging.info("Sanity Check - Highest Seat Number : " + str(highest_seat_id))
        logging.info("Your Seat Number : " + str(missing_seat_id))
    
    except:
        logging.critical("Error in Scanned Data.")

    
    return missing_seat_id
