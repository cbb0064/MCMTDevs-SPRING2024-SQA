# Software Quality Assurance Project Report (COMP 5710/6710) 

## Project Description

The purpose of this project is to integrate SQA activities into a provided zip file (MLForensics.zip). These activities include adding Git Hooks, fuzzing, foresics, and continuous integration. A

## Git Hooks

The pre-commit git hook is a security measure designed to precheck any python files staged for commit that might have any security issues. The static analysis method used i nthis case was bandit, and the script was written to also handle cases in which there were both good and bad files staged simultaneously. The first photo shows the actual pre-commit script which can be found in the Tests directory and the second is the proof of function.

### Git Hooks 1
![image](/images/SQA_1.png?raw=true "SQA 1")

### Git Hooks 2
![image](/images/SQA_2.png?raw=true "SQA 2")

## Fuzzing

Fuzzing is a testing method where software is bombarded with diverse and often unexpected inputs to uncover bugs or vulnerabilities. Fuzz Image 1 shows how the program responds to various inputs, while Fuzz Image 2 displays the list of inputs used for testing. By examining how the program handles these inputs, developers can identify potential issues such as crashes or security flaws. Automated tools are often employed to streamline this process.

### Fuzz Image 1
![image](/images/FUZZ_1.png?raw=true "Fuzz 1")

### Fuzz Image 2
![image](/images/FUZZ_2.png?raw=true "Fuzz 2")

## Forensics

Logging is the process of recording events and messages during the execution of a program or system. It helps developers debug issues, monitor performance, and track user activities. The logs that I implemented are stored in a file called SIMPLE-LOGGER.log in the directory that the logging occurred.

Added Logging to 5 methods:

FAME-ML/main.py
- runFameML()
- getAllPythonFilesinRepo()
- getCSVData()

mining/git.repo.miner.py
- deleteRepo()
- deleteRepos()



## Continuous Integration

Adding continuous integration allows static analysis of code that developers upload. It runs on a code repository whenever specified, such as a set time schedule or on a pull request. This allows for easy debugging and formatting of code across different versions of the code, as seen in CI Image 1 below. When opening the static analysis, various errors and warnings can be seen, as seen in CI Image 2 below. Continuous integration provides easier transition upon versions of code so that work across multiple developers can be easily integrated with pre-existing code.

### CI Image 1
![image](/images/CI_1.JPG?raw=true "CI 1")

### CI Image 2
![image](/images/CI_2.JPG?raw=true "CI 2")
