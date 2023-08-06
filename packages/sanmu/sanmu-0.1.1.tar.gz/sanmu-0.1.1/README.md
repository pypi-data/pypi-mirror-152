# Sanmu

Sanmu 是一个纯用Excel描述测试用例的UI自动化测试框，基于python实现，支持unittest和pytest两种模式。

借助Sanmu框架，不需要掌握编程语言，也不需要编写代码，只需要编辑Excel即可完成UI自动化测试。



## 功能特点
- [x] 纯Excel测试用例，不需要任何代码
- [x] 支持pytest及其插件生态
- [x] webdriver：**自动就绪**，支持ChromeDriver（国内网络复杂，暂时只关注ChromeDriver）
- [x] 关键字驱动：内置常用关键字，实现**关键字驱动测试**，提供了接口可以**扩展自定义关键字**
- [x] 变量：使用`save`关键字**创建变量**，使用`{vars}`标签**使用变量**
- [x] 定位：内置可配置的等待策略+XPath智能补全功能，实现元素**智能定位**
- [x] 用例截图：元素交互时自动聚焦，交互后**自动截图**记录
- [x] HTML报告：自动生成HTML测试报告，展示用例执行过程、**交互截图**
- [x] 用例筛选：通过 `-k` 参数，可以**筛选指定的用例**进行执行
- [x] 命令指定excel文件路径（pytest模式）
- [x] 支持allure报告（pytest模式）
- [x] 自动生成**关键字文档**
- [x] 支持**并行测试**(pytest-xdist插件)
- [x] 一键生成的**excel文件模板**
- [x] excel文件内容增加**关键字提示**（不用死记硬背关键字了）
- [ ] 变量类型：支持变量进行**类型转换**
- [x] 支持基于pytest.ini 的框架配置
- [ ] 增加逻辑控制关键字：for、if 、else、sleep等
- [ ] 调用python内置函数
- [ ] 调用python**自定义函数**
- [x] 弹窗：自动处理弹窗，避免用例阻塞、定位失败等问题
- [ ] 支持Appium，实现App端的自动化测试
- [x] 支持docker run，开箱即用
- [ ] 在线测试报告：展示框架运行日志，支持查看历史报告
- [x] 测试结果即时通知：测试执行完毕后，自动通知到相关人员，支持**Email、钉钉、企业微信**



## 安装

sanmu可以通过pip进行安装

```bash
pip install sanmu -U
```



## 使用

在控制台输入 `sanmu --help` 后可以看到帮助信息

```bash
>sanmu --help 
Usage: sanmu [OPTIONS] COMMAND [ARGS]...           
                                                   
  Sanmu 是一个纯用Excel描述测试用例的UI自动化测试框
                                                   
  默认执行 run_pytest 命令                         
                                                   
Options:                                           
  --help  Show this message and exit.              

Commands:
  report        调用allure，生成HTML报告
  run-pytest    （默认）启动 Pytest 框架执行用例，通过pytest-html生成报告
  run-unittest  启动UnitTess框架执行用例，通过HTMLTestRunner生成报告
  show_keys  查看关键字文档
  start         创建demo文件，并命名为 test_{name}.xlsx

```



如果只输入`sanmu` 将调用默认子命令`run-pytest`，开始执行pytest模式的用例
```
>sanmu        
========================== test session starts ==========================
platform win32 -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: D:\Users\Tianyu\PycharmProjects\UI_by_Excel, configfile: pytest.ini
plugins: allure-pytest-2.9.45, html-3.1.1, metadata-1.11.0, rerunfailures-10.2, sanmu-0.0.6
collected 2 items

test_电商项目.xlsx ..                                         [100%]           
========================== 2 passed in 15.22s ===========================
```





## 编写用例

通过excel文件编写用例：

- 每个sheet视为一个TestSuite，
- 数据行，视为测试用例的“步骤”
- 如果步骤为“0”，视为一个新的用例

基本关系：

- 每个excel中有**多个 sheet**
- 每个sheet中有**多个 用例**
- 每个用例中有**多个 步骤**
- 每个步骤中有**说明、关键字、参数**

