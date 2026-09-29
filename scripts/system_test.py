import sys
import torch
import numpy as np
import pandas as pd
from Bio import __version__ as biopython_version

print("=" * 60)
print("PROTEIN DESIGN BENCHMARK - SYSTEM TEST")
print("=" * 60)

print(f"Python:     {sys.version.split()[0]}")
print(f"PyTorch:    {torch.__version__}")
print(f"NumPy:      {np.__version__}")
print(f"Pandas:     {pd.__version__}")
print(f"BioPython:  {biopython_version}")
print(f"CUDA:       {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU:        {torch.cuda.get_device_name(0)}")

print("=" * 60)
print("ENVIRONMENT OK")
print("=" * 60)
