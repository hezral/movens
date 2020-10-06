import os, sys, subprocess, json
key_value = subprocess.check_output(["systemctl", "show", sys.argv[1]], universal_newlines=True).split('\n')
json_dict = {}
for entry in key_value:
    kv = entry.split("=", 1)
    if len(kv) == 2:
        json_dict[kv[0]] = kv[1]
json.dump(json_dict, sys.stdout)