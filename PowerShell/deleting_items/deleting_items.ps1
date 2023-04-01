#change the location to the example directory based on your computer or virtual environment
Set-Location C:\Users\adolo\Downloads\example_folder

#delete a single item using the Remove-Item function
Remove-Item .\txt_file_1.txt

#delete files of a certain extension type
Remove-Item * -Include *.txt

#delete files of a certain extension, but keep files with a certain file name
Remove-Item * -Include *.xlsx -Exclude *1*

#delete a sub directory
Remove-Item .\sub_directory\

#delete all files in the current directory
Remove-Item *