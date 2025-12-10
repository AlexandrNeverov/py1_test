from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    a = ""
    b = ""
    op = "add"
    result = None
    error = None

    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()
        op = request.form.get("op", "add")

        try:
            av = float(a)
            bv = float(b)

            if op == "add":
                result = av + bv
            elif op == "sub":
                result = av - bv
            elif op == "mul":
                result = av * bv
            elif op == "div":
                if bv == 0:
                    error = "Ошибка: деление на ноль"
                else:
                    result = av / bv
            else:
                error = "Неизвестная операция"
        except ValueError:
            error = "Введите корректные числа"

    return render_template(
        "index.html",
        a=a,
        b=b,
        op=op,
        result=result,
        error=error,
    )


@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
