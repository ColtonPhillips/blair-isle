def out_file_name():
	import inspect
	# this is gonna work on my machine only
	return "out/" + inspect.stack()[-1][1].replace('./', "").replace(".\\", "").replace(".py",".png")
