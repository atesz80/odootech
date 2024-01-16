from dataclasses import dataclass
import json
import os
import pprint

# -----------------------------------------------------------

@dataclass(frozen=True)
class Auto(object):

    """ ------ Az autó típusú objektum leírása ------- """

    id: str
    type: int
    ajtok_szama: int
    marka: str
    
    @property
    def get_auto(self):
        return(f'{self.id}, {self.type}, {self.ajtok_szama}, {self.marka}')

@dataclass(frozen=True)
class Bicikli(object):

    """ ------ A bicikli típusú objektum leírása ------- """

    id: str
    type: int
    terhelhetoseg: int
    marka: str
    
    @property
    def get_bicikli(self):
        return(f'{self.id}, {self.type}, {self.terhelhetoseg}, {self.marka}')


if __name__ == "__main__":

    pprint.pprint(' -- A script futása elkezdődött! --')

    def levalogatas(tipus: str = "auto") -> list:


        """ Objektumok listáját adja vissza a függvény """


        lista = []
        file_list = []            

        for dirpath, _, fnames in os.walk("./data"):
            for f in fnames:
                if f.endswith(".dat"):
                    file_list.append({'path': dirpath, 'file': f})

        for file in file_list:
            with open(os.path.join(file['path'], file['file']), 'r') as f:
                    
                data = {'id': file['file']}
                data.update(json.load(f))

                if data['type'] == tipus:
                    if tipus == 'auto':
                        lista.append(Auto(*data.values()))

                    elif tipus == 'bicikli':
                        lista.append(Bicikli(*data.values()))

        if not lista:
           
            pprint.pprint('Nincs ilyen eszköz!')
    
        return lista
    

    def kiiratas(lista: list) -> None:
        
        """ Kiirja a függvény a képernyőre a listában lévő objektumokat """

        if lista:
            pprint.pprint(lista, indent=1, width=1)

    kiiratas(levalogatas(tipus='bicikli'))

pprint.pprint(' -- A script futása befejeződött! --')
exit(0)
