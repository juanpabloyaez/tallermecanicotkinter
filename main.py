from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
import CRUD as api
from tkinter import messagebox
import re


root=tk.Tk()
root.geometry('730x600')
root.title('Taller Mecánico')
root.resizable(False,False)
global_tier = 0

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
                      command=lambda: switch(indicator_lb=users_indicator_lb, page=users_page), state="disabled")
users_btn.place (x=125, y=0, width=125)

users_indicator_lb = tk.Label(options_fm, bg='#0097e8')
users_indicator_lb.place(x=147, y=30, width=80, height=2)

clients_btn = tk.Button(options_fm, text='Clientes', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=clients_indicator_lb, page=clients_page), state="disabled")
clients_btn.place (x=250, y=0, width=125)

clients_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
clients_indicator_lb.place(x=272, y=30, width=80, height=2)

vehicles_btn = tk.Button(options_fm, text='Vehículos', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                         command=lambda: switch(indicator_lb=vehicles_indicator_lb, page=vehicles_page), state="disabled")
vehicles_btn.place (x=375, y=0, width=125)

vehicles_indicator_lb = tk.Label(options_fm, bg='#0097e8')
vehicles_indicator_lb.place(x=397, y=30, width=80, height=2)

repairs_btn = tk.Button(options_fm, text='Reparaciones', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=repairs_indicator_lb, page=repairs_page), state="disabled")
repairs_btn.place (x=500, y=0, width=125)

repairs_indicator_lb = tk.Label(options_fm, bg='#0097e8')
repairs_indicator_lb.place(x=522, y=30, width=80, height=2)

stock_btn = tk.Button(options_fm, text='Piezas', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=stock_indicator_lb, page=stock_page), state="disabled")
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
    
#    normal_login_btn = tk.Button(login_page_fm, text="Inicio de sesión")
#    normal_login_btn.place(x=300, y=200)

#    admin_login_btn = tk.Button(login_page_fm, text="Inicio de sesión para administador")
#    admin_login_btn.place(x=250, y=250)
    
#    registration_btn = tk.Button(login_page_fm, text="Crear cuenta")
#    registration_btn.place(x=300, y=300)
    
#def normal_login_page():
#    normal_login_page_fm = tk.Frame(login_page)
#    normal_login_page_fm.pack(fill=tk.BOTH, expand=True) 

#def admin_login_page():
#    admin_login_page_fm = tk.Frame(login_page)
#    admin_login_page_fm.pack(fill=tk.BOTH, expand=True) 

#def create_user_page():
#    create_user_page_fm = tk.Frame(login_page)
#    create_user_page_fm.pack(fill=tk.BOTH, expand=True)    
    
    
    # Agregando Label y Entry para el username
    username_var = tk.StringVar()
    username_label = tk.Label(login_page_fm, text="Usuario:")
    username_label.place(x=150, y=250)
    username_entry = tk.Entry(login_page_fm, textvariable=username_var)
    username_entry.place(x=220, y=250)
    
    # Agregando Label y Entry para la contraseña
    password_var = tk.StringVar()
    password_label = tk.Label(login_page_fm, text="Contraseña:")
    password_label.place(x=150, y=280)
    password_entry = tk.Entry(login_page_fm, show="*", textvariable=password_var)
    password_entry.place(x=220, y=280)
    
    #Evento Login
    def EventLogin():
        global global_tier
        global_tier = api.LoginUser(username_var.get(),password_var.get())
        clients_btn.config(state=tk.NORMAL if global_tier<4 else tk.DISABLED)
        users_btn.config(state=tk.NORMAL if global_tier<3 else tk.DISABLED)
        vehicles_btn.config(state=tk.NORMAL if global_tier<4 else tk.DISABLED)
        repairs_btn.config(state=tk.NORMAL if global_tier<3 or global_tier==4 else tk.DISABLED)
        stock_btn.config(state=tk.NORMAL if global_tier<3 or global_tier==4 else tk.DISABLED)

    userfm_btn = tk.Button(login_page_fm, text="Iniciar Sesión", command=EventLogin)
    userfm_btn.place(x=150, y=310)
    
    


