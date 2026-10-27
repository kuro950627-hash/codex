# Codex 工作指引

- 此仓库是最小 Python 项目，使用 Python 3.10+，无第三方依赖。
- 在当前仓库目录工作。云端任务已经隔离，除非用户明确要求，不要创建 Git worktree。
- 运行示例：`python3 main.py`。
- 运行全部测试：`python3 -m unittest discover -v`。
- 修改后运行相关测试，保持实现简单，不引入不必要的依赖。
- 不要提交密钥、令牌、`.env` 或虚拟环境。
- 默认使用中文说明变更与测试结果。
