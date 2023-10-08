from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import CRUD
from tkinter import messagebox


root=tk.Tk()
root.geometry('730x600')
root.title('Taller Mecánico')
root.resizable(False,False)

class Cliente:
    def __init__(self) -> None:
       pass 

#funcion para cambiar de ventana
def switch(indicator_lb, page):
    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child['bg'] = 'SystemButtonFace'
            
    indicator_lb['bg'] = '#0097e8'
    
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()
    
    page()
    

#Botones del menu superior

options_fm = tk.Frame(root, bg = 'gray')

login_btn = tk.Button(options_fm, text='Login', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=login_indicator_lb, page=login_page))
login_btn.place (x=0, y=0, width=125)

login_indicator_lb = tk.Label(options_fm, bg='#0097e8')
login_indicator_lb.place(x=22, y=30, width=80, height=2)

users_btn = tk.Button(options_fm, text='Usuarios', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=users_indicator_lb, page=users_page))
users_btn.place (x=125, y=0, width=125)

users_indicator_lb = tk.Label(options_fm, bg='#0097e8')
users_indicator_lb.place(x=147, y=30, width=80, height=2)

clients_btn = tk.Button(options_fm, text='Clientes', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=clients_indicator_lb, page=clients_page))
clients_btn.place (x=250, y=0, width=125)

clients_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
clients_indicator_lb.place(x=272, y=30, width=80, height=2)

vehicles_btn = tk.Button(options_fm, text='Vehículos', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                         command=lambda: switch(indicator_lb=vehicles_indicator_lb, page=vehicles_page))
vehicles_btn.place (x=375, y=0, width=125)

vehicles_indicator_lb = tk.Label(options_fm, bg='#0097e8')
vehicles_indicator_lb.place(x=397, y=30, width=80, height=2)

repairs_btn = tk.Button(options_fm, text='Reparaciones', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=repairs_indicator_lb, page=repairs_page))
repairs_btn.place (x=500, y=0, width=125)

repairs_indicator_lb = tk.Label(options_fm, bg='#0097e8')
repairs_indicator_lb.place(x=522, y=30, width=80, height=2)

stock_btn = tk.Button(options_fm, text='Piezas', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=stock_indicator_lb, page=stock_page))
stock_btn.place (x=625, y=0, width=125)

stock_indicator_lb = tk.Label(options_fm, bg='#0097e8')
stock_indicator_lb.place(x=647, y=30, width=80, height=2)

options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=800, height=35)

#ventana login
def login_page():
    login_page_fm = tk.Frame(main_fm)
    login_page_fm.pack(fill=tk.BOTH, expand=True)  # Asegúrate de empacar el Frame para que sea visible
    
    login_page_lb = tk.Label(login_page_fm, text='Bienvenido al sistema del \ntaller mecánico', font=('Arial', 30), fg='#0097e8')
    login_page_lb.place(x=120, y=30)
    
    normal_login_btn = tk.Button(login_page_fm, text="Inicio de sesión")
    normal_login_btn.place(x=300, y=200)

    admin_login_btn = tk.Button(login_page_fm, text="Inicio de sesión para administador")
    admin_login_btn.place(x=250, y=250)
    
    registration_btn = tk.Button(login_page_fm, text="Crear cuenta")
    registration_btn.place(x=300, y=300)
    
def normal_login_page():
    normal_login_page_fm = tk.Frame(login_page)
    normal_login_page_fm.pack(fill=tk.BOTH, expand=True) 

def admin_login_page():
    admin_login_page_fm = tk.Frame(login_page)
    admin_login_page_fm.pack(fill=tk.BOTH, expand=True) 

def create_user_page():
    create_user_page_fm = tk.Frame(login_page)
    create_user_page_fm.pack(fill=tk.BOTH, expand=True) 


    
    
    
    
    
    
    # Agregando Label y Entry para el username
    #username_label = tk.Label(login_page_fm, text="Usuario:")
    #username_label.place(x=150, y=250)
    #username_entry = tk.Entry(login_page_fm)
    #username_entry.place(x=220, y=250)
    
    # Agregando Label y Entry para la contraseña
    #password_label = tk.Label(login_page_fm, text="Contraseña:")
    #password_label.place(x=150, y=280)
    #password_entry = tk.Entry(login_page_fm, show="*")
    #password_entry.place(x=220, y=280)
    
    


