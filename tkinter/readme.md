参考连接1：https://www.jianshu.com/p/91844c5bca78

# 控件
## 常用控件
控件 | 名称 | 作用
---|---|---
Button |按钮|	单击触发事件
Canvas	|画布|	绘制图形或绘制特殊控件
Checkbutton	|复选框|	多项选择
Entry	|输入框|	接收单行文本输入
Frame	|框架|	用于控件分组
Label	|标签|	单行文本显示
Lisbox	|列表框|	显示文本列表
Menu	|菜单|	创建菜单命令
Message	|消息|	多行文本标签，与Label 用法类似
Radiobutton	|单选按钮|	从互斥的多个选项中做单项选择
Scale	|滑块|	默认垂直方向，鼠标拖动改变数值形成可视化交互
Scrollbar	|滑动条|	默认垂直方向，课鼠标拖动改变数值，可与 Text、Lisbox、Canvas等控件配合移动可视化空间
Text	|文本框|	接收或输出显示多行文本
Toplevel	|新建窗体容器|	在顶层创建新窗体

## 控件的共同属性
通常包括尺寸、颜色、字体、相对位置、浮雕样式、图标样式和悬停光标形状等共同属性

属性 | 说明 | 取值
---|---|---
anchor	|文本起始位置|	CENTER(默认)，E,S,W,N,NE,SE,SW,NW
bg	|背景色|	无
bd	|加粗|(默认 2 像素)	无
bitmap	|黑白二值图标|	网上查找
cursor	|鼠标悬停光标|	网上查找
font	|字体|	无
fg	|前景色|	无
height	|高(单位为行)|	无
width	|宽(单位为行)|	无
image	|显示图像|	无
justify	|多行文本的对其方式|	CENTER(默认),LEFT,RIGHT,TOP,BOTTOM
padx	|水平扩展像素|	无
pady	|垂直扩展像素|	无
relief	|3D浮雕样式|	FLAT(平的);RAISED(凸起的);SUNKEN(凹陷的);GROOVE(沟槽状边缘);和RIDGE(脊状边缘) 
state	|控件实例状态是否可用|	NORMAL(默认),DISABLED

## 控件布局
控件的布局通常有pack()、grid() 和 place() 三种方法

### pack()
是一种简单的布局方法，如果不加参数的默认方式，将按布局语句的==先后==，以==最小占用空间==的方式==自上而下==地排列控件实例，并且保持控件本身的==最小尺寸==。

