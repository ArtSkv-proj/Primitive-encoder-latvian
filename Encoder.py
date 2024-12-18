from tkinter import *
import os

# import re

# Atslēga.

key = {

"a":"b",
"b":"a",
"<":"ļ",
">":"č",
"ļ":"<",
"č":">",
"/":"%",
"%":"/",
"e":"ķ",
"ķ":"e",
"i":"ō",
"ō":"i",
"t":";",
";":"t",
"=":":",
":":"=",
" ":"#",
"#":" ",
"p":"r",
"r":"p",
"(":"1",
"1":"(",
")":"2",
"2":")",
"3":"-",
"-":"3",
".":"4",
"4":".",
"z":"§",
"§":"z",
"d":"ņ",
"ņ":"d",
"5":"n",
"n":"5"

}

# Izveido galveno Interfeisa elementu

dir_path = os.path.dirname(os.path.abspath(__file__))

window = Tk()
window.geometry("700x600")
window.title("Šifrēšanas rīks")
window.configure(bg="lightblue")



def create():
      # Atšifrē/Šifrē tekstu atkarībā no faila paplašinājuma.
            # Atrod failu no ievadītā nosaukuma.
            inputv = T.get("1.0", END).strip()
            for root, dirs, files in os.walk(dir_path):
                  if root == dir_path:
                        for file in files: 

                              if file.endswith(inputv):
                                    file_path = os.path.join(root, file)

                                    # Ja tāds ir, nokopē tā tekstu.

                                    with open(file_path, errors='ignore',encoding="utf-8") as f:
                                          cont = f.read()
                                          global FilePathMemo
                                          FilePathMemo = f

                                    # Ja pastāv paplašinājums .lvc, tekstu atšifrē.

                                    if file.endswith(".lvc"):
                                          transformed_text = ''
                                          for letter in cont:
                                                if letter in key:
                                                      transformed_text += key[letter]
                                                else:
                                                      transformed_text += letter

                                          global fulltextmemo 
                                          fulltextmemo = transformed_text

                                          # Meklē faila iepriekšējo paplašinājumu.

                                          for x in range(100):
                                                if transformed_text[len(transformed_text)-1-x] == ".":
                                                      transformed_text = transformed_text[:len(transformed_text)-1-x]
                                                      break

                                          # Izvada pārveidoto tekstu

                                          T2.config(state=NORMAL)
                                          T2.delete("1.0", END)
                                          T2.insert(END,transformed_text)
                                          T2.config(state=DISABLED)
                                          print(transformed_text)
                                    
                                    # Ja nepastāv tad šifrē

                                    else:

                                          # Šifrē tekstu.

                                          cont += FileType # Šifrētam tekstam klāt pieliek paplašinājumu, lai vēlak to var atgriezt tajā pašā formātā.
                                          transformed_text = ''
                                          for letter in cont:
                                                if letter in key:
                                                      transformed_text += key[letter]
                                                else:
                                                      transformed_text += letter

                                          # Izvada pārveidoto tekstu.

                                          T2.config(state=NORMAL)
                                          T2.delete("1.0", END)
                                          T2.insert(END,transformed_text)
                                          T2.config(state=DISABLED)
                                          print(transformed_text)

def labelcreate():

      # Printē izvēlētā faila tekstu iekš rāmja

           inputv = T.get("1.0", END).strip()
           for root, dirs, files in os.walk(dir_path):
                  for file in files: 
                        if file.endswith(inputv):
                              file_path = os.path.join(root, file)
                              root1, extension = os.path.splitext(file_path)

                              with open(file_path, 'r', errors='ignore',encoding="utf-8") as f:
                                    global FileType
                                    FileType = extension # Iegūst faila palašinājumu
                                    cont = f.read()
                                    T2.config(state=NORMAL)
                                    T2.delete("1.0", END)
                                    T2.insert(END, cont)
                                    T2.config(state=DISABLED)

