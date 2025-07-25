# app.py

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

# 初始化 Flask 應用
app = Flask(__name__)

# 配置資料庫
# 'sqlite:///site.db' 表示在專案根目錄下建立一個名為 site.db 的 SQLite 檔案
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 禁用 SQLAlchemy 事件追蹤，節省資源

# 初始化 SQLAlchemy，將其與 Flask 應用綁定
db = SQLAlchemy(app)

# ====================================================================
# 定義資料庫模型 (這裡用於儲存作品集項目)
# ====================================================================
class PortfolioItem(db.Model):
    # 定義表格名稱 (可選，預設是類名的小寫)
    __tablename__ = 'portfolio_items'

    id = db.Column(db.Integer, primary_key=True) # 主鍵，自動遞增
    image_url = db.Column(db.String(200), nullable=False) # 圖片路徑或 URL
    description = db.Column(db.Text, nullable=False) # 文字敘述
    
    # 也可以添加其他欄位，例如：
    # title = db.Column(db.String(100), nullable=False)
    # created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        # 定義物件的字符串表示形式，方便調試
        return f'<PortfolioItem {self.id}: {self.image_url}>'
    
class pixelartItem(db.Model):
    # 定義表格名稱 (可選，預設是類名的小寫)
    __tablename__ = 'pixelartItem_items'

    id = db.Column(db.Integer, primary_key=True) # 主鍵，自動遞增
    image_url = db.Column(db.String(200), nullable=False) # 圖片路徑或 URL
    description = db.Column(db.Text, nullable=False) # 文字敘述
    
    # 也可以添加其他欄位，例如：
    # title = db.Column(db.String(100), nullable=False)
    # created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        # 定義物件的字符串表示形式，方便調試
        return f'<pixelartItem {self.id}: {self.image_url}>'
    
class gameinfoItem(db.Model):
    # 定義表格名稱 (可選，預設是類名的小寫)
    __tablename__ = 'gameinfoItem_items'

    id = db.Column(db.Integer, primary_key=True) # 主鍵，自動遞增
    image_url = db.Column(db.String(200), nullable=False) # 圖片路徑或 URL
    description = db.Column(db.Text, nullable=False) # 文字敘述
    
    # 也可以添加其他欄位，例如：
    # title = db.Column(db.String(100), nullable=False)
    # created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        # 定義物件的字符串表示形式，方便調試
        return f'<gameinfoItem {self.id}: {self.image_url}>'

