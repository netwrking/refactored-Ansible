#!/usr/bin/env python3
"""
stophelpPrefix_yaml.py

Reads stophelpPrefixlist.yaml (which now has two keys: fromStophelp and toStophelp),
assigns sequence numbers (5, 10, 15, ...) to each prefix in each list,
and writes out stophelp_routes_in.yml with two top‐level keys:
  - stophelp_routes_in: [ {action, prefix, sequence}, … ]
  - stophelp_routes_to: [ {action, prefix, sequence}, … ]
"""

import yaml

# 1) Path to your “stophelpPrefixlist.yaml” (the master file).
MASTER_FILE = "stophelpPrefixlist.yaml"

# 2) Path to the Ansible‐vars file we will (re)generate.
OUTPUT_YAML = "stophelp_routes_in.yml"

def build_entries(prefix_list, action="permit"):
    """
    Given a Python list of prefix‐strings (e.g. ["1.1.1.0/24", "1.2.2.0/24", …]),
    return a list of dicts:
      [ { "action": action, "prefix": "1.1.1.0/24", "sequence": 5 },
        { "action": action, "prefix": "1.2.2.0/24", "sequence": 10 }, … ]
    """
    entries = []
    seq = 0
    for net in prefix_list:
        seq += 5
        entries.append({
            "action": action,
            "prefix": net,
            "sequence": seq
        })
    return entries

def main():
    # Load the YAML from MASTER_FILE
    with open(MASTER_FILE, "r") as f:
        data = yaml.safe_load(f)

    # --------------- build “in” entries ----------------
    from_list = data.get("fromStophelp", [])
    if not from_list:
        print(f"Warning: '{MASTER_FILE}' has no key 'fromStophelp' or it's empty.")
        # We continue anyway, generating an empty list for “in.”
    in_entries = build_entries(from_list)

    # --------------- build “to” entries ----------------
    to_list = data.get("toStophelp", [])
    if not to_list:
        print(f"Warning: '{MASTER_FILE}' has no key 'toStophelp' or it's empty.")
        # We continue anyway, generating an empty list for “to.”
    to_entries = build_entries(to_list)

    # --------------- wrap under two top‐level keys ---------------
    # So Ansible can load BOTH variables from the same file.
    out_data = {
        "stophelp_routes_in": in_entries,
        "stophelp_routes_to": to_entries
    }

    # Write out the YAML that Ansible will consume.
    with open(OUTPUT_YAML, "w") as out:
        out.write("---\n")
        yaml.dump(out_data, out, default_flow_style=False)

    print(f"Wrote {len(in_entries)} entries to key 'stophelp_routes_in'")
    print(f"Wrote {len(to_entries)} entries to key 'stophelp_routes_to'")
    print(f"Output saved in {OUTPUT_YAML}")

if __name__ == "__main__":
    main()
