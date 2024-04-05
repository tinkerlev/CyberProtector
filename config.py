import os
import json
import logging

class ConfigurationError(Exception):
    pass

def load_config(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"Configuration file not found at {file_path}. Using default configurations.")
        return {}

def merge_configs(default_config, external_config):
    for key, value in external_config.items():
        if key in default_config and isinstance(value, type(default_config[key])):
            default_config[key] = value
    return default_config

def validate_config(config):
    if not config.get('encryption_key'):
        raise ConfigurationError("Encryption key is not provided in the configuration.")

    if config.get('max_login_attempts') is None:
        raise ConfigurationError("Max login attempts is not provided in the configuration.")

def encrypt_password(password):
    # Implement password encryption logic here
    return password

DEFAULT_DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')
DEFAULT_DATABASE_CONFIG = get_database_config(DEFAULT_DATABASE_TYPE)

DEFAULT_SECURITY_CONFIG = {
    'encryption_key': os.getenv('ENCRYPTION_KEY', 'your_encryption_key_here'),
    'max_login_attempts': int(os.getenv('MAX_LOGIN_ATTEMPTS', 5)),
}

DEFAULT_SYSTEM_CONFIG = {
    'log_file_path': os.getenv('LOG_FILE_PATH', 'path/to/cyberprotector.log'),
    'scan_interval': int(os.getenv('SCAN_INTERVAL_HOURS', 24)),  # Hours
}

EXTERNAL_CONFIG_FILE_PATH = 'config.json'
external_config = load_config(EXTERNAL_CONFIG_FILE_PATH)

DATABASE_CONFIG = merge_configs(DEFAULT_DATABASE_CONFIG, external_config.get('DATABASE_CONFIG', {}))
SECURITY_CONFIG = merge_configs(DEFAULT_SECURITY_CONFIG, external_config.get('SECURITY_CONFIG', {}))
SYSTEM_CONFIG = merge_configs(DEFAULT_SYSTEM_CONFIG, external_config.get('SYSTEM_CONFIG', {}))

validate_config(SECURITY_CONFIG)

# Encrypting password if provided in configuration
if 'password' in DATABASE_CONFIG:
    DATABASE_CONFIG['password'] = encrypt_password(DATABASE_CONFIG['password'])

# Additional configurations and settings can be added here as the project evolves.