# ====================================================================
# 創建資料庫表格 (如果資料庫檔案或表格不存在)
# ====================================================================
with app.app_context():
    db.create_all() # 這會根據上面定義的模型創建所有表格

    # 也可以在這裡添加一些初始數據 (只在第一次運行時添加)
    if PortfolioItem.query.count() == 0: # 如果資料庫中沒有任何作品項目
        print("Adding initial portfolio items...")
        item1 = PortfolioItem(image_url='/static/images/artwork1.png', description='這是我的第一個像素藝術作品，靈感來自於復古遊戲。')
        item2 = PortfolioItem(image_url='/static/images/artwork2.png', description='這是一幅關於自然風景的像素畫，使用了暖色調。')
        item3 = PortfolioItem(image_url='/static/images/artwork3.png', description='我的遊戲專案概念圖，展示了角色和場景設計。')
        item4 = PortfolioItem(image_url='/static/images/artwork4.png', description='與客戶合作的商業像素插畫，用於網站橫幅。')

        db.session.add_all([item1, item2, item3, item4]) # 將所有項目添加到會話
        db.session.commit() # 提交更改到資料庫
        print("Initial portfolio items added.")
        
    if pixelartItem.query.count() == 0: # 如果資料庫中沒有任何作品項目
        print("Adding initial portfolio items...")
        item1 = pixelartItem(image_url='/static/images/artwork1.png', description='這是我的第一個像素藝術作品，靈感來自於復古遊戲。')
        item2 = pixelartItem(image_url='/static/images/artwork2.png', description='這是一幅關於自然風景的像素畫，使用了暖色調。')
        item3 = pixelartItem(image_url='/static/images/artwork3.png', description='我的遊戲專案概念圖，展示了角色和場景設計。')
        item4 = pixelartItem(image_url='/static/images/artwork4.png', description='與客戶合作的商業像素插畫，用於網站橫幅。')

        db.session.add_all([item1, item2, item3, item4]) # 將所有項目添加到會話
        db.session.commit() # 提交更改到資料庫
        print("Initial portfolio items added.")
        
    if gameinfoItem.query.count() == 0: # 如果資料庫中沒有任何作品項目
        print("Adding initial portfolio items...")
        item1 = gameinfoItem(image_url='/static/images/artwork1.png', description='這是我的第一個像素藝術作品，靈感來自於復古遊戲。')
        item2 = gameinfoItem(image_url='/static/images/artwork2.png', description='這是一幅關於自然風景的像素畫，使用了暖色調。')
        item3 = gameinfoItem(image_url='/static/images/artwork3.png', description='我的遊戲專案概念圖，展示了角色和場景設計。')
        item4 = gameinfoItem(image_url='/static/images/artwork4.png', description='與客戶合作的商業像素插畫，用於網站橫幅。')

        db.session.add_all([item1, item2, item3, item4]) # 將所有項目添加到會話
        db.session.commit() # 提交更改到資料庫
        print("Initial portfolio items added.")

# ====================================================================
# 定義 Flask 路由 (網頁路徑)
# ====================================================================

# 路由：首頁
@app.route('/')
@app.route('/home') # 也可以設定多個路徑指向同一個函數
def home():
    # 這裡可以傳遞數據給 home.html，但目前它是靜態的
    return render_template('home.html')

# 路由：關於我頁面
@app.route('/about')
def about():
    return render_template('about.html')

# 路由：作品集頁面
@app.route('/portfolio')
def portfolio():
    # 從資料庫中獲取所有作品集項目
    all_portfolio_items = PortfolioItem.query.all()
    # 將數據傳遞給 portfolio.html 模板
    return render_template('portfolio.html', portfolio_items=all_portfolio_items)

@app.route('/pixelart')
def pixelart():
    # 從資料庫中獲取所有像素畫項目 (使用 pixelartItem 模型)
    all_pixelart_items = pixelartItem.query.all()
    # 將數據傳遞給 pixelart.html 模板，變數名稱應該和模板中的迴圈變數一致
    return render_template('pixelart.html', pixelart_items=all_pixelart_items)

@app.route('/gameinfo')
def gameinfo():
    # 從資料庫中獲取所有像素畫項目 (使用 pixelartItem 模型)
    all_gameinfo_items = gameinfoItem.query.all()
    # 將數據傳遞給 pixelart.html 模板，變數名稱應該和模板中的迴圈變數一致
    return render_template('gameinfo.html', gameinfo_items=all_gameinfo_items)

# 路由：處理靜態檔案 (圖片等)
# Flask 預設會處理 /static/ 路徑下的靜態檔案
# 您需要在專案根目錄下建立一個 'static' 資料夾，然後在裡面放 'images' 資料夾
# 例如：your-web-project/static/images/artwork1.png
# 如果您的圖片路徑就是 'images/1.png'，則需要調整為 '/static/images/1.png'
# 建議將圖片放在 static/images/
# 如果您不想移動圖片，image_url 也可以是相對路徑，但通常建議用 /static/
# 示例：將您的大圖貼圖片 images/1.png 複製到 static/images/1.png

# 啟動 Flask 伺服器
if __name__ == '__main__':
    # debug=True 允許在程式碼更改時自動重載，並顯示詳細錯誤訊息
    # 僅限於開發環境使用，生產環境應設為 False 以確保安全
    app.run(debug=True)