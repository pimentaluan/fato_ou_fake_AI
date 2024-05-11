# Detector de Fake News com API do Gemini

Este projeto consiste em um detector de fake news que utiliza a API do Gemini para analisar a veracidade de artigos de notícias. O aplicativo permite aos usuários inserir a URL de um artigo de notícia e recebe uma análise sobre se o artigo pode conter informações falsas ou enganosas.

## Funcionalidades

- **Análise de Artigos:** Os usuários podem inserir a URL de um artigo de notícia para receber uma análise sobre sua veracidade.
- **Detecção de Fake News:** O aplicativo utiliza a API do Gemini para analisar o conteúdo do artigo e determinar se ele pode conter fake news.
- **Interface Gráfica Intuitiva:** Uma interface gráfica simples permite aos usuários interagir facilmente com o aplicativo.

## Como Usar

1. **Instalação das Dependências:**
   Certifique-se de ter todas as dependências instaladas. Você pode instalá-las executando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configuração da API Key:**
   Antes de começar, é necessário configurar sua API key do Gemini. Substitua `"SUA_API_KEY"` pelo seu token de acesso.

   ```python
   genai.configure(api_key="SUA_API_KEY")
   ```

3. **Execução do Aplicativo:**
   Execute o aplicativo utilizando o seguinte comando:

   ```bash
   python main.py
   ```

4. **Inserção da URL do Artigo:**
   Na interface gráfica, insira a URL de um artigo de notícia no campo fornecido e clique no botão "Processar Artigo".

5. **Análise do Resultado:**
   O aplicativo processará o artigo e fornecerá uma análise sobre sua veracidade. O resultado será exibido na área de texto da interface gráfica.

## Observações

- **Recomendação de Verificação:** Recomenda-se sempre verificar a veracidade das informações em outras fontes antes de considerar a análise do aplicativo como definitiva.
