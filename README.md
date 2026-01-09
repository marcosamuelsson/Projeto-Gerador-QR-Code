# Projeto Gerador de QR Code

## Descrição

Este é um projeto pessoal desenvolvido em Python para gerar códigos QR (Quick Response) a partir de arquivos de texto (.txt) ou planilhas Excel (.xlsx, .xlsm, .xlsb). O projeto inclui uma interface gráfica amigável construída com CustomTkinter, permitindo ao usuário selecionar arquivos, gerar QR codes e visualizá-los diretamente na aplicação. O QR code gerado é salvo como imagem PNG.

O projeto foi criado para facilitar a geração de QR codes para dados variados, como textos simples, listas de nomes ou dados estruturados em Excel. É ideal para uso pessoal em tarefas como codificação de informações para etiquetas, compartilhamento de dados ou prototipagem rápida.

## Funcionalidades

- **Seleção de Arquivo**: Permite escolher arquivos .txt ou Excel (.xlsx, .xlsm, .xlsb) via diálogo de arquivo.
- **Leitura de Dados**: Lê o conteúdo completo do arquivo selecionado.
  - Para .txt: Lê o texto bruto.
  - Para Excel: Usa pandas para carregar os dados em um DataFrame.
- **Geração de QR Code**: Gera um QR code com correção de erro nível L (baixa), tamanho de caixa 10 e borda 4.
- **Salvamento**: Salva o QR code como imagem PNG em local escolhido pelo usuário.
- **Interface Gráfica**: 
  - Modo tela cheia, não redimensionável.
  - Tema escuro com esquema de cores verde.
  - Painéis esquerdo (controles) e direito (visualização).
  - Mensagens de confirmação e erro via CTkMessagebox.
  - Visualização da imagem do QR gerado, redimensionada para caber no painel.
- **Tratamento de Erros**: Verifica se arquivo foi selecionado antes de gerar; exibe avisos para caminhos inválidos.

## Padrões de Projeto Identificados

O projeto segue um padrão arquitetural simples inspirado no **MVC (Model-View-Controller)**:

- **Model (Modelo)**: Classe `GenerateQR` em `GenerateQRCode.py`, responsável pela lógica de negócio (seleção de arquivo, leitura, geração e salvamento do QR).
- **View/Controller (Visão/Controlador)**: Classe `App` em `Interface.py`, que gerencia a interface gráfica e os eventos do usuário, atuando como controlador para interagir com o modelo.

Essa separação permite que a lógica de geração seja independente da interface, facilitando manutenção e extensões futuras (ex.: adicionar CLI ou web interface).

## Pré-requisitos

- **Python**: Versão 3.7 ou superior (recomendado 3.8+ para compatibilidade com bibliotecas).
- **Sistema Operacional**: Compatível com Windows, macOS ou Linux (desenvolvido e testado em Windows).
- **Bibliotecas Python**:
  - `qrcode[pil]` (versão 7.3.1 ou superior): Para geração de QR codes.
  - `pandas` (versão 1.3.0 ou superior): Para leitura de arquivos Excel.
  - `customtkinter` (versão 5.2.0 ou superior): Para interface gráfica moderna baseada em Tkinter.
  - `CTkMessagebox` (versão 2.5 ou superior): Para caixas de diálogo customizadas.
  - `Pillow` (PIL, versão 8.0.0 ou superior): Para manipulação de imagens (usado implicitamente via qrcode e customtkinter).
  - `openpyxl` (opcional, mas recomendado para Excel): Pandas usa isso internamente para .xlsx.

## Instalação

1. **Clone ou Baixe o Repositório**:
   ```
   git clone https://github.com/seu-usuario/projeto-gerador-qr-code.git
   cd projeto-gerador-qr-code
   ```

2. **Instale as Dependências**:
   Use pip para instalar as bibliotecas necessárias:
   ```
   pip install qrcode[pil] pandas customtkinter CTkMessagebox Pillow openpyxl
   ```
   - Nota: `openpyxl` é necessário para leitura de .xlsx; para .xlsm/.xlsb, pode ser necessário `xlrd` (mas pandas lida bem com openpyxl).

3. **Verifique a Instalação**:
   Execute um teste rápido:
   ```
   python -c "import qrcode, pandas, customtkinter; print('Dependências OK')"
   ```

