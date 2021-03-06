# generate a form

class form(object):
    
    def __init__(self):
        self.rows=[]
        
    def input(self, type, name, textvalue = None, **kw):
        row = '  <input type="%s" name="%s"' % (type, name)
        if textvalue:
            kw['text'] = textvalue                 #means value & text same
            kw['value'] = textvalue
        for k, v in kw.items():
            if k == 'text':
                continue
            if v == True and str(v) == "True":           #@blach
                row += ' %s' % k
            else:
                row += ' %s="%s"' % (k, v)
        if 'text' in kw:
            row += '>%s</input>' % kw['text']
        else:
            row += '/>'
        self.rows.append(row)
        
    def dropdown(self, name, *options):
        self.rows.append('  <select name="%s">' % name)
        for opt in options:
            row = '    <option value="%s">%s</option>' % (opt, opt)
            self.rows.append(row)
        self.rows.append('  </select>')
        
    def submit(self, text = "OK"):
        row = '  <button type="submit">%s</button>' % (text)
        self.rows.append(row)
        
    def text(self, text):
        self.rows.append(text)
    
    def br(self, cnt=1):
        if cnt == 1:
            self.rows.append("<notreallyatag/>")
        for i in range(cnt-1):
            self.rows.append("<br/>")
    
    def html(self, bugg=0):
        s = "\n<form>bugg=%d\n" % bugg
        for r in self.rows:
            if "<" not in r:                                        #no brk for text
                s += r + '\n'
            elif r.strip().find('<input type="radio"') == 0:        #or radio
                s += r + '\n'
            elif r.strip().find('display:none') > 0:                #or hidden
                s += r + '\n'
            else:                                                   #'Kk, line brk
                s += r + '<br/>\n'
        s += "</form>\n"
        return s
        
if __name__ == "__main__":
    f1 = form()
    f1.input('text', "field1", "please enter some shite")
    f1.text("enter stuff:")
    f1.input('text', "field2", placeholder="please enter some mo shite")
    f1.input('radio', "gender", "male")
    f1.input('radio', "gender", "female")
    f1.input('radio', "gender", "other")
    f1.submit("OKPRESSME")
    print f1.html()
