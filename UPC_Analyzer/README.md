Identification Number Check Program

📝 Overview

The Identification Number Check Program is designed to allow users to input a code (numerical identification number), and the program will identify whether the entered code belongs to one of three types: Basic Code, Positional Code, or Universal Code (UPC). It also handles invalid codes that do not belong to any of these categories.

The program continuously prompts the user for input until they choose to exit by entering "0".

🔑 Key Features

Basic Code Check: Identifies if the entered code matches the format of a basic identification code.
Positional Code Check: Validates if the input is a positional code based on predefined criteria.
Universal Code Check (UPC): Recognizes if the code is a valid Universal Product Code (UPC).
Code Categorization: Organizes codes into four lists:
Basic Codes
Positional Codes
Universal Codes (UPC)
Invalid Codes (None of the three types)

⚙️ How It Works

The program starts by greeting the user and prompting them to input an identification code (digits only).
Upon entering the code:
The program checks whether the code is a basic code.
If not, it checks if the code is a positional code.
If neither, it checks if the code is a universal code (UPC).
If the code matches none of the three categories, it is categorized as an invalid code.
After each code check, the program asks the user to either enter another code or exit the program by typing "0".
When the user exits, the program displays a summary of:
- Valid Basic Codes
- Valid Positional Codes
- Valid Universal Codes (UPC)
- Invalid Codes
