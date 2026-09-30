from flask import Flask, render_template

app = Flask(__name__)

restaurants = [
    {
        "name":"긴자 창원점",
        "region":"창원 성산구",
        "type":"일식",
        "rating":4.8,
        "price":50000,
        "image":"https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=800"
    },
    {
        "name":"우화한우",
        "region":"창원 성산구",
        "type":"고기",
        "rating":4.9,
        "price":45000,
        "image":"https://images.unsplash.com/photo-1544025162-d76694265947?w=800"
    },
    {
        "name":"청해횟집",
        "region":"창원 성산구",
        "type":"해산물",
        "rating":4.7,
        "price":55000,
        "image":"https://images.unsplash.com/photo-1559847844-5315695dadae?w=800"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        restaurants=restaurants
    )

if __name__ == "__main__":
2
app.run(host="0.0.0.0", port=5000)