#ventana usuarios
def users_page():
    users_page_fm = tk.Frame(main_fm)
    users_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(users_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=30, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(users_page_fm, textvariable=id_search_var)
    id_search_entry.place(x=180, y=30)
    
    #profile_options = tk.OptionMenu(users_page_fm)
    id_var = tk.StringVar()
    id_lbl = tk.Label(users_page_fm, text="ID: ")
    id_lbl.place(x=30, y=60)
    id_entry = tk.Entry(users_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 150, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(users_page_fm, text="Nombre: ")
    name_lbl.place(x=30, y=90)
    name_entry = tk.Entry(users_page_fm, textvariable=name_var, state=tk.NORMAL if global_tier<2 else tk.READABLE)
    name_entry.place(x= 150, y=90)    

    last_var = tk.StringVar()
    last_name_lbl = tk.Label(users_page_fm, text="Apellidos: ")
    last_name_lbl.place(x=30, y=120)
    last_name_entry = tk.Entry(users_page_fm, textvariable=last_var, state=tk.NORMAL if global_tier<2 else tk.READABLE)
    last_name_entry.place(x= 150, y=120)   

    phone_var = tk.StringVar()
    phone_lbl = tk.Label(users_page_fm, text="Teléfono : ")
    phone_lbl.place(x=30, y=150)
    phone_entry = tk.Entry(users_page_fm, textvariable=phone_var, state=tk.NORMAL if global_tier<2 else tk.READABLE)
    phone_entry.place(x= 150, y=150)  
    
    address_var = tk.StringVar()
    address_lbl = tk.Label(users_page_fm, text="Direccion: ")
    address_lbl.place(x=30, y=180)
    address_entry = tk.Entry(users_page_fm, textvariable=address_var, state=tk.NORMAL if global_tier<2 else tk.READABLE)
    address_entry.place(x= 150, y=180) 

    username_var = tk.StringVar()
    username_lbl = tk.Label(users_page_fm, text="Nombre de usuario: ")
    username_lbl.place(x=30, y=210)
    username_entry = tk.Entry(users_page_fm, textvariable=username_var, state=tk.NORMAL if global_tier<2 else tk.READABLE)
    username_entry.place(x= 170, y=210) 
    
    password_var = tk.StringVar()
    password_lbl = tk.Label(users_page_fm, text="Contraseña: ")
    password_lbl.place(x=30, y=240)
    password_entry = tk.Entry(users_page_fm, textvariable=password_var, state=tk.NORMAL if global_tier<2 else tk.DISABLED)
    password_entry.place(x= 150, y=240)

    profiles = ['Admin', 'Gerente','Supervisor(a)','Secretario(a)','Técnico(a)']
    profile_lbl = tk.Label(users_page_fm, text="Perfil: ")
    profile_lbl.place(x=30, y=270)
    profile_entry = Combobox(users_page_fm, values=profiles, state=tk.NORMAL if global_tier<2 else tk.READABLE)
    profile_entry.place(x= 150, y=270)
    
    #Validaciones
    def Validate():
        validation=name_var.get()
        mes_val=None
        if not validation.isalpha():
            mes_val="\n"+"El nombre solo debe contener letras"
        validation=last_var.get()
        if not validation.isalpha():
            mes_val=str(mes_val)+"\n"+"El apellido solo debe contener letras"
        validation=phone_var.get()
        if not validation.isdigit():
            mes_val=str(mes_val)+"\n"+"El télefono solo debe contener números"
        validation=profile_entry.get()
        if not validation in profiles:
            mes_val=str(mes_val)+"\n"+"No se seleccionó el perfil del usuario"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        
    #Eventos
    def EventSearch(id):
        obj = api.SelectUser(id)
        id_var.set(obj[0])
        username_var.set(obj[1])
        password_var.set(obj[2])
        profile_entry.set(profiles[obj[3]])
        name_var.set(obj[4])
        last_var.set(obj[5])
        phone_var.set(obj[6])
        address_var.set(obj[7])
    
    def EventCreate():
        validate=Validate()
        if validate:
            api.InsertUser(
            username_var.get(),
            password_var.get(),
            profile_entry.current(),
            name_var.get(),
            last_var.get(),
            phone_var.get(),
            address_var.get())
            messagebox.showinfo("REALIZADO","CREADO CORRECTAMENTE")

    def EventSave():
        validate=Validate()
        if validate:
            api.UpdateClient(
            id_var.get(),
            username_var.get(),
            password_var.get(),
            profile_entry.current(),
            name_var.get(),
            last_var.get(),
            phone_var.get(),
            address_var.get())
            messagebox.showinfo("REALIZADO","MODIFICADO CORRECTAMENTE")

    def EventClean():
        id_var.set("")
        username_var.set("")
        password_var.set("")
        profile_entry.set("")
        name_var.set("")
        last_var.set("")
        phone_var.set("")
        address_var.set("")


    def EventDelete():
        api.PseudoDropUser(id_var.get())
        messagebox.showwarning("REALIZADO","USUARIO ELIMINADO")

    def EventEdit():
        messagebox.showwarning("Editar?")
        
        #Botones
    search_btn = tk.Button(users_page_fm, text="Buscar", state=tk.NORMAL if global_tier<3 else tk.DISABLED,
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=450, y=30)
    new_btn = tk.Button(users_page_fm, text="Nuevo", state=tk.NORMAL if global_tier<2 else tk.DISABLED,
                        command=EventCreate)
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(users_page_fm, text="Salvar", state=tk.NORMAL if global_tier<2 else tk.DISABLED,
                         command=EventSave)
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(users_page_fm, text="Cancelar", state=tk.NORMAL if global_tier<3 else tk.DISABLED,
                           command=EventClean)
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(users_page_fm, text="Editar", state=tk.NORMAL if global_tier<2 else tk.DISABLED,
                         command=EventEdit)
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(users_page_fm, text="Remover", state=tk.NORMAL if global_tier<1 else tk.DISABLED,
                            command=EventDelete)
    remove_btn.place(x=270, y=400)

    

#ventana clientes  
def clients_page():
    clients_page_fm = tk.Frame(main_fm)
    clients_page_fm.pack(fill=tk.BOTH, expand=True)
    users=api.ListUsers(0)

    id_search_var=tk.StringVar()
    id_search_label = tk.Label(clients_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=30, y=30)
    id_search_entry = tk.Entry(clients_page_fm, textvariable=id_search_var)
    id_search_entry.place(x=180, y=30)
    
    user_id_lbl = tk.Label(clients_page_fm, text="Seleccione ID Usuario: ")
    user_id_lbl.place(x=30, y=60)
    user_id_entry = Combobox(clients_page_fm, values=users)
    user_id_entry.place(x= 200, y=60)
    
    id_var=tk.StringVar()
    id_lbl = tk.Label(clients_page_fm, text="Cliente ID: ")
    id_lbl.place(x=30, y=90)
    id_entry = tk.Entry(clients_page_fm,textvariable=id_var,state="readonly")
    id_entry.place(x= 150, y=90)

    name_var=tk.StringVar()
    name_lbl = tk.Label(clients_page_fm, text="Nombre: ")
    name_lbl.place(x=30, y=120)
    name_entry = tk.Entry(clients_page_fm,textvariable=name_var,state="readonly")
    name_entry.place(x= 150, y=120)    

    last_var=tk.StringVar()
    last_name_lbl = tk.Label(clients_page_fm, text="Apellidos: ")
    last_name_lbl.place(x=30, y=150)
    last_name_entry = tk.Entry(clients_page_fm,textvariable=last_var,state="readonly")
    last_name_entry.place(x= 150, y=150)   
    
     #Validaciones
    def Validate():
        validation=name_var.get()
        mes_val=None
        if not validation.isalpha():
            mes_val="\n"+"El nombre solo debe contener letras"
        validation=last_var.get()
        if not validation.isalpha():
            mes_val=str(mes_val)+"\n"+"El apellido solo debe contener letras"
        validation=user_id_entry.get()
        if not validation in users:
            mes_val=str(mes_val)+"\n"+"No se seleccionó un usuario válido"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        
    #Eventos
    def EventSearch(id):
        obj = api.SelectClient(id)
        id_var.set(obj[0])
        user_id_entry.set(users[int(obj[3])])
        name_var.set(obj[1])
        last_var.set(obj[2])
    
    def EventCreate():
        validate=Validate()
        if validate:
            api.InsertClient(
            name_var.get(),
            last_var.get(),
            user_id_entry.current())
            messagebox.showinfo("REALIZADO","CREADO CORRECTAMENTE")

    def EventSave():
        validate=Validate()
        if validate:
            api.UpdateClient(
            id_var.get(),
            name_var.get(),
            last_var.get(),
            user_id_entry.current())
            messagebox.showinfo("REALIZADO","MODIFICADO CORRECTAMENTE")

    def EventClean():
        id_var.set("")
        user_id_entry.set("")
        name_var.set("")
        last_var.set("")
        name_entry.config(state="readonly")
        last_name_entry.config(state="readonly")


    def EventDelete():
        api.PseudoDropUser(id_var.get())
        messagebox.showwarning("REALIZADO","USUARIO ELIMINADO")

    def EventEdit():
        name_entry.config(state="normal")
        last_name_entry.config(state="normal")
        
    search_btn = tk.Button(clients_page_fm, text="Buscar", command=lambda:EventSearch(int(id_search_var.get())))
    search_btn.place(x=380, y=26)
    new_btn = tk.Button(clients_page_fm, text="Nuevo", command=EventCreate)
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(clients_page_fm, text="Salvar",command=EventSave)
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(clients_page_fm, text="Cancelar", command=EventClean)
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(clients_page_fm, text="Editar", command=EventEdit)
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(clients_page_fm, text="Remover", command=EventDelete)
    remove_btn.place(x=270, y=400)
    

#ventana vehiculos
def vehicles_page():
    vehicles_page_fm = tk.Frame(main_fm)
    vehicles_page_fm.pack(fill=tk.BOTH, expand=True)
    
    id_search_var = tk.StringVar()
    id_search_label = tk.Label(vehicles_page_fm, text="Ingrese ID a Buscar: ")
    id_search_label.place(x=330, y=30)
    id_search_entry = tk.Entry(vehicles_page_fm,textvariable=id_search_var)
    id_search_entry.place(x=480, y=30)

    clients=api.ListClient()
    client_lbl = tk.Label(vehicles_page_fm, text="Seleccione Cliente: ")
    client_lbl.place(x=30, y=30)
    client_combobox = Combobox(vehicles_page_fm, values=clients)
    client_combobox.place(x= 160, y=30)
     
    id_var = tk.StringVar()
    id_vehicle_label = tk.Label(vehicles_page_fm, text="Vehiculo ID: ")
    id_vehicle_label.place(x=30, y=60)
    id_vehicle_entry = tk.Entry(vehicles_page_fm,textvariable=id_var,state="readonly")
    id_vehicle_entry.place(x=160, y=60)

    idd_var = tk.StringVar()
    idd_vehicle_label = tk.Label(vehicles_page_fm, text="Matricula: ")
    idd_vehicle_label.place(x=30, y=90)
    idd_vehicle_entry = tk.Entry(vehicles_page_fm,textvariable=idd_var,state="readonly")
    idd_vehicle_entry.place(x=160, y=90)

    date_var = tk.StringVar()
    date_label = tk.Label(vehicles_page_fm, text="Fecha (AAAA-MM-DD): ")
    date_label.place(x=330, y=60)
    date_entry = tk.Entry(vehicles_page_fm,textvariable=date_var,state="readonly")
    date_entry.place(x=480, y=60)
    
    brand_var = tk.StringVar()
    brand_label = tk.Label(vehicles_page_fm, text="Marca: ")
    brand_label.place(x=30, y=120)
    brand_entry = tk.Entry(vehicles_page_fm,textvariable=brand_var,state="readonly")
    brand_entry.place(x=160, y=120)
    
    model_var = tk.StringVar()
    model_label = tk.Label(vehicles_page_fm)
    model_label.place(x=30, y=150)
    model_entry = tk.Entry(vehicles_page_fm, text="Modelo: ",textvariable=model_var,state="readonly")
    model_entry.place(x=160, y=150)
    
     #Validaciones
    def Validate():
        validation=idd_var.get()
        mes_val=None
        if not validation.isalnum():
            mes_val="\n"+"Las placas solo deben contener letras y números"
        validation=client_combobox.get()
        if not validation in clients:
            mes_val=str(mes_val)+"\n"+"No se seleccionó un cliente válido"
        validation=date_var.get()
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, validation):
            mes_val=str(mes_val)+"\n"+"Formato de fecha no válido"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        
    #Eventos
    def EventSearch(id):
        obj = api.SelectVehicle(id)
        id_var.set(obj[0])
        client_combobox.set(clients[int(obj[5])-1])
        idd_var.set(obj[1])
        brand_var.set(obj[2])
        model_var.set(obj[3])
        date_var.set(obj[4])
    
    def EventCreate():
        validate=Validate()
        if validate:
            api.InsertVehicle(
        idd_var.get(),
        brand_var.get(),
        model_var.get(),
        date_var.get(),
        client_combobox.current())
            messagebox.showinfo("REALIZADO","CREADO CORRECTAMENTE")

    def EventSave():
        validate=Validate()
        if validate:
            api.UpdateVehicle(
            id_var.get(),
            idd_var.get(),
            brand_var.get(),
            model_var.get(),
            date_var.get(),
            client_combobox.current())
            messagebox.showinfo("REALIZADO","MODIFICADO CORRECTAMENTE")

    def EventClean():
        id_var.set("")
        client_combobox.set("")
        brand_var.set("")
        model_var.set("")
        date_var.set("")
        idd_var.set("")
        brand_entry.config(state="readonly")
        model_entry.config(state="readonly")
        date_entry.config(state="readonly")
        idd_vehicle_entry.config(state="readonly")

    def EventDelete():
        api.PseudoDropVehicle(id_var.get())
        messagebox.showwarning("REALIZADO","USUARIO ELIMINADO")

    def EventEdit():
        brand_entry.config(state="normal")
        model_entry.config(state="normal")
        date_entry.config(state="normal")
        idd_vehicle_entry.config(state="normal")


    search_btn = tk.Button(vehicles_page_fm, text="Buscar", command=lambda:EventSearch(int(id_search_var.get())))
    search_btn.place(x=650, y=26)
    new_btn = tk.Button(vehicles_page_fm, text="Nuevo", command=EventCreate)
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(vehicles_page_fm, text="Salvar", command=EventSave)
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(vehicles_page_fm, text="Cancelar", command=EventClean)
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(vehicles_page_fm, text="Editar", command=EventEdit)
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(vehicles_page_fm, text="Remover", command=EventDelete)
    remove_btn.place(x=270, y=400)



#ventana reparaciones
def repairs_page():
    repairs_page_fm = tk.Frame(main_fm)
    repairs_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_var = tk.StringVar()
    id_search_label = tk.Label(repairs_page_fm, text="Ingrese ID a Buscar: ")
    id_search_label.place(x=330, y=30)
    id_search_entry = tk.Entry(repairs_page_fm,textvariable=id_search_var)
    id_search_entry.place(x=480, y=30)

    vehicles=api.ListVehicles()
    id_vehicle_lbl = tk.Label(repairs_page_fm, text="Vehiculo ID: ")
    id_vehicle_lbl.place(x=30, y=30)
    id_vehicle_entry = Combobox(repairs_page_fm, values=vehicles)
    id_vehicle_entry.place(x= 160, y=30)

    pieces=api.ListPieces()
    id_unit_lbl = tk.Label(repairs_page_fm, text="Pieza ID: ")
    id_unit_lbl.place(x=30, y=60)
    id_unit_combobox = Combobox(repairs_page_fm, values=pieces)
    id_unit_combobox.place(x= 160, y=60)
    
    id_repair_var = tk.StringVar()
    id_repair_label = tk.Label(repairs_page_fm, text="Reparacion ID: ")
    id_repair_label.place(x=30, y=90)
    id_repair_entry = tk.Entry(repairs_page_fm,textvariable=id_repair_var,state="readonly")
    id_repair_entry.place(x=120, y=90)
    
    date_var = tk.StringVar()
    date_label = tk.Label(repairs_page_fm, text="Fecha entrada: ")
    date_label.place(x=250, y=90)
    date_entry = tk.Entry(repairs_page_fm,textvariable=date_var,state="readonly")
    date_entry.place(x=340, y=90)
    
    date2_var = tk.StringVar()
    date2_label = tk.Label(repairs_page_fm, text="Fecha salida: ")
    date2_label.place(x=470, y=90)
    date2_entry = tk.Entry(repairs_page_fm,textvariable=date2_var,state="readonly")
    date2_entry.place(x=560, y=90)
    
    problem_var = tk.StringVar()
    problem_label = tk.Label(repairs_page_fm, text="Falla: ")
    problem_label.place(x=30, y=120)
    problem_entry = tk.Entry(repairs_page_fm,textvariable=problem_var,state="readonly")
    problem_entry.place(x=120, y=120)

    stock_var = tk.StringVar()
    stock_label = tk.Label(repairs_page_fm, text="Cantidad Piezas: ")
    stock_label.place(x=250, y=120)
    stock_entry = tk.Entry(repairs_page_fm,textvariable=stock_var,state="readonly")
    stock_entry.place(x=340, y=120)
    
    
     #Validaciones
    def Validate():
        validation=stock_var.get()
        mes_val=None
        if not validation.isdigit():
            mes_val="\n"+"La cantidad debe ser en números"
        validation=id_unit_combobox.get()
        if not validation in pieces:
            mes_val=str(mes_val)+"\n"+"No se seleccionó una pieza válido"
        validation=id_vehicle_entry.get()
        if not validation in vehicles:
            mes_val=str(mes_val)+"\n"+"No se seleccionó un vehiculo válido"
        validation=date_var.get()
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, validation):
            mes_val=str(mes_val)+"\n"+"Formato de fecha de entrada no válido"
        validation=date2_var.get()
        if not re.match(date_pattern, validation):
            mes_val=str(mes_val)+"\n"+"Formato de fecha de salida no válido"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        
    #Eventos
    def EventSearch(id):
        obj = api.SelectService(id)
        id_repair_var.set(obj[0])
        problem_var.set(obj[1])
        stock_var.set(obj[2])
        date_var.set(obj[3])
        date2_var.set(obj[4])
        id_vehicle_entry.set(vehicles[int(obj[5])-1])
        id_unit_combobox.set(pieces[int(obj[6])-1])
    
    def EventCreate():
        validate=Validate()
        if validate:
            api.InsertService(
            problem_var.get(),
            stock_var.get(),
            date_var.get(),
            date2_var.get(),
            id_vehicle_entry.current(),
            id_unit_combobox.current())
            messagebox.showinfo("REALIZADO","CREADO CORRECTAMENTE")

    def EventSave():
        validate=Validate()
        if validate:
            api.UpdateService(
            id_repair_var.get(),
            problem_var.get(),
            stock_var.get(),
            date_var.get(),
            date2_var.get(),
            id_vehicle_entry.current(),
            id_unit_combobox.current())
            messagebox.showinfo("REALIZADO","MODIFICADO CORRECTAMENTE")

    def EventClean():
        id_repair_var.set("")
        problem_var.set("")
        stock_var.set("")
        date_var.set("")
        date2_var.set("")
        id_vehicle_entry.set("")
        id_unit_combobox.set("")
        problem_entry.config(state="readonly")
        stock_entry.config(state="readonly")
        date2_entry.config(state="readonly")
        date_entry.config(state="readonly")

    def EventDelete():
        api.DropService(id_repair_var.get())
        messagebox.showwarning("REALIZADO","USUARIO ELIMINADO")

    def EventEdit():
        problem_entry.config(state="normal")
        stock_entry.config(state="normal")
        date2_entry.config(state="normal")
        date_entry.config(state="normal")


    search_btn = tk.Button(repairs_page_fm, text="Buscar", command=lambda:EventSearch(int(id_search_var.get())))
    search_btn.place(x=650, y=26)
    new_btn = tk.Button(repairs_page_fm, text="Nuevo", command=EventCreate)
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(repairs_page_fm, text="Salvar", command=EventSave)
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(repairs_page_fm, text="Cancelar", command=EventClean)
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(repairs_page_fm, text="Editar", command=EventEdit)
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(repairs_page_fm, text="Remover", command=EventDelete)
    remove_btn.place(x=270, y=400)
    

