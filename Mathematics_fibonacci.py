from tkinter import*

root=Tk()

root.title('Finbonacci series')
root.geometry('400x400')

label_series = Label(root, text="Fibonacci series")
label_sum = Label(root, text="Fibonacci sum:")

def Fibonacci():
    num = 10
    first_no = 1
    second_no = 1
    sum = 0 
    counter = 1 
    while(counter <= num):
        label_series['text'] += str(sum)+" "
        counter = counter + 1
        first_no+second_no
        second_no = sum 
        sum = first_no + second_no
        label_sum['text'] = "Fibonacci Sum : "+str(sum2)
        
        
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_series.pack()
label_sum()
        