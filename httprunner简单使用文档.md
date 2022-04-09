- 一、什么是httprunner?
    1.	它是面向http协议的测试框架。只需要去维护一份自动生成的yaml/json文件就可以实现接口自动化测试。
    2.	它目前有两个版本，2.X和3.X(推荐3.X)

- 二、httprunner环境搭建
    1.  直接安装httprunner
    pip install httprunner
    Pip install har2case

    2.验证环境
    hrun -V
    Har2case -V
    ![](assets/httprunner简单使用文档/2021-12-13-16-21-40.png)

    3.主要命令
    httprunner   主命令
    hrun   (httprunner的别名)用于运行yaml/json/pytest测试用例
    hmake   (httprunner make的别名)将yaml/json转化成pytest文件
    Har2case   (httprunner har2case的别名)用于将har文件转化成yaml/json文件

    4.创建httprunner项目
    cmd到项目文件夹下执行：httprunner startproject ceshi(ceshi是你的项目名称)
    ![](assets/httprunner简单使用文档/2021-12-13-16-22-16.png)
    ![](assets/httprunner简单使用文档/2021-12-13-16-22-34.png)
 
    
    目录代表的含义：
    har: 可以存放导出的.har文件
    reports: 存储HTML测试报告
    Testcase: 用于存放测试用例
    .env: 存放环境变量
    .gitignore: 设置上传到git时需要忽略那些文件信息
    debugtalk:  存储项目中逻辑运算辅助函数
- 三、快速生成用例
  fiddler抓包选中需要测试的接口

    File -->Export Sessions -->Selected Sessions
    ![](assets/httprunner简单使用文档/2021-12-13-16-22-47.png)
 

    选择HTTPArchive v1.2，Next保存到需要的文件夹
    ![](assets/httprunner简单使用文档/2021-12-13-16-22-57.png)
    ![](assets/httprunner简单使用文档/2021-12-13-16-23-12.png)

 

 



    在PyCharm中打开文件夹
    ![](assets/httprunner简单使用文档/2021-12-13-16-23-20.png)
 



    将.har转化成.yml文件，命令：har2case 测试.har -2y
    ![](assets/httprunner简单使用文档/2021-12-13-16-23-31.png) 

    转化成功，自动生成yaml文件，一个yaml文件就对应一个用例
    ![](assets/httprunner简单使用文档/2021-12-13-16-24-18.png)


    用例结构(每个步骤都要对齐)
    ![](assets/httprunner简单使用文档/2021-12-13-16-24-25.png)
    运行用例yaml文件生成.py文件，命令：hrun 测试.yml
    ![](assets/httprunner简单使用文档/2021-12-13-16-24-34.png)
    运行成功，自动生成.py脚本文件
    ![](assets/httprunner简单使用文档/2021-12-13-16-24-40.png)

    .py文件脚本内容
    ![](assets/httprunner简单使用文档/2021-12-13-16-24-48.png)
- 四、Httprunner关联参数
    如果当前测试的接口需要使用前一个接口返回的参数，就需要用到参数的提取（extract）和参数的引用（$参数名）。
    ![](assets/httprunner简单使用文档/2021-12-13-16-25-01.png)
    例如，当我们使用账号密码登录系统时，通过抓包工具可以看到响应值token，我	们可以在当前用例中把它取出来，以便后面调用
    

    我们可以在teststeps	中用extract: [{“token”:”content.token”}]将它提取出来
    ![](assets/httprunner简单使用文档/2021-12-13-16-25-27.png)
    其中token是自己取的参数名称，后面调用就用$token
    ![](assets/httprunner简单使用文档/2021-12-13-16-25-35.png)

    如果提取和引用是在同一个测试步骤（teststepts）中可以直接引用，如果不在同一	个测试步骤（teststepts）中就需要在全局配置（config）中申明export：[token]	 
    ![](assets/httprunner简单使用文档/2021-12-13-16-25-47.png)
    这样就可以在其他测试用例中引用token了



- 五、Httprunner全局配置
    在用httprunner做接口测试时，我们可以在全局配置（config）中用base_url配置	接口的地址，这样teststeps中的url就只用写相对路径
    ![](assets/httprunner简单使用文档/2021-12-13-16-25-54.png)

    每个用例都配置接口地址，这样一旦修改起来太麻烦，我们可以直接在.env文件中	配置环境变量
    ![](assets/httprunner简单使用文档/2021-12-13-16-26-00.png)

    然后在全局配置中引用，这样修改的时候只需要该.env文件里的环境变量就可以了
    ![](assets/httprunner简单使用文档/2021-12-13-16-26-04.png)
