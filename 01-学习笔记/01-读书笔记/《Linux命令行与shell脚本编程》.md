# Linux命令行与shell脚本编程

## 第一部分 Linux命令行

### 第1章 初试Linux shell

### 第2章 走进shell

### 第3章 bash shell基础命令

## 第二部分 shell脚本编程基础

### 第14章 处理用户输入

#### 14.1传递参数

``` Shell
./addem 10 30
```

##### 14.1.1读取参数

位置参数（positional parameter）

|$0|脚本名|
|-|-|
|$1|第一个命令行参数|
|$2|第二个命令行参数|
|$3|第三个命令行参数|
|$4|第四个命令行参数|
|$5|第五个命令行参数|
|...|...|

```Shell
$ cat positional1.sh
#!/bin/bash
# Using one command-line parameter 计算阶乘
#
factorial=1
for (( number = 1; number <= $1; number++ ))
do
factorial=$[ $factorial * $number ]
done
echo The factorial of $1 is $factorial
exit
$
$ ./positional1.sh 5
The factorial of 5 is 120  
$
参数之间用空格分隔
```

```Shell
$ cat positional10.sh
#!/bin/bash
# Handling lots of command-line parameters
#
product=$[ ${10} * ${11} ]
echo The tenth parameter is ${10}.
echo The eleventh parameter is ${11}.
echo The product value is $product.
exit
$
$ ./positional10.sh 1 2 3 4 5 6 7 8 9 10 11 12
The tenth parameter is 10.
The eleventh parameter is 11.
The product value is 110.
$
```

##### 14.1.2读取脚本名

```Shell
$ cat positional0.sh
#!/bin/bash
# Handling the $0 command-line parameter
#
echo This script name is $0.
exit
$
$ bash positional0.sh
This script name is positional0.sh.
$
```

basename可以返回不包含路径的脚本名

```Shell
$ cat posbasename.sh
#!/bin/bash
# Using basename with the $0 command-line parameter
#
name=$(basename $0)
#
echo This script name is $name.
exit
$
$ ./posbasename.sh
This script name is posbasename.sh.
$
```

```Shell
$ cat checksystem.sh
#!/bin/bash
# Using the $0 command-line parameter in messages
#
scriptname=$(basename $0)
#
echo The $scriptname ran at $(date) >> $HOME/scripttrack.log
exit
$
$ ./checksystem.sh
$ cat $HOME/scripttrack.log
The checksystem.sh ran at Thu 04 Jun 2020 10:01:53 AM EDT
$
```

##### 14.1.3参数测试

如果运行脚本时没有指定所需的参数，则可能出问题

#### 14.2特殊参数变量

