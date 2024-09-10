class Lampada:
    def __init__(self):
        self.estado = 'apagada'  
    def ligar(self):
        self.estado = 'acesa'

    def desligar(self):
        self.estado = 'apagada'

    def esquentar(self):
        if self.estado == 'acesa':
            self.estado = 'acesa_quente'


lampada1 = Lampada()
lampada2 = Lampada()
lampada3 = Lampada()

def interruptor1():
    lampada1.ligar()
    lampada1.esquentar()  

def interruptor2():
    lampada2.ligar()

def interruptor3():
    lampada3.ligar()


def descobrir_interruptores():
    
    interruptor1()

    
    lampada1.desligar() 
    interruptor2()  

    
    print("Estado da lâmpada 1:", lampada1.estado)
    print("Estado da lâmpada 2:", lampada2.estado)
    print("Estado da lâmpada 3:", lampada3.estado)

   
    if lampada2.estado == 'acesa':
        print("Lâmpada 2 é controlada pelo Interruptor 2")

    if lampada1.estado == 'acesa_quente':
        print("Lâmpada 1 é controlada pelo Interruptor 1")

    if lampada3.estado == 'apagada':
        print("Lâmpada 3 é controlada pelo Interruptor 3")


descobrir_interruptores()