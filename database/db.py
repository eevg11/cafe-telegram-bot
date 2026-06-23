import sqlite3

DB_NAME = "cafe.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Таблица товаров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Таблица корзины
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER DEFAULT 1,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    ''')
    
    # Заполним меню тестовыми данными, если таблица пустая
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        menu_items = [
            ("Espresso", 40.0),
            ("Cappuccino", 55.0),
            ("Croissant", 60.0),
            ("Cheesecake", 75.0)
        ]
        cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", menu_items)
        
    conn.commit()
    conn.close()

def get_menu():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def add_to_cart(user_id: int, product_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Проверяем, есть ли уже такой товар в корзине у юзера
    cursor.execute("SELECT id, quantity FROM cart WHERE user_id = ? AND product_id = ?", (user_id, product_id))
    item = cursor.fetchone()
    
    if item:
        cursor.execute("UPDATE cart SET quantity = quantity + 1 WHERE id = ?", (item[0],))
    else:
        cursor.execute("INSERT INTO cart (user_id, product_id) VALUES (?, ?)", (user_id, product_id))
        
    conn.commit()
    conn.close()

def get_cart(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT products.name, products.price, cart.quantity 
        FROM cart 
        JOIN products ON cart.product_id = products.id 
        WHERE cart.user_id = ?
    ''', (user_id,))
    items = cursor.fetchall()
    conn.close()
    return items

def clear_cart(user_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()