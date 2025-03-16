Feature: Onboard Command

    Scenario: Running onboard with all tasks
        Given I have a CLI application
        When I run the onboard command with all tasks
        Then the CLI should configure Git with username, email, default branch name, and commit template

    Scenario: Running onboard with a single task
        Given I have a CLI application
        When I run the onboard command with the task "git"
        Then the CLI should configure Git with username, email, default branch name, and commit template

    Scenario: Running onboard with a single dev tool
        Given I have a CLI application
        When I run the onboard command to configure "git"
        Then the CLI should configure Git with username, email, default branch name, and commit template

    Scenario: Running onboard with dry-run flag
        Given I have a CLI application
        When I run the onboard command with dry-run flag for "checklist"
        Then the CLI should print checklist contents to stdout without creating any files
