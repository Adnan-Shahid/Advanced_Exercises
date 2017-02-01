# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Adnan Shahid
# MarkUs Login: shahid41
#

PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # your code here
    # total occurrences left to right
    occurrencesLtoR = lr_occurrences(puzzle, word)
    # total occurrences top to bottom
    # rotates the puzzle 90 degrees and then scans occurrences
    top_to_bottom = rotate_puzzle(puzzle)
    occurrencesTtoB = lr_occurrences(top_to_bottom, word)
    # total occurrences right to left
    # Creates a puzzle that goes right to left, by rotating another 90°
    # (180° in total rotation)
    right_to_left = rotate_puzzle(top_to_bottom)
    occurrencesRtoL = lr_occurrences(right_to_left, word)
    # puzzle is rotated another 90° to achieve a bottom to top orientation
    bottom_to_top = rotate_puzzle(right_to_left)
    # total occurences bottom to top
    occurrencesBtoT = lr_occurrences(bottom_to_top, word)
    # total occurrences
    return (occurrencesTtoB + occurrencesRtoL +
            occurrencesLtoR + occurrencesBtoT)

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> bool
    Checks if a word occurs in a horizontal orientation,
    returns true if a given word is within the puzzle when looking from either
    left-right or right-left, if not, it will return false
    >>> in_puzzle_horizontal(PUZZLE1, 'nick')
        True
    >>> in_puzzle_horizontal(PUZZLE1, 'asdasda')
        False
    >>> in_puzzle_horizontal(PUZZLE1, 'qeuf')
        False
    '''
    # checking if there are any occurences of the word from left to right
    occurrencesLtoR = lr_occurrences(puzzle, word)
    # rotating the puzzle twice to get a right-left orientation
    top_to_bottom = rotate_puzzle(puzzle)
    right_to_left = rotate_puzzle(top_to_bottom)
    # checking if there are any occurences of the word from right to left
    occurrencesRtoL = lr_occurrences(right_to_left, word)
    # gets total horizontal occurences
    horizontalOccurrence = occurrencesRtoL + occurrencesLtoR
    # checks if there were any horizontal occurrences, if there were
    # horizontalOccurrence would be greater than 0, and return true
    return (horizontalOccurrence > 0)

# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> bool
    Checks if a word occurs in within the vertical orientation
    returns true if a given word is within the puzzle when looking from either
    top-bottom or bottom-top, if not, it will return false
    >>> in_puzzle_vertical(PUZZLE1, 'nick')
        True
    >>> in_puzzle_vertical(PUZZLE1, 'asdasda')
        False
    >>> in_puzzle_vertical(PUZZLE1, 'qeuf')
        True
        '''
    # rotating the puzzle once to get a top to bottom orientation
    top_to_bottom = rotate_puzzle(puzzle)
    # scanning for any occurrences of word in this orientation
    occurrencesTtoB = lr_occurrences(top_to_bottom, word)
    # rotating the puzzle 2 more times to get a bottom to top orientation
    right_to_left = rotate_puzzle(top_to_bottom)
    bottom_to_top = rotate_puzzle(right_to_left)
    # scanning for any occurrences of word in this orientation
    occurrencesBtoT = lr_occurrences(bottom_to_top, word)
    # gets total vertical occurences
    verticalOccurrence = occurrencesTtoB + occurrencesBtoT
    # checks if there were any vertical occurrences, if there were
    # verticalOccurrence would be greater than 0, and return true
    return (verticalOccurrence > 0)

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str, str) -> bool
    Checks if the given variable word occurs within the puzzle, returns true
    if the word does occur within the puzzle
    >>> in_puzzle(PUZZLE1, 'nick')
        True
    >>> in_puzzle(PUZZLE1, 'asdasda')
        False
    >>> in_puzzle(PUZZLE1, 'qeuf')
        True
    >>> in_puzzle('xaxy\nyaaa', 'xy')
        True
    '''
    # calls the function total_occurrences, and checks if the number
    # of that function is greater than 0
    return (total_occurrences(puzzle, word) > 0)

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''(str,str) -> bool
    Checks if a given word is in exactly one dimension (either horizontal
    or vertical) and returns true if it is. If the given word is in both
    dimensions, it will return false, and if the given word is in neither
    it will return true
    >>> in_exactly_one_dimension(PUZZLE1, 'brian')
        False
    >>> in_exactly_one_dimension(PUZZLE1, 'asdasda')
        False
    >>> in_exactly_one_dimension(PUZZLE1, 'qeuf')
        True
    >>> in_exactly_one_dimension(PUZZLE2, 'nick')
        False
    '''
    # checks if the word is in the vertical dimension
    inVertical = in_puzzle_vertical(puzzle, word)
    # checks if the word is in the horizontal dimension
    inHorizontal = in_puzzle_horizontal(puzzle, word)
    # checks all cases and returns true if it passes them
    return (not(inVertical and inHorizontal) and
            ((inVertical or inHorizontal)))

# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str,str) -> bool
    Checks if a given word is within puzzle, and if all the occurrences of
    this given word are within the horizontal dimension, and will return true
    if so. If the word is not within the puzzle, it will also return true

    >>> all_horizontal(PUZZLE1,'aaaa')
        True
    >>> all_horizontal(PUZZLE1,'brian')
        False
    >>> all_horizontal(PUZZLE1,'glkut')
        True
    >>> all_horizontal(PUZZLE1,'qeuf')
        False

    '''
    # checks if the word is in the vertical dimension
    inVertical = in_puzzle_vertical(puzzle, word)
    # checks if the word is in the horizontal dimension
    inHorizontal = in_puzzle_horizontal(puzzle, word)
    return ((not(inHorizontal and inVertical)) and not inVertical)

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str,str) -> bool
    Checks if word appears at most once in puzzle, if it appears 0 times
    it will return true, it will also return true if that
    one occurance is a vertical occurance

    >>> at_most_one_vertical(PUZZLE1, 'glkut')
        False
    >>> at_most_one_vertical(PUZZLE1, 'asdasd')
        True
    >>> at_most_one_vertical(PUZZLE1, 'brian')
        False
    >>> at_most_one_vertical(PUZZLE1, 'qeuf')
        True
    >>> at_most_one_vertical(PUZZLE1, 'fueq')
        True


    '''
    # Checking total occurrences of the word
    occurrences = total_occurrences(puzzle, word)
    # Checks if there are any horizontal cases of the word
    isHorizontal = all_horizontal(puzzle, word)
    # total occurrences must be 0 or 1
    # and there cannot be a horizontal occurance
    return ((occurrences == 0) or
            ((occurrences == 1) and not isHorizontal))


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print(lr_occurrences(puzzle, name))

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    # Creates a puzzle that goes top to bottom by rotating the puzzle 90°
    top_to_bottom = rotate_puzzle(puzzle)
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences(top_to_bottom, name))

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.

    # Creates a puzzle that goes right to left, by rotating another 90°
    # (180° in total rotation)
    right_to_left = rotate_puzzle(top_to_bottom)
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(right_to_left, name))

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.

    # Creates a puzzle that goes bottom to top by rotating another 90°
    # (270° in total rotation)
    bottom_to_top = rotate_puzzle(right_to_left)
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(bottom_to_top, name))

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print(total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, 'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE2, 'anya'))
