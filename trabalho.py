import tkinter
def calculo(entrada, estados, estado_inicial, estado_final, alfabeto, regras, estado_presente):
    for i in range(len(entrada)):
        try:
            if entrada[i] not in alfabeto:
                return 'simbolo desconhecido'
            else:
                print(str(estado_presente) + " recebe " + str(entrada[i]) + " -> " + str(regras[(estado_presente, entrada[i])]))
                regras[(estado_presente, entrada[i])]
        except:
            return 'Entrada sem transicao'
            continue
        else:
            estado_presente = regras[(estado_presente, entrada[i])]

    if estado_presente == estado_final:
        return 'ACEITA'
    else:
        return 'REJEITA'

i=0
def interface():
    m=tkinter.Tk()
    tkinter.Label(m, text='entrada').grid(row=0)
    tkinter.Label(m, text='estados').grid(row=1)
    tkinter.Label(m, text='estado_inicial').grid(row=2)
    tkinter.Label(m, text='estado_final').grid(row=3)
    tkinter.Label(m, text='alfabeto').grid(row=4)
 
    e1 = tkinter.Entry(m)
    e2 = tkinter.Entry(m)
    e3 = tkinter.Entry(m)
    e4 = tkinter.Entry(m)
    e5 = tkinter.Entry(m)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    def ver():
        temp = {}
        for x in e6:
            sep = x.get().split(":")
            sep2= sep[0].split(",")
            d={(sep2[0],sep2[1]):sep[1]}
            temp.update(d)
        tkinter.Label(m, text=calculo(e1.get(),e2.get().split(","),e3.get(),e4.get(),e5.get().split(","),temp,e3.get())).grid(row=6+i)
    e6 = []
    def addRegra():
        global i
        i=i+1
        tkinter.Label(m, text='regra').grid(row=5+i,column=0)
        e6.append(tkinter.Entry(m))
        e6[i].grid(row=i+5, column = 1)
        button = tkinter.Button(m, text='add',  command=addRegra).grid(row=5+i,column=2)
    e6.append(tkinter.Entry(m))
    tkinter.Label(m, text='regra').grid(row=5+i,column=0)
    e6[i].grid(row=i+5, column = 1)
    button = tkinter.Button(m, text='add',  command=addRegra).grid(row=5+i,column=2)

    button = tkinter.Button(m, text='Verificar',  command=ver).grid(row=80+i)

    m.mainloop()


interface()
