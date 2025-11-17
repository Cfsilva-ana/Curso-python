# Configuração do Ambiente Python no VS Code

## 1. Instalação do Python

1. Baixe o Python 3.13 do site oficial: https://www.python.org/downloads/
2. Durante a instalação, marque "Add Python to PATH"
3. Instale no diretório padrão: `C:\Users\{seu_usuario}\AppData\Local\Programs\Python\Python313\`

## 2. Instalação do VS Code

1. Baixe o VS Code: https://code.visualstudio.com/
2. Instale com as configurações padrão

## 3. Extensões Necessárias

Instale as seguintes extensões no VS Code:

- **Python** (Microsoft) - Suporte completo para Python
- **Code Runner** (Jun Han) - Para executar código rapidamente
- **Material Icon Theme** (Philipp Kief) - Ícones dos arquivos
- **OM Theme** - Tema Dracula com itálico

## 4. Configuração do VS Code

Adicione as seguintes configurações no arquivo `settings.json`:

```json
{
    "window.zoomLevel": 0,
    "workbench.startupEditor": "none",
    "explorer.compactFolders": false,
    "workbench.iconTheme": "material-icon-theme",
    "editor.fontSize": 18,
    "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
    "code-runner.executorMap": {
        "python": "clear ; py -u",
    },
    "code-runner.runInTerminal": true,
    "code-runner.ignoreSelection": true,
    "python.defaultInterpreterPath": "c:\\Users\\[usuario]\\AppData\\Local\\Programs\\Python\\Python313\\python.exe",
    "workbench.statusBar.visible": false,
    "explorer.confirmDragAndDrop": false
}
```

## 5. Testando a Instalação

1. Crie um arquivo `teste.py`
2. Adicione o código: `print("Hello, Python!")`
3. Execute com `Ctrl + F5` ou clique no botão ▶️ do Code Runner

## 6. Atalhos Úteis

- `Ctrl + F5` - Executar código
- `Ctrl + Shift + P` - Paleta de comandos
- `Ctrl + '` - Abrir terminal