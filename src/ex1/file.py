import os


class Files:

    def read(self, file_path):
        file_content = ''

        with open(file_path, 'r+') as file:
            for line_in_file in file:
                file_content += line_in_file

        return file_content

    def overwrite(self, file_path, text_to_write):
        with open(file_path, "w+") as file:
            file.write(text_to_write)

    def remove_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError("File doesn't exist")
