import sys
import leancloud

MasterKey = str(sys.argv[1])
AppId = 'CDhsl3xYSgOtBsa7h4FRi95J-MdYXbMMI'
times = 100


def get_version():
    with open('../.version', encoding="utf-8") as f:
        SdS_Version = f.read()
        return SdS_Version


def get_times():
    leancloud.init(app_id=AppId,
                   master_key=MasterKey)
    EnvInfo = leancloud.Object.extend('EnvInfo')

    query = EnvInfo.query
    return query.count()


def write_readme(version, started_times):
    with open('../README.md', "w", encoding="utf-8") as f:
        f.write(f"""
# 
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Lparksi/Sohn_des_Sterns.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Lparksi/Sohn_des_Sterns/)
![Lines of code](https://img.shields.io/tokei/lines/github/lparksi/Sohn_des_Sterns)
![GitHub](https://img.shields.io/github/license/Lparksi/Sohn_des_Sterns)

> 直到v{version},星之子已被启动{started_times}次!  

## 星之子
> "无限星河之子" 
### 隐私政策
我们将收集你的静态信息(Mac码、我们生成的唯一身份码、已加密的活跃群聊号)  
*对于加密的理解*  
我们采用md5单向加密，也就是说我们只能吃真实数值算出md5值，不能通过md5值反推出原文。  
我们收集群聊的md5主要是想在不侵犯用户隐私的情况下，收集基本信息，为星之子开发助力。  

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

### 鸣谢
> Jetbrains 为开源开发者提供免费的实用IDE.
> 我们使用 Pycharm 开发并维护星之子
![https://www.jetbrains.com/?from=Sohn_des_Sterns](https://s3.ax1x.com/2020/12/24/r2HJeI.png)
""")


if __name__ == '__main__':
    write_readme(version=get_version(),
                 started_times=get_times())
