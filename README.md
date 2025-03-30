# Godaddy Dyndns

### El script es para actualizar la ip de los subdominios en godaddy


Se tiene que crear un archivo config.json en la carpeta raiz del proyecto

Ejemplo:

{
    "GODADDY_API_KEY": "",
    "GODADDY_API_SECRET": "",
    "TIMEOUT": 1,
    "tasks": [
        {
            "domain": "dominio.com",
            "record_name": "subdominio",
            "record_type": "A",
            "last_public_ip": "0.0.0.0"
        }
    ]
}
