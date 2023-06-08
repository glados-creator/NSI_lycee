import os
import sys
import argparse
import inspect
import importlib.util


def extract_functions_and_methods(filename):
    module_name = os.path.splitext(os.path.basename(filename))[0]
    try:
        spec = importlib.util.spec_from_file_location(module_name, filename)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
    except Exception as ex:
        print(ex, file=sys.stderr)
        return []

    functions_and_methods = []

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) or inspect.ismethod(obj):
            signature = inspect.signature(obj)
            docstring = inspect.getdoc(obj) or ''
            functions_and_methods.append((name, signature, docstring))

    return functions_and_methods


def write_functions_and_methods_to_file(items, output_filename):
    with open(output_filename, 'w') as file:
        for name, signature, docstring in items:
            file.write(f'{name}{str(signature)}:\n')
            file.write(f'{docstring}\n\n')


def scan_directory(path, output_dir, should_print,recursive):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) and filename.endswith('.py'):
            if not should_print:
                print(f'Scanning file: {file_path}\n')
            functions_and_methods = extract_functions_and_methods(file_path)
            if should_print:
                print(f'---- {filename} ----')
                for name, signature, docstring in functions_and_methods:
                    print(f'{name}{str(signature)}:')
                    print(f'{docstring}\n')
            else:
                relative_path = os.path.relpath(path).replace("\\","_").replace("/","_").replace(" ","-")
                output_file = os.path.join(output_dir, f'doc_{relative_path}_{filename.replace(".py","")}.txt')
                write_functions_and_methods_to_file(functions_and_methods, output_file)

        elif recursive and os.path.isdir(file_path):
            # Recursive call for subdirectories
            if not should_print:
                print(f'\nScanning subdirectory: {file_path}\n')
            scan_directory(file_path, output_dir, should_print)


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Scan Python file(s) and extract function signatures and docstrings')
    parser.add_argument('path', nargs='+', help='Path(s) to the file(s) or directory(s) to scan')
    parser.add_argument('-o', '--output', help='Output directory (default: gen_doc)', default='.\\gen_doc\\')
    parser.add_argument('-p', '--print', action='store_true', help='Print the result instead of writing to a file')
    parser.add_argument('-r', '--recursive', action='store_true', help='recursive search or not')
    args = parser.parse_args()

    output_dir = args.output
    should_print = args.print
    recursive = args.recursive

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not should_print:
        print("cwd",os.curdir)
        for file in args.path:
            print(file,"file" if os.path.isfile(file) else "dir" if os.path.isdir(file) else "unknown")
    for path in args.path:
        if os.path.isdir(path):
            # Scan directory
            if not should_print:
                print(f'Scanning directory: {path}\n')
            scan_directory(path, output_dir, should_print,recursive)
        elif os.path.isfile(path):
            # Scan single file
            if not should_print:
                print(f'Scanning file: {path}\n')
            filename = os.path.basename(path)
            output_file = os.path.join(output_dir, f'doc_{filename.replace(".py","")}.txt').replace("\\","_").replace("/","_").replace(" ","-")
            functions_and_methods = extract_functions_and_methods(path)
            if should_print:
                print(f'---- {filename} ----')
                for name, signature, docstring in functions_and_methods:
                    print(f'{name}{str(signature)}:')
                    print(f'{docstring}\n')
            else:
                write_functions_and_methods_to_file(functions_and_methods, output_file)
