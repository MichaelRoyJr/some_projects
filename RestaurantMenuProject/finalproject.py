from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/')
def showRestaurant():
    restaurants = session.query(Restaurant).all()
    if restaurants == [{}]:
        flash('You currently have no restaurants')
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurants/new/', methods = ['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        restaurantToAdd = Restaurant(name=request.form['name'])
        session.add(restaurantToAdd)
        session.commit()
        flash('New Restaurant Created')
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('newrestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit/',methods = ['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurantToEdit = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            restaurantToEdit.name = request.form['name']
        session.add(restaurantToEdit)
        session.commit()
        flash("Restaurant Successfully Edited")
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('editrestaurant.html', restaurant=restaurantToEdit)

@app.route('/restaurants/<int:restaurant_id>/delete/', methods = ['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        flash('Restaurant Deleted')
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('deleterestaurant.html', restaurant=restaurantToDelete)

@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    if items ==[{}]:
        flash('You have no menu items')
    return render_template('restaurantmenu.html', restaurant=restaurant, items=items)

@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        newMenuItem = MenuItem(name=request.form['name'], restaurant_id=restaurant.id, price=request.form['price'], description=request.form['description'], course=request.form['course'])
        session.add(newMenuItem)
        session.commit()
        flash('Menu Item Created')
        return redirect(url_for('showMenu', restaurant_id=restaurant.id))
    else:
        return render_template('newmenuitem2.html', restaurant_id=restaurant.id)
    
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    updateItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            updateItem.name = request.form['name']
        if request.form['price']:
            updateItem.price = request.form['price']
        if request.form['description']:
            updateItem.description = request.form['description']
        if request.form['course']:
            updateItem.course = request.form['course']
        session.add(updateItem)
        session.commit()
        flash('Menu ItemSuccessfully Edited')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem2.html', restaurant_id=restaurant_id, item=updateItem)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem2.html', restaurant_id=restaurant_id, item=deleteItem)

@app.route('/restaurants/JSON/')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants = [r.serialize for r in restaurants])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id = menu_id).one()
    return jsonify(MenuItem = item.serialize)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)