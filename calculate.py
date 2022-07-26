import sys
import re

def calc(left_operand, right_operand, operation):
    try:
        match operation:
            case '+':
                return left_operand + right_operand
            case '-':
                return left_operand - right_operand
            case '*':
                return left_operand * right_operand
            case '/':
                return left_operand / right_operand
            case '%':
                return left_operand % right_operand
    except ZeroDivisionError:
        print('Division by zero is not allowed')
        return

def calculate():

    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print('Invalid arithmetic expression')
        return

    operators = ['+', '-', '*', '/', '%']

    match len(sys.argv):
        case 2:
            try:
                left_operand, right_operand = [int(i) for i in re.split('[\\+\\-\\*\\/\\%]', sys.argv[1])]
                operator = re.search(r'[\\+\\-\\*\\/\\%]', sys.argv[1]).group()

                if operator not in operators:
                    print('Unavailable arithmetic operation')
                    return

                return calc(left_operand, right_operand, operator)

            except ValueError:
                print('Both operands must be a number')
                return

        case 4:
            try:
                float(sys.argv[1])
            except ValueError:
                print('Left operand must be a number')
                return

            try:
                float(sys.argv[3])
            except ValueError:
                print('Right operand must be a number')
                return

            if sys.argv[2] not in operators:
                print('Unavailable arithmetic operation')
                return

            return calc(int(sys.argv[1]), int(sys.argv[3]), sys.argv[2])

if __name__ == '__main__':
    print(calculate())
