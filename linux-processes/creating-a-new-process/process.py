import os

pid = os.fork()

# pid greater than 0 represents the parent process
if pid > 0 :
  print("I am parent process and my process ID: ", os.getpid())
  print("Child process ID:", pid)
# pid equal to 0 represents the child process
else :
  print("\nI am child process and my process ID: ", os.getpid())
  print("Parent process ID:", os.getppid())
