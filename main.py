import tkinter as tk
import tkinter.messagebox as mb
import processar_dados as pd
import validacao as v
from tkinter import font as tkfont
import threading

def markdown_para_texto(md_text):
    """Converte texto em Markdown para texto simples."""
    texto_simples = md_text.replace('## ', '').replace('**', '')
    texto_simples = texto_simples.replace('- ', '\n• ')
    return texto_simples

historico_urls = []
favoritos_urls = []

def processar_artigo():
    url = url_entry.get()
    if not url:
        mb.showerror("Erro", "Por favor, insira uma URL.")
        return
    historico_urls.append(url)
    status_label.config(text="Processando...")
    root.update()
    threading.Thread(target=processar_e_atualizar_ui, args=(url,)).start()

def processar_e_atualizar_ui(url):
    try:
        processed_text = pd.obter_conteudo_do_artigo_processado(url)
        if processed_text:
            v.convo.send_message(f"Do site: {url}\n\n{processed_text}")
            resposta = v.convo.last.text
            resposta_simples = markdown_para_texto(resposta)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, resposta_simples)
            status_label.config(text="Processamento concluído.")
            root.state('zoomed')
        else:
            status_label.config(text="Falha ao processar o artigo.")
    except Exception as e:
        mb.showerror("Erro", str(e))
        status_label.config(text="Erro ao processar o artigo.")


def exportar_resultado():
    with open('resultado.txt', 'w') as f:
        f.write(result_text.get(1.0, tk.END))

# Janela principal
root = tk.Tk()
root.title("Fato ou Fake?")

# Fonte
fontStyle = tkfont.Font(family="Arial", size=12)

# Rótulo e campo de entrada para URL
tk.Label(root, text="Digite a URL do artigo:", font=fontStyle).grid(row=0, column=0, sticky="w", padx=10, pady=5)
url_entry = tk.Entry(root, font=fontStyle, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Botão de processamento de artigo
process_button = tk.Button(root, text="Processar Artigo", command=processar_artigo, bg="#4937FF", fg="white", font=fontStyle)
process_button.grid(row=0, column=2, padx=10, pady=5)


# Botão para exportar resultado
export_button = tk.Button(root, text="Exportar Resultado", command=exportar_resultado, bg="#4937FF", fg="white", font=fontStyle)
export_button.grid(row=2, column=2, padx=10, pady=5)

# Rótulo de status
status_label = tk.Label(root, text="", font=fontStyle)
status_label.grid(row=3, columnspan=3, padx=10, pady=5)

# Área de texto para exibir o resultado
result_text = tk.Text(root, font=fontStyle, wrap="word")
result_text.grid(row=4, columnspan=3, padx=10, pady=5, sticky="nsew")

# Barra de rolagem
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.grid(row=4, column=3, sticky="nse")
result_text.config(yscrollcommand=scrollbar.set)

# Pesos de coluna e linha
root.columnconfigure((0, 1, 2), weight=1)
root.rowconfigure(4, weight=1)

# Iniciar loop principal
root.mainloop()