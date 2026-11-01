# Blockchain-Based Evidence Management System

## Overview
The Blockchain-Based Evidence Management System is a secure and transparent digital platform designed to manage criminal evidence records using blockchain technology. The project aims to eliminate the risk of tampering, unauthorized modifications, and data loss by storing important evidence-related information on an immutable blockchain ledger.

This system combines:
- Django (Python web framework) for the user interface
- Solidity smart contracts for secure blockchain logic
- Web3.py for interacting with the Ethereum blockchain
- SQLite for local database support
- HTML/CSS for web pages and user interaction

The project is intended for law enforcement and evidence management scenarios where data integrity, trust, and auditability are critical.

---

## Problem Statement
Traditional evidence management systems often rely on centralized databases that can be altered, manipulated, or hacked. In forensic and criminal investigation environments, evidence must remain trustworthy and tamper-proof. A centralized system creates risks such as:
- unauthorized modifications
- evidence deletion or loss
- lack of transparency
- weak audit trails
- reliance on a single vulnerable data source

To address these issues, this project uses blockchain technology to securely store and retrieve evidence records.

---

## Objective
The primary objectives of the project are:
- To build a secure evidence management system
- To store evidence and officer-related records on a blockchain
- To improve data integrity and traceability
- To provide a user-friendly interface for management and verification
- To create a tamper-resistant system for law enforcement operations

---

## Why Blockchain?
Blockchain provides the following advantages for evidence management:
- Immutability: Data once stored cannot be easily changed
- Transparency: Records can be verified by authorized users
- Traceability: Every transaction is stored in a secure ledger
- Security: Blockchain reduces the risk of manipulation and unauthorized editing
- Trust: Data integrity is strengthened because records cannot be silently altered

For sensitive records such as evidence, witness statements, crime cases, and officer details, blockchain is a strong solution.

---

## Key Features
- Admin login system
- Officer login and authentication
- Officer registration
- Evidence record creation
- Crime details and evidence details tracking
- Witness information management
- Image upload support for evidence files
- Blockchain-backed storage of evidence and user records
- View and access evidence entries
- Officer and evidence listing pages
- System designed for audit-friendly investigation workflows

---

## System Architecture
The application consists of the following layers:

1. Frontend Layer
   - Django templates
   - HTML/CSS pages
   - User interaction screens

2. Backend Layer
   - Django views
   - Request handling
   - Business logic
   - Validation and file uploads

3. Blockchain Layer
   - Solidity smart contract
   - Ethereum blockchain
   - Contract functions for creating and retrieving users/evidence

4. Data Interaction Layer
   - Web3.py integration
   - Smart contract ABI usage
   - Blockchain transactions and retrieval

---

## Technologies Used
### Frontend
- HTML
- CSS
- Django Templates

### Backend
- Python
- Django
- Web3.py

### Blockchain
- Solidity
- Ethereum-compatible smart contracts

### Database
- SQLite

---

## Project Structure
- `Evidence/` — Django project settings and core project files
- `EvidenceApp/` — app logic, templates, views, routes
- `Evidence.sol` — smart contract for user and evidence management
- `Evidence.json` — ABI file for blockchain interaction
- `manage.py` — Django project entry point
- `hello-eth/` — Ethereum-related files
- `db.sqlite3` — SQLite database
- `SCREENS.docx` — project screenshots/documents
- `run.bat` — script to run the project

---

## Smart Contract Functionality
The Solidity contract includes:
- `createUser()` — adds an officer/user
- `getUserCount()` — gets user count
- `getUsername()`, `getPassword()`, etc. — retrieves user details
- `createEvidence()` — stores evidence information
- `getEvidenceCount()` — returns evidence count
- `getEvidenceid()`, `getOfficername()`, `getReportedcrime()`, etc. — retrieves evidence details

This ensures that evidence and user data are stored in a decentralized and structured way.

---

## Screenshots
Add your screenshots here for better presentation.

![Login Page](add-your-login-image.png)
![Officer Dashboard](add-your-officer-dashboard-image.png)
![Add Evidence Form](add-your-evidence-form-image.png)
![Evidence List](add-your-evidence-list-image.png)

> Replace the image filenames with actual screenshots from your project.

---

## Demo Video
A demo video can be added here to showcase the working system.

[Demo Video Link](https://your-video-link-here.com)

Example:
- Upload a short project presentation video
- Record the login flow
- Show officer registration
- Show evidence creation
- Show blockchain interaction
- Show evidence retrieval

---

## Use Case
This system can be used in:
- police departments
- forensic investigation units
- cybercrime evidence repositories
- legal and compliance tracking systems
- centralized public safety record systems

It helps ensure a clear and verifiable trail for every evidence item managed by authorities.

---

## Benefits
- Tamper-resistant evidence storage
- Increased trust in digital records
- Better accountability for police and officers
- More secure handling of criminal records
- Improved digital record keeping for investigation agencies

---

## Future Enhancements
- Add role-based access control
- Add admin approval workflow
- Add stronger authentication and MFA
- Integrate with real blockchain wallets
- Improve UI/UX design
- Add document scanning and OCR support
- Add cloud storage for uploaded evidence files
- Add dashboard analytics and reporting

---

## Comments
This project demonstrates how blockchain technology can be applied to real-world public safety and evidence management systems. It is a practical solution that combines modern web development and blockchain principles to make sensitive records more secure and trustworthy. Although the project is based on a simple local blockchain implementation, it effectively shows the potential of blockchain in law enforcement and evidence integrity.

The system is suitable for academic projects, demonstrations, and real-world prototypes for secure digital evidence handling.

---

## Conclusion
The Blockchain-Based Evidence Management System is a strong example of combining blockchain, web development, and digital security to solve a real-world problem. It helps create trust and transparency in sensitive evidence records while also showcasing practical application of Ethereum smart contracts and Django web development.

---

## License
This project is intended for educational and demonstration purposes.
