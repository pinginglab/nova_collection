# nova_collection
整个攻防系统「pingsec」的核心模块，负责接收请求，完成具体的容器生成和下发等工作，以及端口映射到外网的工作。将成为本系统对企业合作，前后端分离，本项目仅负责后端部分，目前将鉴权、登录功能都集合在一起，后续会将这部分功能独立成一个项目即tokenstore


# 版本开发

## version 1
1. 邮箱验证码功能测试完成
  1.1 增加异步发送，未完成
2. 容器创建以及下发，端口映射完成
3. 登录功能
4. 注册功能
5. 首页展示
6. 鉴权功能
