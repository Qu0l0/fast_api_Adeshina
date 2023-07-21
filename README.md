# fast_api_Adeshina
# книга Adbulaziz_Abdulaziz_Adeshina_Sozdanie_veb-API_Python_s_pomoschyu_FastAPI.pdf 
# git https://github.com/PacktPublishing/Building-Python-Web-APIs-with-FastAPI/tree/main
# страница 57

curl -X "POST" "http://127.0.0.1:8000/todo" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\": \"1\",\"item\": \"one\" }"
curl -X "GET" "http://127.0.0.1:8000/todo" -H "accept: application/json"
curl -X "PUT" "http://127.0.0.1:8000/todo/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":\"1\",\"item\": \"Read the next chapter of the book\"}"
