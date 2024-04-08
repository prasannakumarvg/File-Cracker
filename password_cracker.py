import pikepdf
import sys
import os
import subprocess
import zipfile


def check_file_exists(filename):
    return os.path.exists(file_path)

def crack_password_protected_pdf(file_path,password_txt):
    with open(password_txt,'r') as password_file:
        for password in password_file:
            password = password.strip()
            try:
                with pikepdf.open(file_path, password=password) as pdf:
                    print(f"Password found: {password}")
                    return
            except pikepdf.PasswordError:
                continue

def crack_password_protected_zip(file_path,password_txt):
 with zipfile.ZipFile(file_path,'r') as file:
    with open(password_txt,'r') as password_file:
        for password in password_file:
            password = password.strip()
            try:
                file.extractall(pwd=password.encode())
                print(f"Password found: {password}")
                return
            except (RuntimeError, zipfile.BadZipFile, RuntimeError):
                        continue
            

def  crack_password_protected_pptx(file_path,password_txt):
    with open(file_path,'r') as file:
        with open(password_txt,'r') as password_file:
            for password in password_file:
                password.strip()
                try:
                    file1=msoffcrypto.OfficeFile(file)
                    file1.load(password = password, verify_password = True)
                    print(f"Password found: {password}")
                    return
                except:
                    continue


if __name__ == "__main__":
    file_path = os.path.abspath(sys.argv[1])
    password_file=os.path.abspath(sys.argv[2])
    if not check_file_exists(file_path): 
        print("Error: The specified file does not exist.")
    else:
        if file_path.endswith('.pdf'):
            crack_password_protected_pdf(file_path, password_file)
        elif file_path.endswith('.zip'):
            crack_password_protected_zip(file_path, password_file)
        elif file_path.endswith('.pptx'):
            crack_password_protected_pptx(file_path, password_file)
        else:
            print("Error: Unsupported file format.")