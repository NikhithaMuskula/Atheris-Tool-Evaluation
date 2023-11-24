import atheris

import sys


def perform_operation(operation, operand1, operand2):
    try:
        if operation == 'add':
            result = operand1 + operand2
        elif operation == 'subtract':
            result = operand1 - operand2
        elif operation == 'multiply':
            result = operand1 * operand2
        elif operation == 'divide':
            result = operand1 / operand2
        else:
            result = None
            raise ValueError("Invalid operation")

        return result
    except ZeroDivisionError:
        raise RuntimeError("Error input found!")
        # pass
    except Exception as e:
        print("Exception" + e)


# Fuzzing function
@atheris.instrument_func
def fuzz(data):
    try:
        # Parse the input data for the perform_operation function
        print(data)
        operation = data.get('operation', '')
        operand1 = data.get('operand1', 0)
        operand2 = data.get('operand2', 0)

        # Call the perform_operation function
        result = perform_operation(operation, operand1, operand2)

        # Process the result or handle errors accordingly
        if result is not None:
            pass
    except Exception as e:
        pass


# Run the fuzzer
atheris.Setup(sys.argv, fuzz)
atheris.Fuzz()