#ventana usuarios
def users_page():
    users_page_fm = tk.Frame(main_fm)
    users_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(users_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=30, y=30)
    id_search_entry = tk.Entry(users_page_fm)
    id_search_entry.place(x=180, y=30)
    
    search_btn = tk.Button(users_page_fm, text="Buscar")
    search_btn.place(x=450, y=30)
    new_btn = tk.Button(users_page_fm, text="Nuevo")
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(users_page_fm, text="Salvar")
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(users_page_fm, text="Cancelar")
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(users_page_fm, text="Editar")
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(users_page_fm, text="Remover")
    remove_btn.place(x=270, y=400)
    
    #profile_options = tk.OptionMenu(users_page_fm)
    
    id_lbl = tk.Label(users_page_fm, text="ID: ")
    id_lbl.place(x=30, y=60)
    id_entry = tk.Entry(users_page_fm)
    id_entry.place(x= 150, y=60)

    name_lbl = tk.Label(users_page_fm, text="Nombre: ")
    name_lbl.place(x=30, y=90)
    name_entry = tk.Entry(users_page_fm)
    name_entry.place(x= 150, y=90)    

    last_name_lbl = tk.Label(users_page_fm, text="Apellidos: ")
    last_name_lbl.place(x=30, y=120)
    last_name_entry = tk.Entry(users_page_fm)
    last_name_entry.place(x= 150, y=120)   

    phone_lbl = tk.Label(users_page_fm, text="Teléfono : ")
    phone_lbl.place(x=30, y=150)
    phone_entry = tk.Entry(users_page_fm)
    phone_entry.place(x= 150, y=150)  
    
    address_lbl = tk.Label(users_page_fm, text="Direccion: ")
    address_lbl.place(x=30, y=180)
    address_entry = tk.Entry(users_page_fm)
    address_entry.place(x= 150, y=180) 

    username_lbl = tk.Label(users_page_fm, text="Nombre de usuario: ")
    username_lbl.place(x=30, y=210)
    username_entry = tk.Entry(users_page_fm)
    username_entry.place(x= 170, y=210) 
    
    password_lbl = tk.Label(users_page_fm, text="Contraseña: ")
    password_lbl.place(x=30, y=240)
    password_entry = tk.Entry(users_page_fm)
    password_entry.place(x= 150, y=240)

    profile_lbl = tk.Label(users_page_fm, text="Perfil: ")
    profile_lbl.place(x=30, y=270)
    profile_entry = Combobox(users_page_fm, values=['Admin', 'Usuario'])
    profile_entry.place(x= 150, y=270)
    
    
    
    

#ventana clientes  
def clients_page():
    clients_page_fm = tk.Frame(main_fm)
    clients_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(clients_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=30, y=30)
    id_search_entry = tk.Entry(clients_page_fm)
    id_search_entry.place(x=180, y=30)
    
    user_id_lbl = tk.Label(clients_page_fm, text="Seleccione ID Usuario: ")
    user_id_lbl.place(x=30, y=60)
    user_id_entry = Combobox(clients_page_fm, values=['Usuario 1'])
    user_id_entry.place(x= 200, y=60)
    
    id_lbl = tk.Label(clients_page_fm, text="Cliente ID: ")
    id_lbl.place(x=30, y=90)
    id_entry = tk.Entry(clients_page_fm)
    id_entry.place(x= 150, y=90)

    name_lbl = tk.Label(clients_page_fm, text="Nombre: ")
    name_lbl.place(x=30, y=120)
    name_entry = tk.Entry(clients_page_fm)
    name_entry.place(x= 150, y=120)    

    last_name_lbl = tk.Label(clients_page_fm, text="Apellidos: ")
    last_name_lbl.place(x=30, y=150)
    last_name_entry = tk.Entry(clients_page_fm)
    last_name_entry.place(x= 150, y=150)   
    
    
    search_btn = tk.Button(clients_page_fm, text="Buscar")
    search_btn.place(x=380, y=26)
    new_btn = tk.Button(clients_page_fm, text="Nuevo")
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(clients_page_fm, text="Salvar")
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(clients_page_fm, text="Cancelar")
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(clients_page_fm, text="Editar")
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(clients_page_fm, text="Remover")
    remove_btn.place(x=270, y=400)
    

#ventana vehiculos
def vehicles_page():
    vehicles_page_fm = tk.Frame(main_fm)
    vehicles_page_fm.pack(fill=tk.BOTH, expand=True)
    
    id_search_label = tk.Label(vehicles_page_fm, text="Ingrese ID a Buscar: ")
    id_search_label.place(x=330, y=30)
    id_search_entry = tk.Entry(vehicles_page_fm)
    id_search_entry.place(x=480, y=30)

    client_lbl = tk.Label(vehicles_page_fm, text="Seleccione Cliente: ")
    client_lbl.place(x=30, y=30)
    client_combobox = Combobox(vehicles_page_fm, values=['Cliente 1'])
    client_combobox.place(x= 160, y=30)
     
    id_vehicle_label = tk.Label(vehicles_page_fm, text="Vehiculo ID: ")
    id_vehicle_label.place(x=30, y=60)
    id_vehicle_entry = tk.Entry(vehicles_page_fm)
    id_vehicle_entry.place(x=160, y=60)

    idd_vehicle_label = tk.Label(vehicles_page_fm, text="Matricula: ")
    idd_vehicle_label.place(x=30, y=90)
    idd_vehicle_entry = tk.Entry(vehicles_page_fm)
    idd_vehicle_entry.place(x=160, y=90)
    
    date_label = tk.Label(vehicles_page_fm, text="Fecha: ")
    date_label.place(x=330, y=60)
    date_entry = tk.Entry(vehicles_page_fm)
    date_entry.place(x=480, y=60)
    
    brand_label = tk.Label(vehicles_page_fm, text="Marca: ")
    brand_label.place(x=30, y=120)
    brand_entry = tk.Entry(vehicles_page_fm)
    brand_entry.place(x=160, y=120)
    
    model_label = tk.Label(vehicles_page_fm, text="Modelo: ")
    model_label.place(x=30, y=150)
    model_entry = tk.Entry(vehicles_page_fm)
    model_entry.place(x=160, y=150)
    
    search_btn = tk.Button(vehicles_page_fm, text="Buscar")
    search_btn.place(x=650, y=26)
    new_btn = tk.Button(vehicles_page_fm, text="Nuevo")
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(vehicles_page_fm, text="Salvar")
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(vehicles_page_fm, text="Cancelar")
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(vehicles_page_fm, text="Editar")
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(vehicles_page_fm, text="Remover")
    remove_btn.place(x=270, y=400)



