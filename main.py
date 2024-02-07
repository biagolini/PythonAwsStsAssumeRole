import boto3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve AWS role ARN, session name, and profile from environment variables
ROLE_ARN = os.getenv('ROLE_ARN')
SESSION_NAME = os.getenv('SESSION_NAME')
AWS_PROFILE = os.getenv('AWS_PROFILE')

# Create a session using the specified AWS profile
session = boto3.Session(profile_name=AWS_PROFILE)

# Initialize the STS client
sts_client = session.client('sts')

# Assume the specified role
assumed_role = sts_client.assume_role(
    RoleArn=ROLE_ARN,
    RoleSessionName=SESSION_NAME
)

# Extract credentials from the assumed role
credentials = assumed_role['Credentials']

# Write the credentials to a shell script for environment variable configuration
with open('setenv.sh', 'w') as f:
    f.write(f"export AWS_ACCESS_KEY_ID={credentials['AccessKeyId']}\n")
    f.write(f"export AWS_SECRET_ACCESS_KEY={credentials['SecretAccessKey']}\n")
    f.write(f"export AWS_SESSION_TOKEN={credentials['SessionToken']}\n")

# Print a message to inform the user about the generated script
print("Script 'setenv.sh' generated. Execute 'source setenv.sh' to configure the environment variables.")
