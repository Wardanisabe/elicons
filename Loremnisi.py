import json

def align_keys(json_file1, json_file2, aligned_json2_file):
    # Load JSON data from the first file
    with open(json_file1, 'r') as f1:
        data1 = json.load(f1)
    
    # Load JSON data from the second file
    with open(json_file2, 'r') as f2:
        data2 = json.load(f2)
    
    # Create a new dictionary for the aligned data
    aligned_data = {}
    
    # Align keys of data2 with data1
    for key in data1:
        if key in data2:
            aligned_data[key] = data2[key]
        else:
            aligned_data[key] = None  # or some default value
    
    # Save the aligned data to the new file
    with open(aligned_json2_file, 'w') as f3:
        json.dump(aligned_data, f3, indent=4)
    
    # Print the confirmation message
    print(f"Keys of {json_file2} have been aligned with {json_file1} and saved to {aligned_json2_file}.")

# Example usage:
json_file1 = 'file1.json'
json_file2 = 'file2.json'
aligned_json2_file = 'aligned_file2.json'

align_keys(json_file1, json_file2, aligned_json2_file)
