import sys
import os

module_path = os.path.abspath(os.path.join(os.pardir))
print(module_path)
if module_path not in sys.path:
    sys.path.append(module_path)