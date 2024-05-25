import turtle

def draw_pifagor_tree(t, branch_len, level):
    if level == 0:
        return
    t.forward(branch_len * level)
    t.right(45)
    draw_pifagor_tree(t, branch_len, level-1)
    t.left(90)
    draw_pifagor_tree(t, branch_len, level-1)
    t.right(45)
    t.backward(branch_len * level)

def main():
    # Встановлення вікна для малювання
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Створення об'єкта черепахи
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.left(90)  # Поворот початкової точки на 90 градусів вліво, щоб відобразити дерево вгору
    
    # Введення користувача для вказівки рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    # Малювання дерева Піфагора
    draw_pifagor_tree(t, 10, level)

    # Закриття вікна при кліку
    window.exitonclick()

if __name__ == "__main__":
    main()
