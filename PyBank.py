class PyBank:

    def clear(self, file_name: str):
        with open(file_name, 'w') as f:
            f.write("")

    def append(self, file_name: str, variable_name: str, variable_value):
        with open(file_name, 'a') as f:
            f.write(f'{variable_name}: {variable_value}\n')

    def get_value(self, file_name: str, variable_name: str):
        with open(file_name, 'r') as f:
            for line in f:
                if ': ' in line:
                    name, value = line.strip().split(': ', 1)
                    if name == variable_name:
                        return value
        return None
        
    def show_all(self, file_name: str):
    	with open(file_name, 'r') as f:
    		return f.read()
    
    def replace(self, file_name: str, variable_name: str, new_value):
        with open(file_name, 'r') as f:
        	lines = f.readlines()

        updated_lines = []
        found = False
        
        for line in lines:
            if ': ' in line:
            	name, value = line.strip().split(': ', 1)
            	if name == variable_name:
                    updated_lines.append(f"{name}: {new_value}\n")
                    found = True
            	else:
                    updated_lines.append(line)
            else:
            	updated_lines.append(line)
        with open(file_name, "w") as f:
        	f.writelines(updated_lines)
        return found
