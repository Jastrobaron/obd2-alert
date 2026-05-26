# OBD2 Alerter
Author: Jakub "Jastrobaron" Hresko

## Overview
This is a simple script that will alert you if you drive too fast. It does so by monitoring your engine RPM through the OBD2 port.

## Requirements
- OBD2 diagnostic tool (e.g. ELM327)
- Laptop
    - Bluetooth/WiFi/USB/whatever connectivity to communicate with the OBD2 diagnostic tool
    - Python3.9 installed
- Running instance of [my Discord bot](https://github.com/Jastrobaron/AlfaX-Bot) that you have at least one server in common with, can be running locally on your machine
- Sense of humor (optional, but strongly recommended)

## Connection setup
This section contains some advice on how to connect your laptop to the OBD2 diagnostsics tool. Wireless connections face a lot of issues (especially if you're running Linux).

### USB
This is pretty straight-forward - just connect the diagnostics tool to the laptop and a serial port should appear. You can then proceed straight to the usage.

### Bluetooth
TBD

### WiFi
TBD

## Usage
Assuming a stable connection to the OBD2 diagnostics and a running instance of [the bot](https://github.com/Jastrobaron/AlfaX-Bot), the steps to use this script are the following:

**1. Clone the repository:**
```bash
git clone git@github.com:Jastrobaron/obd2-alert.git
cd obd2-alert/
```

**2. Set up a Python virtual environment inside the repository (optional but recommended):**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**3. Adjust the environment variables** - this is where you enter the config values
```bash
cp .env.example .env
nano .env
```

The config values have the following semantics:

- `API_KEY` - the API key required for authentication against the bot API
- `USER_ID` - ID of your user account (accessible through developer settings)
- `MESSAGE` - text of the message you want to send
- `URL` - URL of the bot API
```

## Issues
If you encounter any issues, feel free to open a GitHub issue or a pull request.

## License
Published under MIT license.
