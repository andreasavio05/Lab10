import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            threshold = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.show_alert('Inserisci un numero valido')
            return

        self._model.costruisci_grafo(threshold)

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di hub: {self._model.get_num_nodes()}'))

        self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di tratte: {self._model.get_num_edges()}'))

        for u, v, peso in self._model.get_all_edges():
            self._view.lista_visualizzazione.controls.append(ft.Text(f'{u.nome} ({u.stato}) {v.nome} ({v.stato}) : {peso} $'))

        self._view.update()

