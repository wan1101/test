import time
import pywinauto
from PIL import Image
from pywinauto import mouse
from pywinauto.application import Application
#
app = Application('uia').start(r"D:\程序\DingDing\main\current\DingTalk.exe")  # 或者钉钉的可执行文件路径
a=Application('uia').connect(process=18300)

main_window = a["钉钉"]
if main_window.get_show_state() != 1:
    main_window.maximize()
    mouse.click(coords=(20, 100))
mouse.click(coords=(165, 55))
mouse.click(coords=(400, 55))
mouse.click(coords=(400, 120))
s=main_window["ListBox"]

s.children()[-2].capture_as_image().save("打卡.png")
main_window.close()

from pywinauto.keyboard import SendKeys


class WChat:
    def __init__(self):
        Application('uia').start(r"D:\WeChat\WeChat.exe")
        self.conn = Application('uia').connect(process=3792)
        self.dlg = self.conn.window(class_name='WeChatMainWndForPC')


    # 搜索用户名称
    def sarch_with(self,name,txt):
        self.dlg.child_window(title="搜索", control_type="Edit").click_input()
        self.dlg.child_window(title="搜索", control_type="Edit").type_keys(name)
        time.sleep(1)
        self.dlg.child_window(title_re=name, control_type="ListItem").wrapper_object()[0].click_input()
        time.sleep(1)
        self.dlg.child_window(title_re=name, control_type="Edit").click_input()
        time.sleep(1)
        self.dlg.child_window(title_re=name, control_type="Edit").type_keys(txt)
        time.sleep(1)
        self.dlg.child_window(title='发送(S)', control_type="Button").click_input()

    def Top_with(self, name, txt):
        self.dlg.child_window(title="聊天", control_type="Button").click_input()
        time.sleep(1)
        self.dlg.child_window(title="会话", control_type="List").children()
        self.dlg.child_window(title_re=name,control_type="ListItem").click_input()
        time.sleep(1)
        self.dlg.child_window(title_re=name, control_type="Edit").click_input()
        self.dlg.child_window(title_re=name, control_type="Edit").type_keys(txt)
        self.dlg.child_window(title_re='发送文件', control_type="Button").click_input()

        time.sleep(1)
        self.dlg.child_window(title='打开', control_type="Window")

        self.dlg.child_window(title_re='此电脑', control_type="SplitButton").click_input()
        time.sleep(1)
        self.dlg.child_window(title="文件名(N):", auto_id="1148", control_type="ComboBox").draw_outline(colour="red")

        self.dlg.child_window(title="文件名(N):", auto_id="1148", control_type="Edit").type_keys(r"D:\PYTHON\Pyside2\UI_EXE\打卡.png")

        self.dlg.child_window(title="打开(O)", auto_id="1", control_type="SplitButton").click_input()
        # self.dlg.print_control_identifiers()

        SendKeys("{ENTER}")
        self.dlg.child_window(title='发送(S)', control_type="Button").click_input()


#
WChat().Top_with('Marlboro','今日打卡：')


