# Importando bibliotecas/módulos
import requests
from deep_translator import GoogleTranslator
import os
import platform

# Função que limpa o terminal dependendo do Sistema Operacional
def limpar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Função que pausa o terminal dependendo do Sistema Operacional
def pausar_terminal():
    if platform.system() == "Windows":
        os.system('pause')
    else:
        os.system('read -p "Pressione qualquer tecla para continuar..."')

class Conselhos:
    """
    Classe Conselhos que busca conselhos da API Advice Slip e os traduz do inglês para o português.
    """
    def __init__(self):
        """
        Construtor da classe Conselhos.
        Inicializa o tradutor e o dicionário de conselhos e chama o método mostra_conselho.
        """
        self.tradutor = GoogleTranslator(source = 'en', target = 'pt')
        self.tradutor_consulta = GoogleTranslator(source = 'en', target = 'pt')
        self.conselhos = {} # Armazena todos os conselhos gerados
        self.conselhos_consulta = {} # Armazena todos os conselhos consultados
        self.mostra_conselho()
        self.conselhos_consulta()
        self.procura_conselhos_id()

    def mostra_conselho(self):
        """
        Método que faz uma requisição à API Advice Slip, traduz o conselho recebido para o português e o armazena no dicionário de conselhos.
        Retorna o conselho traduzido.
        """
        self.url = 'https://api.adviceslip.com/advice'
        self.resposta = requests.get(self.url)
        self.dados = self.resposta.json()
        self.texto = self.dados['slip']['advice']
        self.traducao = self.tradutor.translate(self.texto)
        self.id = self.dados['slip']['id']

        self.conselho = [
            '\n',
            '=' * 100,
            f'--- Conselho (ID): {self.id} ---'.center(100),
            '-' * 100,
            'Texto original (Inglês):',
            self.texto,
            '\nTexto traduzido (Português - Brazil):',
            self.traducao,
            '=' * 100
        ]
        
        # Armazena o conselho gerado
        self.conselhos[self.id] = '\n'.join(self.conselho)
        
        return self.conselhos[self.id]
            
    def procura_conselho(self, id):
        """
        Método que procura um conselho pelo ID no dicionário de conselhos.
        Retorna o conselho se encontrado, caso contrário retorna uma mensagem de erro.
        """
        self.id = id
        if id in self.conselhos: # Verifica se o ID está no dicionário self.conselhos
            return self.conselhos[id]
        else:
            return f'ID de conselho {id} não encontrado.'
        
    def conselhos_mostrados_antes(self):
        """
        Método que imprime os IDs de todos os conselhos guardados no dicionário.
        """
        print('Conselhos Guardados'.center(100))
        for itens in self.conselhos:
            print(f'- ID: {itens}')

def conselhos_consulta(self, consulta):
    self.consulta = consulta
    self.url_consulta = f'https://api.adviceslip.com/advice/search/{consulta}'
    
    self.resposta_consulta = requests.get(self.url_consulta)
    self.dados_consulta = self.resposta_consulta.json()
    
    self.textos_consultado = self.dados_consulta['slip']['advice']
    self.traducao_consulta = self.tradutor.translate(self.textos_consultado)
    self.resultados_totais = len(self.dados_consulta['slips'])

    self.conselho_consulta = [
        '\n',
        '=' * 100,
        f'--- Conselho Consultado (ID): {self.id_consulta} ---'.center(100),
        '-' * 100,
        'Texto original (Inglês):',
        self.textos_consultado,
        '\nTexto traduzido (Português - Brazil):',
        self.traducao_consulta,
        '=' * 100
    ]

    # Armazena o conselho gerado
    self.conselhos[self.id_consulta] = '\n'.join(self.conselho_consulta)
    
    return self.conselhos[self.id_consulta]

        
    def procura_conselhos_id(self, id):
        self.id = id
        
        return None

classe_conselhos = Conselhos()

menu = [
    '\n',
    '=' * 100,
    'Menu de Conselhos'.center(100),
    '-' * 100,
    '[1] Mostrar conselho aleatório',
    '[2] Procurar conselho gerado anteriormente por ID',
    '[3] Mostrar conselhos por ID já guardado',
    '[4] Procurar conselho por palavra-chave/termo',
    '[5] Procurar conselho por número de ID',
    '[6] Sair',
    '=' * 100
]

while True:
    try:
        limpar_terminal()
        
        for item in menu:
            print(item)
        op = int(input('Opção: '))

        match op:    
            case 1:
                print(classe_conselhos.mostra_conselho())
                
            case 2:
                while True:
                    id = int(input('\nProcurar ID: '))
                    print('Procurando conselho...')
                    procurar_id = classe_conselhos.procura_conselho(id)
                    
                    if procurar_id == f'ID de conselho {id} não encontrado.':
                        classe_conselhos.mostra_conselho()
                        print(classe_conselhos.procura_conselho(id))
                    else:
                        print(procurar_id)
                    
                    continuar = str(input('Procurar outro ID? (S/N)\nOpção: ')).strip().lower()
                    
                    if continuar == 'n' or continuar == 'não' or continuar == 'nao':
                        break
                    
            case 3:
                classe_conselhos.conselhos_mostrados_antes()
            
            case 4:
                consulta = input('Consulte uma palavra-chave: ')

                if type(consulta) == str:
                    consulta.strip().lower()

                classe_conselhos.conselhos_consulta(consulta)

            case 5:
                id = int(input('Digite um ID: '))
                
                classe_conselhos.procura_conselhos_id(id)

            case 6:
                limpar_terminal()
                print('\nSaindo...')
                break
            
            case other:
                print('\nERRO: Opção inválida.\nSelecione entre [1] e [4]')
                
        pausar_terminal()
                
    except TypeError:
        print('\nErro: tipo de argumento inapropriado.')
        pass
    except KeyError:
        print('\nErro: Argumento não encontrado.')
        pass
    except ValueError:
        print('\nErro: Valor inválido à atributo.')
        pass
    except requests.exceptions.HTTPError as errh:
        print(f'\nErro HTTP: {errh}.')
    except requests.exceptions.ConnectionError as errc:
        print(f'\nErro de conexão: {errc}.')
    except requests.exceptions.Timeout as errt:
        print(f'\nTempo de resposta excedido: {errt}.')
    except requests.exceptions.RequestException as err:
        print(f'\nErro de aquisição: {err}.')
        