##### 14.2.1参数统计

 $#

 !($#)

?

|特殊变量|意义|
|-|-|
|$#|脚本运行时携带的命令行参数的个数
没有任何参数时，$#的值为0|
|!{$#}|最后一个位置变量
没有任何参数时，返回脚本名|

```Shell
$ cat countparameters.sh
#!/bin/bash
# Counting command-line parameters
#
if [ $# -eq 1 ]
then
fragment="parameter was"
else
fragment="parameters were"
fi
echo $# $fragment supplied.
exit
$
$ ./countparameters.sh
0 parameters were supplied.
$
$ ./countparameters.sh Hello
1 parameter was supplied.
$
$ ./countparameters.sh Hello World
2 parameters were supplied.
$
$ ./countparameters.sh "Hello World"
1 parameter was supplied.
$
```

##### 14.2.2获取所有数据

|特殊变量|意义|
|-|-|
|$*|将参数视为整体|
|$@|将参数是为多个独立的单词|

?

?

```Shell
$ cat grabbingallparams.sh
#!/bin/bash
# Testing different methods for grabbing all the parameters
#
echo
echo "Using the \$* method: $*"
echo
exit
$
$ ./grabbingallparams.sh alpha beta charlie delta

Using the $* method: alpha beta charlie delta

$
```

```Shell
$ cat grabdisplayallparams.sh
#!/bin/bash
# Exploring different methods for grabbing all the parameters
#
echo
echo "Using the \$* method: $*"
count=1
for param in "$*"
do
echo "\$* Parameter #$count = $param"
count=$[ $count + 1 ]
done
echo
exit
$
$ ./grabdisplayallparams.sh alpha beta charlie delta

Using the $* method: alpha beta charlie delta
$* Parameter #1 = alpha beta charlie delta
$
```

?

```Shell
$ cat grabbingallparams.sh
#!/bin/bash
# Testing different methods for grabbing all the parameters
#
echo
echo "Using the \$@ method: $@"
echo
exit
$
$ ./grabbingallparams.sh alpha beta charlie delta

Using the $@ method: alpha beta charlie delta

$
```

```Shell
$ cat grabdisplayallparams.sh
#!/bin/bash
# Exploring different methods for grabbing all the parameters
#
echo
echo "Using the \$@ method: $@"
count=1
for param in "$@"
do
echo "\$@ Parameter #$count = $param"
count=$[ $count + 1 ]
done
echo
exit
$
$ ./grabdisplayallparams.sh alpha beta charlie delta

Using the $@ method: alpha beta charlie delta
$@ Parameter #1 = alpha
$@ Parameter #2 = beta
$@ Parameter #3 = charlie
$@ Parameter #4 = delta

$
```

?

#### 14.3移动参数

##### shift 转移 / 改变 / 轮班

```Shell
$ cat shiftparams.sh
#!/bin/bash
# Shifting through the parameters
#
echo
echo "Using the shift method:"
count=1
while [ -n "$1" ]
do
echo "Parameter #$count = $1"
count=$[ $count + 1 ]
shift
done
echo
exit
$
$ ./shiftparams.sh alpha bravo charlie delta

Using the shift method:
Parameter #1 = alpha
Parameter #2 = bravo
Parameter #3 = charlie
Parameter #4 = delta

$
```

##### 参数

n（可选）：大于等于1且小于等于参数个数的整数，默认为1。

#### 14.4处理选项

同时提供参数和选项的bash命令

##### 14.4.1查找选项

###### 1.处理简单选项

```Shell
$ cat extractoptions.sh
#!/bin/bash
# Extract command-line options
#
echo
while [ -n "$1" ]
do
case "$1" in
-a) echo "Found the -a option" ;;
-b) echo "Found the -b option" ;;
-c) echo "Found the -c option" ;;
*) echo "$1 is not an option" ;;
esac
shift
done
echo
exit
$
$ ./extractoptions.sh -a -b -c -d

Found the -a option
Found the -b option
Found the -c option
-d is not an option

$
```

case语句会检查每个参数，确认是否为有效的选项。找到一个处理一个

###### 2.分离参数和选项

双连字符（--）

?

?

```Shell
$ cat extractoptionsparams.sh
#!/bin/bash
# Extract command-line options and parameters
#
echo
while [ -n "$1" ]
do
case "$1" in
-a) echo "Found the -a option" ;;
-b) echo "Found the -b option" ;;
-c) echo "Found the -c option" ;;
--) shift
break;;           #break跳出while循环，需要再加入一个shift
*) echo "$1 is not an option" ;;
esac
shift
done
#
echo
count=1
for param in $@
do
echo "Parameter #$count: $param"
count=$[ $count + 1 ]
done
echo
exit
$
```

?

```Shell
$ ./extractoptionsparams.sh -a -b -c test1 test2 test3

Found the -a option
Found the -b option
Found the -c option
test1 is not an option
test2 is not an option
test3 is not an option

$
```

```Shell
$ ./extractoptionsparams.sh -a -b -c -- test1 test2 test3

Found the -a option
Found the -b option
Found the -c option

Parameter #1: test1
Parameter #2: test2
Parameter #3: test3

$
```

###### 3.处理含值的选项

```Shell
$ cat extractoptionsvalues.sh
#!/bin/bash
# Extract command-line options and values
#
echo
while [ -n "$1" ]
do
case "$1" in
-a) echo "Found the -a option" ;;
-b) param=$2
echo "Found the -b option with parameter value $param"
shift;;
-c) echo "Found the -c option" ;;
--) shift
break;;
*) echo "$1 is not an option" ;;
esac
shift
done
#
echo
count=1
for param in $@
do
echo "Parameter #$count: $param"
count=$[ $count + 1 ]
done
exit
$
$ ./extractoptionsvalues.sh -a -b BValue -d

Found the -a option
Found the -b option with parameter value BValue
-d is not an option
$
```

##### 14.4.2使用getopt命令（-ab参数)

###### 1.命令格式

getopt optstring parameters

在optstring中列出要在脚本中用到的每个命令行选项字母。然后，在每个需要参数值的选项字母后面加一个冒号。

ab:cd：参数为abcd，其中b需要额外参数值

```Shell
$ getopt ab:cd -a -b BValue -cd test1 test2
-a -b BValue -c -d -- test1 test2
$
```

警告：getopt和getopts（更高级的版本）是两个命令

###### 2.在脚本中使用getopt

set -- $(getopt -q ab:cd "$@")

```Shell
$ cat extractwithgetopt.sh
#!/bin/bash
# Extract command-line options and values with getopt
#可以将位置变量的值替换成set命令所指定的值。
set -- $(getopt -q ab:cd "$@")
#
echo
while [ -n "$1" ]
do
case "$1" in
-a) echo "Found the -a option" ;;
-b) param=$2
echo "Found the -b option with parameter value $param"
shift;;
-c) echo "Found the -c option" ;;
--) shift
break;;
*) echo "$1 is not an option" ;;
esac
shift
done
#
echo
count=1
for param in $@
do
echo "Parameter #$count: $param"
count=$[ $count + 1 ]
done
exit
$
```

getopt命令不擅长处理带空格和引导的参数值  “test1 test2"

##### 14.4.3 ??使用getopts命令

```Shell
$ cat extractwithgetopts.sh
#!/bin/bash
# Extract command-line options and values with getopts
#
echo
while getopts :ab:c opt
do
case "$opt" in
a) echo "Found the -a option" ;;
b) echo "Found the -b option with parameter value $OPTARG";;
c) echo "Found the -c option" ;;
*) echo "Unknown option: $opt" ;;
esac
done
exit
$
$ ./extractwithgetopts.sh -ab BValue -c

Found the -a option
Found the -b option with parameter value BValue
Found the -c option
$
```

#### 14.5选项标准化

通用

- case语句中不用连字符--

- 可以在参数值中加入空格

```Shell
$ ./extractwithgetopts.sh -b "BValue1 BValue2" -a

Found the -b option with parameter value BValue1 BValue2
Found the -a option
$
```

- 可以将选项字母和参数值写在一起，两者之间不加空格

```Shell
$ ./extractwithgetopts.sh -abBValue

Found the -a option
Found the -b option with parameter value BValue
$
```

- 能够在-b选项中正确解析出值,并且可以将未定义的选项输出为'?'

```Shell
$ ./extractwithgetopts.sh -d

Unknown option: ?
$
$ ./extractwithgetopts.sh -ade

Found the -a option
Unknown option: ?
Unknown option: ?
$
```

在处理每个选项时，getopts会将OPTIND环境变量值增1。可以使用shift和OPTIND值来移动参数

##### OPTIND

```Shell
$ cat extractoptsparamswithgetopts.sh
#!/bin/bash
# Extract command-line options and parameters with getopts
#
echo
while getopts :ab:cd opt
do
case "$opt" in
a) echo "Found the -a option" ;;
b) echo "Found the -b option with parameter value $OPTARG";;
c) echo "Found the -c option" ;;
d) echo "Found the -d option" ;;
*) echo "Unknown option: $opt" ;;
esac
done
#
shift $[ $OPTIND - 1 ]
#
echo
count=1
for param in "$@"
do
echo "Parameter $count: $param"
count=$[ $count + 1 ]
done
exit
$
$ ./extractoptsparamswithgetopts.sh -db BValue test1 test2

Found the -d option
Found the -b option with parameter value BValue

Parameter 1: test1
Parameter 2: test2
$/h5
```

?

|选项|功能|
|-|-|
|-a|显示所有对象|
|-c|生成计数|
|-d|指定目录|
|-e|扩展对象|
|-f|指定读入数据的文件|
|-h|显示命令的帮助信息|
|-i|忽略文本大小写|
|-l|产生长格式输出|
|-n|使用非交互模式（批处理）|
|-o|将所有输出重定向至指定的文件|
|-q|以静默模式运行|
|-r|递归处理目录和文件|
|-s|以静默模式运行|
|-v|生成详细输出|
|-x|排除某个对象|
|-y|对所有问题回答yes|

#### 14.6 获取用户输入

更多的交互，运行时询问用户并等待用户回答

##### 14.6.1 基本的读取

```Shell
$ cat askname.sh
#!/bin/bash
# Using the read command
#
echo -n "Enter your name: "
read name
echo "Hello $name, welcome to my script."
exit
$
$ ./askname.sh
Enter your name: Richard Blum
Hello Richard Blum, welcome to my script.
$
```

## 第三部分 高级shell脚本编程

## 第四部分 创建实用脚本
