import random
import time
import tkinter
import os
from fpdf import FPDF
import datetime
import pytz

def fibonacci():
    a = random.choice([i for i in range(-70, 70) if i not in [0]])
    d = random.choice([i for i in range(-70, 70) if i not in [0]])
    outlist = [a,d]
    for i in range(random.randint(5, 7)):
        outlist.append(outlist[i]+outlist[i+1])
    answer = outlist.pop()
    outlist.append("?")
    explanation = f"The first term is {a} and second is {d},it is a fibonacci series where sum of previous two numbers is equal to next number "
    return outlist,answer, explanation

def exponent():
    a = random.choice([i for i in range(-10,10) if i not in [0]])
    d = random.choice([i for i in range(-2,2) if i not in [0]])
    e = random.choice([2,3])
    outlist = []
    for i in range(random.randint(4, 5)):
        outlist.append((a+i*d)**e)
    answer = outlist.pop()
    outlist.append("?")
    explanation = f"The first term is {a},the common difference among base terms is {d} and the exponent is {e}"
    return outlist,answer ,explanation


def GP():
    a = random.choice([i for i in range(-100,100) if i not in [0]])
    d = random.choice([i for i in range(-10,10) if i not in [0]])
    outlist = []
    for i in range(random.randint(4, 5)):
        outlist.append(a * d **i)
    answer = outlist.pop()
    outlist.append("?")
    explanation = f"The first term is {a},the common product is {d} "
    return outlist,answer,explanation

def AP():
    a = random.choice([i for i in range(-1000,1000) if i not in [0]])
    d = random.choice([i for i in range(-100,100) if i not in [0]])
    outlist = []
    for i in range(random.randint(4,6)):
        outlist.append(a+i*d)
    answer = outlist.pop()
    outlist.append("?")
    explanation = f"The first term is {a},the common difference is {d} "
    return outlist,answer,explanation


def doubledifference():
    a = random.choice([i for i in range(-500, 500) if i not in [0]])
    b = random.choice([i for i in range(-30, 30) if i not in [0]])
    d = random.choice([i for i in range(-10, 10) if i not in [0]])
    outlist = []
    for i in range(1,random.randint(5, 7)):
        outlist.append(a +b*(i-1) + (d*(i-1)*(i-2))/2)
    answer = outlist.pop()
    outlist.append("?")
    explanation = f"The first term is {a},the common difference between the differences is {d} "
    return outlist,answer, explanation

def tripledifference():
    a = random.choice([i for i in range(-500, 500) if i not in [0]])
    b = random.choice([i for i in range(-30, 30) if i not in [0]])
    c = random.choice([i for i in range(-10, 10) if i not in [0]])
    d = random.choice([i for i in range(-5, 5) if i not in [0]])
    outlist = []
    for i in range(1, random.randint(6,8)):
        outlist.append(a + b * (i - 1) + (c * (i - 1) * (i - 2)) / 2 + (d * (i-1)*(i-2)*(i-3))/6)
    answer = outlist.pop()
    outlist.append("?")
    explanation = f"The first term is {a},the common difference between the differences of the differences is {d} "
    return outlist,answer, explanation

def Options(ans):
    Optionslist = []
    Optionslist.append(ans)
    for i in range(3):
        Optionslist.append(ans+(random.choice([i for i in range(-30,30) if i not in [0]])))

    random.shuffle(Optionslist)

    abcd = ["A.", "B.","C.","D."]
    index = Optionslist.index(ans)
    option=""
    if index==0:
        option="a"
    elif index==1:
        option="b"
    elif index==2:
        option="c"
    elif index==3:
        option="d"
    else:
        raise IndexError
    for i in range(4):
        Optionslist[i]=abcd[i]+str(Optionslist[i])

    return Optionslist,option


timelist = [0]

higheststreak = 0
localstreak = 0
nofcorrect=0
nofincorrect=0
rounds=0

