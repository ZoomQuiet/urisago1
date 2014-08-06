欢迎进入 金山卫士开源计划 !

在这里你可以接触到中国最专业的安全类软件源代码;
你可以自由的使用／研究／修订／再发布 这些代码以及延伸作品;

进一步的详细信息请访问:
  http://code.ijinshan.com/


#   URIsA ~ 在线网址安全性查询服务

## 概述
基于 http://code.ijinshan.com/api/devmore4.html 服务,包装为更加易用的在线RESTful 服务
进一步的:

    +-- 提供 FireFox 插件
    +-- 提供 Chrome 插件
    +-- 提供 本地批量扫描脚本
    +-- ...


## 发布

### http://urisago1.appsp0t.com

当前接口:

http://urisago1.appsp0t.com
    
- POST 想查询的 URL
- 从金山云安全服务 返回是否安全


    usage:
        $ curl -d "uri=http://sina.com" urisago1.appsp0t.com/chk
    or with GAE Datastore quick resp. if ahd checked:
        $ curl -d "uri=http://sina.com" urisago1.appsp0t.com/qchk



