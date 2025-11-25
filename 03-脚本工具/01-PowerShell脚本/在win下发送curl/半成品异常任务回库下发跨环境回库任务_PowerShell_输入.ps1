write('该脚本用于对半成品异常任务货架停留下发回库任务，需要输入点位和货架')

$qrContent = "12345737"
$nodeStatus = "0"
$ip = "27"
$ip32 = "32"

# $ip = Read-Host "需要变更库位状态的服务器ip，如10.68.2.31 服务器，则输入31"
$qrContent = Read-Host "需要变更库位状态的点"
$shelfNumber = Read-Host "需要绑定的货架号"
#$nodeStatus = Read-Host "0 空库位 2 满库位"
$nodeStatus = "2" # 默认设置为满库位
$body = "{`n`"qrContent`":`"$qrContent`",`n`"nodeStatus`":`"$nodeStatus`"`n}"
$url_stock = "http://10.68.2.$ip`:7000/ics/stock/update/appStockStatus"


$response = Invoke-WebRequest -Uri $url_stock `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
$response
write('库位状态已变更')



#绑定货架
# $body = "[{`n`"areaId`":`"2`",`n`"destPostition`":`"$qrContent`",`n`"shelfNum`":`"$shelfNumber`",`n`"action`":`"1`"`n}]"
# 使用Here-String构建规范JSON
$body = @"
[
  {
    "areaId": "2",
    "destPosition": "$qrContent",
    "shelfNum": "$shelfNumber",
    "action": "1"
  }
]
"@
$url_shelf = "http://10.68.2.$ip`:7000/ics/out/shelf/changePosition"
$response = Invoke-WebRequest -Uri $url_shelf `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
$response
# try {
#   # 发送带证书验证的HTTPS请求
#   $response = Invoke-RestMethod -Uri $url_shelf `
#     -Method Post `
#     -ContentType "application/json; charset=utf-8" `
#     -Body $body `
#     -SkipCertificateCheck `
#     -ErrorAction Stop

#   # 验证响应
#   if ($response.code -eq 200) {
#     Write-Output "货架绑定成功 | Shelf:$shelfNumber @ $qrContent"
#   } else {
#     Write-Error "绑定失败 [$($response.code)]: $($response.message)"
#   }
# }
# catch {
#   Write-Error "请求异常: $($_.Exception.Message)"
# }
# write($body)
# write('货架已绑定')


# #上报NOC异常信息恢复
# $body = "{`n    `"orderId`": `"$orderId`",`n    `"processRate`": `"1/1`",`n    `"status`": 8`n}"
# $url = "http://10.1.107.31:5000/Api/RCS/PushJobStatus"
# $response = Invoke-WebRequest -Uri $url `
#     -Method Post `
#     -ContentType "application/json" `
#     -Body $body
# $response
# write ('已上报')
# #上报结束
#下发回库任务
#$ip = Read-Host "需要变更库位状态的服务器ip，如10.68.2.31 服务器，则输入31"
#$ip = "27"
#$qrContent = Read-Host "需要变更库位状态的点"
#$nodeStatus = Read-Host "0 空库位 2 满库位"


$dateTimeString = Get-Date -Format "MMddyyyyhhmm"
$orderid = "powershell$dateTimeString"
#$shelfNumber = "AG051058"
$body = "{`"modelProcessCode`":`"Full_BCPtoHX_go`",`"priority`":6,`"orderId`":`"$orderid`",`"fromSystem`": `"powershell`",`"taskOrderDetail`":{`"taskPath`":`"`",`"deviceNum`":`"`",`"shelfNumber`":`"$shelfNumber`"}}"
$url = "http://10.68.2.$ip32`:7000/ics/taskOrder/addTask"

$response = Invoke-WebRequest -Uri $url `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
$response
write('回库任务已下发，请检查32服务器中是否存在该任务')
#下发回库任务结束

 function Pause(){
[System.Console]::Write('按任意键继续...')
[void][System.Console]::ReadKey(1)
}
pause
