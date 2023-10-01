import tkinter as tk
import CRUD as api

root=tk.Tk()
root.geometry('730x600')
root.title('Taller Mecánico')
root.resizable(False,False)

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

clients_indicator_lb = tk.Label(options_fm, bg='#0097e8')
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
    
    login_page_lb = tk.Label(login_page_fm, text='Inicio de sesión', font=('Arial', 30), fg='#0097e8')
    login_page_lb.place(x=200, y=100)
    
    # Agregando Label y Entry para el username
    username_label = tk.Label(login_page_fm, text="Usuario:")
    username_label.place(x=150, y=250)
    username_entry = tk.Entry(login_page_fm)
    username_entry.place(x=220, y=250)
    
    # Agregando Label y Entry para la contraseña
    password_label = tk.Label(login_page_fm, text="Contraseña:")
    password_label.place(x=150, y=280)
    password_entry = tk.Entry(login_page_fm, show="*")
    password_entry.place(x=220, y=280)
    
    


#ventana usuarios
def users_page():
    users_page_fm = tk.Frame(main_fm)
    users_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(users_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=30, y=30)
    id_search_entry = tk.Entry(users_page_fm)
    id_search_entry.place(x=180, y=30)
    
    search_btn = tk.Button(users_page_fm, text="Buscar")
    search_btn.place(x=450, y=28)
    search_btn = tk.Button(users_page_fm, text="Nuevo")
    search_btn.place(x=30, y=550)
    search_btn = tk.Button(users_page_fm, text="Salvar")
    search_btn.place(x=80, y=550)
    search_btn = tk.Button(users_page_fm, text="Cancelar")
    search_btn.place(x=130, y=550)
    search_btn = tk.Button(users_page_fm, text="Editar")
    search_btn.place(x=180, y=550)
    search_btn = tk.Button(users_page_fm, text="Remover")
    search_btn.place(x=230, y=550)
    
    profile_options = tk.OptionMenu(users_page_fm)
    
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
    phone_lbl.place(x=30, y=120)
    phone_entry = tk.Entry(users_page_fm)
    phone_entry.place(x= 150, y=120)  
    
    address_lbl = tk.Label(users_page_fm, text="Direccion: ")
    address_lbl.place(x=30, y=120)
    address_entry = tk.Entry(users_page_fm)
    address_entry.place(x= 150, y=120) 

    address_lbl = tk.Label(users_page_fm, text="Nombre de usuario: ")
    address_lbl.place(x=30, y=120)
    address_entry = tk.Entry(users_page_fm)
    address_entry.place(x= 150, y=120) 
    
    address_lbl = tk.Label(users_page_fm, text="Contraseña: ")
    address_lbl.place(x=30, y=120)
    address_entry = tk.Entry(users_page_fm)
    address_entry.place(x= 150, y=120)

    address_lbl = tk.Label(users_page_fm, text="Perfil: ")
    address_lbl.place(x=30, y=120)
    address_entry = tk.Entry(users_page_fm)
    address_entry.place(x= 150, y=120)
    
    
    
    

#ventana clientes  
def clients_page():
    clients_page_fm = tk.Frame(main_fm)
    
    clients_page_lb = tk.Label(clients_page_fm, text='Clientes', font=('Arial', 15), fg='#0097e8')
    clients_page_lb.pack(pady=80)
    clients_page_fm.pack(fill=tk.BOTH, expand=True)

#ventana vehiculos
def vehicles_page():
    vehicles_page_fm = tk.Frame(main_fm)
    
    vehicles_page_lb = tk.Label(vehicles_page_fm, text='Vehiculos', font=('Arial', 15), fg='#0097e8')
    vehicles_page_lb.pack(pady=80)
    vehicles_page_fm.pack(fill=tk.BOTH, expand=True)

#ventana reparaciones
def repairs_page():
    repairs_page_fm = tk.Frame(main_fm)
    
    repairs_page_lb = tk.Label(repairs_page_fm, text='Reparaciones', font=('Arial', 15), fg='#0097e8')
    repairs_page_lb.pack(pady=80)
    repairs_page_fm.pack(fill=tk.BOTH, expand=True)

#ventana piezas
def stock_page():
    stock_page_fm = tk.Frame(main_fm)
    
    stock_page_lb = tk.Label(stock_page_fm, text='Piezas', font=('Arial', 15), fg='#0097e8')
    stock_page_lb.pack(pady=80)
    stock_page_fm.pack(fill=tk.BOTH, expand=True)
    

main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)


login_page()
users_page()
clients_page()
vehicles_page()
repairs_page()
stock_page()
root.mainloop()