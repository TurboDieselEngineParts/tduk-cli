from pytest_bdd import scenario, given, when, then
import subprocess
import pytest

@pytest.fixture
def context():
    return {}

@scenario("onboard.feature", "Running onboard with all tasks")
def test_onboard_all_tasks(context):
    pass

@scenario("onboard.feature", "Running onboard with a single task")
def test_onboard_single_task(context):
    pass

@scenario("onboard.feature", "Running onboard with a single dev tool")
def test_onboard_single_dev_tool(context):
    pass

@scenario("onboard.feature", "Running onboard with dry-run flag")
def test_onboard_dry_run(context):
    pass

@given("I have a CLI application")
def i_have_a_cli_application(context):
    context["cli_initialized"] = True

@when("I run the onboard command with all tasks")
def i_run_the_onboard_command_with_all_tasks(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "onboard", "--all"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")

@when('I run the onboard command with the task "git"')
def i_run_the_onboard_command_with_task_git(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "onboard", "--task", "git"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")

@when('I run the onboard command to configure "git"')
def i_run_the_onboard_command_to_configure_git(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "onboard", "--configure", "git"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")

@when('I run the onboard command with dry-run flag for "checklist"')
def i_run_the_onboard_command_with_dry_run_flag(context):
    result = subprocess.run(
        ["poetry", "run", "tduk-cli", "onboard", "--dry-run", "--task", "checklist"],
        capture_output=True,
        text=True,
        check=True,
    )
    context["output"] = result.stdout.strip()
    print(f"CLI Output: '{context['output']}'")

@then('the CLI should run the onboarding task "git"')
def cli_should_run_onboarding_task(context):
    expected_output = (
        "Configuring Git...\n"
        "Username: <username>\n"
        "Email: <email>\n"
        "Default Branch: main\n"
        "Commit Template: <template>"
    )
    assert expected_output in context["output"]


@then("the CLI should configure Git with username, email, default branch name, and commit template")
def cli_should_configure_git(context):
    expected_output = (
        "Configuring Git...\n"
        "Username: <username>\n"
        "Email: <email>\n"
        "Default Branch: main\n"
        "Commit Template: <template>"
    )
    assert expected_output in context["output"]


@then('the CLI should configure the dev tool "git"')
def cli_should_configure_dev_tool(context):
    expected_output = (
        "Configuring Git...\n"
        "Username: <username>\n"
        "Email: <email>\n"
        "Default Branch: main\n"
        "Commit Template: <template>"
    )
    assert expected_output in context["output"]


@then("the CLI should print checklist contents to stdout without creating any files")
def cli_should_print_checklist_contents(context):
    expected_output = (
        "Dry run mode enabled. No changes will be made.\n"
        "Checklist:\n"
        "- Task 1\n"
        "- Task 2\n"
        "- Task 3"
    )
    assert expected_output.rstrip() in context["output"].rstrip()


