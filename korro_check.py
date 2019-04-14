"""

Мэйн создает форму.

"""



import tkinter



def chek_korro():

    """

    Функция высчитывает 6 и 7 колонку книги КОРРО. Проверяет валидность полученых значений.

    """

    #Warning for incorrect input

    try:

        obig_a = float(ENTRY_OBIG.get())

        pdv_a = float(ENTRY_PDV.get())

        zbir_a = float(ENTRY_ZBIR.get())

    except (TypeError, ValueError):

        RESULT_6["text"] = "Только цифры!"

        RESULT_7["text"] = "Разделение точкой!"

        CHECK_R_6["fg"] = 'black'

        CHECK_R_7["fg"] = 'black'

    #Count result

    pdv_and_zbir = pdv_a + zbir_a

    RESULT_6["text"] = round(obig_a - pdv_and_zbir, 2)

    RESULT_7["text"] = round(obig_a - zbir_a, 2)

    #Check result for 6

    if abs((obig_a - pdv_and_zbir) * 0.2 - pdv_a) <= 0.0049:#Allow difference up to 0.5 cent 

        CHECK_R_6["text"], CHECK_R_6["fg"] = 'Пройдено', 'black'

    else:

        CHECK_R_6["text"], CHECK_R_6["fg"] = 'НЕ ПРОЙДЕНО', 'red'

    #Check result for 7

    if abs((obig_a - zbir_a) * 0.05 - zbir_a) <= 0.0049:#Allow difference up to 0.5 cent 

        CHECK_R_7["text"], CHECK_R_7["fg"] = 'Пройдено', 'black'

    else:

        CHECK_R_7["text"], CHECK_R_7["fg"] = 'НЕ ПРОЙДЕНО', 'red'





WINDOW = tkinter.Tk()



##Definition

#Input

LABKE_OBIG = tkinter.Label(WINDOW, text="Оборот А: ")

LABLE_PDV = tkinter.Label(WINDOW, text="ПДВ А: ")

LABLE_ZBIR = tkinter.Label(WINDOW, text="Сбор А: ")

#Output lable

LABLE_K6 = tkinter.Label(WINDOW, text="Колонка 6: ")

LABLE_CHECK_6 = tkinter.Label(WINDOW, text="Проверка:")

LABLE_K7 = tkinter.Label(WINDOW, text="Колонка 7: ")

LABLE_CHECK_7 = tkinter.Label(WINDOW, text="Проверка:")

#Output result

RESULT_6 = tkinter.Label(WINDOW)

CHECK_R_6 = tkinter.Label(WINDOW)

RESULT_7 = tkinter.Label(WINDOW)

CHECK_R_7 = tkinter.Label(WINDOW)

#Input data

ENTRY_OBIG = tkinter.Entry(WINDOW)

ENTRY_PDV = tkinter.Entry(WINDOW)

ENTRY_ZBIR = tkinter.Entry(WINDOW)



#Execute button

BUTTOM_EXECUTE = tkinter.Button(WINDOW, text="Расчитать!", command=chek_korro)



##Grid

#Input

LABKE_OBIG.grid(row=0, column=0)

LABLE_PDV.grid(row=1, column=0)

LABLE_ZBIR.grid(row=2, column=0)

#Output lable

LABLE_K6.grid(row=4, column=0)

LABLE_CHECK_6.grid(row=5, column=0)

LABLE_K7.grid(row=6, column=0)

LABLE_CHECK_7.grid(row=7, column=0)

#Output result

RESULT_6.grid(row=4, column=1)

CHECK_R_6.grid(row=5, column=1)

RESULT_7.grid(row=6, column=1)

CHECK_R_7.grid(row=7, column=1)

#Input data

ENTRY_OBIG.grid(row=0, column=1)

ENTRY_PDV.grid(row=1, column=1)

ENTRY_ZBIR.grid(row=2, column=1)

#Execute button

BUTTOM_EXECUTE.grid(row=3, column=1)



#Run

WINDOW.mainloop()
