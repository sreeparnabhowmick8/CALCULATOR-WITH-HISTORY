history_file="history.txt" #declear a txt file where history of calculation is stored
def show_history():
    # open the file
    #count length of the line of the file
    #if length==0 then no history present
    #else print the history
    file=open(history_file,'r')
    lines=file.readlines()
    if(len(lines)==0):
        print(f"no history found")
    else:
        for line in reversed(lines):
            print(line.strip())  
    file.close()
def clear_history():
      file=open(history_file,'w') #open file in write mode
      file.close()
      print("history cleared")
def save_history(equation,result):
    file=open(history_file,'a') #open file in append mode
    file.write(equation+" = "+str(result)+"\n")
    file.close()
def calculation(equation):
    parts=equation.split()
    if(len(parts)!=3):
        print("invalid input")
        return
    num1=float(parts[0])
    operator=parts[1]
    num2=float(parts[2])
    if(operator=="+"):
        res=num1+num2
    elif(operator=="-"):
        res=num1-num2
    elif(operator=="*"):
        res=num1*num2
    elif(operator=="/"):
        if(num2==0):
            print("invalid second input")
            return
        res=num1/num2
    else:
        print("invalid operator .. use only + - * /")
    if(int(res)==res):
        res=int(res)  
    print("RESULT: ",res) 
    save_history(equation,res) #calculation stored in txt file
def main():
    print("____________SIMPLE CALCULATOR ______________")    
    while True:
        user_input=input("Enter calculation(+,-,*,/) or command(history,clear,exit)::::::::: ") 
        if(user_input=="exit"):
            print("EXIT")
            break
        elif(user_input=="clear"):
            clear_history()
        elif(user_input=="history"):
            show_history()
        else:
            calculation(user_input) 
main() #calling main function           

    



             
