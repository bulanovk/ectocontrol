"""Constants for Ectocontrol."""
# Base component constants
NAME = "Ectocontrol"
DOMAIN = "ectocontrol"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.0.0"

ATTRIBUTION = "Data provided by https://my.ectostroy.ru/"
ISSUE_URL = "https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]

# Defaults
DEFAULT_NAME = DOMAIN

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

CONF_PUBLIC_TOKEN = "public_token"
