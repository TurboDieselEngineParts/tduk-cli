Feature: Help Command

    Scenario: Running CLI with no arguments or help command
        Given I have a CLI application
        When I run the CLI with no arguments
        Then the CLI should display all available commands

    Scenario: Running CLI with help command
        Given I have a CLI application
        When I run the CLI with the help command
        Then the CLI should display all available commands

    Scenario: Running help command with a specific command
        Given I have a CLI application
        When I run the help command with the onboard command
        Then the CLI should display usage information for the onboard command
