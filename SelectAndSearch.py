# @Author   : 919106840638肖林航
# @time     : 2021/10/08 上午11:12
# @Software : PyCharm
import time
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog
from search import *
import os


class SelectAndSearch(object):
    def __init__(self, master=None):
        self.app = master
        self.app.geometry("1280x720")
        # 启动后创建组件
        self.create()

    def create(self):
        # 创建一个输入框
        img_path = tk.Entry(self.app, font=("宋体", 18), )
        # 顺序布局
        img_path.pack()
        # 坐标
        img_path.place(relx=0.15, rely=0.3, relwidth=0.6, relheight=0.1)

        # 参数是：要适应的窗口宽、高、Image.open后的图片
        # 调整尺寸
        def img_resize(w_box, h_box, pil_image):
            print(pil_image)
            # 获取图像的原始大小
            width, height = pil_image.size
            f1 = 1.0 * w_box / width
            f2 = 1.0 * h_box / height
            factor = min([f1, f2])
            width = int(width * factor)
            height = int(height * factor)
            # 更改图片尺寸，Image.ANTIALIAS：高质量
            return pil_image.resize((width, height), Image.ANTIALIAS)

        #  添加搜索图标
        img_s = Image.open('icon/search.png')
        img_s_resized = img_resize(0.05 * 1280, 0.1 * 720, img_s)
        self.img_s = ImageTk.PhotoImage(img_s_resized)
        lbs = tk.Label(self.app, imag=self.img_s, compound=tk.CENTER, bg='white')
        lbs.place(relx=0.1, rely=0.3, relwidth=0.05, relheight=0.1)

        #  添加图片图标
        img_t = Image.open('icon/picture.png')
        img_t_resized = img_resize(0.05 * 1280, 0.1 * 720, img_t)
        self.img_t = ImageTk.PhotoImage(img_t_resized)
        lbt = tk.Label(self.app, imag=self.img_t, compound=tk.CENTER, bg='#6888a8')
        lbt.place(relx=0.05, rely=0.05, relwidth=0.05, relheight=0.1)

        #  添加作者图标
        img_c = Image.open('icon/author.png')
        img_c_resized = img_resize(0.05 * 1280, 0.1 * 720, img_c)
        self.img_c = ImageTk.PhotoImage(img_c_resized)
        lbc = tk.Label(self.app, imag=self.img_c, compound=tk.CENTER, bg='#f4cf93')
        lbc.place(relx=0.7, rely=0.9, relwidth=0.05, relheight=0.1)

        #  标注作者姓名
        author = tk.Label(self.app, text="@作者：919106840638肖林航", font=("宋体", 15), bg="#f4cf93")
        author.place(relx=0.75, rely=0.9, relwidth=0.2, relheight=0.1)

        #  本地上传图标
        upload = tk.Button(self.app, text="选择图片", font=("宋体", 20), command=lambda: img_choose(img_path))
        upload.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.1)

        #  基于VGG特征检索
        enter_sift = tk.Button(self.app, text="搜索", font=("宋体", 20), command=lambda: enter())
        enter_sift.place(relx=0.8, rely=0.3, relwidth=0.1, relheight=0.1)

        #  选择图片
        def img_choose(img_path):
            # 打开文件管理器，选择图片
            self.app.picture = filedialog.askopenfilename(parent=self.app, initialdir=os.getcwd(), title="本地上传")
            # 同时将图片路径写入行内
            # img_path.delete(0,"end")
            img_path.insert(0, self.app.picture)
            # img_path[0] = self.app.picture

        #  根据输入框地址进行图像检索
        def enter():
            # 被检索的图像路径
            search_path = img_path.get()

            # 未选择图片，则不检索
            if (search_path == ''):
                return

            # 计算检索的耗时
            # 获取当前系统时间
            start = time.perf_counter()
            # 存储检索结果
            im_ls = searchByVgg(search_path)

            # 获取当前系统时间
            end = time.perf_counter()

            # 计算得到检索所用的总时间
            run_time = end - start
            print('检索时长:', run_time)

            # 获取相似度
            score = getScores()

            #  关闭主页面，创建结果界面
            self.app.destroy()
            result = tk.Tk()
            result.geometry("1280x720")
            result.title('查询结果')
            photo = tk.PhotoImage(file="icon/background.gif")  # 背景图片

            background = tk.Label(result, image=photo, compound=tk.CENTER)
            background.place(relx=0, rely=0, relwidth=1, relheight=1)

            backbutton = tk.Button(result, text="返回", font=("宋体", 25), command=lambda: back(result))
            backbutton.place(relx=0.8, rely=0.1, relwidth=0.08, relheight=0.08)

            word1 = tk.Label(result, text='被检索的图片：', font=("宋体", 25), image=photo, compound=tk.CENTER)
            word1.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.07)

            word2 = tk.Label(result, text='检索结果：', font=("宋体", 20), image=photo, compound=tk.CENTER)
            word2.place(relx=0.15, rely=0.4, relwidth=0.18, relheight=0.07)

            #  上传的图片
            img0 = Image.open(search_path)
            img0_resized = img_resize(0.3 * 1280, 0.3 * 720, img0)
            img0 = ImageTk.PhotoImage(img0_resized)
            lb0 = tk.Label(result, imag=img0, compound=tk.CENTER)
            lb0.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.3)

            #  十张检索结果图
            score1 = tk.Label(result, text='相似度：' + str(score[0]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score1.place(relx=0, rely=0.45, relwidth=0.19, relheight=0.07)
            img1 = Image.open(im_ls[0])
            img1_resized = img_resize(0.19 * 1280, 0.2 * 720, img1)
            img1 = ImageTk.PhotoImage(img1_resized)
            lb1 = tk.Label(result, imag=img1, compound=tk.CENTER)
            lb1.place(relx=0, rely=0.5, relwidth=0.19, relheight=0.2)

            score2 = tk.Label(result, text='相似度：' + str(score[1]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score2.place(relx=0.2, rely=0.45, relwidth=0.19, relheight=0.07)
            img2 = Image.open(im_ls[1])
            img2_resized = img_resize(0.19 * 1280, 0.2 * 720, img2)
            img2 = ImageTk.PhotoImage(img2_resized)
            lb2 = tk.Label(result, imag=img2, compound=tk.CENTER)
            lb2.place(relx=0.2, rely=0.5, relwidth=0.19, relheight=0.2)

            score3 = tk.Label(result, text='相似度：' + str(score[2]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score3.place(relx=0.4, rely=0.45, relwidth=0.19, relheight=0.07)
            img3 = Image.open(im_ls[2])
            img3_resized = img_resize(0.19 * 1280, 0.2 * 720, img3)
            img3 = ImageTk.PhotoImage(img3_resized)
            lb3 = tk.Label(result, imag=img3, compound=tk.CENTER)
            lb3.place(relx=0.4, rely=0.5, relwidth=0.19, relheight=0.2)

            score4 = tk.Label(result, text='相似度：' + str(score[3]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score4.place(relx=0.6, rely=0.45, relwidth=0.19, relheight=0.07)
            img4 = Image.open(im_ls[3])
            img4_resized = img_resize(0.19 * 1280, 0.2 * 720, img4)
            img4 = ImageTk.PhotoImage(img4_resized)
            lb4 = tk.Label(result, imag=img4, compound=tk.CENTER)
            lb4.place(relx=0.6, rely=0.5, relwidth=0.19, relheight=0.2)

            score5 = tk.Label(result, text='相似度：' + str(score[4]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score5.place(relx=0.8, rely=0.45, relwidth=0.19, relheight=0.07)
            img5 = Image.open(im_ls[4])
            img5_resized = img_resize(0.19 * 1280, 0.2 * 720, img5)
            img5 = ImageTk.PhotoImage(img5_resized)
            lb5 = tk.Label(result, imag=img5, compound=tk.CENTER)
            lb5.place(relx=0.8, rely=0.5, relwidth=0.19, relheight=0.2)

            score6 = tk.Label(result, text='相似度：' + str(score[5]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score6.place(relx=0, rely=0.7, relwidth=0.19, relheight=0.07)
            img6 = Image.open(im_ls[5])
            img6_resized = img_resize(0.19 * 1280, 0.2 * 720, img6)
            img6 = ImageTk.PhotoImage(img6_resized)
            lb6 = tk.Label(result, imag=img6, compound=tk.CENTER)
            lb6.place(relx=0, rely=0.75, relwidth=0.19, relheight=0.2)

            score7 = tk.Label(result, text='相似度：' + str(score[6]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score7.place(relx=0.2, rely=0.7, relwidth=0.19, relheight=0.07)
            img7 = Image.open(im_ls[6])
            img7_resized = img_resize(0.19 * 1280, 0.2 * 720, img7)
            img7 = ImageTk.PhotoImage(img7_resized)
            lb7 = tk.Label(result, imag=img7, compound=tk.CENTER)
            lb7.place(relx=0.2, rely=0.75, relwidth=0.19, relheight=0.2)

            score8 = tk.Label(result, text='相似度：' + str(score[7]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score8.place(relx=0.4, rely=0.7, relwidth=0.19, relheight=0.07)
            img8 = Image.open(im_ls[7])
            img8_resized = img_resize(0.19 * 1280, 0.2 * 720, img8)
            img8 = ImageTk.PhotoImage(img8_resized)
            lb8 = tk.Label(result, imag=img8, compound=tk.CENTER)
            lb8.place(relx=0.4, rely=0.75, relwidth=0.19, relheight=0.2)

            score9 = tk.Label(result, text='相似度：' + str(score[8]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score9.place(relx=0.6, rely=0.7, relwidth=0.19, relheight=0.07)
            img9 = Image.open(im_ls[8])
            img9_resized = img_resize(0.19 * 1280, 0.2 * 720, img9)
            img9 = ImageTk.PhotoImage(img9_resized)
            lb9 = tk.Label(result, imag=img9, compound=tk.CENTER)
            lb9.place(relx=0.6, rely=0.75, relwidth=0.19, relheight=0.2)

            score10 = tk.Label(result, text='相似度：' + str(score[9]), font=("宋体", 10), image=photo, compound=tk.CENTER)
            score10.place(relx=0.8, rely=0.7, relwidth=0.19, relheight=0.07)
            img10 = Image.open(im_ls[9])
            img10_resized = img_resize(0.19 * 1280, 0.2 * 720, img10)
            img10 = ImageTk.PhotoImage(img10_resized)
            lb10 = tk.Label(result, imag=img10, compound=tk.CENTER)
            lb10.place(relx=0.8, rely=0.75, relwidth=0.19, relheight=0.2)

            result.mainloop()

        #  返回按键
        def back(result):
            # 摧毁当前结果页面
            result.destroy()
            #  创建主界面
            app = tk.Tk()
            app.title('基于内容的图像检索（CBIR）')
            background = tk.PhotoImage(file="icon/background.gif")  # 背景图片

            #  添加背景和标题
            bg = tk.Label(app, image=background, compound=tk.CENTER)
            bg.place(relx=0, rely=0, relwidth=1, relheight=1)
            title = tk.Label(app, text='基于内容的图像检索（CBIR）', font=("宋体", 18), image=background, compound=tk.CENTER)
            title.place(relx=0.35, rely=0.2, relwidth=0.4, relheight=0.1)

            introduction = tk.Label(app, text='快速开始：点击“选择图片”->选择一张被检索的图片->点击“搜索”，\n'
                                              '即可检索出10张最相关的图片。', font=("宋体", 12), image=background,
                                    compound=tk.CENTER)
            introduction.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.15)

            SelectAndSearch(app)
            app.mainloop()
