### 如何查看已安装的库
打开 Anaconda Command Prompt ,在命令提示符窗口中输入以下命令：

pip list
 或者
conda list
其中，pip list 只能查看库，而 conda list 则可以查看库以及库的版本

### 如何安装或更新库
以安装 更新 scipy 为例

pip install scipy
pip install scipy --upgrade
或者
conda install scipy
conda update scipy

### 更新所有库
conda update --all

### 更新 conda 自身
conda update conda

### 更新 anaconda 自身
conda update anaconda