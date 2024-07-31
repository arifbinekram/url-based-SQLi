
# URL-based SQL Injection Tester

This repository contains a Python script designed to test for SQL injection vulnerabilities in web applications by sending payloads via URL parameters and analyzing the response for database-specific error messages.

## Description

The script sends an initial payload to the specified URL and checks the response for common SQL error messages. Based on the error message detected, it identifies the type of database system (MySQL, MSSQL, PostGRES, Oracle) that may be vulnerable to SQL injection.

## Features

- Tests for SQL injection vulnerabilities by sending payloads in URL parameters.
- Detects the type of database system based on error messages in the response.
- Supports identification of MySQL, MSSQL, PostGRES, and Oracle databases.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/arifbinekram/url-based-SQLi.git
    cd url-based-SQLi
    ```

2. Install the required library:

    ```bash
    pip install requests
    ```

## Usage

Run the script and provide the target URL as input:

```bash
python sql_injection_tester.py
```

When prompted, enter the target URL. For example:

```sh
Enter the URL :
```

### Example

```sh
python sql_injection_ttester.py
```

Output:

```sh
Enter the URL :
Testing http://127.0.0.1/SQL/sqli-labs-master/Less-1/index.php?id=
Injectable MySQL detected
```

## Script Explanation

```python
import requests

# Take the URL as input
url = input("Enter the URL (e.g., http://127.0.0.1/SQL/sqli-labs-master/Less-1/index.php?id=): ")

# Initial payload to test for SQL injection
initial = "'"

print("Testing " + url)
first = requests.post(url + initial)

# Check for different SQL error messages in the response
if "mysql" in first.text.lower():
    print("Injectable MySQL detected")
elif "native client" in first.text.lower():
    print("Injectable MSSQL detected")
elif "syntax error" in first.text.lower():
    print("Injectable PostGRES detected")
elif "ORA" in first.text.lower():
    print("Injectable Oracle detected")
else:
    print("Not Injectable :)")
```

### Details

- **Imports**: Imports the necessary `requests` library for HTTP requests.
- **Argument Check**: Prompts the user to enter the target URL.
- **Fetch URL**: Retrieves the HTML content of the target URL with an initial payload.
- **Check SQL Errors**: Analyzes the response for SQL error messages to determine the database type.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Feel free to customize this README further based on your specific requirements or preferences.
