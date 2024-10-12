from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()


class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_ordens = []
        root.mainloop()

    def tela(self):
        self.root.title("ORDEM FACIL_OUTI APPLICATION")
        self.root.configure(background="lightgreen")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(
            self.root,
            bd=4,
            bg="white",
            highlightbackground="darkgreen",
            highlightthickness=3,
        )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(
            self.root,
            bd=4,
            bg="white",
            highlightbackground="darkgreen",
            highlightthickness=3,
        )
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.lb_descricao = Label(
            self.frame_1, text="Descrição", bg="white", fg="black"
        )
        self.lb_descricao.place(relx=0.05, rely=0.05)

        self.descricao_entry = Entry(self.frame_1)
        self.descricao_entry.place(relx=0.05, rely=0.15, relwidth=0.8)

        self.lb_data = Label(self.frame_1, text="Data", bg="white", fg="black")
        self.lb_data.place(relx=0.05, rely=0.35)

        self.data_entry = Entry(self.frame_1)
        self.data_entry.place(relx=0.05, rely=0.45, relwidth=0.4)

        self.lb_status = Label(self.frame_1, text="Status", bg="white", fg="black")
        self.lb_status.place(relx=0.5, rely=0.35)

        self.status_entry = Entry(self.frame_1)
        self.status_entry.place(relx=0.5, rely=0.45, relwidth=0.4)

        self.lb_funcionario = Label(
            self.frame_1, text="Funcionário", bg="white", fg="black"
        )
        self.lb_funcionario.place(relx=0.05, rely=0.55)

        self.funcionario_entry = Entry(self.frame_1)
        self.funcionario_entry.place(relx=0.05, rely=0.65, relwidth=0.8)

        self.bt_adicionar = Button(
            self.frame_1,
            text="Adicionar",
            bd=2,
            bg="darkgreen",
            fg="white",
            command=self.adicionar_ordem,
        )
        self.bt_adicionar.place(relx=0.05, rely=0.8, relwidth=0.2, relheight=0.15)

        self.bt_visualizar = Button(
            self.frame_1,
            text="Visualizar",
            bd=2,
            bg="darkgreen",
            fg="white",
            command=self.visualizar_ordens,
        )
        self.bt_visualizar.place(relx=0.3, rely=0.8, relwidth=0.2, relheight=0.15)

        self.bt_deletar = Button(
            self.frame_1,
            text="Deletar",
            bd=2,
            bg="darkgreen",
            fg="white",
            command=self.deletar_ordem,
        )
        self.bt_deletar.place(relx=0.55, rely=0.8, relwidth=0.2, relheight=0.15)

        self.bt_dar_baixa = Button(
            self.frame_1,
            text="Dar Baixa",
            bd=2,
            bg="red",
            fg="white",
            command=self.abrir_janela_baixa,
        )
        self.bt_dar_baixa.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.15)

        self.bt_imprimir = Button(
            self.frame_1,
            text="Imprimir",
            bd=2,
            bg="darkgreen",
            fg="white",
            command=self.imprimir_ordens,
        )
        self.bt_imprimir.place(relx=0.8, rely=0.65, relwidth=0.2, relheight=0.15)

    def adicionar_ordem(self):
        descricao = self.descricao_entry.get()
        data = self.data_entry.get()
        status = self.status_entry.get()
        funcionario = self.funcionario_entry.get()

        if descricao and data and status and funcionario:
            self.lista_ordens.append(
                {
                    "descricao": descricao,
                    "data": data,
                    "status": status,
                    "funcionario": funcionario,
                }
            )
            messagebox.showinfo("Sucesso", "Ordem de serviço adicionada com sucesso!")
            self.descricao_entry.delete(0, END)
            self.data_entry.delete(0, END)
            self.status_entry.delete(0, END)
            self.funcionario_entry.delete(0, END)
            self.visualizar_ordens()
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def visualizar_ordens(self):
        self.frame_2.destroy()
        self.frame_2 = Frame(
            self.root,
            bd=4,
            bg="white",
            highlightbackground="darkgreen",
            highlightthickness=3,
        )
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        self.text_ordens = Text(self.frame_2, bg="white", fg="black")
        self.text_ordens.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        for idx, ordem in enumerate(self.lista_ordens):
            self.text_ordens.insert(END, f"Ordem {idx+1}\n")
            self.text_ordens.insert(END, f"Descrição: {ordem['descricao']}\n")
            self.text_ordens.insert(END, f"Data: {ordem['data']}\n")
            self.text_ordens.insert(END, f"Status: {ordem['status']}\n")
            self.text_ordens.insert(END, f"Funcionário: {ordem['funcionario']}\n\n")

    def deletar_ordem(self):
        if self.lista_ordens:
            self.lista_ordens.pop()
            messagebox.showinfo(
                "Sucesso", "Última ordem de serviço deletada com sucesso!"
            )
            self.visualizar_ordens()
        else:
            messagebox.showwarning("Atenção", "Não há ordens de serviço para deletar!")

    def abrir_janela_baixa(self):
        self.janela_baixa = Toplevel()
        self.janela_baixa.title("Dar Baixa na Ordem")
        self.janela_baixa.configure(background="lightgreen")
        self.janela_baixa.geometry("400x300")

        self.lb_ordem_num = Label(
            self.janela_baixa, text="Número da Ordem", bg="lightgreen", fg="black"
        )
        self.lb_ordem_num.place(relx=0.1, rely=0.1)

        self.ordem_num_entry = Entry(self.janela_baixa)
        self.ordem_num_entry.place(relx=0.1, rely=0.2, relwidth=0.8)

        self.bt_salvar = Button(
            self.janela_baixa,
            text="Salvar",
            bd=2,
            bg="darkgreen",
            fg="white",
            command=self.dar_baixa_ordem,
        )
        self.bt_salvar.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.2)

    def dar_baixa_ordem(self):
        ordem_num = self.ordem_num_entry.get()

        if ordem_num.isdigit() and 1 <= int(ordem_num) <= len(self.lista_ordens):
            idx = int(ordem_num) - 1
            self.lista_ordens[idx]["status"] = "Liberado"
            messagebox.showinfo("Sucesso", "Ordem de serviço liberada com sucesso!")
            self.janela_baixa.destroy()
            self.visualizar_ordens()
        else:
            messagebox.showwarning("Atenção", "Número da ordem inválido!")

    def imprimir_ordens(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if file_path:
            with open(file_path, "w") as file:
                for idx, ordem in enumerate(self.lista_ordens):
                    file.write(f"Ordem {idx+1}\n")
                    file.write(f"Descrição: {ordem['descricao']}\n")
                    file.write(f"Data: {ordem['data']}\n")
                    file.write(f"Status: {ordem['status']}\n")
                    file.write(f"Funcionário: {ordem['funcionario']}\n\n")
            messagebox.showinfo("Sucesso", "Ordens de serviço salvas com sucesso!")


Application()
