# Filename: config.py

# This configuration file contains essential settings for the CyberProtector project.
# It includes database configurations, security settings, and other system-wide preferences.

# Database configurations: Defines the connection parameters to the SQLite database.
# 'path' specifies the location of the SQLite database file relative to the project root.
DATABASE_CONFIG = {
    'path': 'path/to/cyberprotector.db',
}

# Security configurations: Contains settings related to the security aspects of the application.
# 'encryption_key' is a placeholder for an actual encryption key that should be securely generated and stored.
# 'max_login_attempts' defines the maximum number of unsuccessful login attempts allowed before locking out the user.
SECURITY_CONFIG = {
    'encryption_key': 'your_encryption_key_here',
    'max_login_attempts': 5,
}

# System configurations: General settings that affect the behavior of the system.
# 'log_file_path' points to the location of the system log file.
# 'scan_interval' determines how frequently (in hours) the system should perform routine checks or scans.
SYSTEM_CONFIG = {
    'log_file_path': 'path/to/cyberprotector.log',
    'scan_interval': 24,  # Hours
}

# Additional configurations and settings can be added here as the project evolves.
# For example, email server settings for sending alerts or API keys for integrating external services.
