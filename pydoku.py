# Pydoku
# 2020 Sebastian Salazar

# Brute Force, still fast and fun
# Cool GUI for input
# Based on Computerphile approach
# On the future, you could also check if there is less than 17 inputs, in which 
# case no sudoku can be solved (proved by MIT)


if __name__ == '__main__':

    import tkinter as tk
    from tkinter import messagebox
    import numpy as np
    import itertools

    entries = []
    grid_to_colour = []


    def input_window():
        global entries
        
        master = tk.Tk()
        master.title("Input")
        master.attributes("-topmost", True)     # for the window to be in top of others

        w = tk.Canvas(master, width=404, height=444)
        w.pack()

        def thin_line(x1, y1, x2, y2):
            w.create_line(x1, y1, x2, y2, fill="black")

        def wide_line(x1, y1, x2, y2):
            w.create_line(x1, y1, x2, y2, fill="black", width= 3)

        #Draw thin lines
        #draw the verticals
        for x in range(52, 380, 44):
            thin_line(x,10,x,404)

        #draw the horizontals
        for y in range(52, 380, 44):
            thin_line(10,y,400,y)

        #Draw wide lines
        #draw the verticals
        for x in range(120 + 20, 360 + 20, 120 + 12):
            wide_line(x,10,x,404)

        #draw the horizontals
        for y in range(120 + 20, 360 + 20, 120 + 12):
            wide_line(10,y,400,y)


        #Now the entry boxes
        for a in range(30, 130*3, 44):
            for b in range(30, 130*3, 44):
                large_font = ('Verdana',24)

                entry1Var = tk.StringVar()
                temp = tk.Entry(master,textvariable=entry1Var,font=large_font, width=1, borderwidth = 0, highlightthickness = 0)
                w.create_window(b, a, window=temp)
                #b and a are swapped to follow the solver logic
                entries.append(temp)

        #Text and button
        Label_pydoku = tk.Label(master, text="Pydoku", font=('Helvetica', 22, 'bold'))
        w.create_window(52, 425, window=Label_pydoku)

        Label_seb = tk.Label(master, text="by Seb Salazar", font=('Helvetica', 14))
        w.create_window(150, 427, window=Label_seb)

        def buttonAction():
            #global master
            getInputs()
            master.destroy()
            solver()


        solveButton = tk.Button(master, text = "Solve", command = buttonAction)
        solveButton.configure(width = 10, activebackground = "#33B5E5")
        solveButton_window = w.create_window(300, 427, window=solveButton)


        master.mainloop()



    # get inputs and prepare the solution

    grid_output = []

    def getInputs():
        global grid_output
        global grid_to_colour
        wrongChecker = 0

        if all(elements.get() == "" for elements in entries):
            wrongChecker += 1

        else:

            for element in entries:
                if isinstance(element.get(), str) and not element.get().isdigit() and element.get()!= "" :
                    wrongChecker += 1


        if wrongChecker != 0:
            showMsg()

        else:
            grid_input = []
            for input in range(9):
                grid_input.append([entries[input*9 + increment].get() for increment in range(9)])

            #transform all "" in 0's
            for row in grid_input:
                row_new = map(lambda x: 0 if x == "" else (int(x) if 0<int(x)<10 else showMsg()), row)
                grid_output.append(list(row_new))



        # To colour the answer
        flatten = itertools.chain.from_iterable
        grid_to_colour = tuple(flatten(grid_output[:]))




    def showMsg():
        messagebox.showinfo("Error", "Input a number, from 1 to 9")

    
    '''
    #"The hardest one there is" (according to Google Search)
    grid_output = [[0,0,5,3,0,0,0,0,0],
        [8,0,0,0,0,0,0,2,0],
        [0,7,0,0,1,0,5,0,0],
        [4,0,0,0,0,5,3,0,0],
        [0,1,0,0,7,0,0,0,6],
        [0,0,3,2,0,0,0,8,0],
        [0,6,0,5,0,0,0,0,9],
        [0,0,4,0,0,0,0,3,0],
        [0,0,0,0,0,9,7,0,0]
        ]
    '''

    def isPossible(y,x,n):
        global grid_output
        for i in range(0,9):
            if grid_output[y][i] == n:
                return False
        for i in range(0,9) :
            if grid_output[i][x] == n:
                return False
        x0 = (x//3)*3   #floor division
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if grid_output[y0+i][x0+j] == n:
                    return False
        return True



    def solver():
        #new_window()
        global grid_output
        for y in range(9):
            for x in range(9):
                if grid_output[y][x] == 0:
                    for n in range(1,10):
                        if isPossible(y,x,n):
                            grid_output[y][x] = n
                            solver()
                            grid_output[y][x] = 0
                            
                    return
        print(np.matrix(grid_output))

        # To wait for solver to respond
        output_window()
        #input("Want more")
        #raw_input("Want more")
        

    #window to display the solution
    
    def output_window():
        global solution
        global grid_to_colour

        flatten = itertools.chain.from_iterable
        solution = list(flatten(grid_output))


        master = tk.Tk()
        master.title("Solution")
        master.attributes("-topmost", True)    

        w = tk.Canvas(master, width=404, height=444)
        w.pack()

        def thin_line(x1, y1, x2, y2):
            w.create_line(x1, y1, x2, y2, fill="black")

        def wide_line(x1, y1, x2, y2):
            w.create_line(x1, y1, x2, y2, fill="black", width= 3)

        #Draw thin lines
        #draw the verticals
        for x in range(52, 380, 44):
            thin_line(x,10,x,404)

        #draw the horizontals
        for y in range(52, 380, 44):
            thin_line(10,y,400,y)

        #Draw wide lines
        #draw the verticals
        for x in range(120 + 20, 360 + 20, 120 + 12):
            wide_line(x,10,x,404)

        #draw the horizontals
        for y in range(120 + 20, 360 + 20, 120 + 12):
            wide_line(10,y,400,y)

        labels = []

        #Now the display boxes
        for a in range(30, 130*3, 44):
            for b in range(30, 130*3, 44):
                large_font = ('Verdana',24)

               
                temp = tk.Label(master,font=large_font, width=1, borderwidth = 0, highlightthickness = 0)
                w.create_window(b, a, window=temp)
                #b and a are swapped to follow the solver logic
                labels.append(temp)

        #Text and button
        Label_pydoku = tk.Label(master, text="Pydoku", font=('Helvetica', 22, 'bold'))
        w.create_window(52, 425, window=Label_pydoku)

        Label_seb = tk.Label(master, text="by Seb Salazar", font=('Helvetica', 14))
        w.create_window(150, 427, window=Label_seb)


        for i in range(81):
            labels[i]['text'] = str(solution[i])
            if grid_to_colour[i] == 0:
                labels[i]['text'] = str(solution[i])
                labels[i].config(fg="red")
            

        master.mainloop()

    
    input_window()
