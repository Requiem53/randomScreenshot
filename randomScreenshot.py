import webbrowser, random, string
linklist = []

def get_random_letters(length):
    rLetters_str = ''.join(random.choice(string.ascii_lowercase)for i in range(length))
    linklist.append(rLetters_str)
def get_random_numbers(length):
    rNumbers_str = ''.join(random.choice(string.digits) for i in range(length))
    linklist.append(rNumbers_str)

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'    
print('Look for a random screenshot')

numberofPages = input('Type the number of pages: ')
numberofPages = int(numberofPages)
count = 0

while(count < numberofPages):
    count = count+1
    print('Iteration no. ' + str(count))
    get_random_letters(2)
    get_random_numbers(4)
    print(linklist)
    webbrowser.get(chrome_path).open('https://prnt.sc/' + linklist[0] + linklist[1])
    linklist.clear()
    



    
