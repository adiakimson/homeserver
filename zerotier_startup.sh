#!/bin/bash

# Initialize ZeroTier
echo "Initializing ZeroTier..."
zerotier-cli start

# Join the network using your Network ID (replace XXXXXXXXX with your Network ID)
echo "Joining ZeroTier network..."
zerotier-cli join XXXXXXXXX

# Wait for ZeroTier to establish connection
echo "Waiting for ZeroTier to connect..."
sleep 10

# Check the ZeroTier IP address and assign a specific IP if necessary
ZT_IP=$(zerotier-cli listnetworks | grep -E '^172\.25\.0\.' | awk '{print $3}')
if [ -z "$ZT_IP" ]; then
    echo "ZeroTier IP not found. Assigning 172.25.0.X IP..."
    zerotier-cli assign 172.25.0.100
else
    echo "ZeroTier IP already assigned: $ZT_IP"
fi

echo "ZeroTier setup complete."

