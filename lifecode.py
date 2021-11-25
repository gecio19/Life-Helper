import PySimpleGUI as sg
from selenium import webdriver
from telesign.messaging import  MessagingClient
from telesign.util import random_with_n_digits
import sys
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()

option.add_argument('--user-data-dir=C:/Users/Grześ/AppData/Local/Google/Chrome/User Data/Default')


if sys.version[0]=="3": raw_input=input
customer_id = "29C12B40-ADB0-4BCA-B19C-D97D1702FC04"
api_key = "nEdIJUnhApXrCkG5Gxflg2ShYfux8rL/3unQRV13e4ANQ9imeZexWKkGhyNbX3fF0lr6EVKV8Ra4A/XIQl96sw==nEdIJUnhApXrCkG5Gxflg2ShYfux8rL/3unQRV13e4ANQ9imeZexWKkGhyNbX3fF0lr6EVKV8Ra4A/XIQl96sw==nEdIJUnhApXrCkG5Gxflg2ShYfux8rL/3unQRV13e4ANQ9imeZexWKkGhyNbX3fF0lr6EVKV8Ra4A/XIQl96sw=="

phone_number = "+48733057546"



 #####   L: Programowanie_skryptowy  H: Programowanie_skryptowy123@







index = -1
list1=list()
Witryny = list()
login = list()
haslo = list()
Napewnonie_haslo = list()
skrot = list()
link = list()

Napewnonie_haslo = ["********","********","********"]

list1 = ["cos","innecos","li","lu","la"]


filepath = "Witryny.txt"
filepath1 = "login.txt"
filepath2 = "haslo.txt"
filepath3 = "skrot.txt"
filepath4 = "link.txt"

f = open(filepath, "r")
Witryny = f.read().splitlines()
f.close()
l = open(filepath1, "r")
login = l.read().splitlines()
h = open(filepath2, "r")
haslo = h.read().splitlines()
l.close()
h.close()
s = open(filepath3,"r")
l = open(filepath4,"r")
skrot = s.read().splitlines()
link = l.read().splitlines()
s.close()
l.close()

slownik = dict()







Yt =list()
Yt = ["Jakaś piosenka", "lalila","la","lu"]

font = ("Arial , 11")



def Zmiana():
    indexb = values['ZmianayWitryna']
    try:

        if(indexb[0] == "Interia"):
            index = 0

        elif(indexb[0] == "Facebook"):
            index = 1
        elif (indexb[0] == "Gmail"):
            index = 2
        elif (indexb[0] == "Nk"):
            index = 3
    except:
        print("")
    input_login = values['-ZLogin-']
    if(input_login == ""):
        print("Nic nie ma")
    else:
        login[index] = input_login
        l = open(filepath1, "w")
        for i in range(0, len(login)):
            l.write(login[i] + "\n")
        l.close()
    input_haslo = values['-Zhaslo-']
    if(input_haslo == ""):
        print("Nie nie ma")
    else:
        haslo[index] = input_haslo
        h = open(filepath2,"w")
        for i in range(0, len(haslo)):
            h.write(haslo[i] + "\n")
        h.close()



kodwery = random_with_n_digits(5)

def Weryfikacja(kod):
    verify_code = kod
    message = "Your code is {}".format(verify_code)
    message_type = "OTP"
    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)




def zapisz():

    s = open(filepath3, "a")
    s.write(values['-Skrót-']+"\n")
    s.close()
    l = open(filepath4, "a")
    l.write(values['-ZLink-'] + "\n")
    l.close()
    s = open(filepath3, "r")
    l = open(filepath4, "r")
    skrot = s.read().splitlines()
    link = l.read().splitlines()
    window['ListaSkr'].update(values=skrot)
    window['menuskrot'].update(values=skrot)
    print(len(skrot))






def usuń():
    indexA = 0
    s = open(filepath3, "r")
    skrot = s.read().splitlines()
    s.close()
    l = open(filepath4, "r")
    link = l.read().splitlines()
    l.close()




    nazwa = values['ListaSkr']
    for i in range(0,len(skrot)):
        if (nazwa[0] == skrot[i]):
            indexA = i

        else:
            print("brak")
    print("TO jest leg:" , len(skrot)-1)

    del skrot[indexA]
    del link[indexA]
    s = open(filepath3, "w")
    for i in range(0,len(skrot)):
        s.write(skrot[i]+ "\n")
    s.close()
    l = open(filepath4, "w")
    for i in range(0,len(link)):
        l.write(link[i]+ "\n")
    l.close()












