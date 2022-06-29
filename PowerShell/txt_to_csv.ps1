#save the text files in a variable within the directory where the ps script is saved
$payroll_data = get-childitem -file *.txt 

#loop over each of the text files and export them to csv keeping the original file name
foreach ($file in $payroll_data) {
    import-csv $file | export-csv "$($file.basename).csv" -notypeinformation
}