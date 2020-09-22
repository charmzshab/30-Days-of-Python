Set-Variable FLASk_APP = server1.py 
$env:FLASK_APP = "server1.py"
flask run --host=127.0.0.1 --port=8000