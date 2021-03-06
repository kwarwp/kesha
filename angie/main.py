# kesha.angie.main.py
#utilizando html
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from browser import html, document, alert, doc
from browser.html import *

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> 
    <title>Torre de Londres</title>
</head>
<body>
<form action="" method="post" name="Simetrico">
    {% raw xsrf_form_html() %}
    
    <input type="hidden" name="sessionid" value="{{ SESSIONID }}" />
    <input type="hidden" name="shape" value="" />
    <input type="hidden" name="status" value="" /> 
    <input type="hidden" name="score" value="" /> 
    <input type="hidden" name="criteria" value='{{json_encode(CRITERIA)}}' /> 
    <input type="hidden" name="return_url" value="/simetrico/index" /> 


    <input type="submit" name="change" value="Tenta Novamente a Fase"            onClick="this.form.action='/api/retry';this.form.return_url.value+='?init=0'; this.form.submit();" />
    <input type="submit" name="change" value="Não quero jogar"                   onClick="this.form.action='/api/quit'; this.form.status.value='{{RESULT.QUIT}}';this.form.submit();" />
    <input type="submit" name="change" value="Desisto"                           onClick="this.form.action='/api/quit'; this.form.status.value='{{RESULT.ABORT}}';this.form.submit();" />
    <input type="submit" name="change" value="Terminei mas acho que está errado" onClick="this.form.action='/api/next'; this.form.return_url.value+='?init=1'; this.form.status.value='{{RESULT.ALMOST}}';this.form.submit();" />
    <input type="submit" name="change" value="Terminei e acho que está certo"    onClick="this.form.action='/api/next'; this.form.return_url.value+='?init=1'; this.form.status.value='{{RESULT.SUCCESS}}';this.form.submit();" />
    <h3>Fase {{ LEVEL }}</h3>
{% for bead in HAND %}
  <img alt="" src="/static/plugins/tol/{{ bead }}.png" style="width: 60px; height: 60px; position: absolute; left: 150px; top:100px" />
{% end %}
{% for model in (50,550) %}
    {% if model==50 %}
      {% for pin, size in ((0,'big'),(60,'mid'),(120,'lit')) %}
    		<input type="image" alt="" src="/static/plugins/tol/pin.png" style="width: 25px; height: {{ 240 - pin }}px; position: absolute; left: {{ model+ 2*pin }}px; top:{{ 200 + pin}}px" onClick="this.form.action='{{ size }}';this.form.submit();" />
    		{% for height, img in enumerate(BEADS[model][pin]) %}
    			<input type="image"  alt="" src="/static/plugins/tol/{{ img }}.png" style="width: 60px; height: 60px; position: absolute; left: {{ model+ 2*pin -20 }}px; top:{{ 380 - 60 * height}}px"  onClick="this.form.action='{{ size }}';this.form.submit();" />
    			
    		{% end %}
    	{% end %}
    {% else %}
        {% for pin, size in ((0,'big'),(60,'mid'),(120,'lit')) %}
            <img alt="" src="/static/plugins/tol/pin.png" style="width: 25px; height: {{ 240 - pin }}px; position: absolute; left: {{ model+ 2*pin }}px; top:{{ 200 + pin}}px" />
            {% for height, img in enumerate(BEADS[model][pin]) %}
                <img alt="" src="/static/plugins/tol/{{ img }}.png" style="width: 60px; height: 60px; position: absolute; left: {{ model+ 2*pin -20 }}px; top:{{ 380 - 60 * height}}px" />
                
            {% end %}
        {% end %}
    {% end %}
{% end %}
</form>
  </body>
</html>