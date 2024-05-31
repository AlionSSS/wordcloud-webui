# wordcloud-webui
The web UI for wordcloud (text to word cloud picture converter)

## 描述(Description)

- 功能：利用 [word_cloud](https://github.com/amueller/word_cloud) 将 **普通文本** 转为 **词云图像** 文件
- 可视化：使用 [Gradio](https://github.com/gradio-app/gradio) 将该功能可视化

## 界面
![image.png](doc-resources%2Fimage.png)

## 安装(Install)
- 新建一个虚拟环境(Python 3.9.16)，或使用已有的Python环境
  - 例如 `$ conda create -n env_name python=3.9` 
- 安装依赖
  - `$ pip install gradio==4.29 -i "https://pypi.doubanio.com/simple/"`
  - `$ pip install wordcloud==1.9.3 -i "https://pypi.doubanio.com/simple/"` 
  - `$ pip install jieba==0.42.1 -i "https://pypi.doubanio.com/simple/"`
- 下载本项目代码
  - 点击[本项目GitHub页面](https://github.com/AlionSSS/wordcloud-webui)右上角的绿色的按钮`Code`，再点击`Download ZIP`

## 启动服务(Start Service)
- 进入到本项目的目录下
- 二选一
  - 在本地电脑端启动，直接执行 `$ python main.py`
  - 在服务器端启动，执行 `$ nohup python main.py 1>server_run.log 2>&1 &`
