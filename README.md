# Data Model Generator
If you have a text file with multiple lines of JSON records, you can use this script to automatically generate the structure of JSON records.

- It looks for every key of JSON records recursively and if there is any key with multiple value type usages, it will generate a list for this key.


Sample usage:
`python data_model_generator input_file.txt output_file.json`

If the output file is not created yet, script will automatically generate it with the model structure of input file.

