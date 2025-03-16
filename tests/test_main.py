from pytest_bdd import scenario, given, when, then
import subprocess
import pytest

# Define a fixture to hold shared state
@pytest.fixture
def context():
    return {}


@scenario("hello.feature", "Running the hello command with a name")
def test_hello_with_name(context):
    pass


@scenario("hello.feature", "Running the hello command with default")
def test_hello_without_name(context):
    pass


@given("I have a CLI application")
def i_have_a_cli_application(context):
    context["cli_initialized"] = True


@when("I run the hello command with the name Behave")
def i_run_the_hello_command_with_name(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "--name", "Behave"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Command: poetry run tduk-cli --name Behave")
    print(f"CLI Output: '{context['output']}'")


@when("I run the hello command with no name")
def i_run_the_hello_command_with_no_name(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")


@then('the output should contain "Hello Behave"')
def the_output_should_contain_hello_behave(context):
    expected_output = "Hello Behave"
    print(f"Expected Output: '{expected_output}'")
    print(f"Actual Output: '{context['output']}'")
    assert expected_output in context["output"]


@then('the output should contain "Hello World"')
def the_output_should_contain_hello_world(context):
    expected_output = "Hello World"
    print(f"Expected Output: '{expected_output}'")
    print(f"Actual Output: '{context['output']}'")
    assert expected_output in context["output"]
