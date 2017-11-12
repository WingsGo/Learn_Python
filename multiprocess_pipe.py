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
        self.button('test').clicked.connect(self.start_slave_ui)
        self.button('test2').clicked.connect(self.send_data)
        self.receiver,self.sender = mp.Pipe(duplex=False)           #单向通信

    def start_slave_ui(self):
        process = mp.Process(target=slave_ui.class_exec,args=(self.receiver,))
        process.start()

    def send_data(self):
        send_data = self.__get_widget__('edit','send').toPlainText()
        self.sender.send(send_data)

class slave_ui(quite.DialogUiController):
    def __init__(self,pipe_receive,parent=None):
        super().__init__(parent,'receive.ui')
        self.receive_signal = SignalWrapper()
        self.receive_signal.signal.connect(self.show_data)

        def check_data():
            while True:
                try:
                    new_data = pipe_receive.recv()
                    self.receive_signal.signal.emit(new_data)
                except BaseException as e:
                    logging.warning("Pipe Error %s" % e)
        if pipe_receive is not None:
            th.Thread(target=check_data,daemon=True).start()        #启动守护线程监听信号

    def show_data(self,data):
        self.__get_widget__('edit','receive').append(data)

if __name__ == '__main__':
    main_ui.class_exec()