#ventana reparaciones
def repairs_page():
    repairs_page_fm = tk.Frame(main_fm)
    repairs_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(repairs_page_fm, text="Ingrese ID a Buscar: ")
    id_search_label.place(x=330, y=30)
    id_search_entry = tk.Entry(repairs_page_fm)
    id_search_entry.place(x=480, y=30)
    
    id_vehicle_lbl = tk.Label(repairs_page_fm, text="Vehiculo ID: ")
    id_vehicle_lbl.place(x=30, y=30)
    id_vehicle_entry = Combobox(repairs_page_fm, values=['Vehiculo 1'])
    id_vehicle_entry.place(x= 160, y=30)

    id_unit_lbl = tk.Label(repairs_page_fm, text="Pieza ID: ")
    id_unit_lbl.place(x=30, y=60)
    id_unit_combobox = Combobox(repairs_page_fm, values=['Pieza 1'])
    id_unit_combobox.place(x= 160, y=60)
    
    id_repair_label = tk.Label(repairs_page_fm, text="Reparacion ID: ")
    id_repair_label.place(x=30, y=90)
    id_repair_entry = tk.Entry(repairs_page_fm)
    id_repair_entry.place(x=120, y=90)
    
    date_label = tk.Label(repairs_page_fm, text="Fecha entrada: ")
    date_label.place(x=250, y=90)
    date_entry = tk.Entry(repairs_page_fm)
    date_entry.place(x=340, y=90)
    
    date2_label = tk.Label(repairs_page_fm, text="Fecha salida: ")
    date2_label.place(x=470, y=90)
    date2_entry = tk.Entry(repairs_page_fm)
    date2_entry.place(x=560, y=90)
    
    problem_label = tk.Label(repairs_page_fm, text="Falla: ")
    problem_label.place(x=30, y=120)
    problem_entry = tk.Entry(repairs_page_fm)
    problem_entry.place(x=120, y=120)

    stock_label = tk.Label(repairs_page_fm, text="Cantidad Piezas: ")
    stock_label.place(x=250, y=120)
    stock_entry = tk.Entry(repairs_page_fm)
    stock_entry.place(x=340, y=120)
    
    search_btn = tk.Button(repairs_page_fm, text="Buscar")
    search_btn.place(x=650, y=26)
    new_btn = tk.Button(repairs_page_fm, text="Nuevo")
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(repairs_page_fm, text="Salvar")
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(repairs_page_fm, text="Cancelar")
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(repairs_page_fm, text="Editar")
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(repairs_page_fm, text="Remover")
    remove_btn.place(x=270, y=400)
    

#ventana piezas
def stock_page():
    stock_page_fm = tk.Frame(main_fm)
    stock_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(stock_page_fm, text="Ingrese ID a Buscar: ")
    id_search_label.place(x=330, y=30)
    id_search_entry = tk.Entry(stock_page_fm)
    id_search_entry.place(x=480, y=30)
    
    unit_id_lbl = tk.Label(stock_page_fm, text="Pieza ID: ")
    unit_id_lbl.place(x=30, y=30)
    unit_id_entry = tk.Entry(stock_page_fm)
    unit_id_entry.place(x=160, y=30)
    
    descriptn_lbl = tk.Label(stock_page_fm, text="Descripcion: ")
    descriptn_lbl.place(x=30, y=60)
    descriptn_entry = tk.Entry(stock_page_fm)
    descriptn_entry.place(x=160, y=60)
    
    stock_lbl = tk.Label(stock_page_fm, text="Stock: ")
    stock_lbl.place(x=30, y=90)
    stock_entry = tk.Entry(stock_page_fm)
    stock_entry.place(x=160, y=90)
    
    
    search_btn = tk.Button(stock_page_fm, text="Buscar")
    search_btn.place(x=650, y=26)
    new_btn = tk.Button(stock_page_fm, text="Nuevo")
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(stock_page_fm, text="Salvar")
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(stock_page_fm, text="Cancelar")
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(stock_page_fm, text="Editar")
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(stock_page_fm, text="Remover")
    remove_btn.place(x=270, y=400)
    
    

main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)


login_page()
users_page()
clients_page()
vehicles_page()
repairs_page()
stock_page()
root.mainloop()