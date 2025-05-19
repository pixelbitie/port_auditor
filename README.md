# port_auditor
Python script that scans through all open TCP listening ports on a system, and determines them as authorised or unauthorised based on user-defined ports in a ``allowed_ports.txt`` file.

## Requirements:
Run the following to install dependencies
```bash
  pip install -r requirements.txt
```

## Usage
Execute the script through
```bash
  sudo python3 port_auditor.py
```
(root permissions is required for the script to work)

Ensure that ``allowed_ports.txt`` is put in the same directory as the running script and that it is configured as per the following syntax:
```
  8000 16000 23
```
