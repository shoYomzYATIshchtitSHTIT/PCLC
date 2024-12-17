from behave import given, when, then
import sys
import io
from main import main

# Mocking input and output for testing
def run_main_with_args(args):
    sys.argv = ['main.py'] + args
    captured_output = io.StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

@given('the coefficients a = {a}, b = {b}, c = {c}')
def step_given_coefficients(context, a, b, c):
    context.coefficients = [a, b, c]

@when('I solve the bi-quadratic equation')
def step_when_solve_equation(context):
    context.output = run_main_with_args(context.coefficients)

@then('the result should be "{expected_result}"')
def step_then_check_result(context, expected_result):
    assert context.output == expected_result, f"Expected '{expected_result}', but got '{context.output}'"

@then('the result should contain "{expected_result}"')
def step_then_check_result_contains(context, expected_result):
    assert expected_result in context.output, f"Expected '{expected_result}' to be in '{context.output}'"