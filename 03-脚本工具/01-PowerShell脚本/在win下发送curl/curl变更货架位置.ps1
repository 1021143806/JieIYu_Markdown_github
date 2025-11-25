#$qrContent = Read-Host "需要变更库位状态的点"
#$shelfNumber = Read-Host "需要绑定的货架号"
$qrContent = "33260329"
$shelfNumber = "DB001"
$ip = "27"
$url_shelf = "http://10.68.2.$ip`:7000/ics/out/shelf/changePosition"
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

write('已变更')

 function Pause(){
[System.Console]::Write('按任意键继续...')
[void][System.Console]::ReadKey(1)
}
pause
