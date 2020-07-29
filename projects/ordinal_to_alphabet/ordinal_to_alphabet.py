print(r'''
___/\\\\\\\\\\\\\\\_________________/\\\___________________________/\\\_____/\\\\\\\\\\__
 __\/\\\///////////_________________\/\\\_______________________/\\\\\\\___/\\\///////\\\_
  __\/\\\____________________________\/\\\____________/\\\______\/////\\\__\///______/\\\__
   __\/\\\\\\\\\\\\______/\\\____/\\\_\/\\\_________/\\\\\\\\\\\_____\/\\\_________/\\\//___
    __\////////////\\\___\/\\\___\/\\\_\/\\\\\\\\\__\////\\\////______\/\\\________\////\\\__
     _____________\//\\\__\/\\\___\/\\\_\/\\\////\\\____\/\\\__________\/\\\___________\//\\\_
      __/\\\________\/\\\__\/\\\___\/\\\_\/\\\__\/\\\____\/\\\_/\\______\/\\\__/\\\______/\\\__
       _\//\\\\\\\\\\\\\/___\//\\\\\\\\\__\/\\\\\\\\\_____\//\\\\\_______\/\\\_\///\\\\\\\\\/___
        __\/////////////______\/////////___\/////////_______\/////________\///____\/////////_____
                    
 _________________________________________/\\\_______________________________________________         
  ______________________________________/\\\//\\\_____________________________________________        
   _____________________________________/\\\_/\\\______________________________________________       
    ____________________________________\//\\\\//_______________________________________________      
     ___________________________________/\\\///\\\_______________________________________________     
      _________________________________/\\\/__\///\\\/\\\_________________________________________    
       ________________________________/\\\______\//\\\//__________________________________________   
        _______________________________\//\\\\\\\\\\\//\\\__________________________________________  
         ________________________________\///////////_\///___________________________________________ 

__/\\\\\\\\\\\\__________________________________/\\\________/\\\______________________________        
 _\/\\\////////\\\_______________________________\/\\\_____/\\\//_______________________________       
  _\/\\\______\//\\\______________________________\/\\\__/\\\//__________________________________      
   _\/\\\_______\/\\\__/\\\\\\\\\________/\\\\\\\\_\/\\\\\\//\\\_________/\\\\\\\\___/\\/\\\\\\\__     
    _\/\\\_______\/\\\_\////////\\\_____/\\\//////__\/\\\//_\//\\\______/\\\/////\\\_\/\\\/////\\\_    
     _\/\\\_______\/\\\___/\\\\\\\\\\___/\\\_________\/\\\____\//\\\____/\\\\\\\\\\\__\/\\\___\///__   
      _\/\\\_______/\\\___/\\\/////\\\__\//\\\________\/\\\_____\//\\\__\//\\///////___\/\\\_________  
       _\/\\\\\\\\\\\\/___\//\\\\\\\\/\\__\///\\\\\\\\_\/\\\______\//\\\__\//\\\\\\\\\\_\/\\\_________ 
        _\////////////______\////////\//_____\////////__\///________\///____\//////////__\///__________
''')

code = []
numbers = []
output = []
final_output = []

print('Welcome to the upgraded version of "5ubt13\'s number-to-alphabet-letter converter" by DacKer!')
print('Please input your code to decode. Example: "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"')

code = list(input('Enter the code: ').strip().split())

x = 0
for i in code:
    if code[x].isnumeric() == True:
        numbers.append(int(code[x]))
    else:
        pass
    x += 1

for i in numbers:
    i += 96
    i = chr(i)
    output.append(i)

x = 0
y = 0
if len(output) == len(code):
    final_output = output
else:
    for i in code:
        if code[x].isnumeric() == True:
            final_output.append(output[y])
            y += 1
        else:
            final_output.append(code[x])
        x += 1

decode = ''.join(final_output)
print("Here's the result: " + decode)