def Play():
    global higheststreak
    global localstreak
    global nofcorrect
    global nofincorrect
    global rounds
    root = tkinter.Tk()
    root.title("Random Series Generator")
    root2 = tkinter.Tk()
    root2.title("Random Mat question generator")

    def GameLoop():


        timestart = time.time()

        r = random.randrange(6)
        if r == 0:
            outlist, answer, explanation = AP()

        elif r == 1:
            outlist, answer, explanation = GP()

        elif r == 2:
            outlist, answer, explanation = exponent()
        elif r == 3:
            outlist, answer, explanation = doubledifference()
        elif r == 4:
            outlist, answer, explanation = tripledifference()
        elif r == 5:
            outlist, answer, explanation = fibonacci()

        options,correct = Options(answer)



        l1 = tkinter.Label(root, text="RANDOM MAT QUESTION GENERATOR")
        l1.pack()
        l3 = tkinter.Label(root, text=f"Question-{rounds+1}")
        l3.pack()
        Q = ""
        for i in outlist:
            Q+=str(i)+"  ,  "
        Q = Q.removesuffix("  ,  ")
        l2 = tkinter.Label(root, text=Q)
        l2.pack()

        def clickA():
            global higheststreak
            global localstreak
            global nofcorrect
            global nofincorrect
            global rounds

            rounds +=1
            t = time.time() - timestart
            timelist.append(round(t, 2))
            for widgets in root.winfo_children():
                widgets.destroy()
            if correct.lower() == "a":
                localstreak +=1

                nofcorrect +=1
                if localstreak > higheststreak:
                    higheststreak = localstreak



            else:
                localstreak=0
                nofincorrect += 1


            GameLoop()


        a = tkinter.Button(root, text=options[0], command=clickA)
        a.pack()

        def clickB():
            global higheststreak
            global localstreak
            global nofcorrect
            global nofincorrect
            global rounds
            rounds += 1
            t = time.time() - timestart
            timelist.append(round(t, 2))
            for widgets in root.winfo_children():
                widgets.destroy()
            if correct.lower() == "b":
                localstreak += 1

                nofcorrect += 1
                if localstreak > higheststreak:
                    higheststreak = localstreak

            else:
                localstreak = 0
                nofincorrect += 1


            GameLoop()

        b = tkinter.Button(root, text=options[1], command=clickB)
        b.pack()

        def clickC():
            global higheststreak
            global localstreak
            global nofcorrect
            global nofincorrect
            global rounds
            rounds += 1
            t = time.time() - timestart
            timelist.append(round(t, 2))
            for widgets in root.winfo_children():
                widgets.destroy()
            if correct.lower() == "c":
                localstreak += 1

                nofcorrect += 1
                if localstreak > higheststreak:
                    higheststreak = localstreak

            else:
                localstreak = 0
                nofincorrect += 1


            GameLoop()

        c = tkinter.Button(root, text=options[2], command=clickC)
        c.pack()

        def clickD():
            global higheststreak
            global localstreak
            global nofcorrect
            global nofincorrect
            global rounds
            rounds += 1
            t = time.time() - timestart
            timelist.append(round(t, 2))
            for widgets in root.winfo_children():
                widgets.destroy()
            if correct.lower() == "d":
                localstreak += 1

                nofcorrect += 1
                if localstreak > higheststreak:
                    higheststreak = localstreak

            else:
                localstreak = 0
                nofincorrect += 1


            GameLoop()

        d = tkinter.Button(root, text=options[3], command=clickD)
        d.pack()

        t1="Incorrect-",nofincorrect
        l3 = tkinter.Label(root,text=t1)
        l3.pack()

        t2 = "Correct-", nofcorrect
        l4 = tkinter.Label(root, text=t2)
        l4.pack()

        t3 = "Highest Streak-", higheststreak
        l5 = tkinter.Label(root, text=t3)
        l5.pack()

        t4 = "Current streak-", localstreak
        l5 = tkinter.Label(root, text=t4)
        l5.pack()

        l6 = tkinter.Label(root, text=f"Time taken for previous question-{timelist.pop()}s")
        l6.pack()
    def Newfile():
        t1 = tkinter.Label(root2,text="Number of questions in Sheet")
        t1.pack()
        e1 = tkinter.Entry(root2)
        e1.pack()
        t2 = tkinter.Label(root2, text="Number of Sheets")
        t2.pack()
        e2 = tkinter.Entry(root2)
        e2.pack()
        t3 = tkinter.Label(root2, text="Name of each sheet")
        t3.pack()
        e3 = tkinter.Entry(root2)
        e3.insert(0,"QuestionPaper")
        e3.pack()
        def clickb1():
            currentdate = str(datetime.date.today())
            currenttime = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour) + "-" + str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).minute)+"-"+str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).second)
            currentdatetime= 'QuestionPapers'+currentdate+"_"+currenttime
            parent_dir = 'C:/Users/user/Desktop/MatQuestionPapers/'
            newdir = os.path.join(parent_dir,currentdatetime)
            os.mkdir(newdir)
            newrawfolder = str(newdir)+"/rawdata"
            os.mkdir(newrawfolder)
            newanswerfolder = str(newdir)+"/answers"
            os.mkdir(newanswerfolder)
            name = str(e3.get())
            for i in range(int(e2.get())):
                file = open(f"{newrawfolder}/{name+str(i+1)}.txt",'w+')
                answerkey = open(f"{newanswerfolder}/{e3.get() + str(i+1)}_AnswerKey.txt", 'w+')
                answerlist=[]

                for x in range(int(e1.get())):
                    r = random.randrange(6)
                    if r == 0:
                        outlist, answer, explanation = AP()

                    elif r == 1:
                        outlist, answer, explanation = GP()

                    elif r == 2:
                        outlist, answer, explanation = exponent()
                    elif r == 3:
                        outlist, answer, explanation = doubledifference()
                    elif r == 4:
                        outlist, answer, explanation = tripledifference()
                    elif r == 5:
                        outlist, answer, explanation = fibonacci()

                    options, correct = Options(answer)
                    answerlist.append(correct)
                    Q = ""
                    for p in outlist:
                        Q += str(p) + "  ,  "
                    Q = f"Q{x+1}) "+Q.removesuffix("  ,  ")
                    optionline = "     "+str(options[0])+"     "+str(options[1])+"     "+str(options[2])+"     "+str(options[3])
                    questiontotal = f"{Q}\n{optionline}\n\n"
                    file.write(questiontotal)
                for u in range(int(e1.get())):
                    answerkey.write(f"{u+1}){answerlist[u]}\n")
                file.close()
                file = open(f"{newrawfolder}/{name + str(i + 1)}.txt", 'r')
                pdf=FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=15)
                pdf.cell(200, 10, txt=f"MAT Question Paper {i+1}", ln=1,align="C")
                pdf.cell(200, 10, txt="", ln=2, align="C")
                for y in file:

                    pdf.cell(200,10,txt = y,ln=1)
                pdf.output(f"{newdir}/{name}{str(i+1)}.pdf",'F')

                answerkey.close()

        b1 = tkinter.Button(root2,text="Go",command=clickb1)
        b1.pack()


    GameLoop()
    Newfile()

    root.mainloop()
    root2.mainloop()



Play()