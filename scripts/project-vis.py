import os
import argparse
from graphviz import Digraph

'''
    Скрипт строит стуркутуру проекта в формате .dot

    Использование: 
        python project-vis.py DIR_PATH [-o file_name.dot]
'''

IGNORE_DIRS = ['__pycache__', '.git','scripts','.vscode','.github', 'deployment', 'migrations','api']

IGNORE_FILES = ['go.mod', 'go.sum', 'makefile', 'README.md','.gitignore','Dockerfile','.env.example']

def build_graph(root_dir, output_dot_file='filesystem_graph.dot'):
    dot = Digraph(comment='File system graph')
    
    dot.attr(rankdir='TB', ranksep='1.0', nodesep='0.5')
    
    for foldername, subfolders, filenames in os.walk(root_dir):
        relative_foldername = os.path.relpath(foldername, root_dir)
        folder_label = os.path.basename(foldername) or relative_foldername
        

        if folder_label in IGNORE_DIRS:
            continue
        

        dot.node(relative_foldername, label=folder_label, shape='box', color='blue')  
        
        with dot.subgraph() as subgraph:
            subgraph.attr(rank='same')
            
            for subfolder in subfolders[:]:
                if subfolder in IGNORE_DIRS:
                    subfolders.remove(subfolder) 
                    continue
                
                subfolder_path = os.path.join(foldername, subfolder)
                relative_subfolder_path = os.path.relpath(subfolder_path, root_dir)
                subgraph.node(relative_subfolder_path, label=subfolder, shape='box', color='blue')  
                dot.edge(relative_foldername, relative_subfolder_path)  
        
        for filename in filenames:
            if filename in IGNORE_FILES:
                continue  
            
            file_path = os.path.join(foldername, filename)
            relative_file_path = os.path.relpath(file_path, root_dir)
            dot.node(relative_file_path, label=filename, shape='ellipse', color='green')  
            dot.edge(relative_foldername, relative_file_path)  
    
    dot.save(output_dot_file)
    print(f"Граф сохранен в файл {output_dot_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Построение графа файловой системы в формате .dot")
    parser.add_argument("directory", help="Путь к целевой директории")
    parser.add_argument("-o", "--output", default="filesystem_graph.dot", help="Имя выходного файла .dot (по умолчанию filesystem_graph.dot)")
    
    args = parser.parse_args()

    build_graph(args.directory, args.output)