# Basic file read and write with error handling

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
except:
    print("❌ Error: Could not read the file.")
    exit()

# Modify the content
modified = content.upper()
# Write to a new file
new_filename = "new_" + filename
with open(new_filename, 'w') as new_file:
    new_file.write(modified)

print(f"✅ Modified content written to '{new_filename}'.")