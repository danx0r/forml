# generate a form

class form(object):
    
    def __init__(self):
        self.rows=[]
        
    def input(self, type, name, value = None, **kw):
        row = '<type="%s" input name="%s"' % (type, name)
        if value != None:
            row += ' value="%s"' % value
        for k in kw:
            if k == True:
                row += ' %s'
            else:
                row += ' %s="%s"'
        row += '/>'
        print row
        self.rows.append(row)
        
f = form()
f.input('text', "field1", "please enter some shite")