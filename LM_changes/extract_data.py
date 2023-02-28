import json 
import os
def write_data(dir, file_name):
    json_path = os.path.join(dir, 'json_files',file_name + ".json")
    lm_path = os.path.join(dir, 'data_LM')
    if not os.path.exists(lm_path):
        os.makedirs(lm_path)

    txt_file = os.path.join(lm_path, file_name + '.txt')
    with open(txt_file , 'w') as f:
        f_json = open(json_path)
        json_file = json.load(f_json)
        for item in json_file.values():
            f.write(item['words'] + '\n')
        

def main():
    data_dir = "/users/PAS2348/ramirez537/data/librispeech/"
    #write valid.txt
    write_data(data_dir, 'valid')
    write_data(data_dir, 'train')
    write_data(data_dir, 'test')
    
    
    
if __name__=='__main__':
    main()