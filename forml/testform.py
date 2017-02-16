import forml

form = forml.form()
form.input('text', "field1", value="please enter some shite")
form.text("enter stuff:")
form.input('text', "field2", placeholder="please enter some mo shite")
form.br()
form.text("gender stuff:")
form.br()
form.input('radio', "gender", "male", checked=True)
form.input('radio', "gender", "female")
form.input('radio', "gender", "other")
form.br(2)
form.submit("OKPRESSME")
