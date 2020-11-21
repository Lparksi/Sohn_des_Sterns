# 
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Lparksi/Sohn_des_Sterns.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Lparksi/Sohn_des_Sterns/)
![Lines of code](https://img.shields.io/tokei/lines/github/lparksi/Sohn_des_Sterns)
![GitHub](https://img.shields.io/github/license/Lparksi/Sohn_des_Sterns)



## 星之子
> "无限星河之子" 
### 隐私政策
自 v0.2.1 之后我们默认起用了反馈机制。

反馈信息中包括了IP等敏感信息，所以我们并不会开放查询权限。

如果你实在不放心，你可以在配置文件里关闭反馈。
```python
# pluginsConfig.py

# Line 21: Feedback
Feedback = True

# make it closed
Feedback = False
```
你可以在 `plugins/feedback/core/main.py` 查询我们具体收集了什么信息。
### 快速部署

参考[Nonebot](https://docs.nonebot.dev/guide/installation.html)
## 支持的功能  
TODO.

  
### 注解  
- Only to me ： 在群聊中是否需要“@”机器人
### 插件详情
- hitokoto  
使用 [Hitokoto](https://hitokoto.cn/) 提供的API
- 智能闲聊  
使用 [腾讯AI](https://ai.qq.com/) 提供的API
### 插件配置文件  
1. 根据注释修改根目录的 `pluginsConfigDefault.py`  
2. 将文件名改为 `pluginsConfig.py`    

使用配置的插件：
- weather
- 智能闲聊
### 配置文件
1. 根据注释修改根目录的 `configDefault.py` 
2. 将文件名改为 `config.py`
### 问答系统
```
.teach <question> <answer>
```
添加一条教学。
```
<question>
```
调起问答。
```
## <question_id>
## <question>
```
查询问答详情
```
### <question_id>
```
删除问答