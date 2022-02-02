# Searching Through Emails

Helpful script to search through one or multiple .txt files. 
The output file (emails.txt) contains all unique emails. 
Restrictions can be introduced to make sure that all output emails contain a certain literal text or regular expression.

## Requirements

You will need to have python 3 installed on your system to use this script on the command line (Windows: PowerShell, CMD | Linux & Mac: Terminal).

[Here](https://www.youtube.com/watch?v=XF_rklW9XkU) is a link to a tutorial on how to install Python3.

## Command Flags

You can use the following parameters (also called flags) for the script:

```shell
-f <name of a file in current working dir or path to file>
```

The file(s) from which the data is read. At leased one file is necessary. You can use this flag multiple times, if you want to search all files for unique entries.


```shell
-p
```

If you want to get the email printed out to the console instead of writing it to a file. You only need to write the flag no further value required. Default: false

## Example
You can test the script ```unique_emails.py``` on ```test.txt``` in this folder, with this command:

```shell
python3 unique_emails.py -f test.txt
```

This will write all unique emails that must contain the literal text ```joe```, as indicated in the begining of [unique_emails.py](unique_emails.py) with the code ```MUST_CONTAIN = "joe"```