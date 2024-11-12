import simple_structured_markup as ssm

data = {
    "title": "My Application",
    "version": 1,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

# Writing to an SSM file
with open("output_of_writessmfile.ssm", "w") as file:
    ssm.dump(data, file)