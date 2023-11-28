import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def t2list2lists(list):
    list1=[]
    list2=[]
    for i in list:
        list1.append(i[0])
        list2.append(i[1])
    return list1,list2

def barplot(frame, x, y, plot_dict):
    list1,list2 = t2list2lists(plot_dict)
    fig=plt.Figure(figsize=(6, 4))
    ax=fig.add_axes([0.15, 0.1, 0.75, 0.75])
    ax.bar(list1, list2)
    ax.set_title("Character Frequency")
    ax.set_ylabel("Frequency", fontsize = 14)
    chart_type = FigureCanvasTkAgg(fig, frame.label)
    chart_type.get_tk_widget().grid(column = x, columnspan = 10, row = y, rowspan = 9, padx = 5, pady = 5)
    plt.show()

def wordsplit(str_input):
    letters = []
    index = 0
    for letter in str_input:
        if index!= 0 and index%5 == 0:
            letters.append(" ")
        if letter == " ":
            continue
        index+=1
        letters.append(letter)
    return ''.join(letters)