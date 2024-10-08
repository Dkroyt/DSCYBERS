# DSCYBER Mass Reporter

This tool automates the process of reporting Instagram accounts for spam or scams using the Instagram Graph API. It randomly generates user IDs and sends multiple reports based on the number of reports entered by the user.

## Features
- **Automated reporting**: Send multiple reports with randomly generated user IDs.
- **Tkinter GUI**: Simple graphical interface to input the number of reports and initiate the process.
- **UUID and secrets-based credentials**: Generates random client IDs, client secrets, and access tokens for each session.

## Requirements
- Python 3.x
- `requests` library
- `uuid` library (comes pre-installed with Python)
- `secrets` library (comes pre-installed with Python)
- `tkinter` library (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dscyber-mass-reporter.git
    cd dscyber-mass-reporter
    ```

2. Install the required dependencies:
    ```bash
    pip install requests
    ```

3. Run the script:
    ```bash
    python mass_reporter.py
    ```

## How to Use

1. Enter the number of reports you want to send in the entry field.
2. Click on "Start Reporting" to initiate the report generation process.
3. A confirmation message will appear when the reporting process is complete.

### Example Usage

Once the tool starts, a GUI window will appear. Simply input the desired number of reports and click the "Start Reporting" button. The tool will automatically generate random user IDs and report them as spam or scam.

### Instagram API Integration

This script uses Instagram's Graph API for reporting users. It sends a POST request to the API endpoint to report a user, generating a unique `client_id`, `client_secret`, and `access_token` for each session. Ensure your Instagram API access is properly set up.

## Disclaimer

This project is intended for educational and ethical hacking purposes only. Misuse of this tool for malicious activities is strictly prohibited, and the creator takes no responsibility for illegal or unethical use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
