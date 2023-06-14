# Coding Assignment

# Boarding Pass Finder

The Boarding Pass Finder is a Python module that decodes seat numbers from boarding pass strings and finds the missing seat number from a list of scanned boarding pass data by elimniation method.

Approach to the problem :
1. Use phone's camera to scan nearby boarding passes and store it a data source.
2. Binary space partitioning to determine seat location.
3. Decode the seat code by following the specified rules.
4. Identify the row and column based on the seat code.
5. Calculate the seat ID by multiplying the row by 8 and adding the column.
6. Find the highest seat ID among all the boarding passes.
7. Your seat is missing from the list, but seats with IDs +1 and -1 from yours will be present.
8. Determine the ID of your seat.


## Requirements

- Python 3.6 and above. Can be run in Github codespace.
- Not dependent on any other Python libraries.

## Installation

No installation is required for the Boarding Pass Finder module. Simply clone the repo and make sure you have the gitlab actions setup. Commit on the master will perform unit testing. Otherwise, refer unit testing command below. Can be run in Github codespace.

## Usage


1. Decode the seat number from a boarding pass string using the `decode_seat_number_from_boarding_pass` function:

```python
boarding_pass_string = "BFFFBBFRRR"
seat_number = decode_seat_number_from_boarding_pass(boarding_pass_string)
print(seat_number)  # Output: 567
```

2. Find the missing seat number from a set of scanned boarding pass data using the `find_seat_from_scanned_boarding_pass` function:
   All the scanned boarding passes are loaded into a set from the textfile and then passed on this function during the unit tests.

```python
scanned_boarding_pass_data = {"BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"}
missing_seat_number = find_seat_from_scanned_boarding_pass(scanned_boarding_pass_data)
print(missing_seat_number)  # Output: 640
```

## Testing

The module includes unit tests for the `decode_seat_number_from_boarding_pass` and `find_seat_from_scanned_boarding_pass` functions. This is included in the continous integration. So, every push on the main branch will automatically run these unit tests and will only fail on unittests failure.
The test cases can be executed by running the module as follows:

```bash
python unittests.py
```

The test results of the unit tests will be displayed in the console of the CI/CD pipeline.

## Logging

The module utilises the Python logging module to log informational and error messages. The logs are saved in the `coding_Challenge.log` file. The log file is created in the same directory as the module. It also captures the outcome of the challenge and other errors if exist.

## License

NA.

## Acknowledgments
NA
