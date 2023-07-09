# goit-python-hw-07

## Task

Many people have a folder on their desktop called something like "To be sorted". As a rule, you never get around to actually sorting this folder.

We are going to write a script that will sort files in such folder. In the end, you will be able to customize this program for yourself and it will execute a customized script that meets your needs. To do this, our application will check the file extension and, depending on the file extension, decide which category to assign the file to.

The script accepts one argument at runtime - the name of the folder in which it will sort. Suppose the program file is called sort.py, then to sort the /user/Desktop/Junk folder, you need to run the script with the python command sort.py /user/Desktop/Junk

- In order to successfully cope with this task, you must put the logic for processing the folder in a separate function.
- For the script to be able to go to any nesting depth, the folder processing function must recursively call itself when it encounters a nested folder.

The script should go through the folder specified during the call and sort all files into groups:

- images ('JPEG', 'PNG', 'JPG', 'SVG');
- video files ('AVI', 'MP4', 'MOV', 'MKV');
- documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
- music ('MP3', 'OGG', 'WAV', 'AMR');
- archives ('ZIP', 'GZ', 'TAR');
- unknown extensions.

You can expand and add to this list if you want.

## The results should include:

- A list of files in each category (music, video, photos, etc.)
- A list of all extensions known to the script that are found in the target folder.
- A list of all extensions that are unknown to the script.

Then you need to add functions that will be responsible for processing each type of file.

In addition, all files and folders need to be renamed, removing all characters from the name that cause problems. To do this, apply the normalize function to file names. It is important to understand that you need to rename files in a way that does not change the file extension.

## The normalize function:

1. Converts the Cyrillic alphabet to the Latin alphabet.
2. Replaces all characters except Latin letters and numbers with '_'.

Requirements for the normalize function:

- takes a string as input and returns a string;
- transliteration of Cyrillic characters into Latin;
- replaces all characters except Latin letters and numbers with the '_' character;
- the transliteration may not meet the standard, but be readable;
- uppercase letters remain uppercase and lowercase letters remain lowercase after transliteration.

## Conditions for processing:

- images are moved to the images folder
- documents are moved to the documents folder
- audio files are moved to audio folder
- video files to video folder
- archives are unpacked and their contents are transferred to the archives folder

## Job acceptance criteria

- All files and folders are renamed using the normalize function.
- The file extensions are not changed after renaming.
- empty folders are deleted
- The script ignores the archives, video, audio, documents, images folders;
- unpacked archive content is moved to the archives folder in a subfolder named the same as the archive, but without the extension at the end;
- Files with unknown extensions are left unchanged.
