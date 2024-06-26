import matplotlib.pyplot as plt

from random_walk import RandomWalk

# новые блуждания строятся до тех пор, пока программа остается активной.
while True:
# Построение случайного блуждания и нанесения на диграмму
    rw = RandomWalk()
    rw.fill_walk()
    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap = plt.cm.Blues, edgecolor=None, s=15)

    # Выделение первой и последней точки
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break