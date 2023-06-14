# Coding Assignment

Problem Statement : 

```Text

£$%$£%R%£$ is company and they send you to a conference!

You head off to the airport and when it’s time to board your flight, you discover a problem; you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the other passengers.

Not to worry, you write a quick program to use your phone's camera to scan all of the nearby boarding passes (your input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last three characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

As it’s time to board... you’ll also need to find your seat ID!

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
```

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
Note : The test data can be edited in the file ```testdata.txt```
## Testing

The module includes unit tests for the `decode_seat_number_from_boarding_pass` and `find_seat_from_scanned_boarding_pass` functions. 
This is further extended by Github continous integration configured inside the workflow folder. 
So, every push on the main branch will automatically run these unit tests and will only fail on unittests failure.
The test cases can be executed by running the module as follows:

```bash
python unittests.py
```
The test results of the unit tests will be displayed in the console of the CI/CD pipeline.

## Logging

The module utilises the Python logging module to log informational and error messages. The logs are saved in the `coding_Challenge.log` file. The log file is created in the same directory as the module. It also captures the outcome of the challenge and other errors if exist.
Example from the file

```
root - INFO - Sanity Check - Highest Seat Number : 871
root - INFO - Your Seat Number : 640
```

## License

NA.

## Author
<a href="https://www.linkedin.com/in/surendersampath/" title="Title Text">Surender Sampath </a>

