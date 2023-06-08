import random
import tkinter as tk
import project2

#opt format (
# color of the background ,
# color of the obj ,
# font size )
d_background = '#4234be'
d_obj = 'white'
d_size = 30

main_window=None

def fond(surf,color = d_background):
    surf.configure(bg=color)

def text(surf,tx : str = "implement",packt = True,opt=(d_background,d_obj,d_size)):
    x=tk.Label(surf,bg=opt[0],text=tx,font=('Calibri', opt[2]),fg=opt[1])
    if packt:
        x.pack()
    return x

def bouton(surf,tx : str = "implement",callback : callable = lambda:print("callback to implement"),packt = True,opt=(d_background,d_obj,d_size)):
    fb = tk.Frame(surf, bg=opt[0])
    fb.pack()
    x =tk.Button(fb,text=tx, font=('Calibri', opt[2]), bg=opt[0], fg=opt[1], command=callback)
    if packt:
        x.pack()
    return x

def entry(surf,default="",packt = True):
    x = tk.Entry(surf,font=('Calibri',d_size))
    x.insert(tk.END,default)
    if packt:
        x.pack()
    return x

def clear(surf):
    try:
        for widgets in surf.winfo_children():
            widgets.pack_forget()
            widgets.destroy()
    except Exception:
        pass
    surf.pack_forget()
    surf.destroy()
    x= tk.Frame(maine)
    fond(x)
    x.pack()
    return x

def menu_final(surf,score,ma):
    surf = clear(surf)
    text(surf,f"\n\nvotre score est {str(score)} / {ma}")
    bouton(surf,"retour en arrière",lambda:main(surf))

def menu_play(surf : tk.Frame,quest : dict,pages =None,page : int=None,score : int=None,reponse : list = None):
    surf.pack_forget()
    surf = clear(tk.Frame())
    text(surf,"QCM")

    def init(quest : dict):
        f = quest.items()
        f = list(f)
        random.shuffle(f)
        ma = len(f) % 5
        #ajoute de text fantome pour que les question sont un multiple de 5
        if ma != 0:
            x = 5 - ma
            for x in range(x+1):
                f.append(("",{"type":-1}))
        ret = []
        for n in range(0,len(f)-1,5):
            di = {f[n][0]:f[n][1]}
            for x in range(n,n+5):
                di[f[x][0]] = f[x][1]
            ret.append(di)
        return ret
    
    def verificate(surf,r : list,quest : dict,score):
        text(surf,"correction")
        for typ,fun,rep in r:
            inp : str= fun()
            inp = inp.strip()
            if typ == -1:
                pass
            elif typ == 0:
                if inp == rep:
                    score =+1
            elif typ == 1:
                if inp == rep:
                    score =+1
            elif typ == 2:
                if inp in rep:
                    score =+1
            else:
                raise RuntimeError(typ)
        for x in range(5):
            f = tk.Frame(surf)
            f.configure(borderwidth=5)
            fond(f)
            f.pack()
            question = list(quest.keys())[x]
            if isinstance(quest[question]["correct"],list):
                text(f,question,packt=False).pack(side=tk.RIGHT)
                text(f,"".join([quest[question]["reponse"][x] for x in quest[question]["correct"][0] ]),packt=False).pack(side=tk.LEFT)
            else:
                text(f,question,packt=False).pack(side=tk.RIGHT)
                text(f,quest[question]["reponse"][quest[question]["correct"]],packt=False).pack(side=tk.LEFT)
        return score

    def ask(syr,l : dict):
        surf = syr
        ret = []
        #ret in type , func to get , rep 
        for question,dic in l.items():
            if dic["type"] == -1:
                #text
                text(surf,question) if question else 0
                ret.append((-1,0,0))
            elif dic["type"] == 0:
                #réponse libre
                f = tk.Frame(surf)
                f.pack()
                text(f,question,packt=False).pack(side=tk.LEFT)
                e = entry(f,packt=False)
                e.pack(side=tk.RIGHT)
                ret.append((0,lambda:e.get(),dic["reponse"][0]))
            elif dic["type"] == 1:
                #réponse seul
                f = tk.Frame(surf)
                f.pack()
                text(f,question,packt=False).pack(side=tk.TOP)
                var = tk.StringVar()
                for index , tx in enumerate(dic["reponse"]):
                    tk.Radiobutton(f,text=tx,value=tx,variable=var,font=('Calibri',d_size)).pack(side= tk.LEFT if index > 2 else tk.RIGHT)
                ret.append((1,lambda: var.get(),dic["reponse"]))
            elif dic["type"] == 2:
                # reponse multiple dic["correct"] est une list de possibiliter de combinaison de réponse
                # techniquemenet marche
                f = tk.Frame(surf)
                f.pack(fill=tk.X)
                text(f,question,packt=False).pack(side=tk.TOP)
                ret.append(2,lambda:"",[[dic["reponse"][y] for y in x] for x in dic["correct"]])
            else:
                raise
        return ret
    
    #logic
    if not pages:
        #we just started there in no order so prepare
        score = 0
        reponse = False
        page = 0
        pages = init(quest)

    if page == len(pages):
        menu_final(surf,score,len(quest.keys()))
        return None
    
    text(surf,f"page {page}/{len(pages)-1}")
    
    if reponse:
        verificate(surf,reponse,pages[page],score)
        bouton(surf,"page suivante",lambda:menu_play(surf,quest,pages,page+1,score,False))
    else:
        reponse = ask(surf,pages[page])
        bouton(surf,"valider",lambda:menu_play(surf,quest,pages,page,score,reponse))
    
    bouton(surf,"retour en arrière",lambda:main(surf))
    return None

def menu_im(surf):
    surf = clear(surf)
    text(surf,"\n")
    y = entry(surf,"input.json")
    bouton(surf,"importer un test" ,lambda : menu_play(surf,project2.js(y)))
    text(surf,"\ntest aléatoire")
    text(surf,"nombre de question")
    x = entry(surf,"10")
    text(surf,"\n")
    bouton(surf,"confirmer",lambda:menu_play(surf,project2.gen(x.get())))
    bouton(surf,"retour en arrière",lambda:main(surf))

def menu_gen(surf):
    surf = clear(surf)
    bouton(surf,"retour en arrière",lambda:main(surf))

def menu_ex(surf):
    surf = clear(surf)
    bouton(surf,"retour en arrière",lambda:main(surf))
    #menu_gen(surf)

def main(surf):
    #écrand main
    surf = clear(surf)
    fond(surf)
    text(surf,"\n")
    text(surf,"générateur de QCM")
    text(surf,"\n")
    bouton(surf,"passer un test",lambda: menu_im(surf))
    text(surf,"\n")
    bouton(surf,"faire un test",lambda: menu_ex(surf))

if __name__ == "__main__":
    #Afichage fenêtre
    maine = tk.Tk()
    maine.title("QCM") 
    maine.geometry("1500x720")
    maine.minsize(1500, 520)
    main_window = tk.Frame(maine)
    main_window.pack()
    fond(maine)
    main(main_window)
    maine.mainloop()