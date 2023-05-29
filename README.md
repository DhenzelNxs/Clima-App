# Previs-o-do-Tempo-App
Um app de previsão do tempo que mostra todas as informações climaticas da cidade que você buscar, as informações são geradas a partir de uma api

Na linha 47 é informado a Api na qual o app buscará as informações:
api="https://api.openweathermap.org/data/2.8/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid={API Key}"

Na String acima, na API KEY você deve preencher com a sua API Propria gerada do site climatico que fornece as informações
SITE = https://openweathermap.org/
acesse o site, Registre-se e na aba 'Yours API' Gere sua APi e depois modifique no codigo
