from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)



    

    # The shopping cart
    cart = []

    class Item:
        def __init__(self, name):
            self.name = name

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/product')
    def product():
        return render_template('product.html')

    @app.route('/add_to_cart/<item>')
    def add_to_cart(item):
        cart.append(Item(item))
        return redirect(url_for('product'))

    @app.route('/cart')
    def view_cart():
        return render_template('cart.html', cart=cart)

    @app.route('/remove_from_cart/<item>')
    def remove_from_cart(item):
        for i in cart:
            if i.name == item:
                cart.remove(i)
                break
        return redirect(url_for('cart'))

    if __name__ == '__main__':
        app.run(debug=True)


        from flask import Flask, render_template, request, redirect, url_for
        from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

        app = Flask(__name__)
        app.secret_key = 'your secret key'

        login_manager = LoginManager()
        login_manager.init_app(app)

        class User(UserMixin):
            def __init__(self, id):
                self.id = id

        @login_manager.user_loader
        def load_user(user_id):
            return User(user_id)

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                user_id = request.form.get('user_id')
                user = User(user_id)
                login_user(user)
                return redirect(url_for('home'))
            return render_template('login.html')

        @app.route('/logout')
        @login_required
        def logout():
            logout_user()
            return redirect(url_for('home'))

        # Your other routes and code go here

        if __name__ == '__main__':
            app.run(debug=True)

            

            from flask import Flask, render_template, request, redirect, url_for

            app = Flask(__name__)

            # Assume we have a list of products
            products = ['Product 1', 'Product 2', 'Product 3']

            @app.route('/search', methods=['GET', 'POST'])
            def search():
                if request.method == 'POST':
                    query = request.form.get('query')
                    results = [product for product in products if query.lower() in product.lower()]
                    return render_template('search_results.html', results=results)
                return render_template('search.html')

            # Your other routes and code go here

            if __name__ == '__main__':
                app.run(debug=True)


    