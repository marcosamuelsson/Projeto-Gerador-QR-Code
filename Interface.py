import tkinter
import customtkinter
from CTkMessagebox import CTkMessagebox
from GenerateQRCode import GenerateQR
from PIL import Image

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    
        # CHAMAR A CLASE GENERATE QR CODE
        self.gerar = GenerateQR()
    
        self.title("GENERATE QR CODE SCHNEIDER")
        
        # remove title bar , page reducer and closing page !!!most have a quit button with app.destroy!!! (this app have a quit button so don't worry about that)
        self.attributes("-fullscreen", True)
        self.resizable(False, False)

        
        # make the app as big as the screen (no mater wich screen you use) 
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # root!
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # self.iconbitmap(".\schneider-electric-icon.ico")
        
        # left side panel -> for frame selection
        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
        
        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.left_side_panel.grid_rowconfigure((4, 5), weight=1)

        # Chamar a função para adicionar a imagem após um pequeno atraso
        # self.after(100, self.AddImage)
        
        # self.left_side_panel WIDGET
        self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="GENERATE QR CODE SCHNEIDER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # button to select correct frame IN self.left_side_panel WIDGET
        self.selectFile_bt = customtkinter.CTkButton(self.left_side_panel, text="Select FIle", command=self.SelectFile, fg_color="#089c4c", width=200, height=50, font=("Arial", 17))
        self.selectFile_bt.grid(row=1, column=0, padx=20, pady=10)

        self.generate_bt = customtkinter.CTkButton(self.left_side_panel, text="Generate QR", command=self.Generate, fg_color="#089c4c", width=200, height=50, font=("Arial", 17))
        self.generate_bt.grid(row=2, column=0, padx=20, pady=10)

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
        
        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        # painel to see file selected
        self.top_select_painel = customtkinter.CTkFrame(self.right_dashboard, corner_radius=10, fg_color="#089c4c")
        self.top_select_painel.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)

        self.label_file = customtkinter.CTkLabel(self.top_select_painel, text="File Selected", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label_file.pack(side=tkinter.LEFT, padx=5, pady=5)

        self.top_select_painel2 = customtkinter.CTkFrame(self.top_select_painel, corner_radius=10, fg_color="#000811", height=40)
        self.top_select_painel2.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)

        self.img_screen = customtkinter.CTkFrame(self.right_dashboard, corner_radius=10, fg_color="#000811", height=1000)
        self.img_screen.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)

        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Exit", fg_color= '#EA0000', hover_color = '#B20000', command= self.close_window, width=200, height=50, font=("Arial", 17))
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)

    # def AddImage(self):
    #     # Criando espaço para o Life is ON
    #     original_image_life = Image.open(".\Schneider Electric Life is On.png")
    #     container_w_left = self.left_side_panel.winfo_width()
    #     container_h_left = self.left_side_panel.winfo_height()

    #     # Calcular a proporção para redimensionar a imagem
    #     life_width, life_height = original_image_life.size
    #     aspect_ratio_life = life_width / life_height

    #     # Calcular novas dimensões com verificação
    #     if container_w_left > 0 and container_h_left > 0:
    #         if container_w_left / container_h_left > aspect_ratio_life:
    #             new_w = container_h_left * aspect_ratio_life
    #             new_h = container_h_left
    #         else:
    #             new_w = container_w_left
    #             new_h = container_w_left / aspect_ratio_life

    #         # Redimensionar a imagem
    #         resized_image_life = original_image_life.resize((int(new_w), int(new_h)))

    #         # self.left_side_panel WIDGET
    #         self.life_image = customtkinter.CTkImage(light_image=resized_image_life, dark_image=resized_image_life, size=(int(new_w), int(new_h)))
    #         self.logo_label = customtkinter.CTkLabel(self.left_side_panel, image=self.life_image, text="", font=customtkinter.CTkFont(size=20))
    #         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    #     else:
    #         print("Erro: Dimensões do container são inválidas.")

    #  self.right_dashboard   ----> statement widget
    def SelectFile(self):
        self.clear_frame(self.top_select_painel2)
        self.clear_frame(self.img_screen)
        self.gerar.SelectFile()
        self.bt_from_file = customtkinter.CTkLabel(self.top_select_painel2, text=self.gerar.file, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.bt_from_file.pack(side=tkinter.LEFT, padx=10, pady=5)

        print(self.gerar.file)
        if self.gerar.file == "":
            CTkMessagebox(title="Warning", 
                    message="The path is not correct!", 
                    icon="warning", 
                    option_1="Cancel")
        
        else:
            CTkMessagebox(title="Successful",
                    message="Selected File!", 
                    icon="check", 
                    option_1="OK")
    
    #  self.right_dashboard   ----> dashboard widget  
    def Generate(self):
        if self.gerar.file == "":
            CTkMessagebox(title="Error", 
                        message="Unable to generate a QR Code!", 
                        icon="cancel", 
                        option_1="Ok")
        else:
            self.clear_frame(self.img_screen)
            self.gerar.Select_Save()

            if self.gerar.image_path == "":
                CTkMessagebox(title="Error", 
                        message="Unable to save a QR Code!", 
                        icon="cancel", 
                        option_1="Ok")
            else:
                self.gerar.Generate()

                # Carregar a imagem
                original_image = Image.open(self.gerar.image_path)
                
                # Obter as dimensões do container
                container_width = self.img_screen.winfo_width()
                container_height = self.img_screen.winfo_height()

                # Calcular a proporção para redimensionar a imagem
                original_width, original_height = original_image.size
                aspect_ratio = original_width / original_height

                if container_width / container_height > aspect_ratio:
                    new_width = container_height * aspect_ratio
                    new_height = container_height
                else:
                    new_width = container_width
                    new_height = container_width / aspect_ratio

                # Redimensionar a imagem
                resized_image = original_image.resize((int(new_width), int(new_height)))

                # Criar a imagem para o CTkLabel
                self.image = customtkinter.CTkImage(light_image=resized_image, dark_image=resized_image, size=(int(new_width), int(new_height)))
                self.image_label = customtkinter.CTkLabel(self.img_screen, image=self.image, text="")
                self.image_label.pack(padx=5, pady=5)

                CTkMessagebox(title="Successful",
                        message="QR Code generated successfully!", 
                        icon="check", 
                        option_1="OK")

    # close the entire window    
    def close_window(self): 
        msg=CTkMessagebox(title="Warning", 
                message="Are you sure to Exit?", 
                icon="warning", 
                option_1="Yes",
                option_2="No")
        
        if msg.get() == "Yes":
            App.destroy(self)
        else:
            pass

    # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page       
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

a = App()
a.mainloop()