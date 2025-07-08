swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/docs.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "To-Do API",
        "description": "Essa API é o backend do meu aplicativo de tarefas To-Do.",
        "version": "1.0"
    },
    "basePath": "/",
    "schemes": ["http"]
}