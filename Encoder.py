from tkinter import *
import os
import sys
import re

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
"t":"§",
"§":"t",
"=":"¦",
"¦":"=",
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
"4":"."

}


dir_path = os.path.dirname(os.path.abspath(__file__))

window = Tk()
window.geometry("700x600")



def create():
            inputv = T.get("1.0", END).strip()
            for root, dirs, files in os.walk(dir_path):
                  if root == dir_path:
                        for file in files: 

                              if file.endswith(inputv):
                                    file_path = os.path.join(root, file)
                                    with open(file_path) as f:
                                          cont = f.read()
                                          global FilePathMemo
                                          FilePathMemo = f

                                    if file.endswith(".lvc"):
                                          transformed_text = ''
                                          for letter in cont:
                                                if letter in key:
                                                      transformed_text += key[letter]
                                                else:
                                                      transformed_text += letter

                                          global fulltextmemo 
                                          fulltextmemo = transformed_text

                                          for x in range(100):
                                                if transformed_text[len(transformed_text)-1-x] == ".":
                                                      transformed_text = transformed_text[:len(transformed_text)-1-x]
                                                      break

                                          T2.config(state=NORMAL)
                                          T2.delete("1.0", END)
                                          T2.insert(END,transformed_text)
                                          T2.config(state=DISABLED)
                                          print(transformed_text)
                                    else:
                                          cont += FileType
                                          transformed_text = ''
                                          for letter in cont:
                                                if letter in key:
                                                      transformed_text += key[letter]
                                                else:
                                                      transformed_text += letter
                                          T2.config(state=NORMAL)
                                          T2.delete("1.0", END)
                                          T2.insert(END,transformed_text)
                                          T2.config(state=DISABLED)
                                          print(transformed_text)

def labelcreate():
      # No multiple file support
           inputv = T.get("1.0", END).strip()
           for root, dirs, files in os.walk(dir_path):
                  for file in files: 
                        if file.endswith(inputv):
                              file_path = os.path.join(root, file)
                              root1, extension = os.path.splitext(file_path)
                              with open(file_path) as f:
                                    global FileType
                                    FileType = extension
                                    cont = f.read()
                                    T2.config(state=NORMAL)
                                    T2.delete("1.0", END)
                                    T2.insert(END, cont)
                                    T2.config(state=DISABLED)

def export():
      inputv = T2.get("1.0", END).strip()
      if FileType == ".lvc":
            inputv = fulltextmemo
            global exten
            exten = ""
            for x in range(100):
                  if inputv[len(inputv)-1-x] == ".":
                        for y in range(x+1):
                              exten += inputv[len(inputv)-1-x+y]
                        break
            name = str(os.path.splitext(FilePathMemo.name)[0])
            if os.path.exists(name+exten):
                  max_number = "1"
                  number = ""
                  # Vajadzētu pārtaisīt šo daļu

                  # new
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
                  f = open(name+f"({max_number})"+exten, "x")

                  for x in range(100):
                        if inputv[len(inputv)-1-x] == ".":
                              inputv = inputv[:len(inputv)-1-x]
                              break

                  f.write(inputv)

                  # old
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
                  f = open(name+exten,"x")
                  f.write(inputv)
      else:
            f = open(str(os.path.splitext(FilePathMemo.name)[0])+".lvc","x")
            f.write(inputv)




T = Text(window,height=5,width=10)

F = Frame(window)

T2 = Text(F, wrap=NONE)

S = Scrollbar(F,orient=VERTICAL, command=T2.yview)
S2 = Scrollbar(F,orient=HORIZONTAL,command=T2.xview)

S.pack(side=RIGHT, fill="y")
S2.pack(side=BOTTOM, fill="x")

F.pack(expand=True,fill=BOTH)
T2.pack(expand=True,side=LEFT,fill=BOTH)






T2.config(yscrollcommand= S.set,xscrollcommand = S2.set, wrap= NONE)
T2.config(state=DISABLED)

T2.pack(fill = BOTH, expand=0)


T.pack()
Button(window, text="read", command=labelcreate).pack()
Button(window, text="encode/decode", command=create).pack()
Button(window, text="export", command=export).pack()
window.mainloop()

#Test