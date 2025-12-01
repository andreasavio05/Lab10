from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        hubs = DAO.readHub()
        hubs_dict = {hub.id: hub for hub in hubs}
        spedizioni = DAO.readSpedizioni(hubs_dict)

        self.G.clear()
        for hub in hubs:
            self.G.add_node(hub)

        for spedizione in spedizioni:
            if spedizione.peso >= threshold:
                self.G.add_edge(spedizione.hub1, spedizione.hub2, weight=spedizione.peso)

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return [(u, v, d['weight']) for u, v, d in self.G.edges(data=True)]

