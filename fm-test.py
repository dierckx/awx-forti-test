import os
import sys

# Ansible provides connection variables as environment variables starting with ANSIBLE_
# when running against a host in the inventory.

HOST = os.environ.get('ANSIBLE_HOST')
USER = os.environ.get('ANSIBLE_USER')
PASSWORD = os.environ.get('ANSIBLE_PASS') # Or ANSIBLE_SSH_PASS
ADOM = os.environ.get('ADOM_NAME', 'global') # Use an extra var for ADOM

if not all([HOST, USER, PASSWORD]):
    print("Error: Required environment variables not set by AWX.")
    sys.exit(1)

print(f"Connecting to FortiManager at: {HOST}")
print(f"Using Username: {USER}")
print(f"Target ADOM: {ADOM}")
# In a real script, you would now use a library (like requests or fortimanager-api)
# to authenticate and perform your tasks using the variables above.

print("Script finished successfully.")
