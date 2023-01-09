from app import app, routes

if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context=('cert.pem', 'key.pem'), port=443)
