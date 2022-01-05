

class Cell:
    def __init__(self):
        self._status = 'dead'

    def set_dead(self):
        self._status = 'dead'
    
    def set_live(self):
        self._status = 'live'

    def check_live(self):
        if self._status == 'live':
            return True
        else:
            return False

    def value_on_field(self):

        if self.check_live():
            return '*'
        else:
            return '.'
