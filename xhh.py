import os
import time
import subprocess
import os
import time
import subprocess
import ctypes
import sys
def is_admin():
    """检查是否具有管理员权限"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def connect_emulator():
    """连接模拟器"""
    try:
        # 尝试连接模拟器（默认端口5555）
        result = subprocess.run(['adb', 'connect', '127.0.0.1:5555'], 
                              capture_output=True, 
                              text=True)
        
        if "connected" in result.stdout:
            print("模拟器连接成功")
            return True
        else:
            print("模拟器连接失败")
            return False
    except Exception as e:
        print(f"连接模拟器时出错: {e}")
        return False

def start_xhh():
   
    try:
        # 启动应用（需要替换为实际的包名和活动名）
        subprocess.run(['adb', 'shell', 'am', 'start', '-n', 
                       ''])
        print("启动成功")
        return True
    except Exception as e:
        print(f"启动时出错: {e}")
        return False

def start_mumu():
    """启动MuMu模拟器"""
    try:
        # 替换为实际的MuMu模拟器路径
        mumu_path = r"D:\MuMu\emulator\nemu\EmulatorShell\NemuPlayer.exe"
        
        if os.path.exists(mumu_path):
            if not is_admin():
                # 如果没有管理员权限，则请求权限
                ctypes.windll.shell32.ShellExecuteW(
                    None, 
                    "runas", 
                    sys.executable, 
                    " ".join(sys.argv), 
                    None, 
                    1
                )
                return True
                
            # 以管理员权限启动模拟器
            subprocess.Popen(mumu_path)
            print("MuMu模拟器启动成功")
            # 等待模拟器启动
            time.sleep(30)
            return True
        else:
            print("未找到MuMu模拟器程序")
            return False
    except Exception as e:
        print(f"启动MuMu模拟器时出错: {e}")
        return False

def main():
    """主函数"""
    # 1. 启动模拟器
    if not start_mumu():
        print("启动模拟器失败")
        return
    
    # 2. 连接模拟器
    retry_count = 0
    while retry_count < 3:
        if connect_emulator():
            break
        retry_count += 1
        time.sleep(5)
    else:
        print("连接模拟器失败，请检查模拟器是否正常运行")
        return
    
    # 3. 等待系统完全启动
    time.sleep(10)
    
    # 4. 启动小黑盒
    if not start_xhh():
        print("启动小黑盒失败")
        return
    
    print("所有操作完成")

if __name__ == "__main__":
    main()