def chromeopen():
    if(values['-IN-'] == True):

        try:
            web.execute_script("window.open('https://poczta.interia.pl/logowanie/');")
            web.switch_to.window(web.window_handles[-1])         ### Zmiana focusu na inną karte
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/div[1]/div[1]/input").send_keys(login[0])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/div[1]/div[2]/div/input").send_keys(haslo[0])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/button").click()
        except:
            print("")

    else:
        print("")
        try:
            web.get("https://poczta.interia.pl/logowanie/")
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/div[1]/div[1]/input").send_keys(login[0])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/div[1]/div[2]/div/input").send_keys(haslo[0])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/button").click()

        except:
            print("")




def facebook():
    if (values['-IN-'] == True):
        try:
            web.execute_script("window.open('https://www.facebook.com/');")
            web.switch_to.window(web.window_handles[-1])
            web.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(login[1])
            web.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(haslo[1])
        except:
            print("")


    else:
        try:
            web.get("https://www.facebook.com/")
            web.switch_to.window(web.window_handles[-1])
            web.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]").click()
            web.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(login[1])
            web.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(haslo[1])
        except:
            print("")



def Gmail():
    if (values['-IN-'] == True):
        try:
            web.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin');")
            time.sleep(3)
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(login[2])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
            time.sleep(2)
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(haslo[2])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
        except:
            print("")
    else:
        try:
            web.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            time.sleep(3)
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(login[2])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
            time.sleep(2)
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(haslo[2])
            web.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
        except:
            print("")



sprawdz = "https://www.youtube.com/c/RazzHD/videos"

def wybierz(indexaa):




    if(indexaa == "Interia"):
        chromeopen()
    if(indexaa == "Facebook"):
        facebook()

    if(indexaa == "Gmail"):
        Gmail()

wybrana = 0






def O_wybór(indexotworz):
    l = open(filepath4, "r")
    link = l.read().splitlines()
    l.close()
    s = open(filepath3, "r")
    skrot = s.read().splitlines()
    s.close()



    for i in range(0,len(skrot)):
        if(indexotworz == skrot[i]):
            wybrana = i
    strona = link[wybrana]
    if (values['-IN-'] == True):
        try:
            web.execute_script('window.open("{}","_blank");'.format(strona))
        except:
            print("")
    else:
        try:
            web.get(strona)
        except:
            print("")










 ### web.execute_script('window.open("{}","_blank");'.format(link))     /// otwarcie w nowej karcie

def cos():
    if (values['-IN-'] == True):
        print("cos")
    else:
        try:
            web.get(link[wybrana])
            print("przchodze")
        except:
            print("")



































# ----------- Create the 3 layouts this Window will display -----------
layout1 = [[sg.Text("        "),sg.Button('Włącz',size=(30,6)) , sg.Checkbox('Nowa Karta',size=(10,1) , key= '-IN-' , visible=False) , sg.Text("                                          ")  , sg.Button('Hasła',size=(30,6))],


                    [sg.Text("        "), sg.Text("Inne Strony:") ],


                   [sg.Text("        "),sg.Combo(Witryny,size=(35,10) , key="InneStrony"), sg.Text("                ") , sg.Button('Uruchom',size=(30,6)) , ],
                    [sg.Text("Piosenki z YT")],

                   [sg.Text("        "), sg.Combo(skrot, size=(35, 10),key='menuskrot'), sg.Text("                                      ", ), sg.Button('Otwórz', size=(14, 6)),sg.Button('Dodaj', size=(14, 6))]

]














layout2 = [  [ sg.Button('<',size=(3,2)), sg.Text("                  "), sg.Text("Hasła" , size=(20,1), font='Arial,20' ) ,   sg.Button('Pokaz hasła',size=(20,4) ) ],

            [sg.Text('Witryna'), sg.Text('                                  '), sg.Text('Login'),sg.Text('                                  '), sg.Text('Hasło')],
           [sg.Listbox(values=Witryny , size=(20,5) ) , sg.Listbox(values=login , size=(20,5), key= 'Loginy') , sg.Listbox(values=Napewnonie_haslo , size=(20,5) , key = 'Hasla'),  sg.Button('Zmień dane',size=(20,4), visible=False)]







           ]







layout3 = [    [sg.Button('< ',size=(3,2),) ,sg.Text('Dodawanie skrotu strony') , sg.Button('Dodaj Stronę',size=(12,4),)],




         [ sg.Listbox(skrot, size=(20,4) , key= 'ListaSkr') , sg.Button("Usuń" )]


                ]




