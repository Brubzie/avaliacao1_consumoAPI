# Importando bibliotecas/módulos
import requests
from deep_translator import GoogleTranslator

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
        self.conselhos = {} # Armazena todos os conselhos gerados
        self.mostra_conselho()

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
            f'--- ID: {self.id} ---'.center(100),
            '-' * 100,
            'Texto original (en):',
            self.texto,
            '\nTexto traduzido (pt):',
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
        if id in self.conselhos: # Verifica se o ID está no dicionário self.conselhos
            return self.conselhos[id]
        else:
            return f'ID de conselho {id} não encontrado.'
        
    def conselhos_guardados(self):
        """
        Método que imprime os IDs de todos os conselhos guardados no dicionário.
        """
        for itens in self.conselhos:
            print(f'- ID: {itens}')

conselhos = Conselhos()

menu = [
    '\n',
    '=' * 100,
    'Menu de Conselhos'.center(100),
    '-' * 100,
    '[1] Mostrar conselho aleatório',
    '[2] Procurar conselho gerado anteriormente por ID',
    '[3] Mostrar ID de conselhos guardados',
    '[4] Sair',
    '=' * 100
]

while True:
    try:
        for item in menu:
            print(item)
        op = int(input('Opção: '))

        match op:    
            case 1:
                print(conselhos.mostra_conselho())
                
            case 2:
                while True:
                    id = int(input('\nProcurar ID: '))
                    print('Procurando conselho...')
                    procurar_id = conselhos.procura_conselho(id)
                    
                    if procurar_id == f'ID de conselho {id} não encontrado.':
                        conselhos.mostra_conselho()
                        print(conselhos.procura_conselho(id))
                    else:
                        print(procurar_id)
                    
                    continuar = str(input('Continuar a procurar ID? (S/N)\nOpção: ')).strip().lower()
                    
                    if continuar == 'n' or continuar == 'não' or continuar == 'nao':
                        break
                    
            case 3:
                conselhos.conselhos_guardados()
                    
            case 4:
                print('\nSaindo...')
                break
            
            case other:
                print('\nERRO: Opção inválida.\nSelecione entre [1] e [4]')
                
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
        