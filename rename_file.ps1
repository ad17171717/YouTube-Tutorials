Set-Location "C:\Users\your_name\Downloads\Axis Bold as Love"

$song_names = (Get-ChildItem).Name
$artist = 'Jimi Hendrix -'

foreach ($name in $song_names)
{
    $len = $name.Length - 2
    Write-Host $name.substring(2,$len)
    $new_file_name = $artist + $name.substring(2,$len)
    Rename-Item $name -NewName $new_file_name

}