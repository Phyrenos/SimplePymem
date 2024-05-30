import pymem
import pymem.exception
import pymem.process
from typing import Union

SPM_OK = True
SPM_FAIL = False

def IsOffset(offset: Union[str, int]):
    if isinstance(offset, str):
        if offset.startswith("0x"):
            return True
        else:
            return False
    elif isinstance(offset, int):
        return True
    else:
        return False

def AlwaysTrue(pm: pymem.Pymem, lpBaseOfDll, Offset, Value: bool) -> bool:
    """
    Make a function always return true/false

    INFO: 
    ----------
    any code in that function that you are patching will be gone 
    
    and the only code in it will be "return true/false"

    Parameters
    ----------
    pm: Pymem
        The pymem object to use
    lpBaseOfDll: .lpBaseOfDll 
        the base dll of the game
    Offset: Hex
        The offset of the function to patch 
    Value: bool
        True or False

    Examples
    --------
    pm = pymem.Pymem("UnityGame.exe")

    client = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

    if AlwaysTrue(pm, client, 0x1234567) == SPM_OK:
        print("Unlocked all cosmetics in UnityGame!")
    else:
        print("Failed to unlock all cosmetics in UnityGame!")
    """

    if IsOffset(Offset):
        pass
    else:
        return SPM_FAIL
    # NASM 2.16.01
    if Value == True:
        patch = b'\xb8\x01\x00\x00\x00\xc3' # mov rax, 1; ret = True
    else:
        patch = b'\xb8\x00\x00\x00\x00\xc3' # mov rax, 0; ret = False

    try:
        FuncOffset = lpBaseOfDll + Offset
        try: 
            pm.write_bytes(FuncOffset, patch, len(patch))
            return SPM_OK
        except:
            return SPM_FAIL
    except:
        return SPM_FAIL


def DiscontinuedCode():
    #b'\x48\xC7\xC0\x00\x00\x00\x00\xC3'
    # print("Cosmetic Function offset:", CosmeticFunc)
    #func_addr_bytes = pm.read_bytes(CosmeticFunc, 8)
    # print("Function Address Bytes:", func_addr_bytes)
    # print("Successfully Patched The Function!")
    #print("Failed to patch Function! : Offsets are wrong or outdated!")
    #print("Process Not Found, Please make sure the game is running!")
    d = ""
