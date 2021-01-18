# Auto Flaming 自动续火 #

帮助广大健忘症患者自动续火。

## Using ##

首先，安装包：
```
PyAutoGUI==0.9.52
pyperclip==1.8.1
pywin32==300
schedule==0.6.0
```

然后，运行`flame_now.py`或`flame_sch.py`，取决于你想在现在续火一次还是计划每天的续火。

## 自定义参数 ##
`flaming.py`下：
```python
FLAMING_COUNT = 15 # 续火人数
FLAMING_MESSAGES = [ # 续火信息。从列表中随机抽取，*开头的为图片
    "*小丑竟是我自己",
    "*好吧，我是小丑"
]
WHEEL_CLICKS_PER_PERSON = -45 # 鼠标滑轮滚过一个联系人的click数量
```

`flame_sch.py`下：
```python
FLAMING_TIME = '09:00' # 续火时间。格式为"HH:MM"
```