示例：

![基于Excel的测试用例](images/case_by_excel.jpg)

## 查看报告

### 1. unittest模式

在unittest模式下，sanmu强绑定了HTMLTestRunner，在执行完毕后，自动在**当前目录**生成前缀为`TestResults`的HTML文件，效果如下：

![](images/report_by_unittest.png)

### 2. pytest模式

在pytest模式下，可以按照pytest的惯例，使用以下插件生成报告，sanmu对其有良好的兼容和支持：

- pytest-html
- allure-pytest



![](images/report_by_allure.jpg)



## 结果通知

### 1. 企业微信

在配置文件中填写钉钉通知设置，在测试结束后会自动通知测试结果



配置内容：

```ini
[sanmu]
qywx_url = https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2c253bf4-6412-4f0e-bc7e-5e0f3216bc24
```

消息预览：

![企业微信通知消息](images/msg_to_qywx.jpg)

### 2. 钉钉

在配置文件中填写钉钉通知设置，在测试结束后会自动通知测试结果



配置内容：

```ini
[sanmu]
dingding_url = https://oapi.dingtalk.com/robot/send?access_token=3905a29983f849fc3c6e9728eb1996cfadfefe7e1cab511c506edd3ee89f5200
dingding_secret = SEC51f562f1c05967c13d40907fd495585132fa180af76fb6ef0a61f4f682cd87c2
```

消息预览：

![钉钉消息通知](images/msg_to_dingding.jpg)





## 并发执行

sanmu框架支持为excel用例进行并发执行测试，使用并发执行时，为sanmu 添加参数即可

```
sanmu -n 4
```

也可修改pytest.ini中的adopts项来传递参数

```ini
[pytest]
addopts = -n 4
```

其中`4 `为并发进程数， 如果改为`auto` 则根据CPU数量自动配置并发进程数

**注意：** 并发模式下，每个进程会创建单独的日志文件



