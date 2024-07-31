import requests

# Take the URL as input
url = input("Enter the URL : ")

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
