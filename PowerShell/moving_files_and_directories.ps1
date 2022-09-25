#move specific file
Move-Item -path C:\Users\Adrian\Downloads\tech\AMZN.csv -destination C:\Users\Adrian\Downloads\stock_data

#move all files
Move-Item -path C:\Users\Adrian\Downloads\tech\* -destination C:\Users\Adrian\Downloads\stock_data

#move directories
Move-Item -path C:\Users\Adrian\Downloads\tech -destination C:\Users\Adrian\Downloads\stock_data