class Mammals:
    def __init__(self):
        ''' Something something constructor'''
        # Create some member animals
        self.members = ['Whale', 'Monkey', 'Elephant']
        
    def printMember(self):
        print('Print members of the Mammals class')
        
        for member in self.members:
            print('\t%s' % member)