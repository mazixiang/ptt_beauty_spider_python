# ptt_beauty_spider_python

[zhaoolee/ptt_beauty_spider](https://github.com/zhaoolee/ptt_beauty_spider) 的 `python` 版本，结果上来说，在我的计算机上运行是和期待结果一致的，非常感谢 [原作者](https://github.com/zhaoolee) 的代码❤。我是完全不懂网站的接口相关的东西。

## 😪 你是不是闲的没事，为啥要做这个

我确实是闲的没事😂，偶然在 [W006《资源》为台湾「表特日报」完成的小姐姐爬虫（附4000张成果图片） - V2方圆](https://www.v2fy.com/p/dgithubjikemijijikemiji-mdwebsite-000007-music-3/) 看到这个项目后，我发现爬虫好像挺有意思，详细问题见 [该 issue 链接](https://github.com/zhaoolee/ptt_beauty_spider/issues/1)，我和我的电脑配合的并不是很好，`Powershell` 似乎有自己的想法，[原作者](https://github.com/zhaoolee) 的 `nodejs` 代码跑了一下，只能看到 `==停止==`，也没有结果反复运行也没有结果就直接结束了，这就奇了怪了，然后我就想参考作者的思路，用 `python` 来重写一下，看看能不能运行，结果上来说可以正常运行和下载图片。

另外推荐一下原作者的网站 [V2方圆](https://www.v2fy.com/)，作者推荐了许多优质的 `Chrome` 插件，我的浏览器中装的所有插件都是搁那看的，非常有用，此外作者还推荐了很多网站（包括福利）🤤

## 🤮 你这个破代码怎么写的这么烂呢，一点优化也没有呢

我是 `python` 初学者，就是刚学完语法的那种，也不精通数据结构和算法，要不然怎么能这么闲？对于[原代码](https://github.com/zhaoolee/ptt_beauty_spider/blob/master/index.js) 还没有完全理解，里面的 `async` 没有还原到代码中（也不知道是什么东西），还有其他的部分功能也没还原到胃，其他部分还是还原的很像的。

## ❓ 那你这个程序要怎么运行啊

首先确保你的电脑已经安装了 `git` 客户端和 `python` 运行环境

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

安装代码中需要用到的几个包（pip 下载慢请自行查找 pip 切换源的方法）

```bash
# python 中的 jQuery，原作者 nodejs 依赖中的 cheerio
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

## 👀 有什么需要注意的地方么

这个代码在我的电脑上能跑，但不是在所有人电脑上都能跑，如有问题请 [留下 issue](https://github.com/mazixiang/ptt_beauty_spider_python/issues/new/choose)，说明具体情况。我目前是个学生，不是很忙，如果可以我会尽力帮助。

`rich` 包是让控制台看起来更舒服的，如果不安装，请将代码中的 `console=Console()` 一行删除，并将所有的 `console.log` 删除或者改为 `print`

请自行设置终端代理，大陆的网络无法下载 `imgur` 上的内容。

明日方舟的危机合约活动出了，要改进的话等活动结束吧。
