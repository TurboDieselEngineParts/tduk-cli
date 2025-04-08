Feature: Initialize a new software project repository

  Scenario: Create a new directory with a name provided by the user
    Given I have a CLI application
    When I provide the directory name '<directory_name>'
    And I specify the path '<path>' where the directory should be created
    Then the directory '<directory_name>' should be created at '<path>'

  Scenario: Create a new directory in the current working directory by default
    Given I have a CLI application
    When I provide the directory name '<directory_name>'
    And I do not specify a path
    Then the directory '<directory_name>' should be created in the current working directory

  Scenario: Initialize the project with standard files and structure
    Given I have created a new directory '<directory_name>'
    When I initialize the project
    Then standard files such as README.md, .gitignore, and config files should be added to '<directory_name>'
    And standardized directories for BDD should be created in '<directory_name>'
