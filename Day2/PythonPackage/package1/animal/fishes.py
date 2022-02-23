class Fishes:
    def __init__(self):
        ''' Something something constructor'''
        # Create some member animals
        self.members = ['Azu ndu', 'Alila', 'Asa']
        
    def printMember(self):
        print('Print members of the Fishes class')
        
        for member in self.members:
            print('\t%s' % member)