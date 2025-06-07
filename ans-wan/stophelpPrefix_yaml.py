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

MASTER_FILE = "stophelpPrefixlist.yaml"

OUTPUT_YAML = "stophelp_routes_in.yml"

def build_entries(prefix_list, action="permit"):
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
    in_entries = build_entries(from_list)

    # --------------- build “to” entries ----------------
    to_list = data.get("toStophelp", [])
    if not to_list:
    to_entries = build_entries(to_list)
  
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
