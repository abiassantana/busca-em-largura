graph = {'joao pessoa':['itabaiana', 'campina grande', 'santa rita'],
         'itabaiana': ['joao pessoa','campina grande'],
         'campina grande': ['joao pessoa','itabaiana','areia','coxixola', 'soledade'],
         'santa rita': ['joao pessoa','mamanguape'],
         'mamanguape': ['santa rita','guarabira'],
         'guarabira':['mamanguape','areia'],
         'areia':['guarabira','campina grande'],
         'soledade': ['campina grande','picui', 'patos'],
         'coxixola': ['campina grande', 'monteiro'],
         'picui':['soledade'],
         'patos': ['soledade','itaporanga', 'pombal'],
         'monteiro': ['coxixola','itaporanga'],
         'pombal': ['patos','catole do rocha', 'sousa'],
         'itaporanga': ['patos','monteiro','cajazeiras'],
         'catole': ['pombal'],
         'sousa': ['pombal','cajazeiras'],
         'cajazeiras': ['itaporanga', 'sousa']
         }


class busca_em_largura(object):

    def __init__(self, graph, initial_state, final_state):
        self.graph = graph
        self.initial_state = initial_state
        self.final_state = final_state
        self.explored = []
        self.bordas = []

    #recebe uma string corespondente a um ponto no grapfo
    #adiciona a borda os pontos nao explorados
    def find_borda(self, point):
        for borda in graph[point]:
            if borda not in self.bordas:
                if borda not in self.explored:
                    self.bordas.append(borda)

    def explore(self, point, steps):
        self.explored.append(point)
        if point != self.initial_state:
            self.bordas.remove(point)
        self.find_borda(point)

    def walk(self):
        while self.final_state not in self.explored:
            #print(self.bordas)
            if len(self.bordas)>0:
                self.explore(self.bordas[0])
                

    def search(self):
        self.explore(self.initial_state)
        self.walk()
        print(self.explored)
        

busca = busca_em_largura(graph,'joao pessoa', 'cajazeiras')
busca.search()

        

    
        
