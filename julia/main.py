from _spy.vitollino.main import Cena , Elemento
ghostcity = Cena(img = "http://4.bp.blogspot.com/-8Iiif5ygd8k/VImL62UD2II/AAAAAAAAHvs/YeBNNJFW1EY/s1600/271517.jpg")
death = Elemento(img = "http://www.planetmoviestore.com.br/7267-thickbox_default/pre-venda-t800-bd-terminator-14-exterminador-do-futuro-.jpg"
, style=dict(top=150,left=100,height = "100px",width =100))
death.entra(ghostcity)
ghostcity.vai()
