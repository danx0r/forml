import forml

form1 = forml.form()
form1.input('text', "field1", value="please enter some shite")
form1.text("enter stuff:")
form1.input('text', "field2", placeholder="please enter some mo shite")
form1.br()
form1.text("gender stuff:")
form1.input('radio', "gender", "male", checked=True)
form1.input('radio', "gender", "female")
form1.input('radio', "gender", "other")
form1.br(2)
form1.submit("OKPRESSME")

bug = 10
def form1_do(field1, field2, gender):
    global bug
    bug += 1
    print "form1_do:", field1, field2, gender
    return bug
form1.do = form1_do

form2 = forml.form()
form2.input('text', "field1", value="hidden text", style="display:none")
form2.text("enter another load of stuff:")
form2.input('text', "field2", placeholder="please please hold my hand")
form2.br()
form2.text("age:")
form2.dropdown("age", "21-39", "40-49", "50 or over")
form2.br(2)
form2.submit()

def form2_do(field1, field2, age):
    print "form2_do:", field1, field2, age
form2.do = form2_do
