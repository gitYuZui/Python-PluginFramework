
import os,sys

#插件化(静态 + 动态)
class pluginManager(): 

    #当前的插件
    __Plugin = {}
 
    #初始化时静态注册插件
    def __init__(self):
        pass
    
    def __str__(self):
        return str(self.__class__)

    def __getattr__(self, key):
        if self.hasPlugin(key):
            return self.__Plugin[key]
        else:
            raise pluginError("pluginManager","__getattr__","{} not exists".format(key))

    #添加目录插件
    def addPathPlugin(self, PATH):
        PATH = os.path.join(sys.path[0],PATH)           #转为当前main文件所在的目录
        successPath = []                                #记录成功模块
        fail = []                                       #记录失败模块
        if not os.path.exists(PATH):
            raise pluginError("PluginManager", "addPathPlugin", "{} are not exists".format(PATH) )
        #遍历循环目录
        for pathList in os.listdir(PATH):                #返回文件与文件夹的目录
            pathDir = os.path.join(PATH,pathList)
            if os.path.isdir(pathDir) and pathList[0]!="." and pathList[0]!="_":  #过滤不加载的目录文件 
                workClass = pathDir.split("\\")[-1]      #文件所在的文件夹为class名
                modePath = os.path.join(pathDir,workClass)
                if os.path.isfile( modePath + ".py" ):
                    sys.path.append(pathDir)
                    objMode = __import__( workClass )
                    objClass =  getattr(objMode, workClass,None)  #获取class类
                    if objClass == None:
                        fail.append({'dir':pathDir,'content':"This file ({}) does not have a class named {}.".format(modePath,workClass)})
                    else:
                        obj =  objClass()                   #实例化对象
                        self.addPlugin( **{workClass:obj} )
                        successPath.append(modePath)
                else:
                    fail.append({'dir':pathDir,'content':"Not existent {}.py file".format(modePath) })
        return successPath,fail
    
    #添加插件
    def addPlugin(self, **plugin):
        if type(plugin) != dict:
            raise pluginError("PluginManager", "addPlugin", "Parameter are not dict.")
        for key,value in plugin.items():
            if self.hasPlugin(key):
                raise pluginError("PluginManager", "addPlugin", "Plugin name exists.")
            else:
                self.__Plugin.update( {key:value})

    #获取插件集合
    def getAllPlugin(self):
        return self.__Plugin

    #删除指定创建，成功返回插件聚合，失败报异常
    def delPlugin(self,key):
        if self.hasPlugin(key):
            del self.__Plugin[key]
            return True
        else:
            return False
            #raise pluginError("PluginManager", "delPlugin", "{} are not exists.".format( key))

    #查看插件是否存在
    def hasPlugin(self,key):
        if key in self.__Plugin:
            return True
        else:
            return False

#异常类
class pluginError(Exception):
    __ErrorData = {}
    def __init__(self, className,funName,Content):
        super().__init__(className,funName,Content)
        self.__ErrorData = {"className":className,"funName":funName,"Content":Content}
    def __str__(self):
        return str(self.__ErrorData)


