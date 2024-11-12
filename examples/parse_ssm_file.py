import simple_structured_markup as ssm

# Reading from an SSM file
with open("config.ssm", "r") as file:
    config = ssm.load(file)
    print(config)
