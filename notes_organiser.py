NOTES_FILE="notes.txt"

def add_note():
    title=input("enter note title: ")
    content=input("enter note content: ")

    with open(NOTES_FILE, "a") as f:
        f.write(f"Title : {title}\nContent:{content}\n--\n")

        print("Note saved successfully!\n")



def view_notes():
    print("\n --All Notes-- ")
    try:
        with open(NOTES_FILE,"r") as f :
            data= f.read()
            if data.strip() == "":
                print("no notes are available.\n")
            else :
                print(data)
    except FileNotFoundError:
        print("No Notes Found Yet ! \n")




def search_notes():
    keyword = input("enter keyword to search :")
     
    try:
        with open(NOTES_FILE, "r") as f :
            notes= f.read().split("-\n")
            found=False 
             

            for note in notes :
                if keyword.lower() in note.lower():
                    print("\n Matched Note")
                    print(note)
                    found=True


            if not found :
                print("\n no matching note found .")
    except FileNotFoundError:
        print(" No notes saved yet .")

    print()





while True :
    print("*****NOTES ORGANISER*****")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Note")
    print("4. Exit")




    choice= input ("enter  your choice (1-4):")


    if  choice=="1.":
        add_note()
    elif choice=="2.":
        view_notes()
    elif choice=="3.":
        search_notes()
    elif choice=="4.":
        print("THANK YOU! exiting the program....")
        break
    else :
        print("invalid choice ... try again ")


    

        
            