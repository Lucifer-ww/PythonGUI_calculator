#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/22 17:49
# @Author : Empirefree
# @File : 制作计算器.py
# @Software: PyCharm Community Edition

import wx
from math import *

class Calculator(wx.Frame):

    #删除一个字符并显示在text中
    def OnDel(self, event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)


    #清空text和等式
    def OnAc(self, event):
        self.textprint.Clear()
        self.equation = ""


    #开始计算,除了^运算符号外
    def OnTarget(self, event):
        string = self.equation
        if '^' in string:
            string = string.replace('^', '**')
        try:
            target = eval(string)   #转化为列表
            self.equation += '\n' + str(target)  #计算值
            string = self.equation
            self.equation = ""
            self.textprint.SetValue(string)  #显示在text中

        except SyntaxError:
            dlg = wx.MessageDialog(self, '您语法错误！！！', '请注意',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()


    #运算符和数字：每一个按钮就是一个事件，对应text加上不同的值
    def OnAppend(self, event):
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)


    #删除、清空、求值（与其他按钮不同）
    def createHandler(self, button, labels):
        #根据不同按钮的值调用不同的方法
        if labels == '删除':
            self.Bind(wx.EVT_BUTTON, self.OnDel, button)
        elif labels == '清空':
            self.Bind(wx.EVT_BUTTON, self.OnAc, button)
        elif labels == '=':
            self.Bind(wx.EVT_BUTTON, self.OnTarget, button)
        else:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, button)
    def __init__(self):

        wx.Frame.__init__(self, None, -1, 'Empirefree', size=(350, 480), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        #设置图标
        self.icon1 = wx.Icon(name="ava.ico",  type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon1)

        #设置背景图片
        image_file = 'background.jpg'
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
        image_width = to_bmp_image.GetWidth()
        image_height = to_bmp_image.GetHeight()

        #垂直布局并部署表格
        boxsize = wx.BoxSizer(wx.VERTICAL)
        gridBox = wx.GridSizer(rows = 6, cols = 5, hgap = 7, vgap = 7)

        #按钮的相关布局
        self.equation = ""  #记录等式
        self.textprint = wx.TextCtrl(panel, -1, '',  style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.buttonData = "log2 sqrt ln pi 删除 sin cos tan e / 7 8 9 % * 4 5 6 ^ - 1 2 3 ) + 清空 0 . ( =".split()
        buttonlength = len(self.buttonData)
        for i in range(buttonlength):
            labels = "%s" % self.buttonData[i]         # 存入labels中，与下面的createHandler相对应
            buttonIterm = wx.Button(panel, i, labels, size=(63, 52))
            self.createHandler(buttonIterm, labels)
            gridBox.Add(buttonIterm, 0, 0)
        boxsize.Add(self.textprint, 1, wx.EXPAND)
        boxsize.Add(gridBox, 5, wx.EXPAND)
        panel.SetSizerAndFit(boxsize)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Calculator()
    # 持续性显示Frame框架
    frame.Show()
    app.MainLoop()