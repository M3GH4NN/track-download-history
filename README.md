# Download History Tracker

## Project Overview

This application tracks download history for contributors to ensure accurate compensation. It processes commands from an input source to manage contributors, their resources, and the corresponding downloads. The system calculates and reports statistics including average downloads per day.

## Technical Approach

### Data Handling

The application processes input via standard input (stdin), which allows flexibility in data provision, such as piping data directly from a file or another command.

#### Input Processing

The input is expected to consist of lines with commands that either register a new contributor, add a resource under a contributor, or log a download event. Each command type has specific requirements for arguments, and the input parser checks these before processing:

- **Contributor Command**: Registers a new contributor by name.
- **Resource Command**: Adds a resource with a unique ID and a rating to a specific contributor.
- **Download Command**: Logs a download event with a resource ID and a date.

#### Data Modeling

- **Contributor Model**: Holds the name of the contributor and a dictionary of resources.
- **Resource Model**: Stores resource IDs, ratings, and a list of download dates.

### Calculation Logic

#### Download Tracking

Each download event is associated with a resource, ensuring that downloads are tracked per resource per contributor. The system checks for the existence of the resource before logging a download.

#### Statistics Calculation

The system calculates the total number of downloads for each contributor and the average number of downloads per day:

- **Total Downloads**: Summed up for each contributor based on their resources.
- **Average Downloads per Day**: Calculated by dividing the total downloads by the number of days in the year, considering leap years.

### Error Handling

Robust error handling is implemented to ensure the application behaves predictably under various edge cases:

- **Custom Exceptions**: `ProcessError` is used to manage errors related to processing commands, allowing for specific error messages and handling strategies.
- **Validation Techniques**: Input validation checks ensure that all commands and their parameters meet expected formats, raising informative errors when they do not.

## Architecture

The application's architecture is modular, with distinct components handling different aspects of functionality:

- **Input Parser**: Reads and verifies commands from stdin.
- **Data Managers**: Models that manage contributors and resources.
- **Statistic Calculator**: Computes necessary metrics and generates output.

## Setup and Running Instructions

### Local Setup

Clone the repository and navigate to the project directory:

```bash
git clone URL_TO_REPO
cd DIRECTORY_NAME
pip install -r requirements.txt
python main.py < input.txt
```

### Docker Integration

To containerize this application using Docker:

```bash
docker build -t download-tracker .
docker run -i download-tracker
```

## Testing

The application includes a suite of unit tests to ensure functionality. Run tests using pytest

```bash

pytest tests/
```

## Conclusion and Future Work

The project successfully automates the tracking of download data and statistical analysis for contributors. Future enhancements could include support for a more interactive dashboard for viewing statistics, and extended error management capabilities.

## Future Commits

### Setting Up Pre-Commit Hooks

To install the pre-commit hooks into your git hooks, run:

```bash
pre-commit install
```

This step ensures that pre-commit runs on every commit to check your changes. To manually run pre-commit on all files, you can use:

```bash
pre-commit run --a
```

This command is useful for ensuring that all files meet the required standards before making a commit, even if they are not part of the staged files in git. To run pre-commit on only staged files in git, run:

```bash
pre-commit run
```
