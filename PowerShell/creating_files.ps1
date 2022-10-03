#create a text file
New-Item -Path C:\Users\User\Downloads -Name 'test.txt' -ItemType 'file' -Value 'test file'

#create a Python file
New-Item -Path C:\Users\User\Downloads -Name 'test.py' -ItemType 'file' -Value 'print("test")'

#create multiple text files
New-Item -ItemType 'file' -Path C:\Users\User\Downloads\test1.txt, C:\Users\User\Downloads\test2.txt

#overwrite a file
New-Item -Path C:\Users\User\Downloads -Name 'test.txt' -ItemType 'file' -Value 'overwritten file' -force
