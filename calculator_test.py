# calculator.py
import random

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    calculator = Calculator()
    print("Simple Calculator")
    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == '1':
                print("Result:", calculator.add(x, y))
            elif choice == '2':
                print("Result:", calculator.subtract(x, y))
            elif choice == '3':
                print("Result:", calculator.multiply(x, y))
            elif choice == '4':
                try:
                    print("Result:", calculator.divide(x, y))
                except ValueError as e:
                    print(e)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Tests
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    expected_result = x + y
    actual_result = calculator.add(x, y)
    if actual_result == expected_result:
        print(f"Add test passed: {x} + {y} = {actual_result}")
    else:
        print(f"Add test failed: {x} + {y} != {actual_result}. Expected {expected_result}")

def test_subtract(calculator):
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    expected_result = x - y
    actual_result = calculator.subtract(x, y)
    if actual_result == expected_result:
        print(f"Subtract test passed: {x} - {y} = {actual_result}")
    else:
        print(f"Subtract test failed: {x} - {y} != {actual_result}. Expected {expected_result}")

def test_multiply(calculator):
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    expected_result = x * y
    actual_result = calculator.multiply(x, y)
    if actual_result == expected_result:
        print(f"Multiply test passed: {x} * {y} = {actual_result}")
    else:
        print(f"Multiply test failed: {x} * {y} != {actual_result}. Expected {expected_result}")

def test_divide(calculator):
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    if y != 0:
        expected_result = x / y
        actual_result = calculator.divide(x, y)
        if actual_result == expected_result:
            print(f"Divide test passed: {x} / {y} = {actual_result}")
        else:
            print(f"Divide test failed: {x} / {y} != {actual_result}. Expected {expected_result}")
    else:
        try:
            calculator.divide(x, y)
            print(f"Divide test failed: Divide by zero error not raised")
        except ValueError:
            print(f"Divide test passed: Divide by zero error raised")

if __name__ == "__main__":
    main()
