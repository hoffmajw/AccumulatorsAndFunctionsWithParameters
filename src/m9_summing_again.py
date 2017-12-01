"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jaxon Hoffman.
"""  # Done 1
#change for commit

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # Done 2
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    expected = 9
    actual = sum_powers(2, 3)
    expected2 = 36
    actual2 = sum_powers(3, 3)
    expected3 = 30
    actual3 = sum_powers(4, 2)
    print('Test 1 expected: ', expected)
    print('       actual: ', actual)
    print('Test 2 expected: ', expected2)
    print('       actual: ', actual2)
    print('Test 3 expected: ', expected3)
    print('       actual: ', actual3)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    total = 0

    for k in range(n):
        total += (k + 1) ** p

    return total


    # ------------------------------------------------------------------
    # Done 3
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # Done 4
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    expected = 36
    actual = sum_powers_in_range(1, 3, 3)
    expected2 = 29
    actual2 = sum_powers_in_range(2, 4, 2)
    expected3 = 50
    actual3 = sum_powers_in_range(3, 5, 2)
    print('Test 1 expected: ', expected)
    print('       actual: ', actual)
    print('Test 2 expected: ', expected2)
    print('       actual: ', actual2)
    print('Test 3 expected: ', expected3)
    print('       actual: ', actual3)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """

    total = 0

    for k in range(m, n + 1):
        total = total + (k ** p)

    return total

    # ------------------------------------------------------------------
    # Done 5
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
