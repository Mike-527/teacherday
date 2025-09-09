# 导入 Flask 模块
from flask import Flask, render_template

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义网站的首页路由'/'
# 当有人访问这个地址时，下面的函数就会被触发
@app.route('/')
def hello_world():
    # 这行代码会自动去'templates'文件夹里寻找'index.html'文件并显示它
    return render_template('index.html')

# 这是一个标准的启动入口
if __name__ == '__main__':
    # 启动Web服务器，并开启调试模式(debug=True)
    # debug=True意味着你修改代码后，服务器会自动重启，很方便
    app.run(debug=True)