# cifrado-archivos-python
 Proyecto Jr.
 # Encryption and Decryption of Files in Python

## **Project Description**
This project demonstrates how to secure sensitive files using symmetric encryption implemented in Python. The system uses the `cryptography` library to encrypt and decrypt files, ensuring confidentiality and data protection.

### **Features:**
- **Key Generation**: Generates unique encryption keys and stores them securely in a file (`clave.key`).
- **File Encryption**: Encrypts any given file, creating an encrypted version (`filename.enc`).
- **File Decryption**: Decrypts encrypted files back to their original state using the stored key.
- **Interactive Menu**: User-friendly interface for seamless execution of key functions.

---

## **Technologies Used**
- **Language**: Python
- **Library**: Cryptography
- **Operating System**: macOS (M1 Pro-compatible)

---

## **How to Use**

### **Requirements**
Ensure you have Python 3 installed. Install the required library:
```bash
pip3 install cryptography
```

### **Running the Script**
1. Save the script in a file named `encryption.py`.
2. Open a terminal and execute:
   ```bash
   python3 encryption.py
   ```
3. Follow the on-screen menu:
   - **Option 1**: Generate a new encryption key.
   - **Option 2**: Encrypt a file.
   - **Option 3**: Decrypt an encrypted file.

### **Example Usage**
1. **Generate a Key**:
   - Run the program and choose `Option 1`. This will create a file `clave.key` containing the encryption key.

2. **Encrypt a File**:
   - Place a text file (e.g., `example.txt`) in the same directory as the script.
   - Choose `Option 2` and enter the file name. The script will generate `example.txt.enc`.

3. **Decrypt a File**:
   - Choose `Option 3` and provide the name of the encrypted file (e.g., `example.txt.enc`). The script will decrypt and restore the original file (`example.txt`).

---

## **Key Features Highlighted in Resume**
### **Project Name**: File Encryption and Decryption System in Python

### **Description**:
- Designed and implemented a Python program to secure files using symmetric encryption.
- Integrated a user-friendly menu for generating encryption keys, encrypting files, and decrypting them.
- Used the `cryptography` library to apply secure file handling techniques.

### **Results**:
- Enhanced knowledge of Python libraries for data security.
- Demonstrated proficiency in implementing encryption systems for real-world scenarios.

### **Key Technologies**:
- **Language**: Python
- **Library**: Cryptography
- **System**: macOS M1 Pro

---

## **GitHub Repository**
### **Title**: File Encryption and Decryption in Python

#### **Repository Link**:
[GitHub - Encryption System](https://github.com/ejimenez01/cifrado-archivos-python1) 

#### **Contents of the Repository**:
- The complete Python script.
- Instructions for setting up and running the project.
- Example files to test encryption and decryption.
- A `README.md` file with project documentation.

---

## **Next Steps**
- Add error handling for missing or invalid files.
- Expand the encryption system to support multiple keys for different files.
- Deploy the project as an executable application.

---

For further assistance or questions, feel free to contact me!


