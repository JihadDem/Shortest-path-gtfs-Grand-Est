from model import Model
from view import View
from PyQt4.QtGui import QApplication

class App(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)
        self.view = View(self)
        self.model = Model(self)
        self.reloadStops()
        self.exec_()

    # FROM MODEL TO VIEW
    def askNewWorkspace(self, path = '~'): return self.view.askNewWorkspace(path)
    def askInitWorkspace(self): return self.view.askInitWorkspace()
    def askInitWorkspaceParameters(self, lat, lon, r): return self.view.askInitWorkspaceParameters(lat, lon, r)
    def showLoading(self, txt): return self.view.showLoading(txt)

    # FROM VIEW TO MODEL
    def reloadStops(self, modes = [1, 3]):
        names, ids, lats, lons, types = self.model.workspace.getAllStops(modes)
        self.view.drawStops(lats, lons, types)
        self.view.fillStopSelectors(ids, names)
    def drawStopPath(self, path, withStopTimes = False):
        names, ids, lats, lons, types, rnames, rcols = self.model.workspace.getStopsByStopIds(path)
        self.view.drawStopPath(lats, lons)
        if withStopTimes != False: self.view.fillResultTable(withStopTimes, names, types, rnames, rcols)
    def runShortestPath(self, modes, params):
        stop_ids, stop_times = self.model.dijkstra(params['from_stop_id'], params['departure_time'], params['to_stop_id'], modes)
        self.drawStopPath(stop_ids, stop_times)