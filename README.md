# Password Cracker

This Python script helps crack password-protected files such as PDFs, ZIP archives, and PPTX presentations.

## Features

- **PDF Password Cracking**: Crack passwords of protected PDF files.
- **ZIP Password Cracking**: Extract contents of password-protected ZIP archives.
- **PPTX Password Cracking**: Unlock password-protected PowerPoint presentations.

## Usage

1. Clone the repository:
    > git clone https://github.com/your-username/password-cracker.git
    
Navigate to the project directory:
    > cd password-cracker

Install dependencies:
    > pip install pikepdf msoffcrypto-tool
    
Run the script with the path to the protected file and the password list:
    > python3 password_cracker.py <file_path> <password_txt>
     
     <file_path>: Path to the password-protected file.
     <password_txt>: Path to the text file containing passwords to try.
     
Example:
       python3 password_cracker.py protected.zip password.txt
       
Requirements
  Python 3.x
  pikepdf
  msoffcrypto-tool

Contributing

Contributions are welcome! If you have any suggestions, bug reports, or want to add more features, please open an issue or submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
