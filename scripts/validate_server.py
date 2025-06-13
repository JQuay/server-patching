import sys

env = sys.argv[1].strip()
server = sys.argv[2].strip()

valid = True

with open("data/servers.txt") as f:
    servers = [line.strip() for line in f.readlines()]
if server not in servers:
    print(f"::error ::Server {server} not found in servers list.")
    valid = False

with open("data/environments.txt") as f:
    envs = [line.strip() for line in f.readlines()]
if env not in envs:
    print(f"::error ::Environment {env} not found in environments list.")
    valid = False

if valid:
    print("::set-output name=valid::true")
else:
    print("::set-output name=valid::false")
    exit(1)
