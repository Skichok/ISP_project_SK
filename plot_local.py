import re
from datetime import datetime

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def normalize_expr(expr: str) -> str:
    """
    Небольшая нормализация ввода:
    - убираем лишние пробелы
    - вставляем '*' между числом и переменной: 2x -> 2*x
    - '^' заменяем на '**' (часто так вводят степени)
    """
    expr = expr.strip()
    expr = expr.replace("^", "**")
    expr = re.sub(r'(?<=[0-9])(?=[a-zA-Z])', '*', expr)
    return expr


def plot_expression(
    expression_text: str,
    x_min: float = -10,
    x_max: float = 10,
    n_points: int = 800,
    dark_theme: bool = True,
    out_dir: str = "Graph_pic",
) -> str:
    """
    Строит график по формуле (sympy) и сохраняет PNG.
    Возвращает путь к файлу.
    """
    import os
    os.makedirs(out_dir, exist_ok=True)

    expression_text = normalize_expr(expression_text)

    x = sp.symbols("x")
    try:
        # sympify понимает: sin(x), ln(x), exp(x), sqrt(x), abs(x) ...
        expression = sp.sympify(expression_text)
    except (sp.SympifyError, ValueError) as e:
        raise ValueError(f"Неверное выражение: {expression_text}") from e

    x_values = np.linspace(x_min, x_max, n_points)

    try:
        f = sp.lambdify(x, expression, modules=["numpy"])
        y_values = f(x_values)
    except Exception as e:
        raise ValueError("Ошибка при вычислении выражения. Проверь синтаксис функции.") from e

    # Иногда получаются комплексные значения (например, ln(x) при x<0)
    # Отфильтруем их, чтобы matplotlib не ломался:
    y_values = np.asarray(y_values)
    if np.iscomplexobj(y_values):
        y_values = np.real(y_values)

    # И ещё: бесконечности и NaN (например, 1/x в 0)
    y_values = np.where(np.isfinite(y_values), y_values, np.nan)

    # --- Рисование ---
    if dark_theme:
        plt.figure(facecolor="black")
        plt.plot(x_values, y_values, color="cyan", label=f"y = {expression_text}")

        plt.axhline(0, color="white", linewidth=0.8)
        plt.axvline(0, color="white", linewidth=0.8)

        plt.title(f"Graph of y = {expression_text}", color="white")
        plt.xlabel("x", color="white")
        plt.ylabel("y", color="white")

        plt.grid(True, color="gray")
        plt.legend(facecolor="black", edgecolor="white", labelcolor="white", loc="upper right")
        plt.gca().set_facecolor("black")
        plt.tick_params(colors="white")
    else:
        plt.figure()
        plt.plot(x_values, y_values, label=f"y = {expression_text}")
        plt.axhline(0, linewidth=0.8)
        plt.axvline(0, linewidth=0.8)
        plt.grid(True)
        plt.legend(loc="upper right")

    ts = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"{out_dir}/graph_{ts}.png"
    plt.savefig(filename, facecolor=("black" if dark_theme else None))
    plt.close()

    return filename


def main():
    print("Локальный тест построения графиков.")
    print("Примеры: sin(x) + ln(x), x^2-3x+2, 1/x, sqrt(x), exp(-x**2)")
    print("Введите 'exit' чтобы выйти.\n")

    while True:
        expr = input("f(x) = ").strip()
        if expr.lower() in ("exit", "quit", "q"):
            break

        try:
            path = plot_expression(expr)
            print(f"Готово! Файл сохранён: {path}\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")


if __name__ == "__main__":
    main()
