#!/usr/bin/env python3
"""
stophelpPrefix_yaml.py

Reads stophelpPrefixlist.yaml (a YAML list under 'fromStophelp'), 
assigns sequence numbers (3, 6, 9, ...),
and writes out stophelp_routes_in.yml for Ansible.
"""

import yaml

# 1) Path to your new “stophelpPrefixlist.yaml”
MASTER_FILE = "stophelpPrefixlist.yaml"

# 2) Path to the Ansible‐vars file we will (re)generate
OUTPUT_YAML = "stophelp_routes_in.yml"

def main():
    # Load the YAML
    with open(MASTER_FILE, "r") as f:
        data = yaml.safe_load(f)

    # Extract the list under “fromStophelp”
    subnets = data.get("fromStophelp", [])
    if not subnets:
        print(f"Warning: '{MASTER_FILE}' has no key 'fromStophelp' or it's empty.")
        return

    # Build entries with sequence increments of 5
    entries = []
    seq = 0
    for net in subnets:
        seq += 3
        entries.append({
            "action": "permit",     # change to "deny" if needed
            "prefix": net,
            "sequence": seq
        })

    # Wrap it under a single key so Ansible can do vars_files
    out_data = { "stophelp_routes_in": entries }

    with open(OUTPUT_YAML, "w") as out:
        out.write("---\n")
        yaml.dump(out_data, out, default_flow_style=False)

    print(f"Wrote {len(entries)} entries to {OUTPUT_YAML}")

if __name__ == "__main__":
    main()
