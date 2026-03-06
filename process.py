import json
import re

with open("corpus.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for ex in data:
        if "clp" in ex["b"]:
            print("#", ex["b"])
        else:
            ex["b"] = ex["b"].replace("\\nmc{(2m)}", "").replace("\\nmc{(rol:madre)}", "")
            ex["b"] = re.sub(
            print(ex["b"])
