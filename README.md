# Python API Automation

![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-blue)
![Laravel](https://img.shields.io/badge/Laravel-13-red)
![CI](https://github.com/debbytai1017/qa_api_automation/actions/workflows/python-tests.yml/badge.svg)

An API automation testing project built with **Python**, **Pytest**, **Requests**, **Laravel API**, **GitHub Actions**, and **Allure Report**.

## Features

- API Automation with Python Requests
- Pytest-based Test Framework
- Laravel RESTful API Testing
- GitHub Actions CI
- Allure Test Report

## Test Coverage

- Product CRUD APIs
- Database Validation
- API Response Validation
- Status Code Validation

## How to Run

```bash
pip install -r requirements.txt
pytest
```

## Continuous Integration

This project uses **GitHub Actions** to:

- Execute API automated tests
- Generate Allure HTML Report
- Upload Allure Results as workflow artifacts
- Upload Laravel server log
- Upload Laravel error logs on failure

## Artifacts

The following artifacts are generated after each workflow run:

- Allure HTML Report
- Allure Results
- Laravel Server Log
- Laravel Error Log (Failure Only)

These artifacts are uploaded as GitHub Actions workflow artifacts.