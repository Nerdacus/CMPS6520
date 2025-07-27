import json
import os

def save_encrypted_key(cid, encrypted_key):
    keys = {}
    if os.path.exists("encrypted_keys.json"):
        with open("encrypted_keys.json", "r") as f:
            keys = json.load(f)

    keys[cid] = encrypted_key.hex()

    with open("encrypted_keys.json", "w") as f:
        json.dump(keys, f)

def load_encrypted_key(cid):
    if not os.path.exists("encrypted_keys.json"):
        raise FileNotFoundError("encrypted_keys.json not found")
    with open("encrypted_keys.json", "r") as f:
        keys = json.load(f)

    if cid not in keys:
        raise KeyError(f"No encrypted key found for CID: {cid}")

    return bytes.fromhex(keys[cid])

def load_key(filename):
    """
    Load AES Key for a given CID or filename, returned as raw bytes from IPFS.
    """
    import json
    import os

    KEY_FILE = "keys.json"

    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError(f"{KEY_FILE} not found")

    with open(KEY_FILE, "r") as f:
        keys = json.load(f)

    if filename not in keys:
        raise KeyError(f"No key found for: {filename}")

    return bytes.fromhex(keys[filename])
