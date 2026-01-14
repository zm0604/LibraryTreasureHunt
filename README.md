# LibraryTreasureHunt
基于 Tkinter 的校园图书馆寻宝小游戏（人工智能基础作业3）
项目简介
本项目是基于 Python Tkinter 开发的桌面版文字冒险游戏，为「人工智能基础」课程作业 3 的提交作品。游戏以校园图书馆为场景，通过剧情分支选择、道具收集与谜题解谜，让玩家体验沉浸式寻宝冒险，最终达成不同结局。项目支持 Windows/macOS/Linux 跨平台运行，代码结构清晰，第三方可通过详细步骤快速复现运行。

项目信息
项目名称：校园图书馆寻宝游戏
开发环境：Python 3.7及以上版本
核心技术：Python 内置 Tkinter 库（GUI 界面）、Python 标准库（无需额外依赖）
作业要求：人工智能基础课程 A3 作业
开发者：张曼 | 202331223060
提交日期：2026-01-14

项目结构
LibraryTreasureHunt/
├── 校园图书馆寻宝.py       # 主程序入口文件（核心代码）
├── images/                # 游戏资源文件夹（含场景/道具/结局插画）
│   ├── background.png     # 背景图片
│   ├── item_key.png       # 道具图片（钥匙）
│   ├── ending_perfect.png # 完美结局插画
│   └── [其他图片文件]
└── README.md              # 项目说明文档（本文件）

快速复现指南
1. 环境准备（5 分钟完成）
步骤 1：安装 Python 解释器
Windows 系统：
访问 Python 官网，下载 Python 3.7+ 版本（系统自动推荐适配版本）。
运行安装程序，务必勾选「Add Python to PATH」，随后点击「Install Now」完成默认安装。
验证：按下 Win+R 输入 cmd 打开命令行，输入 python --version，显示版本号（如 Python 3.10.12）即成功。
macOS 系统：
打开终端（启动台→其他→终端），输入 brew install python3（若未安装 Homebrew，先执行 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"）。
验证：输入 python3 --version，显示版本号即成功。
Linux 系统：
终端输入 sudo apt update && sudo apt install python3 python3-pip（Ubuntu/Debian 系统）。
验证：输入 python3 --version，显示版本号即成功。
步骤 2：下载项目文件
访问项目 GitHub 仓库：你的仓库链接，如：https://github.com/zm0604/LibraryTreasureHunt。
点击右上角「Code」→「Download ZIP」，下载项目压缩包。
解压压缩包到本地任意路径，确保解压后文件夹结构与「项目结构」一致（images 文件夹与主程序文件在同一目录）。
2. 运行游戏
通过编辑器运行（适合调试）
安装编辑器（推荐 VS Code 或 PyCharm Community 版）：
VS Code：下载 VS Code 官网，安装后搜索「Python」扩展并启用。
PyCharm：下载 PyCharm 社区版，无需额外配置扩展。
打开编辑器，选择「打开文件夹」，导入解压后的项目文件夹。
在编辑器中找到 校园图书馆寻宝.py 文件，右键点击「运行」（VS Code）或点击右上角运行按钮（PyCharm），即可启动游戏。
3. 验证运行成功
成功标志：弹出游戏主窗口，显示「校园图书馆寻宝」标题、背景图片及剧情开场白。
操作测试：点击剧情选项按钮，能正常切换场景；收集道具后，道具栏显示对应图标，说明交互功能正常。
游戏玩法说明
核心目标：在图书馆场景中探索不同区域，收集关键道具，解开隐藏谜题，达成完美结局。
操作方式：全程鼠标操作，点击按钮选择剧情分支、使用道具或进入新场景。
道具系统：收集的道具自动存入道具栏，关键场景需点击对应道具方可解锁剧情（如用「钥匙」打开储物间）。
结局分支：根据选择的路径和收集的道具，最终触发 3 种不同结局（完美结局 / 普通结局 / 失败结局）。

本项目为「人工智能基础」课程作业原创作品，仅用于学习交流与作业提交。项目中图片资源若涉及第三方版权，请联系作者删除。未经允许，不得用于商业用途。
