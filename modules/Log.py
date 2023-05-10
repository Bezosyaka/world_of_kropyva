import os, arrow, traceback
logf="gamelog.log"

def log(arg):

	if callable(arg):
		text = f"Info  [ {arg.__name__} is done succesful"
	else:
		text = arg

	if os.path.exists(logf):

		with open(logf, "a") as f:
			f.write(f"{arrow.utcnow().to('local').format('YYYY-MM-DD HH:mm:ss')} ] {text}\n")
		f.close()

	else:

		f=open(logf, "w")
		f.close()
		log(text)

def log_on_error(func):
	def wrapper(*args, **kwargs):
		try:
			log(f"Info  [ {func.__name__} in progress")
			a = func(*args, **kwargs) #виконуємо функція, якщо не працює то вилезе ексепт, а якщо так то запише що фунція норм
			log(func)
			return a
		except BaseException as e:
			tb = traceback.format_exc()
			log(f"Fatal [ {func.__name__} gone wrong!")
			log(f"Fatal [ game crashed!")
			log(f"Trace [ {tb}")
			raise e		
	return wrapper