## 内置关键字
可通过`show-keys`命令查看内置关键字的说明和参数
```bash
>sanmu show-keys

关键字及其参数
====================
关键字：alert_dismiss
        为alert点击取消
--------------------
关键字：alert_accept
        为alert点击确定

        :param text: 如果输入的内容（可选）
--------------------
关键字 assert
        进行断言

        :param value: 预期结果
        :param assert_name: 断言表达式
        :param actual_value: 实际结果
--------------------
关键字: chosen
        适用于jquery-chosen的下拉选择
        :param xpath: 选择框的定位表达式
        :param value: 要输入的值
--------------------
关键字：click
        点击指定的元素

        等待元素可交互， 可以选择强制点击
        :param locator: 元素定位表达式
        :param force: 是否强制点击，默认为False
--------------------
关键字：frame_ente
        进入指定的iframe

        :param xpath: iframe定位表达式
--------------------
关键字：frame_exit
        退出iframe
--------------------
关键字：frame_top
        返回到顶层frame
--------------------
关键字 ：goto
        跳转到指定页面
        :param url: 指定页面的url
--------------------
关键字：input
        在指定元素内容输入内容

        等待元素可交互
        :param locator: 元素定位表达式
        :param content: 要输入的内容
--------------------
关键字：move
        鼠标移动指定元素的相对位置

        :param xpath: 元素定位表达式
        :param x: 相对元素中心的水平位置，偏移x像素
        :param y: 相对元素中心的垂直位置，偏移y像素
--------------------
关键字：save
        保存变量

        变量应该是一个字符串，在字符串中使用`{}`标签将自动引用已有变量
        例如：
        `save_value("a", "123")`   =>  `a = "123"`
        `save_value("b", "hi:{a})`   =>  `b = "hi:123"`

        :param var_name: 变量名
        :param value: 变量值（字符串）
--------------------
关键字：save_attr
        保存元素属性

        :param var_name: 要保存的变量名
        :param xpath: 元素定位表达式，
        :param attr_name: 属性名
--------------------
关键字：save_text
        保存页面上text内容

        :param var_name: 要保存的变量名
        :param xpath: 元素定位表达式，如果要获取alert的内容，请传递字符串：alert
        :param allow_empty: 是否允许为空，默认为Ture
--------------------
关键字：save_title
        保存网页标题

        :param var_name: 要保存的变量名
--------------------
关键字：save_url
        保存当前网址

        :param var_name: 要保存的变量名
--------------------
关键字：show
        滚动画面使指定元素可见

        :param xpath: 元素定位表达式
--------------------
关键字：sleep
        用例强制等待x 秒

        :param times: 等待的秒数，可以有小数点
--------------------
关键字 ：touch
        聚焦指定元素

        :param locator: 元素定位表达式
--------------------

```





## 自定义关键字（todo）

todo








## 验证器 (obsolete)

验证器(即：verify关键字)接收以下参数

- locator  ，要断言的元素
- verify_name， 要断言的属性
- expression， 断言表达式
- value， 预期值



### verify_name

要断言的属性，在excel独占一个单元格，可选的值如下表

| verify_name | 详情            |      |
| ----------- | --------------- | ---- |
| title       | 网页标题        |      |
| url         | 网页url         |      |
| alert       | alert弹窗的文本 |      |
| text        | 元素内的文本    |      |

### expression

断言表达式在excel独占一个单元格，可选的值如下表

| expression | 详情     | 例子                     |
| ---------- | -------- | ------------------------ |
| >          | 大于     | 3 > 2                    |
| >=         | 大于等于 | 2 >= 2                   |
| <=         | 小于等于 | 1 <= 2                   |
| <          | 小于     | 0 < 2                    |
| ==         | 相等     | 2 == 2<br />张三 == 张三 |
| !=         | 不相等   | 1 != 2<br />张三 != 李四 |
| contains   | 包含     | 张三 contains 张         |
|            |          |                          |
|            |          |                          |



## 配置

可配置项：

- [x] 日志等级
- [x] 日志路径
- [x] 聚焦颜色
- [x] 报告路径
- [x] 等待时长
- [x] 等待频率
- [x] 默认使用强制点击
- [x] Selenium Grid
- [x] 默认浏览器类型
- [x] 默认浏览器启动参数
- [ ] ~~HTMLTestRunner模板路径~~



如果项目中未包含`pytest.ini`，则框架会自动生成，其包含了各项配置的默认值

```ini
[pytest] # pytest原生设置
addopts =
	# allure结果目录
    --alluredir=./.allure_results
    # 执行前自动清空allure结果
    --clean-alluredir
    # 并发执行用例
    -n auto

log_cli = 0 
# 日志文件路径
log_file = pytest.txt
# 日志文件等级
log_file_level = info
# 日志文件格式
log_file_format = %(levelname)-8s %(asctime)s [%(name)s:%(lineno)s]  : %(message)s

[sanmu] # sanmu框架扩展设置

# Allure的绝对路径
allure_path = allure
# Allure报告的保存目录
allure_report = ./report
# allure生成报告后是否自动打开
allure_show = yes

# 浏览器类型
driver_type= chrome
# 浏览器启动参数
driver_option = 
# grid 地址，留空则使用本地浏览器
selenium_grid = 

# 自动等待的检查频率（秒/次）
wait_poll = 0.1
# 自动等待的最大时长（秒）
wait_max = 5

# 元素聚焦时的CSS样式
touch_css = background: #71b95ea1; border: 2px solid red;

# 使用强制点击
force_clieck = no

# email配置
email_server =
email_from = 
email_password = 
email_to = 

# 企业微信
qywx_url =

# 钉钉
dingding_url =
dingding_secret =

```


## 发布流程

1. 开发环境执行pytest，确保测试用例全部通过
2. 修改版本号，并创建新的commit和tag
3. push到github后，手动创建新的releases
4. releases会触发CI/CD，自动完成发布



## 联系作者

如果在使用过程中遇到什么问题，欢迎通过以下方式与我联系：

-   **Email**：dongfangtianyu@gmail.com

-   **WeiXin**:  python_sanmu
