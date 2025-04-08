from pytest_bdd import scenario, given, when, then
import os
import pytest


@pytest.fixture
def context():
    return {}


@pytest.fixture
def directory_name():
    return "MyTestDirectory"  # Replace with the default or dynamic value you want


@pytest.fixture
def path():
    import os

    return os.getcwd()  # Default to current working directory


@scenario(
    "initialize.feature", "Create a new directory with a name provided by the user"
)
def test_create_directory_with_user_provided_name():
    pass


@scenario(
    "initialize.feature",
    "Create a new directory in the current working directory by default",
)
def test_create_directory_in_current_working_directory():
    pass


@scenario(
    "initialize.feature", "Initialize the project with standard files and structure"
)
def test_initialize_project_with_standard_files():
    pass


@given("I have a CLI application")
def cli_application(context):
    context["cli_initialized"] = True


@given("I have created a new directory '<directory_name>'")
def created_a_new_dir(context, directory_name):
    path = os.path.join(os.getcwd(), directory_name)
    if not os.path.exists(path):
        os.makedirs(path)  # Create the directory if it doesn't exist
    context["directory_initialized"] = True
    context["directory_path"] = path  # Store the path in context for later use


@when("I provide the directory name '<directory_name>'")
def provide_directory_name(context, directory_name):
    context["directory_name"] = directory_name


@when("I specify the path '<path>' where the directory should be created")
def specify_path(context, path):
    context["path"] = path


@when("I do not specify a path")
def do_not_specify_path(context):
    context["path"] = os.getcwd()  # Use current working directory as default


@when("I initialize the project")
def initialize_project(context):
    if "path" not in context:
        context["path"] = os.getcwd()  # Default to current directory if not set

    if "directory_name" not in context:
        # Extract directory name from directory_path if available
        if "directory_path" in context:
            context["directory_name"] = os.path.basename(context["directory_path"])
        else:
            context["directory_name"] = "MyTestDirectory"  # Default value

    directory_path = os.path.join(context["path"], context["directory_name"])

    # Create standard files
    with open(os.path.join(directory_path, "README.md"), "w") as f:
        f.write("# Project Title\n\nA brief description of your project.")
    with open(os.path.join(directory_path, ".gitignore"), "w") as f:
        f.write("# Ignore Python cache files\n__pycache__/\n*.pyc\n")
    with open(os.path.join(directory_path, "config.yml"), "w") as f:
        f.write("default_config: true\n")

    # Create BDD directories
    bdd_directories = ["features", "features/steps"]
    for bdd_dir in bdd_directories:
        bdd_path = os.path.join(directory_path, bdd_dir)
        if not os.path.exists(bdd_path):
            os.makedirs(bdd_path)

    context["directory_initialized"] = True


@then("the directory '<directory_name>' should be created at '<path>'")
def verify_directory_creation(context, directory_name, path):
    expected_path = os.path.join(path, directory_name)
    assert os.path.exists(expected_path), f"Directory {expected_path} was not created!"


@then(
    "the directory '<directory_name>' should be created in the current working directory"
)
def verify_directory_creation_in_cwd(context, directory_name):
    expected_path = os.path.join(os.getcwd(), directory_name)
    assert os.path.exists(expected_path), f"Directory {expected_path} was not created!"


@then(
    "standard files such as README.md, .gitignore, and config files should be added to '<directory_name>'"
)
def verify_standard_files(context, directory_name):
    expected_files = ["README.md", ".gitignore", "config.yml"]
    for file in expected_files:
        assert os.path.exists(
            os.path.join(directory_name, file)
        ), f"{file} was not found in {directory_name}!"


@then("standardized directories for BDD should be created in '<directory_name>'")
def verify_bdd_directories(context, directory_name):
    bdd_directories = ["features", "features/steps"]
    for bdd_dir in bdd_directories:
        expected_path = os.path.join(context["path"], directory_name, bdd_dir)
        assert os.path.exists(
            expected_path
        ), f"BDD directory {expected_path} was not created!"
