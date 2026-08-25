import hashlib

def calculate_hash(filename):
    with open(filename, 'rb') as file:
        file_data = file.read()
        return hashlib.sha256(file_data).hexdigest()


print('File Integrity Checker')

filename = 'test_screenshot.png'

file_hash = calculate_hash(filename)
print('SHA-256:', file_hash)

try:
    with open('baseline.txt', 'r') as file:
        baseline_hash = file.read().strip()

    if file_hash == baseline_hash:
        print('Integrity Check: Pass - File has not changed.')
    else:
        print('Integrity Check: Warning - File has changed!')

except FileNotFoundError:
    with open('baseline.txt', 'w') as file:
        file.write(file_hash)

    print('Baseline created.')
#File integrity checker project
#i added this comment
#this a brach for investigating

