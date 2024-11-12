import simple_structured_markup as ssm

data = {
    "title": "My Application",
    "version": 1,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

ssm_string = ssm.dumps(data)
print(ssm_string)
