# Conselhos Aleatórios

Este projeto é uma aplicação Python que busca conselhos aleatórios da API Advice Slip e os traduz do inglês para o português.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `requests`
- `deep_translator`

Você pode instalar essas dependências usando pip:

```bash
pip install requests
```

```bash
pip install deep_translator
```

## Uso

Para usar este programa, siga estas etapas:

1. Clone o repositório para o seu computador local.
2. Navegue até o diretório do projeto no terminal.
3. Execute o script Python com o comando `python main.py` (ou `python3 main.py`, dependendo da sua configuração do Python).
4. Você verá um menu com várias opções. Digite o número da opção que você deseja selecionar e pressione Enter.
5. As opções do menu são as seguintes:
    - `[1] Mostrar conselho aleatório`: Esta opção buscará um conselho aleatório da API Advice Slip, traduzirá para o português e exibirá o conselho.
    - `[2] Procurar conselho gerado anteriormente por ID`: Esta opção permitirá que você digite um ID de conselho. Se o conselho com esse ID foi gerado anteriormente durante a execução do programa, ele será exibido.
    - `[3] Mostrar ID de conselhos guardados`: Esta opção exibirá os IDs de todos os conselhos que foram gerados e guardados durante a execução do programa.
    - `[4] Sair`: Esta opção encerrará o programa.

## Limitações

Por favor, note que a API Advice Slip não fornece uma maneira de buscar um conselho específico por ID. Portanto, a opção `[2] Procurar conselho gerado anteriormente por ID` só pode buscar conselhos que já foram gerados durante a execução do programa.