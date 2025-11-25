$username = "a1"  
$password = ConvertTo-SecureString "1" -AsPlainText -Force  
$credential = New-Object System.Management.Automation.PSCredential ($username, $password)  
  
$command = "echo hello world"  
$session = New-SSHSession -ComputerName "172.19.31.186" -Credential $credential  
Invoke-SSHCommand -Session $session -Command $command  
Remove-SSHSession -Session $session



$username = "a1"
$password = ConvertTo-SecureString "1" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($username, $password)
$linuxServer = "172.19.31.186"
$command = "echo hello world"
ssh $username@$linuxServer -o StrictHostKeyChecking=no -p 22 $command -pw $password.GetNetworkCredential().Password

Import-Module Posh-SSH  
$session = New-SSHSession -ComputerName $linuxServer -Username $username -KeyFile "path_to_private_key"  
Invoke-SSHCommand -SSHSession $session -Command $command  
Remove-SSHSession -SSHSession $session


ssh a1@172.19.31.186 'echo "hello world"' 
ssh a1@172.19.31.186 'nano 1' 

