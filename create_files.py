
def create_n_files(number_files):
	'''
	Принимает количество файлов которое нужно создать, 
	путь до папки и текст внутри файла изменить можно внутри функции.
	'''
	ind = 1
	while number_files >= ind:
		try:
			with open(f"lesson_7\Task_{ind}.py", "w") as file_obj: #путь до папки и имя файла-ов!
				file_obj.write(f"'''\nText task {ind} \n'''\n") #Текст в файлах, можно удалить
			print(f'Файл №{ind} создан!')
		
			ind += 1 
		except IOError:
			print('Ошибка ввода-вывода!')	
create_n_files(3)

