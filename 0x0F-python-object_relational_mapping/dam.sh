#!/bin/bash

# Stop MySQL service
sudo service mysql stop

# Start MySQL in safe mode
sudo mysqld_safe --skip-grant-tables &

# Wait a few seconds to ensure MySQL starts
sleep 5

# Configure root user to use auth_socket
mysql -u root <<EOF
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'auth_socket';
EXIT;
EOF

# Stop the safe mode instance
sudo killall mysqld_safe
sudo killall mysqld

# Start MySQL service
sudo service mysql start

echo "Configuration complete. You can now log in as root without a password."
