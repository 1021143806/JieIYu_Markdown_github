## 1.1 **Luyten**

### **1.1.1** ***\*工具的介绍\****

luyten是一款操作简单，但是功能使用的专为java程序开发的反编译工具，支持.jar、.zip、.class等类型的文件，并对这些文件进行反编译操作，软件的反编译程度非常高，能够轻松让用户获得最完整、最准确的java源代码。

***\*使用场景\****：业务或功能的表现跟实际版本不一致，怀疑可能是模块版本部署错误，此时需要确认模块版本号是否正确，需要通过反编译工具查看模块代码进行确认

***\*说明\****：基本不会有此类操作，只需要了解即可，具体是否是版本导致需要开发确认代码。

 

### **1.1.2** ***\*工具的使用\****

***\*使用举例\****：查看RDMS模块的部署jar包代码

a) 获取模块jar包：打开xftp，登录RDMS模块所在服务器，进入/main/app/rdms/目录下，可以看到rdms.jar文件，将其拷贝到本地

![img](D:\VScode\gitcode\JieIYu_Markdown_1\问题记录\软件使用\Luyten.assets\wps3.jpg) 

 

b) 打开反编译工具（免安装，双击打开）,File-->Open File...，选择拷贝的rdms.jar打开

![img](D:\VScode\gitcode\JieIYu_Markdown_1\问题记录\软件使用\Luyten.assets\wps4.jpg) 

c) 左侧是代码树，双击文件，右侧会显示该文件的详细代码。

![img](D:\VScode\gitcode\JieIYu_Markdown_1\问题记录\软件使用\Luyten.assets\wps5.jpg) 