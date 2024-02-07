# AWS Role Assumption Helper - Python

This README provides comprehensive instructions on setting up and executing a Python script designed to assume an AWS IAM role using temporary credentials. This utility is especially useful for developers and DevOps engineers who need to manage AWS resources securely and efficiently.

## Prerequisites

Before you begin, ensure you have the following installed and configured on your system:

- Python 3.x
- pip (Python package installer)
- AWS CLI, configured with at least one user profile

## Installation and Setup

Follow these steps to get the script up and running on your system:

### Step 1: Install Dependencies

First, install the required Python libraries by executing:

```
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

Create a `.env` file in the root directory of the project and include the following variables:

```
ROLE_ARN=arn:aws:iam::123456789012:role/YourRoleName
SESSION_NAME=YourSessionName
AWS_PROFILE=YourCLIAccountProfile
```

Replace the placeholder values with those relevant to your AWS configuration.

### Step 3: Execute the Script

Run the script using the command:

```
python3 main.py
```

### Step 4: Set System Environment Variables

After the script execution, apply the generated environment variables to your session:

```
source setenv.sh
```

### Step 5: Verification

To verify the script's success, execute an AWS CLI command that requires authentication. For example:

```
aws s3 ls
```

This should list the S3 buckets available to the assumed role, confirming that the temporary credentials are correctly set.

## Additional Information

- Keep your `.env` file secure and do not share it publicly, as it contains sensitive information.
- For troubleshooting, ensure your AWS CLI profile has the necessary permissions to assume the specified IAM role.

## Contributing

Feel free to submit issues, create pull requests, or fork the repository to help improve the project.

## License and Disclaimer

This project is open-source and available under the MIT License. You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.
