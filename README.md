# 定时任务管理器

> 一个功能强大、界面美观的Windows定时任务管理工具，支持定时关机和重启操作。

## 项目简介

定时任务管理器是一个基于Python + PySide6 + SQLite3开发的桌面应用程序，采用现代化的圆角卡片式设计语言，支持多主题切换，提供流畅的翻卡式倒计时动画效果。

## 功能特性

- ✨ **现代化UI设计**：采用圆角卡片式设计，界面简洁美观
- 🎨 **多主题支持**：内置浅色、深色、蓝色三种主题，支持实时切换
- ⏱️ **翻卡式倒计时**：独特的翻卡动画效果，直观展示任务倒计时
- 📅 **灵活的任务设置**：支持每天、每周、每月循环任务
- 🔧 **任务管理**：方便的添加、删除、批量取消任务功能
- 📝 **完善的日志系统**：详细的操作日志记录，便于问题排查
- 🎯 **单一职责原则**：代码结构清晰，每个组件职责明确

## 技术栈

- **编程语言**：Python 3.8+
- **GUI框架**：PySide6 (Qt6)
- **数据库**：SQLite3
- **任务调度**：Windows Task Scheduler (win32com)
- **图标格式**：SVG矢量图标

## 安装说明

### 环境要求

- Python 3.8 或更高版本
- Windows 10/11 操作系统

### 安装步骤

1. 克隆项目到本地：
```bash
git clone https://github.com/bluehints/scheduled-shutdown.git
cd scheduled-shutdown
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行程序：
```bash
python main.py
```

## 使用指南

### 设置定时任务

1. 启动程序后，进入"设置任务"标签页
2. 选择执行时间（时:分）
3. 选择操作类型（关机/重启）
4. 选择循环方式：
   - 每天：每天在指定时间执行
   - 每周：选择星期几执行
   - 每月：选择每月的哪一天执行
5. 点击"添加任务"按钮

### 查看和管理任务

1. 切换到"查看任务"标签页
2. 查看所有已设置的任务列表
3. 点击"取消"按钮删除单个任务
4. 点击"取消全部任务"按钮批量删除所有任务

### 切换主题

1. 在主界面右上角找到主题下拉框
2. 选择想要的主题（浅色/深色/蓝色）
3. 界面会立即切换到新主题

### 倒计时显示

- 主界面顶部显示下次任务的倒计时
- 采用翻卡式动画效果，每秒更新
- 显示天、小时、分钟、秒

## 项目结构

```
scheduled-shutdown/
├── main.py                          # 程序入口
├── requirements.txt                 # 依赖列表
├── .gitignore                       # Git忽略文件
├── src/                             # 源代码目录
│   ├── core/                        # 核心模块
│   │   ├── config.py               # 配置文件
│   │   ├── logger.py               # 日志系统
│   │   ├── database.py             # 数据库管理
│   │   ├── theme_manager.py        # 主题管理器
│   │   ├── task_scheduler.py       # 任务调度器
│   │   └── task_logic.py           # 业务逻辑
│   └── ui/                          # UI模块
│       ├── main_window.py           # 主窗口
│       └── components/              # UI组件
│           ├── countdown_widget.py # 倒计时组件
│           ├── task_setup_widget.py # 任务设置组件
│           ├── task_list_widget.py  # 任务列表组件
│           ├── theme_switcher_widget.py # 主题切换组件
│           └── about_widget.py      # 关于页面组件
├── resources/                       # 资源文件
│   ├── themes/                      # 主题样式
│   │   ├── light.qss               # 浅色主题
│   │   ├── dark.qss                # 深色主题
│   │   └── blue.qss                # 蓝色主题
│   └── icons/                       # SVG图标
│       ├── arrow_down.svg
│       ├── arrow_up.svg
│       ├── shutdown.svg
│       ├── reboot.svg
│       ├── settings.svg
│       ├── clock.svg
│       ├── theme.svg
│       ├── cancel.svg
│       ├── check.svg
│       └── info.svg
└── docs/                            # 文档目录
    ├── architecture.md             # 架构设计文档
    ├── api.md                      # API文档
    ├── theme.md                    # 主题开发文档
    └── development.md              # 开发指南
```

## 版本历史

### v2.0.0 (2026-02-01)
- 全面UI/UX重构，采用圆角卡片式设计
- 新增多主题切换功能（浅色、深色、蓝色）
- 实现翻卡式倒计时动画效果
- 重构代码结构，遵循单一职责原则
- 添加完善的日志系统
- 所有图标采用SVG矢量格式

## 作者信息

**作者**：仲夏梦之夜  
**版本**：2.0.0  
**技术栈**：Python + PySide6 + SQLite3  
**设计风格**：圆角卡片式设计，支持多主题切换

## 许可证

本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进本项目。

## 致谢

感谢所有为本项目做出贡献的开发者。
