line=input('Enter a line of text : ')

file=open("myinfo.txt","a")
file.write(f"{line}\n")
file.close()

