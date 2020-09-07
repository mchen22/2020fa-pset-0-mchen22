#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int
    :param int some_int: the number
    :rtype: int
    """
    try:
        return some_int % 100000000
    except Exception as exc:
        raise NotImplementedError(str(exc))


def optimized_fibonacci(f):
    """Return the fth Fibonacci number of an int
    :param int f: the number
    :rtype: int
    """
    try:
        if f < 2:
            return f
        else:
            # Assign initial value of the sequence to be (0, 1)
            a, b = 0, 1

            # Replace the second value with the sum of previous two
            # to get the i-th number of a Fibonacci sequence
            for i in range(1, f):
                a, b = b, a + b
            return b
    except Exception as exc:
        raise NotImplementedError(str(exc))


class SummableSequence(object):
    def __init__(self, *initial):
        """Initialize the SummableSequence with an instant variable
            to be initial_sq in list
        :param tuple *initial: a sequence of numbers
        :rtype: list
        """
        try:
            self.initial_sq = list(initial)
        except Exception as exc:
            raise NotImplementedError(str(exc))

    def __call__(self, i):
        """Return the ith number in a generalized Fibonacci sequence
            that returns a sum of previous n values given an initial
            sequence of numbers to start
        :param int i: the number
        :rtype: int
        """
        try:
            # Set a start list equal to initial input of the sequence of numbers
            start_lst = self.initial_sq.copy()

            # Get number of elements in the input of the sequence of numbers
            num_of_val = len(start_lst)

            # Return initial input values when n is less than the number of
            # elements in the input of the sequence of numbers
            if i < len(start_lst):
                return start_lst[i]

            temp = 0

            # Create a variable list, temp_list, with (number of inputs - 1) value of 0s
            temp_list = [0] * (num_of_val - 1)

            # Create a loop that generates i-th in a sequence that sums previous
            # n value in case of i >= number of inputs
            for i in range(num_of_val, i + 1):
                temp = sum(start_lst)

                # Store the reverse order of sequence of value from start_list,
                # excluding the first value, into the temp_list
                for j in range(num_of_val - 1):
                    temp_list[j] = start_lst[num_of_val - 1 - j]

                # Recreate the start_list with the sequence of number in temp_list
                # in reverse order
                for k in range(num_of_val - 1):
                    start_lst[k] = temp_list[num_of_val - 2 - k]
                # Make the last value in the start_list equal
                # to temp variable, which is the sum of previous start_list

                start_lst[num_of_val - 1] = temp

            return temp
        except Exception as exc:
            raise NotImplementedError(str(exc))


if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))
    new_seq = SummableSequence(0, 1)
    for n in range(0, 50, 5):
        print(new_seq(n))
    # print("new_seq(100000)[-8:]:", last_8(new_seq(10000)))
