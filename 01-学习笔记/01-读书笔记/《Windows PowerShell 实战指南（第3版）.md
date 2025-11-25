# 《Windows PowerShell 实战指南（第3版）

## 第一章 初识 PowerShell

### 2.2 重新认识代码输入

- Tab 补全
  - Shift + Tab 会循环地显示以输入命令开头的所有命令
- Dir 遍历文件
  - 输入 Dir,按空格键，然后输入“C:/"，再按 Tab 键，PowerShell会从当前文件夹开始循环遍历所有可用的文件和文件夹名
- 循环显示当前命令的所有可用参数
  - 输入 Set-Execu ，按Tab，然后输入 “ -”，按 Tab
- 按 Esc 可以清空命令行

## 第二章 使用帮助手册

## 第三章 使用帮助系统

### 3.5 帮助详解

#### 3.5.1 参数集和通用参数

获取日志

``` shall
名称
    Get-EventLog

语法
    Get-EventLog [-LogName] <string> [[-InstanceId] <long[]>]  [<CommonParameters>]

    Get-EventLog  [<CommonParameters>]
```

#### 3.5.2 可选和必选参数

方括号：可选参数
不提供参数时，PowerShell 会提示输入必选的 LogName 参数

#### 3.5.3  位置参数

参数是具有位置性的。这意味着只要你把参数值放在正确的位置，你就可以只提供这个参数值，而不需要输入具体的参数名。

两种方式用于确认位置参数

- 第一种 通过语法概要重找到位置参数
  - [-LogName] <string> [[-InstanceId] <long[]>]  
  - 第一个参数：-LogName 位置参数
  必选参数，参数名车参数值不在一个方括号里面。但是它的参数名称处在一个方括号内，这让它成了一个位置参数。
  - 第二个参数：-InstanceId 位置参数
  它是可选的，因为它的参数名称与参数值位于同一个方括号内。在方括号内，-InstanceId本身又处在一个方括号里，意味着它同时还是一个位置参数。它出现在第二个位置，所以我们省略这个参数名称，就必须在该位置提供一个参数值。
  - -Before 非位置参数
  因为参数名和参数值同在一个方括号里面。-Before参数名没有单独放在方括号里，这告诉我们，当选择使用这个参数时，必须输入该参数名称（或者至少是它的别名）。

- 第二种 在详细的帮助文档中找到位置参数
  - 使用 Help 命令指定 -full 参数来打开帮助文档
  - Help Get-EventLog-full

#### 3.5.4 参数值

有些参数被称为开关参数，无需任何输入值。

```powershell

          -AsString [<SwitchParameter>]
              以字符串而非对象的形式返回输出。

              是否必需？                  False
              位置？                     named
              默认值
              是否接受管道输入？            False
              是否接受通配符？             False
```

通过[<SwitchParameter>]可以确认这是一个开关参数，并不需要任何输入值。开关参数的位置可以随意放置，你必须输入参数名（或者至少是一个缩写）。开关参数总是可选的，这可以让你选择是否使用它们。

