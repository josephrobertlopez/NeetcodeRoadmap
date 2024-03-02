# NeetcodeRoadmap Python Problem Solutions

This repository contains Python solutions to problems from NeetcodeRoadmap. It utilizes pipenv for managing dependencies.

## Installation

Make sure you have Python and pipenv installed on your system. Then, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/josephrobertlopez/NeetcodeRoadmap
   ```

2. Navigate to the project directory:
   ```bash
   cd NeetcodeRoadmap
   ```

3. Install dependencies using pipenv:
   ```bash
   pipenv install
   ```

## Usage

Once you have installed the dependencies, you can run the Python scripts for individual problems. Each problem is solved in a separate Python file with a descriptive name.

To execute a specific problem, you can use the following command:
```bash
pipenv run python <problem_file.py>
```

Replace `<problem_file.py>` with the filename of the problem you want to run.

### Running Test cases

To run specific test cases 
```bash
pipenv run pytest <test_file.py>::problem_name
```

Replace `<test_file.py>` with the filename of the test file for the problem you want to test.

