### Instructions to run vagrant for the full stack restaurant project


- 1. ```$ cd <to the vagrantfile folder>```

- 2. ```$ vagrant up```

- 3. ```$ vagrant ssh```

- 4. Make sure you work on virtual environment >> venv

- 5. Connection is on. Verified if you see >> 

```vagrant@vagrant:~$```

- 6. To disconnect the connection. 
```$ exit```

- Reload the vagrantfile setting ont your virtual machine.
```vagrant reload```

-  Destroy the virtual machine (can reactivate using $ vagrant up)
```vagrant destroy```

-  Saves the current work and suspends the vm
```vagrant suspend```

- For all other commands
```vagrant --help```