from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def enable():
    # 활성화
    enable = checkstate.get()
    if enable == 1:
        #버튼누르면 PowerSeries combobox 활성화
        PowerSelect.configure(state='enable')
        pass

def Apply():
    Doping_result_list = []
    Effort_result_list = []
    total = []
    Effort_dictionary = {}
    Doping_dictionary = {}

    # dictionary 형태로 Entry 값 가져오기
    Effort_dictionary['H'] = int(H_Value.get())
    Effort_dictionary['A'] = int(A_Value.get())
    Effort_dictionary['B'] = int(B_Value.get())
    Effort_dictionary['C'] = int(C_Value.get())
    Effort_dictionary['D'] = int(D_Value.get())
    Effort_dictionary['S'] = int(S_Value.get())

    effort_result = 0
    for i in Effort_dictionary:
        effort_result += Effort_dictionary[i]     
    
    if effort_result > 510:
        messagebox.showwarning("Warning", "Effort setting value cannot exceed 510. ")
    
    for i in Effort_dictionary:
        Effort_result_list.append(Effort_dictionary[i])

    # dictionary 형태로 Combobox의 값 가져오기
    Doping_dictionary['Hp'] = int(hp_count.get())
    Doping_dictionary['Pr'] = int(protein_count.get())
    Doping_dictionary['Ir'] = int(iron_count.get())
    Doping_dictionary['Cal'] = int(calcium_count.get())
    Doping_dictionary['Zi'] = int(zinc_count.get())
    Doping_dictionary['Car'] = int(carbos_count.get())

    # 도핑약 사용수 * 10
    for i in Doping_dictionary:
        Doping_result_list.append(Doping_dictionary[i] * 10)

    # effort setting 값에서 도핑약 사용수 빼기 단, 둘을 뺀 값이 0보다 작을때 값 저장 멈춤
    for i in range(len(Effort_result_list)):
        total.append(Effort_result_list[i] - Doping_result_list[i])    
        if total[i] < 0:
            messagebox.showwarning("Warning", "The total cannot be less than 0.")
            break



root = Tk()
root.title('Effort Value Calculator')
root.geometry('394x171+750+350')
root.resizable(False, False)

#Effort Setting Frame
EffortFrame = LabelFrame(root, text='Effort Value', padx=13, pady=3)
EffortFrame.place(x=14 , y=3)

H = Label(EffortFrame, text='H ', pady=3).grid(row=0, column=0)
H_Value = Entry(EffortFrame, width=4)
H_Value.bind(Apply)
H_Value.grid(row=0, column=1)

A = Label(EffortFrame, text=' A ', pady=3).grid(row=0, column=2)
A_Value = Entry(EffortFrame, width=4)
A_Value.bind(Apply)
A_Value.grid(row=0, column=3)

B = Label(EffortFrame, text='  B ', pady=3).grid(row=0, column=4)
B_Value = Entry(EffortFrame, width=4)
B_Value.bind(Apply)
B_Value.grid(row=0, column=5)

C = Label(EffortFrame, text='  C ', pady=3).grid(row=0, column=6)
C_Value = Entry(EffortFrame, width=4)
C_Value.bind(Apply)
C_Value.grid(row=0, column=7)

D = Label(EffortFrame, text='  D ', pady=3).grid(row=0, column=8)
D_Value = Entry(EffortFrame, width=4)
D_Value.bind(Apply)
D_Value.grid(row=0, column=9)

S = Label(EffortFrame, text='  S ', pady=3).grid(row=0, column=10)
S_Value = Entry(EffortFrame, width=4)
S_Value.bind(Apply)
S_Value.grid(row=0, column=11)


# Tool
PowerFrame = LabelFrame(root, text='Tool', padx=20, pady=3)
PowerFrame.place(x=14, y=56)
PowerSeries = ['Weight', 'Bracer', 'Belt', 'Lens', 'Band', 'Anklet']

PowerSelect = Combobox(PowerFrame, values=PowerSeries, height=6, state='disabled', width=7)
PowerSelect.current(0)
PowerSelect.grid(row=0, column=0)

checkstate = IntVar()
checkenable = BooleanVar()
PowerSelectEnable = Checkbutton(PowerFrame, variable=checkstate ,command=enable).grid(row=0, column=1)

MachoBrace = Label(PowerFrame, text='Macho Brace').grid(row=1, column=0)
MachoBraceChoice = Checkbutton(PowerFrame).grid(row=1, column=1)

#Doping Frame
DopingFrame = LabelFrame(root, text='Doping', padx=10, pady=5)
DopingFrame.place(x=165, y=56)
count = [0,1,2,3,4,5,6,7,8,9,10]

hp = Label(DopingFrame, text='HP Up ', pady=3).grid(row=0, column=0)
hp_count = Combobox(DopingFrame, height=11, values=count, width=3, state='readonly')
hp_count.current(0)
hp_count.grid(row=0, column=1)

protein = Label(DopingFrame, text=' Protein ', pady=3).grid(row=0, column=2)
protein_count = Combobox(DopingFrame, height=11, values=count, width=3, state='readonly')
protein_count.current(0)
protein_count.grid(row=0, column=3)

iron = Label(DopingFrame, text='Iron ', pady=3).grid(row=1, column=0)
iron_count = Combobox(DopingFrame, height=11, values=count, width=3, state='readonly')
iron_count.current(0)
iron_count.grid(row=1, column=1)

calcium = Label(DopingFrame, text=' Calcium ', pady=3).grid(row=1, column=2)
calcium_count = Combobox(DopingFrame, height=11, values=count, width=3, state='readonly')
calcium_count.current(0)
calcium_count.grid(row=1, column=3)

zinc = Label(DopingFrame, text='Zinc ', pady=3).grid(row=2, column=0)
zinc_count = Combobox(DopingFrame, height=11, values=count, width=3, state='readonly')
zinc_count.current(0)
zinc_count.grid(row=2, column=1)

carbos = Label(DopingFrame, text=' Carbos ', pady=3).grid(row=2, column=2)
carbos_count = Combobox(DopingFrame, height=11, values=count, width=3, state='readonly')
carbos_count.current(0)
carbos_count.grid(row=2, column=3)


#Apply and Reset Button
reset = Button(root, text='Reset', padx=18).place(x=13, y=133)
confirm = Button(root, text='Confirm', padx=10, command=Apply).place(x=88, y=133)

#Effort apply Button

root.mainloop()