def group_by_owners(files):
    output_dict = {}
    for key, value in files.items():
        if(key in files.items()):
            output_dict.update({value: key})
    return output_dict
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))