# Run this from WSL under the conda env 'base' (cond activate)
import arckit
#train_set, eval_set = arckit.load_data() # Load ARC1 train/eval
train_set, eval_set = arckit.load_data(version="ARC2") # Load ARC2 train/eval
#>>> train_set 
#<TaskSet: 400 tasks>
#>>> train_set[0]
#<Task-train 007bbfb7 | 5 train | 1 test>
# Indexing can be done by task ID

train_set[0] == train_set['007bbfb7']

# You can load specific tasks by ID
task = arckit.load_single('007bbfb7')

# Display grid as image
#$ pip install cairosvg		#drawsvgall

from PIL import Image

def show(img_path):
	img = Image.open(img_path)
	img.show()

import arckit.vis as vis

def do(task, i, j, export_image=False):
	print(f'......training #{i}.{j}')
	g = task.train[i][j]
	print(f'{g}')
	grid = vis.draw_grid(g, xmax=len(g[0]), ymax=len(g), padding=.5, label='Example')
	if export_image:
		img_path = f'grid_{i}_{j}.png'
		vis.output_drawing(grid, img_path)
		show(img_path)

def do_task(n):
	task = train_set[n]
	for i in range(len(task.train)):
		print(f'...training pair #{i}')
		for j in range(len(task.train[i])):
			do(task, i, j)
#grid = vis.draw_grid(task.train[0][0], xmax=3, ymax=3, padding=.5, label='Example')
#vis.output_drawing(grid, 'grid_0_0.png')
#do(0, 1)
do_task(0)
