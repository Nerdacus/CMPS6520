from flask import Flask, request, jsonify, Response
from access_proxy.encrypt import aes_encrypt, aes_decrypt
from ipfs_layer.ipfs_utils import ipfs_add, ipfs_cat
from key_manager.store import save_encrypted_key, load_encrypted_key
from audit.logger import log_event
import logging
import tempfile
import os

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()

    # File encryption
    encrypted_data, key = aes_encrypt(data)

    #Writing encoded bytes to the temp file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(encrypted_data)
        temp_path = temp.name

    # IPFS upload
    cid = ipfs_add(temp_path)

    os.remove(temp_path)

    # Save encrypted AES key using CID as label
    save_encrypted_key(cid, key)

    # Log the upload event
    log_event("upload", cid)

    # Print CID and status
    return jsonify({"cid": cid, "status": "success"})


@app.route("/download", methods=["POST"])
def download():
    cid = request.form.get("cid")

    try:
        # Fetch encrypted content from IPFS
        encrypted_data = ipfs_cat(cid)
        if not encrypted_data:
            raise Exception(f"IPFS returned nothing for CID: {cid}")

        # Retrieve AES key
        key = load_encrypted_key(cid)

        # Decrypt file
        decrypted_data = aes_decrypt(encrypted_data, key)

        # Log the download event
        log_event("download", cid)

        return Response(decrypted_data, mimetype="application/octet-stream")

    except Exception as e:
        log_event("download_failed", cid)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)

