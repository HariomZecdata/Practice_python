
file_path = '/home/hp/Downloads/Student_Satisfaction_Survey.csv'

try:
    with open(file_path, 'r') as file:
        print(file.read())
        print("File opened successfully.")
        # Perform further operations with the file if needed
except Exception as e:
    print("Error:", e)

    