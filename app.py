# @Author   : 919106840638肖林航
# @time     : 2021/10/08 上午09:30
# @Software : PyCharm

from SelectAndSearch import *

#  创建主界面
app = tk.Tk()
app.title('基于内容的图像检索（CBIR）')
background = tk.PhotoImage(file="icon/background.gif")  # 背景图片
#  添加背景和标题
bg = tk.Label(app, image=background, compound=tk.CENTER, bg="#989cb8")
bg.place(relx=0, rely=0, relwidth=1, relheight=1)
title = tk.Label(app, text='基于内容的图像检索（CBIR）', font=("宋体", 18), image=background, compound=tk.CENTER)
title.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.1)

introduction = tk.Label(app, text='快速开始：点击“选择图片”->选择一张被检索的图片->点击“搜索”，\n'
                                  '即可检索出10张最相关的图片。', font=("宋体", 12), image=background, compound=tk.CENTER)
introduction.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.15)

SelectAndSearch(app)
app.mainloop()
