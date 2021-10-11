# Auto Flaming 自动续火 #

帮助广大健忘症患者自动续火。

## 使用 ##

首先，安装包：

```
PyAutoGUI==0.9.52
pyperclip==1.8.1
pywin32==300
```

然后，自定义参数：

`flaming.py`下：
```python
# 续火联系人数量
FLAMING_COUNT = 9
# 续火消息，将在列表中随机抽取
FLAMING_MESSAGES = [
    "早上好",
    "晚上好",
]

# 滚轮滑过一名联系人所需要的 click 数，通常不需要更改
WHEEL_CLICKS_PER_PERSON = -45

# 64位系统使用
QQ_HOME = Path(r"C:\Program Files (x86)\Tencent\QQ\Bin")
# # 32位系统使用
# QQ_HOME = Path(r"C:\Program Files\Tencent\QQ\Bin")
```

然后，保证 QQ 的登录模式非自动登录，且已保存密码，所有续火联系人都是置顶。

运行`flaming.py`，开始续火。