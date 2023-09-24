from flask import Flask, request, jsonify, render_template
from models import db, Cupcake,connect_db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='Fooster2023'

connect_db(app)

@app.route('/')
def home():
    """The cupcake home page"""
    return render_template('index.html')


@app.route('/api/cupcakes')
def get_cupcake():
    """API to get all cupcakes"""
    all_cupcakes=[cup.ser_cups() for cup in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_one_cupcake(id):
    """retreives just one cupcake based on ID"""
    cupcake=Cupcake.query.get_or_404(id)
    
    jscup=cupcake.ser_cups()
    return jsonify(cupcake=jscup)

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """Adds a cupcake"""
    new_cupcake= Cupcake(flavor=request.json['flavor'], size=request.json['size'], 
                         rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    return(jsonify(cupcake=new_cupcake.ser_cups()), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_one_cupcake(id):
    """updates a cupcake"""
    update_cupcake=Cupcake.query.get_or_404(id)
    req=request.json
    update_cupcake.flavor = req.get('flavor', update_cupcake.flavor)
    update_cupcake.size = req.get('size', update_cupcake.size)
    update_cupcake.rating = req.get('rating', update_cupcake.rating)
    update_cupcake.image = req.get('image', update_cupcake.image)
    db.session.add(update_cupcake)
    db.session.commit()
        
    jscup=update_cupcake.ser_cups()
    return jsonify(cupcake=jscup)

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def del_a_cupcake(id):
    """deletes a cupcake"""
    del_cupcake=Cupcake.query.get_or_404(id)
    db.session.delete(del_cupcake)
    db.session.commit()
    return jsonify(message="deleted")

    