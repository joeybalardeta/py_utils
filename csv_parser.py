class CSVParser:
    def __init__(self, filename: str):
        self.filename = filename
        self.file_handle = None
    

    def __del__(self):
        self.close()
    

    def close(self):
        if self.file_handle is not None:
            self.file_handle.close()


    def parse(self):
        self.file_handle = open(self.filename, 'r')
        self.data = []

        file_lines = self.file_handle.readlines()

        for i in range(len(file_lines)):
            if i == 0:
                continue
            
            line = file_lines[i]
            line_data = line.split(",")

            # cleaning up line data
            for j in range(len(line_data)):
                line_data[j] = line_data[j].strip("\r\n")

            self.data.append(line_data)
            
        self.file_handle.close()