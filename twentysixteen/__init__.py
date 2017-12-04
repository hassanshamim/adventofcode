import sys, os

dirname = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(1, dirname)

print(sys.path)