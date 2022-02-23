class Birds:
    def __init__(self):
        ''' Something something constructor'''
        # Create some member animals
        self.members = ['Dove', 'Hen', 'Pigeon']
        
    def printMember(self):
        print('Print members of the Birds class')
        
        for member in self.members:
            print('\t%s' % member)