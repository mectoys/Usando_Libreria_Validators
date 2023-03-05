import tkinter as tk
from tkinter import ttk, messagebox
import validators


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Crea widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        self.photocheck = tk.PhotoImage(file="../image/check.png")
        # Crea a Frame
        self.check_frame = ttk.LabelFrame(self, text="VALIDATORS", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        # *********************************between**************************************************************
        # Valor
        # Widget Label
        self.my_Label = ttk.Label(self.check_frame, text="Valor: ", justify=tk.LEFT)
        self.my_Label.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry = ttk.Entry(self.check_frame)
        self.my_Entry.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
        # Min
        # Widget Label
        self.my_Label_Min = ttk.Label(self.check_frame, text=" Mínimo: ")
        self.my_Label_Min.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_Min = ttk.Entry(self.check_frame)
        self.my_Entry_Min.grid(row=0, column=3, padx=5, pady=10, sticky="nsew")
        # Max
        # Widget Label
        self.my_Label_Max = ttk.Label(self.check_frame, text=" Máximo: ")
        self.my_Label_Max.grid(row=0, column=4, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_Max = ttk.Entry(self.check_frame)
        self.my_Entry_Max.grid(row=0, column=5, padx=5, pady=10, sticky="nsew")

        def ButtonBetween_click():

            # **************************************************************
            if validators.between(self.my_Entry.get(), min=self.my_Entry_Min.get(), max=self.my_Entry_Max.get()):
                messagebox.showwarning("Validators Between", "Validación Correcta")
            else:
                messagebox.showerror("Validators Between", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_ButtonBetween = ttk.Button(self.check_frame, command=ButtonBetween_click, text="Validar between",
                                           style="Accent.TButton")
        self.my_ButtonBetween.config(image=self.photocheck, compound="left")
        self.my_ButtonBetween.grid(row=0, column=6, padx=5, pady=10, sticky="nsew")
        # ****************************************Dominio***********************************************************
        # Dominio
        # Widget Label
        self.my_Label_dominio = ttk.Label(self.check_frame, text="Ingresar Dominio: ", justify=tk.LEFT)
        self.my_Label_dominio.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_dominio = ttk.Entry(self.check_frame)
        self.my_Entry_dominio.insert(tk.END, "example.com")
        self.my_Entry_dominio.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

        def ButtonDominio_click():
            # **************************************************************
            if validators.domain(self.my_Entry_dominio.get()):
                messagebox.showwarning("Validators Between", "Validación Correcta")
            else:
                messagebox.showerror("Validators Between", "Validación Incorrecta")

            # **************************************************************

        # Widget boton Calcular
        self.my_ButtonDominio = ttk.Button(self.check_frame, command=ButtonDominio_click, text="Validar Dominio",
                                           style="Accent.TButton")
        self.my_ButtonDominio.config(image=self.photocheck, compound="left")
        self.my_ButtonDominio.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

        # ****************************************Email***********************************************************
        # Email
        # Widget Label
        self.my_Label_email = ttk.Label(self.check_frame, text="Ingresar email: ", justify=tk.LEFT)
        self.my_Label_email.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_email = ttk.Entry(self.check_frame)
        self.my_Entry_email.insert(tk.END, "someone@example.com")
        self.my_Entry_email.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

        def ButtonEmail_click():
            # **************************************************************
            if validators.email(self.my_Entry_email.get()):
                messagebox.showwarning("Validators Email", "Validación Correcta")
            else:
                messagebox.showerror("Validators Email", "Validación Incorrecta")

            # **************************************************************

        # Widget boton Calcular
        self.my_ButtonEmail = ttk.Button(self.check_frame, command=ButtonEmail_click, text="Validar Email     ",
                                         style="Accent.TButton")
        self.my_ButtonEmail.config(image=self.photocheck, compound="left")
        self.my_ButtonEmail.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************IBAN CODE***********************************************************
        # IBAN CODE
        # Widget Label
        self.my_Label_iban = ttk.Label(self.check_frame, text="Ingresar código IBAN: ", justify=tk.LEFT)
        self.my_Label_iban.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_iban = ttk.Entry(self.check_frame)
        self.my_Entry_iban.insert(tk.END, "DE91100000000123456789")
        self.my_Entry_iban.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")

        def ButtonIban_click():
            # **************************************************************
            if validators.iban(self.my_Entry_iban.get()):
                messagebox.showwarning("Validators IBAN", "Validación Correcta")
            else:
                messagebox.showerror("Validators IBAN", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttoniban = ttk.Button(self.check_frame, command=ButtonIban_click, text=" Validar código IBAN",
                                        style="Accent.TButton")
        self.my_Buttoniban.config(image=self.photocheck, compound="left")
        self.my_Buttoniban.grid(row=3, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************ipv4***********************************************************
        # ipv4
        # Widget Label
        self.my_Label_ipv4 = ttk.Label(self.check_frame, text="Ingresar ipv4: ", justify=tk.LEFT)
        self.my_Label_ipv4.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_ipv4 = ttk.Entry(self.check_frame)
        self.my_Entry_ipv4.insert(tk.END, "123.0.0.7")
        self.my_Entry_ipv4.grid(row=4, column=1, padx=5, pady=10, sticky="nsew")

        def ButtonIpv4_click():
            # **************************************************************
            if validators.ipv4(self.my_Entry_ipv4.get()):
                messagebox.showwarning("Validators IPV4", "Validación Correcta")
            else:
                messagebox.showerror("Validators IPV4", "Validación Incorrecta")

            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonipv4 = ttk.Button(self.check_frame, command=ButtonIpv4_click, text=" Validar ipv4    ",
                                        style="Accent.TButton")
        self.my_Buttonipv4.config(image=self.photocheck, compound="left")
        self.my_Buttonipv4.grid(row=4, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************ipv6***********************************************************
        # ipv6
        # Widget Label
        self.my_Label_ipv6 = ttk.Label(self.check_frame, text="Ingresar ipv6: ", justify=tk.LEFT)
        self.my_Label_ipv6.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_ipv6 = ttk.Entry(self.check_frame)
        self.my_Entry_ipv6.insert(tk.END, "abcd:ef::42:1")
        self.my_Entry_ipv6.grid(row=5, column=1, padx=5, pady=10, sticky="nsew")

        def ButtonIpv6_click():
            # **************************************************************
            if validators.ipv6(self.my_Entry_ipv6.get()):
                messagebox.showwarning("Validators IPV6", "Validación Correcta")
            else:
                messagebox.showerror("Validators IPV6", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonipv6 = ttk.Button(self.check_frame, command=ButtonIpv6_click, text=" Validar ipv6    ",
                                        style="Accent.TButton")
        self.my_Buttonipv6.config(image=self.photocheck, compound="left")
        self.my_Buttonipv6.grid(row=5, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************lenght***********************************************************
        # Valor
        # Widget Label
        self.my_Label_lenght = ttk.Label(self.check_frame, text="Valor: ", justify=tk.LEFT)

        self.my_Label_lenght.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_lenght = ttk.Entry(self.check_frame)
        self.my_Entry_lenght.grid(row=6, column=1, padx=5, pady=10, sticky="nsew")
        # Min
        # Widget Label
        self.my_Label_Min_lenght = ttk.Label(self.check_frame, text=" Mínimo: ")
        self.my_Label_Min_lenght.grid(row=6, column=2, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_Min_lenght = ttk.Entry(self.check_frame)
        self.my_Entry_Min_lenght.grid(row=6, column=3, padx=5, pady=10, sticky="nsew")
        # Max
        # Widget Label
        self.my_Label_Max_lenght = ttk.Label(self.check_frame, text=" Máximo: ")
        self.my_Label_Max_lenght.grid(row=6, column=4, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_Max_lenght = ttk.Entry(self.check_frame)
        self.my_Entry_Max_lenght.grid(row=6, column=5, padx=5, pady=10, sticky="nsew")

        def ButtonLenght_click():
            # **************************************************************
            if validators.length(self.my_Entry_lenght.get(), min=int(self.my_Entry_Min_lenght.get()), max=int(self.my_Entry_Max_lenght.get())):
                messagebox.showwarning("Validators Lenght", "Validación Correcta")
            else:
                messagebox.showerror("Validators Lenght", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Button_lenght = ttk.Button(self.check_frame, command=ButtonLenght_click, text="Validar Lenght",
                                           style="Accent.TButton")
        self.my_Button_lenght.config(image=self.photocheck, compound="left")
        self.my_Button_lenght.grid(row=6, column=6, padx=5, pady=10, sticky="nsew")
        # ****************************************mac_address***********************************************************
        # mac_address
        # Widget Label
        self.my_Label_mac_address = ttk.Label(self.check_frame, text="Ingresar mac_address: ", justify=tk.LEFT)
        self.my_Label_mac_address.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_mac_address = ttk.Entry(self.check_frame)
        self.my_Entry_mac_address.insert(tk.END, "01:23:45:67:ab:CD")
        self.my_Entry_mac_address.grid(row=7, column=1, padx=5, pady=10, sticky="nsew")

        def Buttonmac_address_click():
            # **************************************************************
            if validators.mac_address(self.my_Entry_mac_address.get()):
                messagebox.showwarning("Validators mac_address", "Validación Correcta")
            else:
                messagebox.showerror("Validators mac_address", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonmac_address = ttk.Button(self.check_frame, command=Buttonmac_address_click,
                                               text=" Validar mac_address ",
                                               style="Accent.TButton")
        self.my_Buttonmac_address.config(image=self.photocheck, compound="left")
        self.my_Buttonmac_address.grid(row=7, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************url***********************************************************
        # url
        # Widget Label
        self.my_Label_url = ttk.Label(self.check_frame, text="Ingresar url: ", justify=tk.LEFT)
        self.my_Label_url.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_url = ttk.Entry(self.check_frame)
        self.my_Entry_url.insert(tk.END, "http://foobar.dk")
        self.my_Entry_url.grid(row=8, column=1, padx=5, pady=10, sticky="nsew")

        def Buttonmac_url_click():
            # **************************************************************
            if validators.url(self.my_Entry_url.get()):
                messagebox.showwarning("Validators URL", "Validación Correcta")
            else:
                messagebox.showerror("Validators URL", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonmac_url = ttk.Button(self.check_frame, command=Buttonmac_url_click, text=" Validar url ",
                                           style="Accent.TButton")
        self.my_Buttonmac_url.config(image=self.photocheck, compound="left")
        self.my_Buttonmac_url.grid(row=8, column=2, padx=5, pady=10, sticky="nsew")

        # ****************************************VISA***********************************************************
        # visa
        # Widget Label
        self.my_Label_visa = ttk.Label(self.check_frame, text="Ingresar VISA: ", justify=tk.LEFT)
        self.my_Label_visa.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_visa = ttk.Entry(self.check_frame)
        self.my_Entry_visa.insert(tk.END, "4000001234567899")
        self.my_Entry_visa.grid(row=9, column=1, padx=5, pady=10, sticky="nsew")

        def Buttonvisa_click():
            # **************************************************************
            if validators.visa(self.my_Entry_visa.get()):
                messagebox.showwarning("Validators VISA", "Validación Correcta")
            else:
                messagebox.showerror("Validators VISA", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonmac_master = ttk.Button(self.check_frame, command=Buttonvisa_click, text=" Validar VISA ",
                                           style="Accent.TButton")
        self.my_Buttonmac_master.config(image=self.photocheck, compound="left")
        self.my_Buttonmac_master.grid(row=9, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************MASTERCARD***********************************************************
        # Mastercard
        # Widget Label
        self.my_Label_master = ttk.Label(self.check_frame, text="Ingresar MASTERCARD: ", justify=tk.LEFT)
        self.my_Label_master.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_master = ttk.Entry(self.check_frame)
        self.my_Entry_master.insert(tk.END, "5555555555554444")
        self.my_Entry_master.grid(row=10, column=1, padx=5, pady=10, sticky="nsew")

        def Buttonmaster_click():
            # **************************************************************
            if validators.mastercard(self.my_Entry_master.get()):
                messagebox.showwarning("Validators MASTERCARD", "Validación Correcta")
            else:
                messagebox.showerror("Validators MASTERCARD", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonmaster = ttk.Button(self.check_frame, command=Buttonmaster_click, text=" Validar MASTER ",
                                            style="Accent.TButton")
        self.my_Buttonmaster.config(image=self.photocheck, compound="left")
        self.my_Buttonmaster.grid(row=10, column=2, padx=5, pady=10, sticky="nsew")
        # ****************************************AEXPRESS***********************************************************
        # AEXPRESS
        # Widget Label
        self.my_Label_aex = ttk.Label(self.check_frame, text="Ingresar AEXPRESS: ", justify=tk.LEFT)
        self.my_Label_aex.grid(row=10, column=3, padx=5, pady=10, sticky="nsew")
        # Widget Entry
        self.my_Entry_aex = ttk.Entry(self.check_frame)
        self.my_Entry_aex.insert(tk.END, "378282246310005")
        self.my_Entry_aex.grid(row=10, column=4, padx=5, pady=10, sticky="nsew")

        def Buttonaex_click():
            # **************************************************************
            if validators.amex(self.my_Entry_aex.get()):
                messagebox.showwarning("Validators AEXPRESS", "Validación Correcta")
            else:
                messagebox.showerror("Validators AEXPRESS", "Validación Incorrecta")
            # **************************************************************

        # Widget boton Calcular
        self.my_Buttonaex = ttk.Button(self.check_frame, command=Buttonaex_click, text=" Validar AEXPRESS ",
                                            style="Accent.TButton")
        self.my_Buttonaex.config(image=self.photocheck, compound="left")
        self.my_Buttonaex.grid(row=10, column=5, padx=5, pady=10, sticky="nsew")

        # ****************************************Cambio de Theme***********************************************************
        def change_theme():
            # NOTE: The theme's real name is azure-<mode>
            if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
                # Set light theme
                root.tk.call("set_theme", "light")
            else:
                # Set dark theme
                root.tk.call("set_theme", "dark")

        self.my_Buttontheme = ttk.Button(self.check_frame, command=change_theme, text=" Cambiar Theme",
                                         style="Accent.TButton")
        self.my_Buttontheme.grid(row=11, column=0, padx=5, pady=10, sticky="nsew")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ejemplo de uso librería Validators")
    root.iconbitmap("../image/valid.ico")
    # theme https://github.com/rdbende/Forest-ttk-theme
    # https://ttkthemes.readthedocs.io/en/latest/themes.html
    root.tk.call("source", "../azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
