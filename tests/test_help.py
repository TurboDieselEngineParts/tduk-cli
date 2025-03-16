from pytest_bdd import scenario, given, when, then
import subprocess
import pytest


@pytest.fixture
def context():
    return {}


@scenario("help.feature", "Running CLI with no arguments or help command")
def test_cli_with_no_arguments(context):
    pass


@scenario("help.feature", "Running CLI with help command")
def test_cli_with_help_command(context):
    pass


@scenario("help.feature", "Running help command with a specific command")
def test_cli_with_help_and_command(context):
    pass


@given("I have a CLI application")
def i_have_a_cli_application(context):
    context["cli_initialized"] = True


@when("I run the CLI with no arguments")
def i_run_the_cli_with_no_arguments(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")


@when("I run the CLI with the help command")
def i_run_the_cli_with_help_command(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")


@when("I run the help command with the onboard command")
def i_run_the_help_command_with_onboard(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "onboard", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")


@then("the CLI should display all available commands")
def cli_should_display_all_commands(context):
    expected_output = "onboard" in context["output"]
    assert expected_output


@then("the CLI should display usage information for the onboard command")
def cli_should_display_onboard_usage(context):
    expected_output = (
        "This command automates various onboarding tasks" in context["output"]
    )
    assert expected_output
