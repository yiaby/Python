"""
 고객 정보 관리 시스템 구축(메뉴방식)
"""
import tkinter
from tkinter import Tk, Menu, Frame, PanedWindow, ttk, messagebox, filedialog
from tkinter.ttk import Labelframe, Label, Entry, Button
import tkinter.font as tkFont


def refreshTreeview(data_list):
    deleteTreeData()
    refreshTreeData(data_list)

def deleteTreeData():
    children = tree.get_children()  #get_children()함수는 표의 하위 항목을 반환한다.

    if children !='0':
        for item in children:
            tree.delete(item)
def refreshTreeData(data_list):
    #enumerate()함수는 기본적으로 인덱스와 요소로 이루어진 튜플을 만들어 준다.
    for i, item in enumerate(data_list):
        tree.insert('', 'end', iid='IID%d' %(i), values=item)

    entry_name.delete(0,'end')
    entry_phone.delete(0,'end')
    entry_email.delete(0,'end')
seq = 0
def inputEvtHandler():
        print("추가...")
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()

        if name == "" or phone == "" or email == "":
            messagebox.showinfo('알림', '이름, 전화번호, 이메일을 모두 입력 하세요!!')
            return
        # [중요] 함수 안에서 전역변수의 값을 변경하려면 반드시 global로 선언해야 한다.
        global seq
        seq += 1
        # [주의] append()함수 안의 인자 개수는 반드시 하나 여야하낟. 그래서 괄호로 묶어주자!!
        data_list.append((seq, name, phone, email))

        refreshTreeview(data_list)
        # end inputEvtHandler()
def modifyEvtHandler():
    print('수정...')
    sname = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if sname == ''or phone == '' or email == '':
        messagebox.showinfo('알림', '이름, 전화번호, 이메일을 모두 입력 하세요!!')
        return

    idx = -1
    for i, data in enumerate(data_list):
        try:
            if data.index(sname) != -1:
                data_list[i] = (data[0],sname,phone,email)
                refreshTreeview(data_list)
                idx = i
            return
        except:
            pass
    if idx == -1:
        messagebox.showinfo('경고', '찾는 정보가 없습니다.')
# pickle 모듈을 불러온다.
import pickle
def saveEvtHandler():
  print("파일 저장...")
  with open('data_list.pickle','wb')as fw:
      pickle.dump(data_list,fw) # dump(객체, 파일객체)
def loadEvtHandler():
   print("파일 열기...")
   global data_list
   with open('data_list.pickle','rb')as fr:
       data_list = pickle.load(fr)
       refreshTreeview(data_list)
       seq = data_list[len(data_list)-1][0]


win = Tk()
win.title("고객 정보 관리 시스템")
win.geometry('%dx%d+%d+%d'%(800,600,10,10)) # '%dx%d' => '넓이 X 높이'

menubar = Menu(win) #메뉴 객체
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='열기', command=loadEvtHandler)
filemenu.add_command(label='저장', command=saveEvtHandler)
filemenu.add_separator()# 줄넣기
filemenu.add_command(label='닫기', command=win.destroy)


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='help', menu=helpmenu)
helpmenu.add_command(label='About...')

win.config(menu=menubar)

topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100)

panedwindow = PanedWindow(relief='raised',bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=200, height=400,)

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=470, bd=2)

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(win)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=30)

#lefrFrame에 Entry위젯 추가
lable_frame = Labelframe(leftFrame,text='기본 정보 입력')
lable_frame.pack()

lbl_name = Label(lable_frame,text='이름')
lbl_phone = Label(lable_frame,text='전화번호')
lbl_email = Label(lable_frame,text='이메일')

entry_name = Entry(lable_frame)
entry_phone = Entry(lable_frame)
entry_email = Entry(lable_frame)

lbl_name.grid(row=0,column=0)
entry_name.grid(row=0,column=1,padx=5,pady=5)

lbl_phone.grid(row=1,column=0)
entry_phone.grid(row=1,column=1,padx=5,pady=5)

lbl_email.grid(row=2,column=0)
entry_email.grid(row=2,column=1,padx=5,pady=5)

#rightFrame에 목록 추가하기
headerList = ['No','Name','PhoneNumber','E-mail']
data_list =[]

#Treeview는 그리드표를 출력하는데 유용한 위젯이다.
tree = ttk.Treeview(rightFrame,columns=headerList,show='headings')
tree.pack()

for i, col in enumerate(headerList):
    tree.heading(col,text=col.title())
for i, item in enumerate(data_list):
    tree.inserttree.insert('', 'end', iid='IID%d' %(i), values=item)

#Treeview의 각 필드 너비 설정
tree.column(0,width=50)
tree.column(1,width=80)
tree.column(2,width=150)
tree.column(3,width=250)

#treeview높이 설정
tree.config(height=22)

def click_item(event):
    selectedItem = tree.focus()
    getValue = tree.item(selectedItem).get('values')

    if len(entry_name.get()) > 0:entry_name.delete(0,'end')
    if len(entry_phone.get()) > 0: entry_phone.delete(0, 'end')
    if len(entry_email.get()) > 0: entry_email.delete(0, 'end')

    entry_name.insert(0,getValue[1])
    entry_phone.insert(0,getValue,[2])
    entry_email.insert(0,getValue,[3])

    tree.bind('<ButtonRelease-1>',click_item)

panedwindow = PanedWindow(bottomFrame, relief='raised',bd=0)
panedwindow.pack()

btn_output = Button(panedwindow, text='전체보기')
btn_input = Button(panedwindow, text='추가', command=inputEvtHandler)
btn_search = Button(panedwindow, text='검색')
btn_modify = Button(panedwindow, text='수정', command=modifyEvtHandler)
btn_delete = Button(panedwindow, text='삭제')

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)


  #앱 타이트 라벨 추가
fontStyle = tkFont.Font(family='궁서체', size =28)
lbl_title = Label(topFrame,text='고객 정보 관리 시스템', font = fontStyle)
lbl_title.place(relx=0.5,rely=0.5,anchor='center')


win.config(menu=menubar)
if __name__=='__main__': #메인 함수 선언, 시작을 의미함,
    #생성한 윈도우 내부에서 수행되는 마우스 클릭 같은 이벤트들이 발생하게금 유지해주는 함수이다.
 win.mainloop()
