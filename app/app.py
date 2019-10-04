from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping',methods=['GET'])
def ping():
    return jsonify({"mensaje": "Bienvenido"})

@app.route('/products', methods=['GET'])
def getproducts():
    return jsonify({"Mensaje":"Lista de Productos","productos": products})

@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productFound = [product for product in products if product['nombre'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"Producto":productFound[0]})
    return jsonify({"mensaje": "Producto no Encontrado"})

@app.route('/products', methods=['POST'])
def addProducto():
    new_product = {
        "nombre": request.json['nombre'], 
        "precio": request.json['precio'], 
        "cantidad": request.json['cantidad']
    }
    products.append(new_product)
    return  jsonify({
        "Mensaje":"Producto Agregado Exitosamente",
        "productos": products
    })

@app.route('/products/<string:product_name>',methods=['PUT'])
def editproduct(product_name):
    print(product_name)
    productFound = [product for product in products if product['nombre'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['nombre'] = request.json['nombre']
        productFound[0]['precio'] = request.json['precio']
        productFound[0]['cantidad'] = request.json['cantidad']
        print(productFound)
        return  jsonify({
             "Mensaje":"Producto No Encontrado",
             "productos": products
        })
    return jsonify({"mensaje": "Producto no Encontrado"})

@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteproduct(product_name):
    productFound = [product for product in products if product['nombre'] == product_name]
    if(len(productFound) > 0):
        products.remove(productFound[0])
        return  jsonify({
             "Mensaje":"Producto No Encontrado",
             "productos": products
        })
    return jsonify({"mensaje": "Producto no Encontrado"})

if __name__ == '__main__':
    app.run(debug=True,port=3000)
