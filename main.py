import tkinter as tk

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
    
    login_page_lb = tk.Label(login_page_fm, text='Inicio de sesión', font=('Arial', 15), fg='#0097e8')
    login_page_lb.pack(pady=80)
    login_page_fm.pack(fill=tk.BOTH, expand=True)

#ventana usuarios
def users_page():
    users_page_fm = tk.Frame(main_fm)
    
    users_page_lb = tk.Label(users_page_fm, text='Usuarios', font=('Arial', 15), fg='#0097e8')
    users_page_lb.pack(pady=80)
    users_page_fm.pack(fill=tk.BOTH, expand=True)

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
root.mainloop()