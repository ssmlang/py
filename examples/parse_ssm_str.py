import simple_structured_markup as ssm

ssm_data = """
# General information
title = "My Application"
version = 1

# Database configuration
[database]
host = "localhost"
port = 5432
"""

data = ssm.loads(ssm_data)
print(data)