import sys           # To access sys.modules and sys.version for module details and Python version
import os            # To access file paths and file modification times
import datetime      # To convert file modification timestamps into readable date-time formats
from importlib.metadata import distributions  # To get installed libraries and versions (Python 3.8+)

def report_imported_modules():
    target_tree = r'C:\F$\python'
    
    # Loop over all imported modules
    for module_name, module in sys.modules.items():
        # Skip __main__ module
        if module_name == "__main__":
            continue
        
        # Ensure the module has a valid '__file__' attribute
        if module and hasattr(module, '__file__') and module.__file__:
            file_path = module.__file__
            # Only check Python files (.py or .pyc) and limit to target directory
            if file_path.endswith(('.py', '.pyc')) and file_path.startswith(target_tree):
                # Get the last modified time
                last_modified_time = os.path.getmtime(file_path)
                last_modified_dt = datetime.datetime.fromtimestamp(last_modified_time)
                
                # Print module name, file path, and last modified date
                print(f"\nModule: {module_name}")
                print(f"File Path: {file_path}")
                print(f"Last Saved: {last_modified_dt.strftime('%Y-%m-%d %H:%M:%S')}")
                print()

def show_running_file_info():
    # Get the running file path (.py or .pyc)
    current_file = __file__
    
    # Get the last modified time of the file
    last_modified_time = os.path.getmtime(current_file)
    
    # Convert the timestamp to a readable datetime format
    last_modified_dt = datetime.datetime.fromtimestamp(last_modified_time)

    # Output the file name and the last modified time
    print(f"\nRunning file: {current_file}")
    print(f"Last saved: {last_modified_dt.strftime('%Y-%m-%d %H:%M:%S')}")

def sayVersions():
    # Report Python version
    python_version = sys.version
    print(f"Python Version: {python_version}")

    print("\nInstalled Libraries and Versions:")
    for dist in distributions():
        print(f"{dist.metadata['Name']} - {dist.version}")
    
    show_running_file_info()
    report_imported_modules()
