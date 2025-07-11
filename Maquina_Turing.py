class Maquina_Turing:

    def __init__(self, cadena):
        self.transiciones = {
            'q0' : {'-' : ['-', 'R', 'qsigno'], # escribir, pasar, estado_siguiente
                    'num' : ['num', 'R', 'qnum'],
                    '0' : ['0', 'R', 'qcero']},
            'qsigno' : {'num' : ['num', 'R', 'qnum']},
            'qnum' : {'num' : ['num', 'R', 'qnum'],
                      '0' : ['0', 'R', 'qnum'],
                      'B' : ['', '', 'qacc']},
            'qcero' : {'B': ['', '', 'qacc']}
        }

        self.cinta = list(cadena)

        self.pasos = [] # lista de diccionarios: (estado, cinta, cabezal)
        self.transiciones_completas = [
            {"de": "q0", "a": "qsigno", "etiqueta": "-,-,R"},
            {"de": "q0", "a": "qnum", "etiqueta": "num,num,R"},
            {"de": "q0", "a": "qcero", "etiqueta": "0,0,R"},
            {"de": "q0", "a": "qrech", "etiqueta": "otro"},
            {"de": "qsigno", "a": "qrech", "etiqueta": "otro"},
            {"de": "qsigno", "a": "qnum", "etiqueta": "num,num,R"},
            {"de": "qnum", "a": "qnum", "etiqueta": "num,num,R"},
            {"de": "qnum", "a": "qrech", "etiqueta": "otro"},
            {"de": "qnum", "a": "qacc", "etiqueta": "B,B,N"},
            {"de": "qcero", "a": "qrech", "etiqueta": "otro"},
            {"de": "qcero", "a": "qacc", "etiqueta": "B,B,N"}
        ]


    def procesar_cadena(self):
        cinta = self.reescribir_cinta()
        estado_actual = 'q0'
        cabezal = 0
        celda = ''

        while estado_actual != 'qacc':
            
            self.pasos.append({"estado": estado_actual, "cinta": self.cinta, "cabezal": cabezal})
            
            try:

                if cabezal < 0:
                    cinta.insert('B')

                celda = cinta[cabezal]
                _, paso, estado_siguiente = self.transiciones[estado_actual][celda]

                if paso == 'R':
                    cabezal += 1
                elif paso == 'L':
                    cabezal -= 1

                estado_actual = estado_siguiente
            
            except KeyError:
                estado_actual = 'qrech' 
                break

        if estado_actual == 'qacc':
            print('la cadena es aceptada por la máquina') 

        elif estado_actual == 'qrech':
            print(f"la cadena ha sido rechazada por la máquina")

            if cinta[0] == '0' and len(cinta) > 1:
                print('No se permiten ceros a la izquierda exceptuando el caso del 0 mismo') 
            if '.' in cinta or ',' in cinta:
                print('Solo se permiten números enteros')

        self.pasos.append({"estado": estado_actual, "cinta": self.cinta, "cabezal": cabezal})  # guarda último paso
        return estado_actual 
         
    
    def reescribir_cinta(self): 
        self.cinta.append('B')

        tokens_convertidos = [
            'num' if token.isdigit() and 1 <= int(token) <= 9 else token
            for token in self.cinta
            ]
        
        print("cinta ->", self.cinta)

        return tokens_convertidos