layout4 = [  [

sg.Text("                  ") , sg.Text("Zmianna loginu lub hasla")],
    [sg.Listbox(values=Witryny , size=(20,5) , key= 'ZmianayWitryna')],
    [sg.Text("Login:"), sg.Text("            "),   sg.Text("Hasło:"),  ],
    [sg.InputText(size=(10,3) , key='-ZLogin-'), sg.InputText( size=(10,3) , key='-Zhaslo-')],
    [sg.Text("                                  "), sg.Button('Anuluj'), sg.Button('Zmień')]





]

layout5 = [  [

sg.Text("                  ") , sg.Text("Weryfikacja")],
    [ sg.Text("Wpisz kod wysłany na telefon:")],

    [sg.InputText(size=(20,3) , key='-KodWeryfikacji-') , sg.Text("Odpowiedź błędna" , text_color='red',visible=False,key='-Błędna-')],
    [sg.Text("                                  "), sg.Button('Powrót'), sg.Button('Sprawdź')]





]


layout6 = [

    [sg.Text("Skrót:"), sg.Text("            "), sg.Text("Link:"), ],
    [sg.InputText(size=(10, 3), key='-Skrót-'), sg.InputText(size=(20, 3), key='-ZLink-') , sg.Text("NIe wypełnione pole", text_color='red',visible=False,key='niewypełnione' )],
    [sg.Text("                                  "), sg.Button('Wróc'), sg.Button('Zatwierdź')]

]





# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-') , sg.Column(layout4, visible=False, key='-COL4-'),  sg.Column(layout5, visible=False, key='-COL5-') ,sg.Column(layout6, visible=False, key='-COL6-')]]

window = sg.Window('Life Helper', layout)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break

    elif event == 'Włącz':
        web = webdriver.Chrome(chrome_options=option, executable_path="C:\chromedriver")
        window['-IN-'].update(visible=True)




    if event == 'Hasła':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2;
        window[f'-COL{layout}-'].update(visible=True)








    if event == '<':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1;
        window[f'-COL{layout}-'].update(visible=True)

    if event == ('Uruchom'):
        indexaa  = values['InneStrony']   ### pobranie wartości z listy (z combo o key inneStrony) i przypisanie do index
        wybierz(indexaa)




    if event == ('Dodaj'):
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)
    if event == ('< '):

        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
    if event == ('Pokaz hasła'):                                ##### Musi przejśc najpierw weryfikacje
        window[f'-COL{layout}-'].update(visible=False)
        layout = 5
        window[f'-COL{layout}-'].update(visible=True)
        kodwery = random_with_n_digits(5)
        Weryfikacja(kodwery)







    if event == ('Zmień dane'):
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)


    if event == ('Anuluj'):
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
    if event == ('Zmień'):
        Zmiana()
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
        window['Loginy'].update(values=login)
        window['Hasla'].update(values=haslo)
    if event == ('Sprawdź'):
        input_weryfikacja = values['-KodWeryfikacji-']

        if(input_weryfikacja == kodwery):
            window[f'-COL{layout}-'].update(visible=False)
            layout = 2
            window[f'-COL{layout}-'].update(visible=True)
            window['Pokaz hasła'].update(visible=False)

            window['Zmień dane'].update(visible=True)
            window['Hasla'].update(values=haslo)
        else:
            window['-Błędna-'].update(visible=True)


    if event == ('Powrót'):
        window['-Błędna-'].update(visible=False)
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)


    if event == ("Dodaj Stronę"):
        window[f'-COL{layout}-'].update(visible=False)
        layout = 6
        window[f'-COL{layout}-'].update(visible=True)
    if event == ("Zatwierdź"):
        if(values['-Skrót-'] == "" or values['-ZLink-'] == ""):
            print("nic nie ma")
            window['niewypełnione'].update(visible=True)
        else:
            zapisz()
            window[f'-COL{layout}-'].update(visible=False)
            layout = 3
            window[f'-COL{layout}-'].update(visible=True)








    if event == ("Wróc"):
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)
        window['niewypełnione'].update(visible=False)

    if event == ('Usuń'):
        try:
            usuń()
        except:
            print("")
        s = open(filepath3, "r")
        skrot = s.read().splitlines()
        print(skrot)
        window['ListaSkr'].update(values=skrot)
        window['menuskrot'].update(values=skrot)






    if event == ("Otwórz"):
        indexotworz = values['menuskrot']
        O_wybór(indexotworz)

































window.close()