- 通常的输入类型
  - string  一系列字母和数字，有时候会出现空格（全部字符串必须包含在引号内。
    - 不需要引号：C:\Windows
    - 需要引号：C:\Program Files
    - 可以交替使用单引号或者双引号，最好坚持使用单引号
  - Int、Int32 或 Int64  一个整数类型（整个数字不包含小数）
  - DateTime  通常基于本地计算机的时区配置，字符串被解释成的日期会有所不同。
  - [-ComputerName <string[]>]
    - string 后面的方括号并不意味着某些东西是可选的
    - string[] 意味着该参数可以接受数组、集合，或者是一个列表类型的字符串（只提供一个值也符合语法）
    - PowerShell 把以逗号为分隔符的列表作为数组值对待。
      - Get-EventLog Security -computer Server-R2, DC4, Files02
      - 再次说明，任何一个单一值中如果包含了空格，就必须使用引号。但是作为一个整体的列表，不需要使用引号，只有单一值才需要使用引号。这一点非常重要。
    - 另外一种提供列表值的方式是把它们输入到一个文本文件中，每一个值一行。
      - names.txt

      - ``` powershell
        Server-R2
        Files02
        Files03
        DC04
        DC03

      - 你可以使用Get-Content这个Cmdlet命令来读取该文件的内容，并且发送这些内容到-computerName参数中。
      - () 圆括号可以强制这些命令先执行
      - ==Get-EventLog Application -computer (Get-Content names.txt)==

#### 3.5.5 发现命令示例

我们倾向于通过示例学习，这就是在本书放置大量示例的原因

1. 帮助文档末尾
2. -example 参数
   1. Help Get-EventLog -example

### 3.6 访问 “关于” 主题

### 3.7 访问在线帮助

[微软官方 PowerShll 文档](https://learn.microsoft.com/zh-cn/powershell/scripting/learn/ps101/00-introduction?view=powershell-7.4)

### 3.8 动手实验

1. Update-Help
2. 把其他 Cmdlet 命令输出的内容转换到 HTML
   1. help *html
   2. ConvertTo-Html
3. 输出到文件（file）或打印机（printer）
   1. help *file
4. 哪一个 Cmdlet 可以操作进程(processes)

   1. ``` powershell
      Name                              Category  Module                    Synopsis
      ----                              --------  ------                    --------
      Enter-PSHostProcess               Cmdlet    Microsoft.PowerShell.Core Connects to and enters into an interactive session with a local process.
      Exit-PSHostProcess                Cmdlet    Microsoft.PowerShell.Core Closes an interactive session with a local process.
      Debug-Process                     Cmdlet    Microsoft.PowerShell.M... Debugs one or more processes running on the local computer.
      Get-Process                       Cmdlet    Microsoft.PowerShell.M... Gets the processes that are running on the local computer or a remote computer.
      Start-Process                     Cmdlet    Microsoft.PowerShell.M... Starts one or more processes on the local computer.
      Stop-Process                      Cmdlet    Microsoft.PowerShell.M... Stops one or more running processes.
      Wait-Process                      Cmdlet    Microsoft.PowerShell.M... Waits for the processes to be stopped before accepting more input.

5. 哪一个 Cmdlet 命令向事件日志（log）写入（write）数据
   1. help *log
   2. write-eventlog
6. 你必须知道别名是 Cmdlet 命令的昵称。哪一个 Cmdlet 可以用于创建、修改或者导入别名（aliases）？

   1. ``` powershell
      - Get-Alias - Gets all the aliases in the current session.
      - New-Alias - Creates a new alias.
      - Set-Alias - Creates or changes an alias.
      - Export-Alias - Exports one or more aliases to a file.
      - Import-Alias - Imports an alias file into PowerShell.

7. 怎么保证你在 Shell 重的输入都在一个脚本（transcript）中，怎么保存这个脚本到一个文本文件中？
   1. Save-Script
8. 仅Windows：从安全事件（event）日志检索所有的条目可能需要很长时间，你怎么只获取最近的100条记录呢？
9. 仅Windows：是否有办法可以获取一个远程计算机上安装的服务（services）列表？
10. 是否有办法可以看到一个远程计算机运行了什么进程（processes）（你可以在非Windows操作系统找到答案，但命令本身会有区别）？
11. 尝试查看Out-File这个Cmdlet命令的帮助文档。通过该Cmdlet命令输出到文件每一行记录的默认宽度大小为多少个字符？是否有一个参数可以让你修改这个宽度？
12. 在默认情况下，Out-File将覆盖任何已经存在具有相同的文件名。是否有一个参数可以预防Cmdlet命令覆盖现有的文件？
13. 如何查看在PowerShell中预先定义所有别名（aliases）列表？
14. 怎么使用别名和缩写的参数名称来写一条最短的命令，从而能检索出一台名称为Server1的计算机中正在运行的进程列表？
15. 有多少Cmdlet命令可以处理普通对象？（提示：记得使用类似“object”的单数名词好过使用类似“objects”的复数名词。）
16. 这一章简单提到了数组（arrays）。哪一个帮助主题可以告诉你关于数组的更多信息？

## 第四章 运行命令

### 4.1 无需脚本，仅仅是运行命令

ps1

### 4.2 ==剖析一个命令==

|Command|Parameter1|Parameter2|Parameter3|
|-|-|-|-|
|Get-EventLog|-LogName Security|-ComputerName WIN8,SERVER1|-Verbose|
||参数名称 参数值|参数名 参数值（多个）|开关参数（无值）|

- Get-EventLog
  - 动词-名词形式命名
- 第一个参数 -LogName 并赋值 Security
  - 参数值不包含任何空格或标点符号，因此不需要引号
- 第二个参数 -ComputerName 逗号分隔赋了两个值：Win8 和 Server1
- 最后一个参数 -Verbose
  - 开关参数，无需赋值
- 命令名称和第一个参数之间必须有空格
- 参数名称总是以英文短横线（-）开头
- 参数名称之间必须有空格，多个参数值之间也必须有空格
- 无论参数名称之前的破折号，还是参数值本身包含破折号，都不需要加空格
- PowerShell 不区分大小写

### 4.4 别名：命名的昵称

``` powershell
PS C:\> get-alias -Definition "Get-Service"
Capability      Name
----------      ----
Cmdlet          gsv -> Get-Service
```

gsv 为 Get-Service 命令的别名

### 4.5 使用快捷方式

#### 4.5.1 简化参数名称

可以通过输入 -comp 代替 -ComputerName
简化的规则：必须输入足够的字母让 PowerShell 可以识别不同参数

#### 4.5.2 参数名称别名

``` powershell
PS C:\Users\10211> (get-command get-eventlog | select -ExpandProperty parameters).computername.aliases
Cn
```

Cn 是 computername 的别名

``` powershell
PS C:\> Get-EventLog -LogName Security -Cn SERVER2-Newest 10
```

Tab 键可以补全出 Cn

#### 4.5.3 位置参数

对于位置参数来说，你无须输入参数名称——仅需要在正确的位置提供参数值

>我们倾向于不推荐使用位置（也就是不指定参数名）参数，除非你仅仅是即时输入一个命令并不会带来任何后续影响。任何将命令长期保存的方式，包括在批处理文件中或是写入博客中，都要把所有的参数名称带上。

``` powershell
比如说，下面命令将会难以阅读和理解。

    PS C:\> move file.txt users\donjones\
