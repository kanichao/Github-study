import turtle

# 1. 環境の設定（ハードウェアの初期化に近い感覚です）
screen = turtle.Screen()
screen.bgcolor("white") # 背景色
t = turtle.Turtle()
t.shape("turtle")
t.speed(0) # 最速（0はアニメーションを省略する速度です）
t.color("#2c3e50") # 漆や陶器をイメージした深みのある色

# 2. 幾何学的ロジック（ここがあなたの「論理」です）
# 少しずつ長さを変えながら、一定の角度で回転し続ける
for i in range(100):
    t.forward(i * 3)   # 進む距離を徐々に増やす
    t.right(91)        # 90度（直角）から「1度」だけずらすのがポイント（注釈1）

# 3. 終了処理
t.hideturtle() # 最後にカメを隠して図形だけ残す
turtle.exitonclick()
