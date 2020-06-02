# ptt_beauty_spider_python

[zhaoolee/ptt_beauty_spider](https://github.com/zhaoolee/ptt_beauty_spider) 的 `python` 版本，结果上来说，在我的计算机上运行是和期待结果一致的，非常感谢 [原作者](https://github.com/zhaoolee) 的代码，提供了灵感。❤

## 为什么要写

详细问题见 [该 issue 链接](https://github.com/zhaoolee/ptt_beauty_spider/issues/1)，总结一下就是我和我的电脑配合的并不是很好，[原作者](https://github.com/zhaoolee) 的 `nodejs` 代码跑了一下没有任何输出，也没有结果，然后我就想用 `python` 来重写一下，看看能不能运行，结果上来说可以正常运行和下载。

## 缺点

我是 `python` 初学者，[原代码](https://github.com/zhaoolee/ptt_beauty_spider/blob/master/index.js) 里面的 `async` 没有还原到代码中（也不知道是什么），还有其他的部分功能也没还原到胃，其他部分还是模仿的很像的。

## 运行方法

首先确保你已经安装了 `git` 客户端和 `python` 运行环境

克隆此项目

```bash
$ git clone https://github.com/mazixiang/ptt_beauty_spider_python.git
Cloning into 'ptt_beauty_spider_python'...
```

安装并激活 `python` 虚拟环境，虚拟环境是系统的一个位置，你可以在其中安装包，并于其他 `python` 包隔离。将项目的库与其他项目分离是有益的。

```bash
$ python -m venv venv
$ ls
venv
# macOS / Linux
$ source ./venv/bin/activate
```

Windows 系统大致相同，激活虚拟环境的脚本为

```powershell
# Windows
> .\venv\Scripts\activate
```

安装代码中需要用到的几个包

```bash
# python 中的 jQuery，原作者 nodejs 中的 cheerio
(venv) $ pip install pyquery
# （可选）控制台可视化
(venv) $ pip install rich
# 发送请求的包
(venv) $ pip install requests
```

最后运行 `main.py`

```bash
(venv) $ python ./main.py
```

## 注意事项

这个代码在我的电脑上能跑，但不是在所有人电脑上都能跑，如有问题请留下 issue，说明情况。我目前是个学生，不是很忙，如果可以我会尽力帮助。

如果不安装 `rich` 包，请将代码中的 `console=Console()` 一行删除，并将所有的 `console.log` 改为 `print`

请自行设置终端代理，大陆的网络无法下载 `imgur` 上的内容

明日方舟的危机合约活动出了，等活动结束后再继续改进代码……