#ventana piezas
def stock_page():
    stock_page_fm = tk.Frame(main_fm)
    stock_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_var=tk.StringVar()
    id_search_label = tk.Label(stock_page_fm, text="Ingrese ID a Buscar: ")
    id_search_label.place(x=330, y=30)
    id_search_entry = tk.Entry(stock_page_fm, textvariable=id_search_var)
    id_search_entry.place(x=480, y=30)
    
    unit_id_var=tk.StringVar()
    unit_id_lbl = tk.Label(stock_page_fm, text="Pieza ID: ")
    unit_id_lbl.place(x=30, y=30)
    unit_id_entry = tk.Entry(stock_page_fm, textvariable=unit_id_var,state="readonly")
    unit_id_entry.place(x=160, y=30)
    
    descriptn_var=tk.StringVar()
    descriptn_lbl = tk.Label(stock_page_fm, text="Descripcion: ")
    descriptn_lbl.place(x=30, y=60)
    descriptn_entry = tk.Entry(stock_page_fm, textvariable=descriptn_var,state="readonly")
    descriptn_entry.place(x=160, y=60)
    
    stock_var=tk.StringVar()
    stock_lbl = tk.Label(stock_page_fm, text="Stock: ")
    stock_lbl.place(x=30, y=90)
    stock_entry = tk.Entry(stock_page_fm, textvariable=stock_var,state="readonly")
    stock_entry.place(x=160, y=90)
    

         #Validaciones
    def Validate():
        validation=stock_var.get()
        mes_val=None
        if not validation.isdigit():
            mes_val="La cantidad debe ser en números"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        
    #Eventos
    def EventSearch(id):
        obj = api.SelectPiece(id)
        unit_id_var.set(obj[0])
        descriptn_var.set(obj[1])
        stock_var.set(obj[2])
    
    def EventCreate():
        validate=Validate()
        if validate:
            api.InsertPiece(
            descriptn_var.get(),
            stock_var.get())
            messagebox.showinfo("REALIZADO","CREADO CORRECTAMENTE")

    def EventSave():
        validate=Validate()
        if validate:
            api.UpdatePieces(
            unit_id_var.get(),
            descriptn_var.get(),
            stock_var.get())
            messagebox.showinfo("REALIZADO","MODIFICADO CORRECTAMENTE")

    def EventClean():
        unit_id_var.set("")
        descriptn_var.set("")
        stock_var.set("")
        descriptn_entry.config(state="readonly")
        stock_entry.config(state="readonly")


    def EventDelete():
        api.PseudoDropPiece(unit_id_var.get())
        messagebox.showwarning("REALIZADO","USUARIO ELIMINADO")

    def EventEdit():
        descriptn_entry.config(state="normal")
        stock_entry.config(state="normal")
    
    search_btn = tk.Button(stock_page_fm, text="Buscar", command=lambda:EventSearch(int(id_search_var.get())))
    search_btn.place(x=650, y=26)
    new_btn = tk.Button(stock_page_fm, text="Nuevo", command=EventCreate)
    new_btn.place(x=30, y=400)
    save_btn = tk.Button(stock_page_fm, text="Salvar", command=EventSave)
    save_btn.place(x=80, y=400)
    cancel_btn = tk.Button(stock_page_fm, text="Cancelar", command=EventClean)
    cancel_btn.place(x=130, y=400)
    edit_btn = tk.Button(stock_page_fm, text="Editar", command=EventEdit)
    edit_btn.place(x=220, y=400)
    remove_btn = tk.Button(stock_page_fm, text="Remover", command=EventDelete)
    remove_btn.place(x=270, y=400)
    
    

main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)


login_page()
users_page()
clients_page()
vehicles_page()
repairs_page()
stock_page()
switch(indicator_lb=login_indicator_lb, page=login_page)
root.mainloop()