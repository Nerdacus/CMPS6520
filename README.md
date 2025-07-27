# CMPS6520
CMPS6520 - Distributed Storage Systems Term Project

Secure Decentralized Storage Prototype

This project showcases a modular, privacy-preserving cloud storage system using AES encryption, IPFS for decentralized distribution, and standardized logging. Users can encrypt files in memory, upload them via a Flask interface, and retrieve them securely using CID-based lookup.

Requirements
Ubuntu 20.04+
Python 3.8+
IPFS (go-ipfs) installed and initialized
curl, jq installed for testing and log inspection

Launch Instructions
To run the full system, open three separate terminal windows:

 Terminal 1 – Start the IPFS Daemon
  bash
  ipfs daemon
  Ensure IPFS is initialized beforehand using ipfs init (only needed once).

 Terminal 2 – Run the Flask Client App
  Navigate to the project root (where client/app.py lives):
  bash
  python3 client/app.py
  Starts the server at http://localhost:5000

 Terminal 3 – Perform Tests & View Logs
  Use this terminal for interacting with the API and checking logs.

  Upload File
  Replace <inputFile.txt> with the name of the file to be encrypted and uploaded:
  
  bash
  curl -F 'file=@<inputFile.txt>' http://localhost:5000/upload

  Download File
  Replace <CID> with the actual returned value from upload (CASE SENSITIVE):
  Replace <outputFile.txt> with the name of the file the decrypted data is to be written:

  bash
  curl -X POST -F "cid=<CID>" http://localhost:5000/download > <outputFile.txt>\
  
  Verify Integrity
  Replace <inputFile.txt> with the name of the file to be encrypted and uploaded:
  Replace <outputFile.txt> with the name of the file the decrypted data is to be written:
   
  bash
  diff <inputFile.txt> <outputFile.txt>

 View Audit Log
  bash
  cat audit_log.json

Architecture Highlights:
AES encryption (EAX mode) for secure, verifiable data
IPFS integration via subprocess calls for decentralized file hosting
Local token-key mapping and CID indexing
Structured logging of all access attempts

Future Enhancements:
Auto-indexing of CIDs and aliases
IPFS API integration
Tamper-evident audit logs
CID resolution without manual entry
