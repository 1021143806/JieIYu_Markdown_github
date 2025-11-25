$response = Invoke-WebRequest -Uri "http://10.68.2.31:7000/ics/taskOrder/addTask" `
    -Method Post `
    -ContentType "application/json" `
    -Body '[
    {
        "modelProcessCode": "K_17CCBL2F_to_31A2CC1B3F_back",
        "priority": 6,
        "orderId": "test{{$date.now}}",
        "fromSystem": "pc",
        "taskOrderDetail": {
            "taskPath": "",
            "shelfNumber": ""
        }
    }
]'
$response

write('已变更')

 function Pause(){
[System.Console]::Write('按任意键继续...')
[void][System.Console]::ReadKey(1)
}
pause
