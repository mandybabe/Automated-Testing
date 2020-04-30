from xml.dom import minidom

# 打开xml文档
dom = minidom.parse('info.xml')

# 得到文档元素对象
root = dom.documentElement  # documentElement 用于得到XML文件的唯一根元素

# 每一个节点都有它的nodeName、nodeValue、nodeType等属性。
# nodeName为节点名称；nodeValue为节点的值；nodeType为节点的类型。
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

# 获得任意标签名
tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)

tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)

# 获得标签的属性值
logins = root.getElementsByTagName('login')

# 获得login标签的username属性值
username = logins[0].getAttribute("username")
print(username)

# 获得login标签的password属性值
password = logins[0].getAttribute("password")
print(password)

# 获得第二个login标签的username属性值
username = logins[1].getAttribute("username")
print(username)

# 获得第二个login标签的password属性值
password = logins[1].getAttribute("password")
print(password)

# 获得标签对之间的数据
provinces = dom.getElementsByTagName('province')
cities = dom.getElementsByTagName('city')

# 获得第二个province标签对的值
p2 = provinces[1].firstChild.data
print(p2)

# 获得第一个city标签对的值
c1 = cities[0].firstChild.data
print(c1)

# 获得第二个city标签对的值
c2 = cities[1].firstChild.data
print(c2)

# firstChild 属性返回被选节点的第一个子节点。data表示获取该节点的数据，它和WebDriver中提供的text方法类似。
