#! /usr/bin/python3
# -*- coding:utf-8 -*-

from TestPlugin.pluginmanager import pluginManager 
from TestPlugin.pluginmanager import pluginError 
from cordPlugin import cordPlugin                             #通过代码载入模块

MyPlugin = pluginManager()

if __name__ == "__main__":
    
    cordPlugin1 = cordPlugin('模块1')
    cordPlugin2 = cordPlugin('模块2')

    MyPlugin.addPlugin( **{"cord1":cordPlugin1,"cord2":cordPlugin2 })  # 代码载入方式

    successPath,fail =  MyPlugin.addPathPlugin("TestPlugin")           # 载入TestPlugin目录里的模块
    print ("动态加载成功目录： {}".format( str(successPath)))
    [print("加载失败模块目录： {} 失败原因：{} ".format( failList['dir'], failList['content'] )) for failList in fail]
    

    if  MyPlugin.hasPlugin('cord1'):                                    #查看模块是否存在
        MyPlugin.cord1.test()
        status =  MyPlugin.delPlugin('cord1')                           #删除模块
        print("删除状态：%s" % status)
                                       
    try:
        MyPlugin.cord2.test() 
        
        MyPlugin.Plu_1.test()
        MyPlugin.Plu_2.test()
    except pluginError as Error:
        print(Error)
    except AttributeError as Error:
        print(str(Error))

    allPlugin = MyPlugin.getAllPlugin()
    print("当前所有的模块：%s" % str( allPlugin ))
