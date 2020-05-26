# for logging
from IPython import get_ipython
ipython = get_ipython()
ipython.magic('logstart -ortq ~/.logs/global_log.py append')

# for grader
from static_grader import grader
