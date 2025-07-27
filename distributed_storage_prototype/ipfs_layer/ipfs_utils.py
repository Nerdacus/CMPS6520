import subprocess

def ipfs_add(file_path):
    """
    Adds a file to IPFS using its file path.
    Returns the CID (Content Identifier) to be sent to the client.
    """
    try:
        result = subprocess.run(
            ["ipfs", "add", file_path],
            capture_output=True,
            text=False  # Returns raw bytes to prevent unicode error, idk why it works but it does
        )

        output = result.stdout.decode(errors="replace").strip()
        lines = output.splitlines()

        
        for line in reversed(lines):
            parts = line.split()
            if len(parts) >= 2 and parts[0] == "added":
                return parts[1]  # CID

        raise ValueError(f"[IPFS] Unexpected output format:\n{output}")
    except Exception as e:
        print(f"[IPFS] Error during ipfs_add: {e}")
        raise


def ipfs_cat(cid):
    """
    Retrieves a file from IPFS using its CID (key).
    Returns the raw content as bytes.
    """
    try:
        result = subprocess.run(
            ["ipfs", "cat", cid],
            capture_output=True,
            check=True,
            text=False
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode(errors="ignore") if e.stderr else "Unknown error"
        print(f"[IPFS] Error during ipfs_cat: {error_msg}")
        return None
    