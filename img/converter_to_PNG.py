import sys
import os
from PIL import Image
from time import time

# Здесь принимаем аргументы и записываем их в соответсвующие переменные
# Важно помнить, что нулевым аргументом в sys всегда является название исполняемого файла

t1 = time()
print('Конвертируем . . .')

path_to_images = sys.argv[1]
save_folder_name = sys.argv[2]

# Здесь проверяем, сущетсвует ли директория с таким названием, куда мы хотим сохранить наши файлы

if not os.path.exists(f'{path_to_images}/{save_folder_name}'):
    os.makedirs(f'{path_to_images}/{save_folder_name}')
else:
    pass

# Здесь мы создаём массив и с помощью цикла запихиваем в него пути до изображений

images = []

for i in os.listdir(path_to_images):
    images.append(f'{path_to_images}/{i}')

# Здесь циклом проходимся по изображениям, конвертируем их и сохраняем

_counter = 0
for i in images:
    try:
        with Image.open(i) as img:
            img.save(
                f'{path_to_images}/{save_folder_name}/{_counter}.png', 'png')
            _counter += 1
    except IsADirectoryError:
        continue

t2 = time()

print(f'Конвертация заняла {round(t2-t1)} сек.')