def export():

      # Tiek izveidots jauns fails ar tekstu, kas ir iekš galvenā teksta rāmja.

      inputv = T2.get("1.0", END).strip()

      # Pārbauda vai ir iešifrēts.

      if FileType == ".lvc":
            inputv = fulltextmemo # nolasa tekstu no atmiņas

            # Sagatavo teksta paplašinājumu

            global exten
            exten = ""
            for x in range(100):
                  if inputv[len(inputv)-1-x] == ".":
                        for y in range(x+1):
                              exten += inputv[len(inputv)-1-x+y]
                        break

            name = str(os.path.splitext(FilePathMemo.name)[0])  # Sadala faila atrašanās vietas nosaukumu un izvēlas pēdējo vienību, kas ir faila nosaukums.
            
            # Pārbauda vai jau nav tāda faila, ja ir tad nosaukumā ievieto ciparu.

            if os.path.exists(name+exten):
                  max_number = "1"
                  number = ""

                  # Jaunā versija.

                  split_name = name.split("\\")
                  for root, dirs, files in os.walk(dir_path):
                        if root == dir_path:
                              for file in files: 
                                    file_name = file.split(".")
                                    file_name = file_name[0]
                                    if not file_name == "" and file_name.split("(")[0] == split_name[-1]:
                                          for x in range(1000):
                                                if file_name[len(file_name)-1-x] == "(":
                                                      for y in range(x+1):
                                                            print(file_name[len(file_name)-x+y])
                                                            if file_name[len(file_name)-x+y].isdigit():
                                                                  number = (f"{number}{file_name[len(file_name)-x+y]}")

                                                                  if int(number) > int(max_number):
                                                                        max_number = number
                                                            else:
                                                                  if int(number) > int(max_number):
                                                                        max_number = number
                                                                  break
                                                if (len(file_name)-1-x) == 1:
                                                      break
                                          number = ""
                              
                  max_number = int(max_number) + 1
                  f = open(name+f"({max_number})"+exten, "x",encoding="utf-8") # Izveido failu ar attiecīgo, lielāko skaitli.

                  # Izņem no teksta paplašinājumu.

                  for x in range(100):
                        if inputv[len(inputv)-1-x] == ".":
                              inputv = inputv[:len(inputv)-1-x]
                              break

                  f.write(inputv)

                  # Vecā versija, kura izmanto "re" moduli.

                  '''
                  pattern = re.compile(r"\(\d+\)$")
                  match = pattern.search(name+exten)
                  if match:
                        number = int(match.group(1)) +1
                  else:
                        number = 1
        
                  while os.path.exists(name+ f"({number})"+exten):
                        number += 1
                  f = open(name+f"({number})"+exten, "x")
        

                  for x in range(100):
                        if inputv[len(inputv)-1-x] == ".":
                              inputv = inputv[:len(inputv)-1-x]
                              break

                  f.write(inputv)
                  '''
            else:
            
                  # Tāda faila, nav tāpēc netiek lietots cipars

                  f = open(name+exten,"x",encoding="utf-8")
                  f.write(inputv)
      else:

            # Fails tika šifrēts un izveidots.

            f = open(str(os.path.splitext(FilePathMemo.name)[0])+".lvc","x",encoding="utf-8")
            f.write(inputv)



# Sagatavo tkinter interfeisa elementus

T = Text(window,height=5,width=10)

The_frame = Frame(window)

T2 = Text(The_frame, wrap=NONE)

S = Scrollbar(The_frame,orient=VERTICAL, command=T2.yview)
S2 = Scrollbar(The_frame,orient=HORIZONTAL,command=T2.xview)

S.pack(side=RIGHT, fill="y")
S2.pack(side=BOTTOM, fill="x")

The_frame.pack(expand=True,fill=BOTH)
T2.pack(expand=True,side=LEFT,fill=BOTH)






T2.config(yscrollcommand= S.set,xscrollcommand = S2.set, wrap= NONE)
T2.config(state=DISABLED)

T2.pack(fill = BOTH, expand=0)


T.pack()
Button(window, text="Lasīt", command=labelcreate).pack()
Button(window, text="Šifrēt/Atšifrēt", command=create).pack()
Button(window, text="Eksportēt", command=export).pack()

window.mainloop()