下面的版本显式指定了参数名称，将会更容易理解。

    PS C:\> move -Path c:\file.txt -Destination \users\donjones\
```

### 4.6 小小作弊一下：==Show-Command==

Show-Command将成为你的助手。该命令允许你指定你无法用对的命令名称，并以图形化的方式将命令的参数名称展示出来。

需要 GUI

### 4.7 对拓展命令的支持

### 4.8 处理错误

### 4.9 常见误区

#### 4.9.2 输入参数

不会挑剔大小写
但会挑剔空格和破折号

### 4.10

1. 显示正在运行的进程列表。
   1. ps
   2. get-process
  
2. 显示最新的100个应用程序日志（请不要使用Get-WinEvent，我们已经为你展示过完成该任务的另一个命令），任务仅限于Windows操作系统。
   1. get-eventlog application -newest 100

3. 显示所有类型为“Cmdlet”的命令（我们已经展示了Get-Command，你还需要阅读帮助文档，从而找出缩小该列表范围，正如本次动手实验所要求的）。
4. 显示所有的别名。
   1. get-command -commandtype alias
5. 创建一个新的别名。使用该别名，你可以运行“np”从PowerShell提示符中启动一个记事本。该任务仅限于Windows操作系统，除非你在Linux系统上安装了wine。
   1. new-alias -name ll -value ls
6. 显示以字母M开头的服务名称。同样，你需要阅读帮助文档找出所需的命令。请不要忘了星号（*），这是PowerShell中通用的通配符。该任务仅限于Windows操作系统。
   1. Get-Service | Where-Object{$_.Name.StartsWith("M")}
7. 显示所有的Windows防火墙规则，你需要使用Help或Get-Command找出所需的Cmdlet。该任务仅限于Windows操作系统。
8. 显示所有Windows防火墙的入站规则。可以使用和之前任务同样的Cmdlet，但你需要阅读帮助文档找出所需的参数以及可选值。该任务仅限于Windows操作系统。

## 第五章 使用提供程序

### 5.4 使用文件系统

cd：change directory 的简写

New-Item

- 新建文件夹
- MKDir
  - 仍然调用了 New-Item ,隐式赋予了 -Type Directory 参数

### 5.5 使用通配符与字面路径

-Path 属性
  指定一个或多个位置的路径。允许使用通配符。默认位置为当前文件夹。

|通配符|代表含义|
|-|-|
|*|代表0个或者多个字符|
|？|仅代表单个字符|

### 5.6 使用其他提供程序

## 第六章 管道：连接命令

## 第七章 拓展命令

## 第八章 对象的另一个名称

## 第九章 深入理解管道

## 第十章 格式化及如何正确使用

## 第十一章 过滤和比较

## 第十二章 学以致用
