# Python-PluginFramework
这一个轻量级的模块化开发框架

更新时间：2019/7/17

### 版本
python3+

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
 
      *  将 pluginmanager.py 导入项目中，建立好相关文件夹后把模块文件放入其中。
     
      *  模块文件名与文件夹名一致，并在要在模块文件内编写一个 class 名为模块名
    
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

     from TestPlugin.pluginmanager import pluginManager                #框架模块
     from TestPlugin.pluginmanager import pluginError                  #框架异常处理模块

     MyPlugin = pluginManager()                                        #实例化框架模块
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
      
      * 例如： cordPlugin 模块
      ###### 目录结构：
     * Project
        * main.py
        
        * cordPlugin.py
        
        * pluginmanager.py
      ###### main 代码：
      ```python
      #! /usr/bin/python3
      # -*- coding:utf-8 -*-
      from Plugin.pluginmanager import pluginManager 
      from Plugin.pluginmanager import pluginError 
      import cordPlugin
      
      if __name__ == "__main__":
         MyPlugin = pluginManager()
         cordPlugin1 = cordPlugin.staticPlugin('我是模块1')                     #实例化第一个模块
         cordPlugin2 = cordPlugin.staticPlugin('我是模块2')                     #实例化第二个模块
         
         MyPlugin.addPlugin( **{"cord1":cordPlugin1,"cord2":cordPlugin2 } ) #将模块的实例化加载到框架里
         try:
            MyPlugin.cord1.test()                                          #调用模块里的方法
            MyPlugin.cord2.test()
         except pluginError as Error:                                      #没有此模块
             print(Error)
         except AttributeError as Error:                                   #此模块里没有所调用的方法
             print(str(Error))
    
      ```
      ###### cordPlugin 代码：
      ```python
      class cordPlugin:
          def __init__(self,name):
              self.name = name

          def test(self):
              print("我是用代码导入的模块 %s" % self.name)
      
      ```
      
      
      
### 结束语

欢迎大佬们来技术交流 QQ：1170941265

