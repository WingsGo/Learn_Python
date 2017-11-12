#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'WingC'

import multiprocessing as mp
import threading as th
import quite,logging;logging.basicConfig(level=logging.WARNING)
from PySide.QtCore import Signal,QObject

#Signal必须定义在继承自QObject的类方法中
class SignalWrapper(QObject):
    signal = Signal(object)

class main_ui(quite.DialogUiController):
    def __init__(self,parent=None):
        super().__init__(parent,'send.ui')
        self.queue = mp.Queue()
        self.button('test').clicked.connect(self.start_slave_ui)
        self.button('test2').clicked.connect(self.send_data)

    def start_slave_ui(self):
        process = mp.Process(target=slave_ui.class_exec,args=(self.queue,))     #在slave_ui构造时传入queue作为参数进行进程间通信
        process.start()

    def send_data(self):
        value = self.__get_widget__('edit','send').toPlainText()
        self.queue.put(value)

class slave_ui(quite.DialogUiController):
    def __init__(self,queue,parent=None):
        super().__init__(parent,'receive.ui')
        self.new_data_signal = SignalWrapper()
        self.new_data_signal.signal.connect(self.show_data)

        def check_data():
            while True:
                try:
                    if not queue.empty():
                        new_data = queue.get()
                        self.new_data_signal.signal.emit(new_data)
                except BaseException as e:
                    logging.warning("Queue Error %s" % e)

        if queue is not None:
            th.Thread(target=check_data,daemon=True).start()

    def show_data(self,data):
        self.__get_widget__('edit','receive').append(data)

if __name__ == '__main__':
    main_ui.class_exec()

