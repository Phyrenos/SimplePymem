# Simple Pymem

Thanks to [pymem](https://github.com/srounet/Pymem/) for making this possible


## Example

```py
from SimplePymem import SPM_OK, AlwaysTrue
from pymem import *

def main():
    pm = pymem.Pymem("Stumble Guys.exe")
    client = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

    if AlwaysTrue(pm, client, 0x29C6990, True) == SPM_OK:
        print("Unlocked all cosmetics in Stumble Guys!")
    else:
        print("Failed to unlock all cosmetics in Stumble Guys!")
if __name__ == "__main__":
    main()
```

## Output:

```txt
Unlocked all cosmetics in Stumble Guys!
```
