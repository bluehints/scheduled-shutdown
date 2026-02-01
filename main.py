#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定时任务管理器 - 主程序入口
作者：仲夏梦之夜
"""

import sys
import ctypes
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from src.core.logger import setup_logger, logger
from src.ui.main_window import MainWindow
from src.core.config import APP_NAME


def main():
    logger.info(f"{APP_NAME} 启动中...")
    
    app = QApplication(sys.argv)
    
    app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("scheduledshutdown.timer")
    
    window = MainWindow()
    window.show()
    
    logger.info(f"{APP_NAME} 启动成功")
    sys.exit(app.exec())


if __name__ == '__main__':
    main()