## Uso

### Via Interface Gráfica (Recomendado)

1. Execute o arquivo `Interface.py`:
   ```
   python Interface.py
   ```
   - A aplicação abrirá em modo tela cheia.

2. Clique em "Select File" para escolher um arquivo .txt ou Excel.

3. Clique em "Generate QR" para gerar e salvar o QR code.

4. Visualize o QR no painel direito e confirme o salvamento.

5. Use "Exit" para fechar a aplicação.

### Via Script Direto (Sem Interface)

1. Execute `GenerateQRCode.py`:
   ```
   python GenerateQRCode.py
   ```
   - Diálogos de arquivo aparecerão sequencialmente para seleção e salvamento.

2. O QR será gerado e salvo automaticamente.

### Arquivos de Teste

- `teste1.txt`: Contém dados de exemplo (tags como "<<RA>>", "<<15kv>>", etc.).
- `teste2.txt`: Lista de nomes ("Victor", "Joseph", "Marco").
- `teste3.txt`: Texto aleatório para teste.
- `teste.py`: Script para testar leitura de Excel com pandas.
- `teste2.py`: Função utilitária para verificar extensão de arquivo.

Use esses arquivos para testar a funcionalidade.

## Estrutura do Projeto

```
Projeto-Gerador-QR-Code-main/
├── GenerateQRCode.py          # Classe principal para geração de QR (Model)
├── Interface.py                # Interface gráfica (View/Controller)
├── teste.py                    # Script de teste para leitura de Excel
├── teste1.txt                  # Arquivo de teste .txt
├── teste2.py                   # Função utilitária para verificar tipo de arquivo
├── teste2.txt                  # Arquivo de teste .txt com nomes
└── teste3.txt                  # Arquivo de teste .txt com texto aleatório
```

- **GenerateQRCode.py**: Contém a classe `GenerateQR` com métodos para manipulação de arquivos e geração de QR.
- **Interface.py**: Define a classe `App` para a GUI, integrando com `GenerateQR`.
- Arquivos de teste: Usados para validação e exemplos.

## Parâmetros Técnicos

- **Linguagem**: Python 3.x
- **Paradigma**: Orientado a Objetos (classes `GenerateQR` e `App`)
- **Interface Gráfica**: CustomTkinter (baseado em Tkinter), com tema dark e cores customizadas (#089c4c para botões, #000811 para painéis)
- **Geração de QR**:
  - Biblioteca: `qrcode`
  - Configurações: version=1, error_correction=ERROR_CORRECT_L, box_size=10, border=4
  - Formato de saída: PNG
- **Leitura de Arquivos**:
  - .txt: Leitura direta com encoding UTF-8
  - Excel: Usando pandas.read_excel() (suporta .xlsx, .xlsm, .xlsb)
- **Manipulação de Imagens**: Pillow (PIL) para redimensionamento na interface
- **Tratamento de Caminhos**: Conversão de barras (/) para (\) no Windows para compatibilidade
- **Resolução de Tela**: A aplicação se adapta ao tamanho da tela (fullscreen)
- **Dependências Não Utilizadas**: `reportlab` e `io.BytesIO` são importados em `GenerateQRCode.py` mas não usados (possível remanescente de versão anterior para PDF)
- **Compatibilidade**: Desenvolvido em Windows; caminhos absolutos e relativos suportados
- **Performance**: Geração rápida para textos pequenos; para arquivos grandes, considere otimização
- **Limitações**: QR code único por execução; não suporta múltiplos QR ou personalização avançada (ex.: cores customizadas além de preto/branco)

## Contribuição

Como projeto pessoal, contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs ou sugerir melhorias via Issues.
- Enviar Pull Requests com correções ou novas funcionalidades.
- Melhorar a documentação ou adicionar testes.

Para contribuir:
1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Autor

Desenvolvido por Marco Antônio Samuelsson como projeto pessoal para aprendizado e uso prático.

## Agradecimentos

- Bibliotecas open-source: qrcode, pandas, CustomTkinter, etc.
- Inspiração: Necessidade pessoal de gerar QR codes para dados variados.

---

**Nota**: Este README foi gerado considerando todos os arquivos e linhas de código do projeto. Para dúvidas, consulte os comentários no código ou abra uma Issue.
