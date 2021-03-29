echo off
net user PCIDSK1 /random /add
net user PCIDSK2 <password> /add
net user PCIDSK3 /random /add
net user PCIDSK4 <genericpassword> /add

net localgroup administrators PCIDSK2 /add
net localgroup administrators PCIDSK4 /add

net user <username> /delete
