#!/usr/bin/env python3
import os
import subprocess
import urllib.request
from envvars import setEnvironmentVariables


REQUIRED_ENV_VARS = (
    'AZ_GROUP',
    'AZ_LOCATION',
    'POSTGRES_SERVER_NAME',
    'POSTGRES_ADMIN_USER',
    'POSTGRES_ADMIN_PASSWORD',
    'APP_DB_NAME',
)

setEnvironmentVariables()

missing = []
for v in REQUIRED_ENV_VARS:
    if v not in os.environ:
        missing.append(v)
if missing:
    print("Required Environment Variables Unset:")
    print("\t" + "\n\t".join(missing))
    print("Exiting.")
    exit()

# Ref: https://docs.microsoft.com/en-gb/cli/azure/postgres/server?view=azure-cli-latest#az-postgres-server-create
# SKUs: https://docs.microsoft.com/en-us/azure/postgresql/concepts-pricing-tiers
#       {pricing tier}_{compute generation}_{vCores}
create_server_command = [
    'az', 'postgres', 'server', 'create',
    '--resource-group', os.getenv('AZ_GROUP'),
    '--location', os.getenv('AZ_LOCATION'),
    '--name', os.getenv('POSTGRES_SERVER_NAME'),
    '--admin-user', os.getenv('POSTGRES_ADMIN_USER'),
    '--admin-password', os.getenv('POSTGRES_ADMIN_PASSWORD'),
    '--sku-name', 'B_Gen5_1',
]

print("This script will take about 3 minutes to run.")
print("Creating PostgreSQL server...")
subprocess.check_call(create_server_command, shell=True)


# Set up firewall.
# Ref: https://docs.microsoft.com/en-gb/cli/azure/postgres/server/firewall-rule?view=azure-cli-latest#az-postgres-server-firewall-rule-create
azure_firewall_command = [
    'az', 'postgres', 'server', 'firewall-rule', 'create',
    '--resource-group', os.getenv('AZ_GROUP'),
    '--server-name', os.getenv('POSTGRES_SERVER_NAME'),
    '--start-ip-address', '0.0.0.0',
    '--end-ip-address', '0.0.0.0',
    '--name', 'AllowAllAzureIPs',
]

with urllib.request.urlopen('http://ip.42.pl/raw') as f:
    my_ip = f.read().decode("utf-8")

local_ip_firewall_command = [
    'az', 'postgres', 'server', 'firewall-rule', 'create',
    '--resource-group', os.getenv('AZ_GROUP'),
    '--server-name', os.getenv('POSTGRES_SERVER_NAME'),
    '--start-ip-address', my_ip,
    '--end-ip-address', my_ip,
    '--name', 'AllowMyIP',
]

print("Allowing access from Azure...")
subprocess.check_call(azure_firewall_command, shell=True)
print("Allowing access from local IP...")
subprocess.check_call(local_ip_firewall_command, shell=True)


create_db_command = [
    'az', 'postgres', 'db', 'create',
    '--resource-group', os.getenv('AZ_GROUP'),
    '--server-name', os.getenv('POSTGRES_SERVER_NAME'),
    '--name', os.getenv('APP_DB_NAME'),
]

print("Creating App DB...")
subprocess.check_call(create_db_command, shell=True)


connect_details_command = [
    'az', 'postgres', 'server', 'show',
    '--resource-group', os.getenv('AZ_GROUP'),
    '--name', os.getenv('POSTGRES_SERVER_NAME'),
]
print("Getting access details...")
subprocess.check_call(connect_details_command, shell=True)

# Connect to Azure using connection string format (to force SSL)
# psql "host=$POSTGRES_HOST sslmode=require port=5432 user=$POSTGRES_ADMIN_USER@$POSTGRES_SERVER_NAME dbname=postgres" -W