# Codex 最小开发仓库

这是一个供 Codex 云端读取、修改和测试的最小 Python 项目。需要 Python 3.10+，无需安装第三方依赖或配置 API 密钥。

## 运行

在仓库根目录执行：

```bash
python3 main.py
```

预期输出：`Hello, Codex!`

## 测试

```bash
python3 -m unittest discover -v
```

## 使用 Codex

在 Codex 中选择此仓库并创建任务，例如：“给问候程序增加命令行姓名参数，并更新测试。”Codex 会读取 `AGENTS.md`，按其中的指引工作。

这个仓库是 Codex 的开发对象；Codex 云端由平台提供，无需在项目里安装 Codex CLI。若要在自己的电脑使用 CLI，需另外安装并登录。

首次初始化后，将这些文件提交到 GitHub 的 `main` 分支，才能在从 GitHub 拉取的新任务中使用它们。云环境配置草稿需要在环境设置中审阅、保存并发布。
