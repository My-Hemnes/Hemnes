## **Hemnes**

医疗服务检测中心，命名来自宜家客厅家居『汉尼斯』。

### 功能特性

支撑医疗影像AI检测，结节标注，随访, 三维重建等任务调度等，支持多方位扩展。

### 环境依赖

- 语言环境：Python 3.6.8
- 应用框架：Flask 1.1.2, celery 4.3.0
- 日志：loguru 0.5.3
- 构建工具：Jenkins
- 数据库：mongo 4.1.0
- 数据库引擎: Flask-MongoEngine 0.9.5
- 消息中间件：rabbitmq 3.7.28  |  Erlang 22.3.4.7
- 异步处理框架及定时任务 celery 4.3.0 |celery-beat

### 项目结构

- 配置：conf + consul
- 数据模型：models
- 功能/业务模块层：apps
- 序列化以及参数验证：flask-restful, flask-marshmallow
- 接口：api/views
- 脚本：scripts
- 依赖：requirements

### 代码审查

- 规范处理：isort 5.6.4  |  yapf 0.30.0

  [自动规范化引用及代码排序]: https://github.com/PyCQA/isort
  [自动PEP8代码格式化]: https://github.com/google/yapf

- 测试框架：pytest 6.1.2

  [单元及功能测试]: https://github.com/pytest-dev/pytest

  

- 代码检测：pylint 2.6.0

  [构建前的代码格式及错误审查]: https://github.com/PyCQA/pylint