# Python-PluginFramework
这一个轻量级的模块化开发框架

更新时间：2019/7/17

### 功能
* 动态加载目录里的模块文件
* 通过代码加载模块

### 框架项目结构
* Project
    * main.py
    * Plugin
        * pluginmanager.py
        * MyPlugin1
          * MyPlugin1.py
          * Resources
            * nesting.py
        * MyPlugin2
          * MyPlugin2.py
          * Resources
            * nesting.py        
        * ...


### 使用方法
 * 动态加载目录方法： 
 
      * 将 pluginmanager.py 导入项目中，建立好相关文件夹后把模块文件放入其中。
     
      *  模块文件名与文件夹名一致，并在模块文件内编写一个class 名为模块名的
    
      *  例如： PathTest 模块。
     
     ###### 目录结构：
     * Project
        * main.py
        * TestPlugin
            * pluginmanager.py
            * PathTest
              * PathTest.py
              * Resources
                * logo.jpg
                * my.mp3
     ###### main.py 代码：
     ```python
     #! /usr/bin/python3
     # -*- coding:utf-8 -*-

     from TestPlugin.pluginmanager import pluginManager                #导入框架主类文件
     from TestPlugin.pluginmanager import pluginError                  #导入框架异常类文件
     
     MyPlugin = pluginManager()                                        #实例化框架主文件
     successPath,failPath =  MyPlugin.addPathPlugin("TestPlugin")      #执行加载模块目录，返回 [成功目录,失败目录及原因]
     print("加载成功模块目录： " +  str(successPath) )
     print("加载失败模块目录： " +  failPath.dir + "失败原因：" +  failPath.content)
     try:
        MyPlugin.test.Fun()                                           #调用模块里的方法
     except pluginError as Error:                                     #没有此模块
        print(Error)
     except AttributeError as Error:                                   #此模块里没有所调用的方法
        print(str(Error))
     
     ```  
     
     ###### text.py 代码：
     ```python
     class test:
        def __init__(self):
            print(" test 初始化 ")
        def Fun(self):
            print("hello World")
            
     if __name__ != "__main__":
         print("我test被加载了")
     ```
  * 通过代码加载模块：
  
      * 实例化对象，并定义模块名称与对象放到 dict 类型里
      
      * 例如： cordPlugin.py
      ###### 目录结构：
     * Project
        * main.py
        
        * cordPlugin.py
        
        * pluginmanager.py
    


