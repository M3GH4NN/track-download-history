# Download History Tracker

## Project Overview

This application tracks download history for contributors to ensure accurate compensation. It processes commands from an input source to manage contributors, their resources, and the corresponding downloads. The system calculates and reports statistics including total downloads and average downloads per day.

## Technical Approach

- **Data Parsing**: Commands are parsed from standard input or a file to register contributors, add resources, and log downloads.
- **Data Management**: Uses classes to manage contributors and resources efficiently.
- **Statistics Calculation**: Computes total and average downloads for each contributor, sorting them by total downloads.
- **Error Handling**: Includes robust error handling to manage unexpected input and command errors.

## Technologies Used

- Python 3.8
- Docker for containerization

## Setup and Running Instructions

### Local Setup

Clone the repository and navigate to the project directory:
git clone URL
cd DIRECTORY

### Install Dependencies

pip install -r requirements.txt

This will install all the packages listed in `requirements.txt`.

### Setting Up Pre-Commit Hooks

To install the pre-commit hooks into your git hooks, run:
pre-commit install

This step ensures that pre-commit runs on every commit to check your changes. To manually run pre-commit on all files, you can use:
pre-commit run --all-files
This command is useful for ensuring that all files meet the required standards before making a commit, even if they are not part of the staged files in git.

### Usage without Docker

Run the application directly using Python:
python main.py < input.txt

### Using Docker

#### Building the Docker Image

docker build -t download-tracker .

#### Running the Docker Container

The application is set to receive input via stdin:
docker run -i download-tracker < input.txt

## Packaging for Submission

To package your application for submission:
tar zcvf your-code.tgz your-code-dir

or, if using git:
GIT_DIR=your-code-dir/.git git bundle create your-code.gitbundle --all

## Testing

The application includes a suite of unit tests to ensure functionality. Run tests using:
pytest

pip install pytest

pytest tests/
