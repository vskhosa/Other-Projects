$file = c:\temp\userexport.csv
$s = New-PSSession -ComputerName t8pdcp2 -Credential(Get-Credential)
Invoke-Command -Session $s -ScriptBlock {
import-module activedirectory
Get-ADUser -Filter * -SearchBase "OU=Users,OU=Office365,DC=pci,DC=lan" -Properties * | Select-Object name, employeeNumber, @{n="ManagerName";e={get-aduser $_.manager | select -ExpandProperty name}} | export-csv -path c:\temp\userexport.csv
}
Exit-PSSession