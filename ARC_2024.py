# Original source: https://www.kaggle.com/code/allegich/arc-agi-2025-visualization-all-1000-120-tasks

#import pandas as pd
#import numpy as np

import matplotlib.pyplot as plt
from   matplotlib import colors
#import seaborn as sns

import json
import os
#from pathlib import Path
#from glob import glob

#from subprocess import Popen, PIPE, STDOUT

# Loading JSON data
def load_json(file_path):
	# check that file exist
	if os.path.exists(file_path):
		with open(file_path) as f:
			data = json.load(f)
		return data
	else:
		return None

#base_path='/kaggle/input/arc-prize-2025/'
#base_path='data/'
#training_challenges   = load_json(base_path +'arc-agi_training_challenges.json')
#training_solutions    = load_json(base_path +'arc-agi_training_solutions.json')

#evaluation_challenges = load_json(base_path +'arc-agi_evaluation_challenges.json')
#evaluation_solutions  = load_json(base_path +'arc-agi_evaluation_solutions.json')

# 0:black, 1:blue, 2:red, 3:green, 4:yellow, # 5:gray, 6:magenta, 7:orange, 8:sky, 9:brown

cmap = colors.ListedColormap(
	['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00',
	 '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])
norm = colors.Normalize(vmin=0, vmax=9)

def show_legend():
	plt.figure(figsize=(3, 1), dpi=150)
	plt.imshow([list(range(10))], cmap=cmap, norm=norm)
	plt.xticks(list(range(10)))
	plt.yticks([])
	plt.show()

def plot_one(ax, i, task, train_or_test, input_or_output):
	fs=12 
	input_matrix = task[train_or_test][i][input_or_output]
	ax.imshow(input_matrix, cmap=cmap, norm=norm)
	ax.grid(True, which = 'both',color = 'lightgrey', linewidth = 0.5)
	
	plt.setp(plt.gcf().get_axes(), xticklabels=[], yticklabels=[])
	ax.set_xticks([x-0.5 for x in range(1 + len(input_matrix[0]))])     
	ax.set_yticks([x-0.5 for x in range(1 + len(input_matrix))])
	
	ax.set_title(train_or_test + ' ' + input_or_output, fontsize=fs-2)

def plot_task(task, task_solutions, i, t, save_folder=None):
	"""    Plots the first train and test pairs of a specified task,
	using same color scheme as the ARC app    """    

#	if save_folder:
#		plt.figure()

	fs=12    
	num_train = len(task['train'])
	#num_test  = len(task['test'])
	num_test  = 1
	
	w=num_train+num_test
	fig, axs  = plt.subplots(2, w, figsize=(2*w,2*2))
	#fig, axs  = plt.subplots(2, w, figsize=(1.5*w, 1.5*2))
	plt.suptitle(f'Task #{i+1}, id={t}:', fontsize=fs, fontweight='bold', y=0.95)
	#plt.subplots_adjust(top=0.85) 
	#plt.subplots_adjust(hspace = 0.15)
#	plt.subplots_adjust(wspace=20, hspace=20)
	plt.subplots_adjust(wspace=0.4, hspace=0.4)
	
	for j in range(num_train):     
		plot_one(axs[0, j], j, task, 'train', 'input')
		plot_one(axs[1, j], j, task, 'train', 'output')        
	
	plot_one(axs[0, j+1], 0, task, 'test', 'input')

	answer = task_solutions
	input_matrix = answer
	
	if input_matrix:
		axs[1, j+1].imshow(input_matrix, cmap=cmap, norm=norm)
		axs[1, j+1].grid(True, which = 'both',color = 'lightgrey', linewidth = 0.5)
		axs[1, j+1].set_yticks([x-0.5 for x in range(1 + len(input_matrix))])
		axs[1, j+1].set_xticks([x-0.5 for x in range(1 + len(input_matrix[0]))])     
		axs[1, j+1].set_xticklabels([])
		axs[1, j+1].set_yticklabels([])
		axs[1, j+1].set_title('test output')

	axs[1, j+1] = plt.figure(1).add_subplot(111)
	axs[1, j+1].set_xlim([0, num_train+1])
	
	for m in range(1, num_train):
		axs[1, j+1].plot([m,m],[0,1],'--', linewidth=1, color = 'black')
	
	axs[1, j+1].plot([num_train,num_train],[0,1],'-', linewidth=3, color = 'black')

	axs[1, j+1].axis("off")

	fig.patch.set_linewidth(5)
	fig.patch.set_edgecolor('black') 
	fig.patch.set_facecolor('#dddddd')

	plt.subplots_adjust(bottom=0.2)

	plt.tight_layout()
	
	if save_folder:
#		plt.figure()
		save_path = save_folder + f'{i+1:04d}_{t}.png'
		plt.savefig(save_path)
		plt.close()
#		plt.clf()
	else:
		print(f'#{i}, {t}') # for fast and convinience search
		plt.show()  
		print()

	#print()


## Export the training tasks to image files
def plot_training_tasks(challenges, solutions, from_task=0, to_task=100, save_folder=None):
	if to_task<0:
		to_task = len(challenges)
	for i in range(from_task, to_task):
		if (i+1) % 10 == 0:
			print(f'...processing task #{i+1}')
		t=list(challenges)[i]
		task=challenges[t]
		if solutions:
			task_solution = solutions[t][0]
		else:
			task_solution = None
		plot_task(task, task_solution, i, t, save_folder=save_folder)

##--------------------------------------------------------
## The following code are for formatting the tasks (with train/test data)
## into a readable format. The tasks are printed to the screen or to a file
def print_to(line, f):
	if f:
		f.write(line + '\n')
	else:
		print(line)
  
def pretty_print_grid(grid, f=None):
	indent = '\t  '
	for row in grid:
		line = indent + " ".join(map(str, row))
		print_to(line, f)
		
#plot_training_tasks(from_task=0, to_task=100)
def print_task(task, task_solution, i, tid, f=None):
#	show_legend()
	train_pairs = task['train']
	n_train_pairs = len(train_pairs)
#	print_to(f'Task #{i}, id={tid}, #train_pairs={n_train_pairs}', f)
	for j in range(n_train_pairs):
		train_pair = train_pairs[j]
		train_input = train_pair['input']
		train_output = train_pair['output']
		print_to(f'  Train pair #{i+1}.{j+1}/{n_train_pairs}:', f)
		print_to(f'    Input:', f)
		pretty_print_grid(train_input, f)
		print_to(f'    Output:', f)
		pretty_print_grid(train_output, f)	
   
	# Test data
	test_data = task['test']
	n_test_data = len(test_data)
	for k in range(len(test_data)):
		test_input = test_data[k]
		print_to(f'\n  Test input #{i+1}.{k+1}/{n_test_data}:', f)
#		print_to(f'    Input:', f)
		pretty_print_grid(test_input['input'], f)
		if task_solution:
			print_to(f'  Test output #{i+1}.{k+1}/{n_test_data}:', f)
			pretty_print_grid(task_solution, f)
		print_to('', f)

# This converts the train/test data to readable format, either to the screen
# or to a file.	  
def print_training_tasks(challenges, solutions, from_task=0, to_task=100, save_path=None):
	if save_path:
		f = open(save_path, 'w')
	else:
		f = None

	if to_task < 0:
		to_task = len(challenges)

#	tids = training_challenges.keys()
	tids = list(challenges)
	for i in range(from_task, to_task):
#		tid = list(training_challenges)[i]
		if (i+1) % 10 == 0:
			print(f'...processing task #{i+1}')
		tid = tids[i]
		task = challenges[tid]
		npairs = len(task['train'])
		print_to(f'Task #{i+1}, id={tid}, {npairs} train pairs ----------------------', f)
#		if i+1==3:
#			x = 1

		if solutions:
			task_solution = solutions[tid][0]
		else:
			task_solution = None
		print_task(task, task_solution, i, tid, f)

def convert_tasks_to_text(challenges, solutions, save_path=None):
	print_training_tasks(challenges, solutions, from_task=0, to_task=-1, save_path=save_path)

def do_one_phase(phase_name, do_text=False, do_image=False):
	base_path='data/'

	#--------------------------
	# for eval data
	challenges   = load_json(base_path + f'{phase_name}/arc-agi_{phase_name}_challenges.json')
	solutions    = load_json(base_path + f'{phase_name}/arc-agi_{phase_name}_solutions.json')

	if do_text:
		# Exports training data to readable text file
		save_path = f'data/{phase_name}/tasks_formatted.txt'
		#save_path = None
		convert_tasks_to_text(challenges, solutions, save_path=save_path)
	
	if do_image:
		# Exports training data to images
		image_folder = f'data/{phase_name}/images/'
		plot_training_tasks(challenges, solutions, from_task=0, to_task=-1, save_folder=image_folder)

if __name__ == '__main__':
	# Note that all exported tasks to images or text files are indexed from 1 to N,
	# while the task IDs are indexed from 0 to N-1.
	
	# This has been saved as data/image_legend.png
	#show_legend()

#	do_one_phase('training', do_text=True, do_image=True)
#	do_one_phase('evaluation', do_text=True, do_image=True)
	do_one_phase('test', do_text=True, do_image=False)

	import sys
	sys.exit(0)

	#--------------------------
	# for training data - the following is deprecated
	training_challenges   = load_json(base_path +'train/arc-agi_training_challenges.json')
	training_solutions    = load_json(base_path +'train/arc-agi_training_solutions.json')

	'''	
	# Exports training data to readable text file
	save_path = 'data/train/tasks_formatted.txt'
	#save_path = None
	convert_tasks_to_text(training_challenges, training_solutions, save_path=save_path)
	'''
	# Exports training data to images
	image_folder = 'data/train/images/'
	plot_training_tasks(training_challenges, training_solutions, from_task=0, to_task=-1, save_folder=image_folder)


