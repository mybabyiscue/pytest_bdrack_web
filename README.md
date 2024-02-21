## 大数据4.1.6自动化测试脚本

[![](https://img.shields.io/badge/%E5%A4%A7%E6%95%B0%E6%8D%AE-4.1.6-blue.svg)](http://192.168.166.38)

### 测试方法
本项目实现web自动化的技术选型：
Python+selenium+Pytest+YAML+Allure ，主要是针对本人的一个接口项目来开展的，
通过 Python+Requests 来发送和处理HTTP协议的请求接口，
使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。

### 项目说明
本项目在实现过程中，把整个项目拆分成请求、关键字封装、测试用例等模块。<br>
首先利用Python把基本web端操作组装成一个个的关键字，
再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一管理，
然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。
<br>当然，如果感兴趣的话，还可以再对接口自动化进行Jenkins持续集成。<br>
* 本次没有通过yaml文件进行数据驱动，可以简单查看代码，没有数据驱动的话，可以直接运行。

### 项目部署
首先，下载项目源码后，在根目录下找到 requirements.txt 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：
```pip3 install -r requirements.txt```

### 项目结构
```
- base ====>> 封装层，基础操作和共用操作
- tools ====>> 各种工具类
- data ====>> 测试数据文件管理
- page ====>> 页面元素，和操作步骤
- testsuit ====>> 测试用例
- pytest.ini ====>> pytest配置文件
- selenium.txt ====>> 相关依赖包文件
- testcases ====>> 测试用例
- report_allure ====>> allure报告
```

### 测试流程
1. 考试流程
- page_class.py ====>> 班级管理
- page_CourseManage.py ====>> 课程管理
- page_ExamManage.py ====>> 考试管理
- page_userStudent.py ====>> 学生管理
- page_userTeacher.py ====>> 教师管理
- page_examinationPaper.py ====>> 试卷管理
- page_seeionList.py ====>> 学生账号考试
<br>admin账号注册教师，教师账号注册学生，配置试卷，配置考试# pytest_bdrack_web
